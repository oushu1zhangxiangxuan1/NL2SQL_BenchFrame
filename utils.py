import re
import os


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
        return "NO SQL FOUND\n"


def get_all_file_paths(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths


if "__main__" == __name__:
    query = """
    你啊哈哦送达发生发顺丰 ```sql SELECT * FROM
    t1 
    join 
    t2 sql```aasfas
    asfasfa
    """
    # query = """
    # 你啊哈哦送达发生发顺丰 ``` SELECT * FROM
    # t1 ```aasfas
    # ```asfasfa```
    # """
    print(parseOneLineSqlFromQuery(query))

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
