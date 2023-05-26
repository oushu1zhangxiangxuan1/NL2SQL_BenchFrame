# import jsonlines
from config import CurrentConfig, getPredictJsonL, getPredictOutFile
from prompt_mode import PromptMode
from utils import parseOneLineSqlFromQuery
import json


def getDatabases():
    return CurrentConfig.InputDataLoader(CurrentConfig.InputDir).getDatabases()


def getPrompt():
    return CurrentConfig.Prompter


def getModel():
    # 获取模型
    return CurrentConfig.Model


def initMetaData():
    with open(CurrentConfig.MetadataFile, "r") as mf:
        return json.load(mf)
    return None


databases = getDatabases()
predictJsonL = getPredictJsonL(CurrentConfig)
predictOutFile = getPredictOutFile(CurrentConfig)
prompter = getPrompt()
model = getModel()
metaData = initMetaData()


def getMetaData(db_id):
    tables = metaData.get(db_id)
    sqls = []
    for name, sql in tables.items():
        sqls.append(sql)
    return "\n".join(sqls)


# metadata


# def infer_jsonl():
#     with jsonlines.open(predictJsonL, mode="w") as writer:
#         for db.rounds in databases[:1]:
#             item = []
#             history = []
#             if CurrentConfig.PromptMode == PromptMode.Single:
#                 init_prompt = prompter.getInitPrompt(metadata="")
#                 chat = {"utterance": init_prompt}
#                 chat["utterance_with_prompt"] = init_prompt
#                 query, history = model.predict(init_prompt, history)
#                 chat["query"] = query
#                 item.append(chat)

#                 for i, round in enumerate(db.rounds):
#                     print("Round %d" % i)
#                     print("utterance: %s" % round.utterance)
#                     chat = {"utterance": round.utterance}
#                     # utterance_with_prompt = prompter.generate_input(utterance, getMetaData())  # TODO: 在已提供RawPrompt的情况下，还需要再依据MetaData形成新的Prompt
#                     utterance_with_prompt = prompter.generate_input(round.utterance)
#                     chat["utterance_with_prompt"] = utterance_with_prompt
#                     query, history = model.predict(round.utterance, history)
#                     print("query: %s" % query)
#                     chat["query"] = query
#                     item.append(chat)

#             else:
#                 for i, round in enumerate(db.rounds):
#                     print("Round %d" % i)
#                     print("utterance: %s" % round.utterance)
#                     chat = {"utterance": round.utterance}
#                     utterance_with_prompt = prompter.generate_input(round.utterance)
#                     chat["utterance_with_prompt"] = utterance_with_prompt
#                     query, history = model.predict(round.utterance, history)
#                     print("query: %s" % query)
#                     chat["query"] = query
#                     item.append(chat)
#                 # 将  utterance,   utterance_with_prompt,  response 整合放入jsonl
#                 writer.write(item)


def infer_out():
    with open(predictOutFile, mode="w") as writer:
        for db in databases[:2]:
            # for db in databases:
            history = []
            if CurrentConfig.PromptMode == PromptMode.Single:
                metadata = getMetaData(db.db_id)
                init_prompt = prompter.getInitPrompt(metadata=metadata)
                print("init_prompt:")
                print(init_prompt)
                query, history = model.predict(init_prompt, history)

                for i, round in enumerate(db.rounds):
                    print("Round %d" % i)
                    print("---------------------history----------------------------\n")
                    print(history)
                    print()
                    print("---------------------history----------------------------\n")
                    print("utterance: %s" % round.utterance)
                    # utterance_with_prompt = prompter.generate_input(utterance, getMetaData())  # TODO: 在已提供RawPrompt的情况下，还需要再依据MetaData形成新的Prompt
                    # utterance_with_prompt = prompter.generate_input(round.utterance)
                    try:
                        utterance_with_prompt = prompter.generate_input(round.utterance)
                        print("utterance_with_prompt: %s" % utterance_with_prompt)
                        query, history = model.predict(utterance_with_prompt, history)
                        print("query: %s" % query)
                        sql = parseOneLineSqlFromQuery(query)
                        writer.write(sql)
                    except Exception as e:
                        print(e)
                        writer.write("SQL NOT GET: may be TIMEOUT\n")
                    finally:
                        writer.flush()
                writer.write("\n")

            else:
                for i, round in enumerate(db.rounds):
                    print("Round %d" % i)
                    print("---------------------history----------------------------\n")
                    print(history)
                    print()
                    print("---------------------history----------------------------\n")
                    print("utterance: %s" % round.utterance)
                    utterance_with_prompt = prompter.generate_input(round.utterance)
                    print("utterance_with_prompt: %s" % utterance_with_prompt)
                    try:
                        query, history = model.predict(utterance_with_prompt, history)
                        print("query: %s" % query)
                        sql = parseOneLineSqlFromQuery(query)
                        writer.write(sql)
                    except Exception as e:
                        print(e)
                        writer.write("SQL NOT GET: may be TIMEOUT\n")
                    finally:
                        writer.flush()
                writer.write("\n")


if "__main__" == __name__:
    infer_out()
