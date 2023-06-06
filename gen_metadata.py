import os
import sqlite3
import json
from utils import *


def extract_table_sql(db_file):
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT name, sql FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()

    table_sql = {}
    for table in tables:
        table_name = table["name"]
        sql = table["sql"]
        table_sql[table_name] = sql

    conn.close()
    return table_sql


def process_sqlite_files(file_list):
    database_tables = {}
    for db_file in file_list:
        if os.path.isfile(db_file) and db_file.endswith(".sqlite"):
            db_name = os.path.splitext(os.path.basename(db_file))[0]
            print(db_name)
            table_sql = extract_table_sql(db_file)
            database_tables[db_name] = table_sql

    return database_tables


def write_json_file(data, output_file):
    with open(output_file, "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    # CAHSE
    if False:
        sqlite_files = get_all_file_paths("./data/chase/database")  # 替换为您的SQLite文件列表
        output_file = "./metadata/chase_meta_sql.json"  # 替换为输出的JSON文件路径

        database_tables = process_sqlite_files(sqlite_files)
        write_json_file(database_tables, output_file)

        print("建表SQL提取完成并写入JSON文件。")

    # CoSQL
    if False:
        sqlite_files = get_all_file_paths("data/cosql_dataset/database")  # 替换为您的SQLite文件列表
        output_file = BF_ABS_PATH("data/cosql_dataset/meta_sql.json")  # 替换为输出的JSON文件路径

        database_tables = process_sqlite_files(sqlite_files)
        write_json_file(database_tables, output_file)

        print("建表SQL提取完成并写入JSON文件。")

    # Spider
    if True:
        sqlite_files = get_all_file_paths("data/spider/database")  # 替换为您的SQLite文件列表
        output_file = BF_ABS_PATH("data/spider/meta_sql.json")  # 替换为输出的JSON文件路径

        database_tables = process_sqlite_files(sqlite_files)
        write_json_file(database_tables, output_file)

        print("建表SQL提取完成并写入JSON文件。")