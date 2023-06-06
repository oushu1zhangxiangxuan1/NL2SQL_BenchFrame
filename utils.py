import re
import os
import argparse
import backoff
import openai

openai.api_base = 'https://api.openai-proxy.com/v1' 


# 获取当前脚本的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))

# 将当前路径设置为环境变量
os.environ["NL2SQL_BENCHFRAME_HOME"] = current_dir


@backoff.on_exception(backoff.expo, (openai.error.RateLimitError, openai.error.ServiceUnavailableError))
def completions_with_backoff(**kwargs):
    return openai.Completion.create(**kwargs)


@backoff.on_exception(backoff.expo, (openai.error.RateLimitError, openai.error.ServiceUnavailableError))
def chat_completions_with_backoff(**kwargs):
    return openai.ChatCompletion.create(**kwargs)


def remove_chars(string):
    chars_to_remove = " ;"  # 要去除的字符

    # 去除开头的字符
    while string and (string[0] in chars_to_remove):
        string = string[1:]

    # 去除结尾的字符
    while string and (string[-1] in chars_to_remove):
        string = string[:-1]

    return string


def parseOneLineSqlFromQuery(query):
    pattern = r"```(.*?)```"
    match = re.search(pattern, query, re.DOTALL)

    if match:
        sql = match.group(1)
        sql = sql.replace("sql", "", 1)
        sql = sql.replace("\n", " ")
        sql = re.sub(r"\s+", " ", sql)
        sql = remove_chars(sql)
        if len(sql) == 0:
            return "NO SQL FOUND\n"
        return sql + "\n"
    else:
        return parseSqlQueryRaw(query)



def parseSqlQueryRaw(sql):
    sql = sql.replace("\n", " ")
    sql = re.sub(r"\s+", " ", sql)
    sql = remove_chars(sql)
    if len(sql) == 0:
        return "NO SQL FOUND\n"
    return sql + "\n"


def get_all_file_paths(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.sqlite'):
                file_path = os.path.join(root, file)
                file_paths.append(file_path)
    return file_paths


def get_sqlite_path_cascade(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths


def str_to_bool(value):
    if isinstance(value, bool):
        return value
    if value.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif value.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Invalid value for --test argument')


def BF_ABS_PATH(relative_path):
    return os.path.abspath(
        os.path.join(os.environ.get("NL2SQL_BENCHFRAME_HOME", ""), relative_path)
    )


if "__main__" == __name__:
    # query = """
    # 你啊哈哦送达发生发顺丰 ```sql SELECT * FROM
    # t1 
    # join 
    # t2 sql```aasfas
    # asfasfa
    # """
    # query = """
    # 你啊哈哦送达发生发顺丰 ``` SELECT * FROM
    # t1 ```aasfas
    # ```asfasfa```
    # """
    # print(parseOneLineSqlFromQuery(query))

    # query = "This is some text.\n```sql\nSELECT *\nFROM table\nWHERE condition\n``` More text."
    # sql = parseOneLineSqlFromQuery(query)
    # print(sql)  # 输出: SELECT * FROM table WHERE condition

    # query = "This is some text.\n```sql\nSELECT *\nFROM table\n\nWHERE condition\n\nAND another_condition\n``` More text."
    # sql = parseOneLineSqlFromQuery(query)
    # print(sql)  # 输出: SELECT * FROM table WHERE condition AND another_condition

    # query = "This is some text."
    # sql = parseOneLineSqlFromQuery(query)
    # print(sql)  # 输出: NO SQL FOUND

    # query = "This is some text.\n```sql\nSELECT *\nFROM    table\nWHERE  condition\n``` More text."
    # sql = parseOneLineSqlFromQuery(query)
    # print(sql)  # 输出: SELECT * FROM table WHERE condition

    # query = "This is some text.\n```sql\nSELECT *\nFROM     table\n\nWHERE    condition\n\nAND another_condition\n``` More text."
    # sql = parseOneLineSqlFromQuery(query)
    # print(sql)  # 输出: SELECT * FROM table WHERE condition AND another_condition

    # query = "This is some text."
    # sql = parseOneLineSqlFromQuery(query)
    # print(sql)  # 输出: NO SQL FOUND


    query = """SELECT * FROM
    t1 
    join 
    t2 sql
    """
    print(parseSqlQueryRaw(query))
