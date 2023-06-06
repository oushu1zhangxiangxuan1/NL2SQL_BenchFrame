import requests
import json
import websockets

# import asyncio
from utils import *


class BaseModel:
    def predict(self, utterance, history):
        pass


class ChatGLM6B_API(BaseModel):
    def __init__(self, url) -> None:
        self.url = url

    def predict(self, utterance, history):
        payload = {"question": utterance, "history": history}
        # 发送 POST 请求
        # response = requests.post(self.url, json=payload, timeout=30)
        response = requests.post(self.url, json=payload, timeout=300)

        # 获取响应结果
        if response.status_code == 200:
            data = response.json()
            if "response" in data.keys():
                return data["response"], data["history"], 0
            else:
                print(json.dumps(response, ensure_ascii=False, indent=2))
                raise "请求失败"
        else:
            print("请求失败:%d" % (response.status_code))
            raise "请求失败"

    def close(self):
        pass

    def getInitHistory(self, init_prompt):
        return [[init_prompt, "好的"]]


class ChatGLM6B_SOCK(BaseModel):
    def __init__(self, websocket_url) -> None:
        self.websocket_url = websocket_url
        self.websocket = None

    async def connect(self):
        self.websocket = await websockets.connect(
            self.websocket_url, ping_interval=None
        )

    async def send_request(self, req):
        await self.websocket.send(json.dumps(req))

    async def receive_response(self):
        resp = await self.websocket.recv()
        return json.loads(resp)

    async def close(self):
        await self.websocket.close()

    async def predict(self, utterance, history):
        if not self.websocket:
            await self.connect()

        payload = {"question": utterance, "history": history}

        try:
            await self.send_request(payload)
        except Exception as e:
            print(e)

        try:
            resp = await self.receive_response()
        except Exception as e:
            print(e)

        print(resp)

        return resp["response"], resp["history"], 0

    def getInitHistory(self, init_prompt):
        return [[init_prompt, "好的"]]


class TextDavinci003_API(BaseModel):
    def __init__(self, url) -> None:
        self.url = url

    def predict(self, utterance, history):
        dialogue_str = "".join(
            [f"User:{item[0]}\nAssistant:{item[1]}\n" for item in history]
        ) + "\nUser:{}\nAssistant:".format(utterance)
        # dialogue_str = ''.join([f'用户:{item[0]}\n助手:{item[1]}\n' for item in history]) + '\n用户:{}\n助手:'.format(utterance)
        print("-----------------------------------------")
        print("dialogue_str:\n", dialogue_str)
        print("-----------------------------------------")

        response = completions_with_backoff(
            engine="text-davinci-003",
            # engine='text-davinci-002',
            prompt=dialogue_str,
            n=1,
            max_tokens=1000,  # 设置生成的代码长度
            temperature=0.7,  # 控制输出的多样性，较高的值生成更随机的结果，较低的值生成更确定的结果
        )
        response_str = response.choices[0].text.strip()
        print("finish_reason:\t", response.choices[0].finish_reason)
        print("response:\n", response_str)
        history.append([utterance, response_str])
        return response_str, history, response["usage"]["total_tokens"]

    # response:
    #  {
    #   "choices": [
    #     {
    #       "finish_reason": "stop",
    #       "index": 0,
    #       "logprobs": null,
    #       "text": "\n\ndef double_list(lst):\n    return [x * 2 for x in lst]"
    #     }
    #   ],
    #   "created": 1685419452,
    #   "id": "cmpl-7LkseBxlTSMPloeXvWvWHw2eJvVwp",
    #   "model": "text-davinci-003",
    #   "object": "text_completion",
    #   "usage": {
    #     "completion_tokens": 23,
    #     "prompt_tokens": 51,
    #     "total_tokens": 74
    #   }
    # }

    def close(self):
        pass

    def getInitHistory(self, init_prompt):
        return [[init_prompt, "好的"]]


class GPT35Turbo_API(BaseModel):
    def __init__(self, url) -> None:
        self.url = url

    def getInitHistory(self, init_prompt):
        return [{"role": "system", "content": init_prompt}]

    def predict(self, utterance, history):
        # messages is history
        #     messages=[
        #     {"role": "system", "content": "You are a helpful assistant."},
        #     {"role": "user", "content": "Who won the world series in 2020?"},
        #     {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        #     {"role": "user", "content": "Where was it played?"}
        # ]

        print("-----------------------------------------")
        print("history:\n", history)
        print("-----------------------------------------")
        history.append({"role": "user", "content": utterance})
        response = chat_completions_with_backoff(
            model="gpt-3.5-turbo",
            messages=history,
            n=1,
            max_tokens=1000,  # 设置生成的代码长度
            temperature=0.7,  # 控制输出的多样性，较高的值生成更随机的结果，较低的值生成更确定的结果
        )
        # response = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo",
        #     messages=[
        #             {"role": "system", "content": "You are a helpful assistant."},
        #             {"role": "user", "content": "Who won the world series in 2020?"},
        #             {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        #             {"role": "user", "content": "Where was it played?"}
        #         ],
        #         n=1,
        #         max_tokens=1000,  # 设置生成的代码长度
        #         temperature=0.7,  # 控制输出的多样性，较高的值生成更随机的结果，较低的值生成更确定的结果
        #     )
        response_str = response.choices[0].message.content.strip()
        print("finish_reason:\t", response.choices[0].finish_reason)
        print("response:\n", response_str)
        history.append({"role": "assistant", "content": response_str})
        return response_str, history, response.usage.total_tokens

    # response:
    #  {
    #   "choices": [
    #     {
    #       "finish_reason": "stop",
    #       "index": 0,
    #       "message": {
    #         "content": "The 2020 World Series was played at Globe Life Field in Arlington, Texas due to the COVID-19 pandemic.",
    #         "role": "assistant"
    #       }
    #     }
    #   ],
    #   "created": 1685449137,
    #   "id": "chatcmpl-7LsbRMkFNY5YA7qCapR4Ia5maw7Th",
    #   "model": "gpt-3.5-turbo-0301",
    #   "object": "chat.completion",
    #   "usage": {
    #     "completion_tokens": 24,
    #     "prompt_tokens": 57,
    #     "total_tokens": 81
    #   }
    # }

    def close(self):
        pass
