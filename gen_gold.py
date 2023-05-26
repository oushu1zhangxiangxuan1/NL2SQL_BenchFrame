from skip_dbs import SkipDBs
import json


class GoldParser:
    def __init__(self, gold_ore, coffer) -> None:
        self.gold_ore = gold_ore
        self.coffer = coffer

    def smelt(self):
        pass


class ChaseGoldParser(GoldParser):
    def smelt(self):
        ore_json = None
        with open(self.gold_ore, "r") as ore_file:
            ore_json = json.load(ore_file)

        with open(self.coffer, "w") as coffer_file:
            for db in ore_json:
                db_id = db.get("database_id")
                if db_id in SkipDBs:
                    continue
                for round in db.get("interaction"):
                    query = round.get("query")
                    gold = "%s\t%s\n" % (query, db_id)
                    coffer_file.write(gold)
                    coffer_file.flush()
                coffer_file.write("\n")
                coffer_file.flush()


CurrentGoldParser = ChaseGoldParser


def gen_gold():
    parser = CurrentGoldParser(InputDir, GoldFile)
    parser.smelt()


if "__main__" == __name__:
    gen_gold()
