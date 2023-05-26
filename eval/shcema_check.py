import os
from py3_process_sql import get_schema, Schema


def get_all_file_paths(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths


def check(directory):
    file_paths = get_all_file_paths(directory)
    for file_path in file_paths:
        schema = Schema(get_schema(file_path))
        if len(schema.schema) == 0:
            print(file_path)


p = "./data/chase/database"
check(p)
