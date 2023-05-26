def reverse_lines(input_file_path, output_file_path):
    with open(input_file_path, "r") as input_file:
        lines = input_file.readlines()

    reversed_lines = reversed(lines)

    with open(output_file_path, "w") as output_file:
        output_file.writelines(reversed_lines)


# 示例用法
# input_file_path = './output/predict_ChaseDataLoader_ChatGLM6B_API_BaseSqlPrompt_2_2_20230524_204343.out'
# output_file_path = './output/revert_predict_ChaseDataLoader_ChatGLM6B_API_BaseSqlPrompt_2_2_20230524_204343.out'

input_file_path = "./gold/gold_chase.out"
output_file_path = "./gold/revert_gold_chase.out"
reverse_lines(input_file_path, output_file_path)
