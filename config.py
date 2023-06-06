from input import *
from prompt import *  # BaseSqlPrompt_1, BaseSqlPrompt_2, BaseSqlPrompt_3, BaseSqlPrompt_4, BaseSqlPromptEn_1
from model import *
import os
from datetime import datetime
from prompt_mode import *
from utils import *


class BenchConfig:
    InputDir = None
    OutputDir = None
    InputDataLoader = None
    Prompter = None
    Model = None
    PromptMode = None


def get_variable_name(obj):
    for var_name, var_value in globals().items():
        if var_value is obj:
            return var_name
    raise "no var defined"
    # return None


def get_class_name(obj):
    return obj.__class__.__name__


def getPredictJsonL(config):
    return os.path.join(
        config.OutputDir,
        "predict_%s_%s_%s_%s.jsonl"
        % (
            get_variable_name(config.InputDataLoader),
            get_class_name(config.Model),
            get_variable_name(config.Prompter),
            datetime.now().strftime("%Y%m%d_%H%M%S"),
        ),
    )


def getPredictOutFile(config, isTest):
    fileName = "%s_%s_%s_%s.out" % (
            datetime.now().strftime("%Y%m%d_%H%M%S"),
            get_variable_name(config.InputDataLoader),
            get_class_name(config.Model),
            get_variable_name(config.Prompter),
        )
    if isTest:
        fileName = 'test_'+fileName
    return os.path.join(
        config.OutputDir,
        fileName)


class ChaseConfig(BenchConfig):
    # TODO: 改为通过基类的staticmethod进行访问
    InputDir = BF_ABS_PATH("./data/chase/ChaseNoAscii/chase_dev.json")
    OutputDir = BF_ABS_PATH("./output")
    GoldFile = BF_ABS_PATH("./gold/gold_chase.out")
    InputDataLoader = ChaseDataLoader
    Prompter = MetadataPrompt_1
    Model = ChatGLM6B_API("http://localhost:7861/chat-docs/chatno")
    PromptMode = PromptMode.Single
    MetadataFile = BF_ABS_PATH("data/chase/chase_meta_sql.json")
    ParseQueryFunc = parseOneLineSqlFromQuery
    TurnMode = TurnMode.Multi


class ChaseConfig_SOCK(BenchConfig):
    # TODO: 改为通过基类的staticmethod进行访问
    InputDir = BF_ABS_PATH("./data/chase/ChaseNoAscii/chase_dev.json")
    OutputDir = BF_ABS_PATH("./output")
    GoldFile = BF_ABS_PATH("data/chase/gold_chase.out")
    InputDataLoader = ChaseDataLoader
    Prompter = MetadataPrompt_1
    Model = ChatGLM6B_SOCK("ws://localhost:7862/chat-docs/chatno/socket")
    PromptMode = PromptMode.Single
    MetadataFile =  BF_ABS_PATH("data/chase/chase_meta_sql.json")
    ParseQueryFunc = parseOneLineSqlFromQuery
    TurnMode = TurnMode.Multi


class ChaseConfig_TextDavinci003(BenchConfig):
    # TODO: 改为通过基类的staticmethod进行访问
    InputDir = BF_ABS_PATH("./data/chase/ChaseNoAscii/chase_dev.json")
    OutputDir = BF_ABS_PATH("./output")
    GoldFile = BF_ABS_PATH("data/chase/gold_chase.out")
    InputDataLoader = ChaseDataLoader
    Prompter = MetadataPrompt_2
    Model = TextDavinci003_API(None)
    PromptMode = PromptMode.Single
    MetadataFile = BF_ABS_PATH("data/chase/chase_meta_sql.json")
    ParseQueryFunc = parseSqlQueryRaw
    TurnMode = TurnMode.Multi


class CosqlConfig_TextDavinci003(BenchConfig):
    # TODO: 改为通过基类的staticmethod进行访问
    InputDir = BF_ABS_PATH("data/cosql_dataset/sql_state_tracking/cosql_dev.json")
    OutputDir = BF_ABS_PATH("./output")
    GoldFile = BF_ABS_PATH("data/cosql_dataset/sql_state_tracking/dev_gold.txt")
    InputDataLoader = CosqlLoader
    Prompter = MetadataMarkdown_EN_1
    Model = TextDavinci003_API(None)
    PromptMode = PromptMode.Single
    MetadataFile = BF_ABS_PATH("data/cosql_dataset/meta_sql.json")
    ParseQueryFunc = parseSqlQueryRaw
    TurnMode = TurnMode.Multi


class SpiderConfig_TextDavinci003(BenchConfig):
    # TODO: 改为通过基类的staticmethod进行访问
    InputDir = BF_ABS_PATH("data/spider/dev.json")
    OutputDir = BF_ABS_PATH("./output")
    GoldFile = BF_ABS_PATH("data/spider/dev_gold.sql")
    InputDataLoader = SpiderLoader
    Prompter = MetadataMarkdown_EN_1
    Model = TextDavinci003_API(None)
    PromptMode = PromptMode.Single
    MetadataFile = BF_ABS_PATH("data/spider/tables.json")
    ParseQueryFunc = parseSqlQueryRaw
    TurnMode = TurnMode.Single


class CosqlConfig_GPT35Turbo(BenchConfig):
    # TODO: 改为通过基类的staticmethod进行访问
    InputDir = BF_ABS_PATH("data/cosql_dataset/sql_state_tracking/cosql_dev.json")
    OutputDir = BF_ABS_PATH("./output")
    GoldFile = BF_ABS_PATH("data/cosql_dataset/sql_state_tracking/dev_gold.txt")
    InputDataLoader = CosqlLoader
    Prompter = MetadataMarkdown_EN_1
    Model = GPT35Turbo_API(None)
    PromptMode = PromptMode.Single
    MetadataFile = BF_ABS_PATH("data/cosql_dataset/meta_sql.json")
    ParseQueryFunc = parseSqlQueryRaw
    TurnMode = TurnMode.Multi


class SpiderConfig_GPT35Turbo(BenchConfig):
    # TODO: 改为通过基类的staticmethod进行访问
    InputDir = BF_ABS_PATH("data/spider/dev.json")
    OutputDir = BF_ABS_PATH("./output")
    GoldFile = BF_ABS_PATH("data/spider/dev_gold.sql")
    InputDataLoader = SpiderLoader
    Prompter = MetadataMarkdown_EN_1
    Model = GPT35Turbo_API(None)
    PromptMode = PromptMode.Single
    MetadataFile = BF_ABS_PATH("data/spider/meta_sql.json")
    ParseQueryFunc = parseSqlQueryRaw
    TurnMode = TurnMode.Single



class ChaseConfig_GPT35Turbo(BenchConfig):
    # TODO: 改为通过基类的staticmethod进行访问
    InputDir = BF_ABS_PATH("./data/chase/ChaseNoAscii/chase_dev.json")
    OutputDir = BF_ABS_PATH("./output")
    GoldFile = BF_ABS_PATH("data/chase/gold_chase.out")
    InputDataLoader = ChaseDataLoader
    Prompter = MetadataMarkdown_EN_1
    Model = GPT35Turbo_API(None)
    PromptMode = PromptMode.Single
    MetadataFile = BF_ABS_PATH("data/chase/chase_meta_sql.json")
    ParseQueryFunc = parseSqlQueryRaw
    TurnMode = TurnMode.Multi


class CosqlConfig_ChatGLM6B(BenchConfig):
    # TODO: 改为通过基类的staticmethod进行访问
    InputDir = BF_ABS_PATH("data/cosql_dataset/sql_state_tracking/cosql_dev.json")
    OutputDir = BF_ABS_PATH("./output")
    GoldFile = BF_ABS_PATH("data/cosql_dataset/sql_state_tracking/dev_gold.txt")
    InputDataLoader = CosqlLoader
    Prompter = MetadataMarkdown_CH_1_GLM
    Model = ChatGLM6B_API("http://localhost:7861/chat-docs/chatno")
    PromptMode = PromptMode.Single
    MetadataFile = BF_ABS_PATH("data/cosql_dataset/meta_sql.json")
    ParseQueryFunc = parseSqlQueryRaw
    TurnMode = TurnMode.Multi


class SpiderConfig_ChatGLM6B(BenchConfig):
    # TODO: 改为通过基类的staticmethod进行访问
    InputDir = BF_ABS_PATH("data/spider/dev.json")
    OutputDir = BF_ABS_PATH("./output")
    GoldFile = BF_ABS_PATH("data/spider/dev_gold.sql")
    InputDataLoader = SpiderLoader
    # Prompter = MetadataMarkdown_EN_1
    Prompter = MetadataMarkdown_CH_1_GLM
    Model = ChatGLM6B_API("http://localhost:7861/chat-docs/chatno")
    PromptMode = PromptMode.Single
    MetadataFile = BF_ABS_PATH("data/spider/meta_sql.json")
    ParseQueryFunc = parseSqlQueryRaw
    TurnMode = TurnMode.Single


class ChaseConfig_ChatGLM6B(BenchConfig):
    # TODO: 改为通过基类的staticmethod进行访问
    InputDir = BF_ABS_PATH("./data/chase/ChaseNoAscii/chase_dev.json")
    OutputDir = BF_ABS_PATH("./output")
    GoldFile = BF_ABS_PATH("./gold/gold_chase.out")
    InputDataLoader = ChaseDataLoader
    Prompter = MetadataMarkdown_CH_1_GLM
    Model = ChatGLM6B_API("http://localhost:7861/chat-docs/chatno")
    PromptMode = PromptMode.Single
    MetadataFile = BF_ABS_PATH("data/chase/chase_meta_sql.json")
    ParseQueryFunc = parseOneLineSqlFromQuery
    TurnMode = TurnMode.Multi

# CurrentConfig = ChaseConfig_SOCK
CurrentConfig = CosqlConfig_ChatGLM6B


if "__main__" == __name__:
    print(getPredictOutFile(CurrentConfig))
    print(CurrentConfig.InputDir)
