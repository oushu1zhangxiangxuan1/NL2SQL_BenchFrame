from input import ChaseDataLoader
from prompt import *  # BaseSqlPrompt_1, BaseSqlPrompt_2, BaseSqlPrompt_3, BaseSqlPrompt_4, BaseSqlPromptEn_1
from model import ChatGLM6B_API
import os
from datetime import datetime
from prompt_mode import PromptMode

# 获取当前脚本的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))

# 将当前路径设置为环境变量
os.environ["NL2SQL_BENCHFRAME_HOME"] = current_dir


def BF_ABS_PATH(relative_path):
    return os.path.abspath(
        os.path.join(os.environ.get("NL2SQL_BENCHFRAME_HOME", ""), relative_path)
    )


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


def getPredictOutFile(config):
    return os.path.join(
        config.OutputDir,
        "predict_%s_%s_%s_%s.out"
        % (
            get_variable_name(config.InputDataLoader),
            get_class_name(config.Model),
            get_variable_name(config.Prompter),
            datetime.now().strftime("%Y%m%d_%H%M%S"),
        ),
    )


class ChaseConfig(BenchConfig):
    # TODO: 改为通过基类的staticmethod进行访问
    InputDir = BF_ABS_PATH("./data/chase/ChaseNoAscii/chase_dev.json")
    OutputDir = BF_ABS_PATH("./output")
    GoldFile = BF_ABS_PATH("./gold/gold_chase.out")
    InputDataLoader = ChaseDataLoader
    Prompter = MetadataPrompt_1
    Model = ChatGLM6B_API("http://localhost:7861/chat-docs/chatno")
    PromptMode = PromptMode.Single
    # SkipDBs = [
    #     "tvshow",
    #     "concert_singer",
    #     "car_1",
    #     "orchestra",
    #     "museum_visit",
    #     "singer",
    #     "cre_Doc_Template_Mgt",
    #     "real_estate_properties",
    #     "employee_hire_evaluation",
    #     "poker_player",
    #     "student_transcripts_tracking",
    #     "pets_1",
    #     "flight_2",
    #     "dog_kennels",
    #     "course_teach",
    #     "network_1",
    #     "world_1",
    #     "voter_1",
    #     "wta_1",
    #     "battle_death",
    # ]
    MetadataFile = "data/chase/chase_meta_sql.json"

    def __init__(self) -> None:
        super().__init__()


CurrentConfig = ChaseConfig


if "__main__" == __name__:
    print(getPredictOutFile(CurrentConfig))
    print(CurrentConfig.InputDir)
