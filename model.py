import requests
import json


class BaseModel:
    def predict(self, utterance, history):
        pass


class ChatGLM6B_API(BaseModel):
    def __init__(self, url) -> None:
        self.url = url

    def predict(self, utterance, history):
        payload = {
            "question": utterance,
            "history": history
        }
        # 发送 POST 请求
        # response = requests.post(self.url, json=payload, timeout=30)
        response = requests.post(self.url, json=payload, timeout=200)

        # 获取响应结果
        if response.status_code == 200:
            data = response.json()
            if "response" in data.keys():
                return data["response"], data["history"]
            else:
                print(json.dumps(response, ensure_ascii=False, indent=2))
                raise "请求失败"
        else:
            print("请求失败:%d" % (response.status_code))
            raise "请求失败"
