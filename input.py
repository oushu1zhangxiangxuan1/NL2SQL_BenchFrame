import json
from skip_dbs import SkipDBs
from utils import *


class Round:
    def __init__(self, input_map) -> None:
        self.query = input_map.get("query")
        self.utterance = input_map.get("utterance")
        # self.query = input_map.get('query')
        # self.query = input_map.get('query')
        # self.query = input_map.get('query')


class Database:
    def __init__(self, db_id, rounds=[]) -> None:
        self.db_id = db_id
        self.rounds = rounds


class BaseDataLoader:
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self._init = False
        self.databases = []
        # self.interactions = []

    # def getInteractions(self):
    #     pass


class ChaseDataLoader(BaseDataLoader):
    def __init__(self, file_path):
        super().__init__(file_path)

    # @override
    # def getInteractions(self):
    #     print("in ChaseDataLoader interactions")

    #     if self._init:
    #         return self.interactions

    #     with open(self.file_path, "r") as file:
    #         data = json.load(file)
    #         for database in data:
    #             db_id = database.get("database_id")
    #             if db_id in SkipDBs:
    #                 continue
    #             interaction = []
    #             for chat in database.get("interaction"):
    #                 round = Round(chat)
    #                 interaction.append(round)
    #             self.interactions.append(interaction)
    #     self._init = True
    #     return self.interactions

    def getDatabases(self):
        print("in ChaseDataLoader getDatabases")

        if self._init:
            return self.databases

        with open(self.file_path, "r") as file:
            data = json.load(file)
            for database in data:
                db_id = database.get("database_id")
                if db_id in SkipDBs:
                    continue
                interaction = []
                for chat in database.get("interaction"):
                    round = Round(chat)
                    interaction.append(round)
                database = Database(db_id=db_id, rounds=interaction)
                self.databases.append(database)
        self._init = True
        return self.databases



class SparcLoader(BaseDataLoader):
    def __init__(self, file_path):
        super().__init__(file_path)

    def getDatabases(self):
        print("in SparcLoader getDatabases")

        if self._init:
            return self.databases

        with open(self.file_path, "r") as file:
            data = json.load(file)
            for database in data:
                db_id = database.get("database_id")
                if db_id in SkipDBs:
                    continue
                interaction = []
                for chat in database.get("interaction"):
                    round = Round(chat)
                    interaction.append(round)
                database = Database(db_id=db_id, rounds=interaction)
                self.databases.append(database)
        self._init = True
        return self.databases



class CosqlLoader(BaseDataLoader):
    def __init__(self, file_path):
        super().__init__(file_path)

    def getDatabases(self):
        print("in SparcLoader getDatabases")

        if self._init:
            return self.databases

        with open(self.file_path, "r") as file:
            data = json.load(file)
            for database in data:
                db_id = database.get("database_id")
                interaction = []
                for chat in database.get("interaction"):
                    round = Round(chat)
                    interaction.append(round)
                database = Database(db_id=db_id, rounds=interaction)
                self.databases.append(database)
        self._init = True
        return self.databases


class SpiderLoader(BaseDataLoader):
    def __init__(self, file_path):
        super().__init__(file_path)

    def getDatabases(self):
        print("in SpiderLoader getDatabases")

        if self._init:
            return self.databases

        with open(self.file_path, "r") as file:
            data = json.load(file)
            for database in data:
                db_id = database.get("db_id")
                interaction = []
                query = database.get("query")
                utterance = database.get("question")
                round = Round({"query":query, "utterance":utterance})
                interaction.append(round)
                database = Database(db_id=db_id, rounds=interaction)
                self.databases.append(database)
        self._init = True
        return self.databases


if "__main__" == __name__:
    # p = "./data/chase/Chase/chase_dev.json"
    # chaseLoader = ChaseDataLoader(p)
    # inters = chaseLoader.getInteractions()
    # print(
    #     json.dumps(
    #         inters[0], ensure_ascii=False, default=lambda obj: obj.__dict__, indent=2
    #     )
    # )
    # print(
    #     json.dumps(
    #         inters[-1], ensure_ascii=False, default=lambda obj: obj.__dict__, indent=2
    #     )
    # )


    # p = "data/sparc/dev.json"
    # sparcLoader = SparcLoader(p)
    # inters = sparcLoader.getDatabases()
    # print(
    #     json.dumps(
    #         inters[0], ensure_ascii=False, default=lambda obj: obj.__dict__, indent=2
    #     )
    # )
    # print(
    #     json.dumps(
    #         inters[-1], ensure_ascii=False, default=lambda obj: obj.__dict__, indent=2
    #     )
    # )

    if False:
        p = BF_ABS_PATH("data/cosql_dataset/sql_state_tracking/cosql_dev.json")
        cosqlLoader = CosqlLoader(p)
        dbs = cosqlLoader.getDatabases()
        print(json.dumps(
                dbs, ensure_ascii=False, default=lambda obj: obj.__dict__, indent=2
            ))
        print(
            json.dumps(
                dbs[0], ensure_ascii=False, default=lambda obj: obj.__dict__, indent=2
            )
        )
        print(
            json.dumps(
                dbs[-1], ensure_ascii=False, default=lambda obj: obj.__dict__, indent=2
            )
        )

    if True:
        p = BF_ABS_PATH("data/spider/dev.json")
        spiderLoader = SpiderLoader(p)
        dbs = spiderLoader.getDatabases()
        # print(json.dumps(
        #         dbs, ensure_ascii=False, default=lambda obj: obj.__dict__, indent=2
        #     ))
        print(
            json.dumps(
                dbs[0], ensure_ascii=False, default=lambda obj: obj.__dict__, indent=2
            )
        )
        print(
            json.dumps(
                dbs[-1], ensure_ascii=False, default=lambda obj: obj.__dict__, indent=2
            )
        )