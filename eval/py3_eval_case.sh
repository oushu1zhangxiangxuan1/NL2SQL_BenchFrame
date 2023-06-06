# #  CHASE ChatGLM-6B-int4-slim
# python py3_evaluation.py \
#     --etype all \
#     --gold ../data/chase/gold_chase.out \
#     --table ../data/chase/Chase/chase_tables.json \
#     --db ../data/chase/database \
#     --skip_db_dir true \
#     --uni_cap false \
#     --pred ../output/predict_ChaseDataLoader_ChatGLM6B_int4_slim_API_MetadataPrompt_1_20230528_123737.out > ../results/chase_chatglm_6b_int4_slim_case.result

# #  CHASE ChatGLM-6B-int8
# python py3_evaluation.py \
#     --etype all \
#     --gold ../data/chase/gold_chase.out \
#     --table ../data/chase/Chase/chase_tables.json \
#     --db ../data/chase/database \
#     --skip_db_dir true \
#     --uni_cap false \
#     --pred ../output/predict_ChaseDataLoader_ChatGLM6B_INT_8_API_MetadataPrompt_1_20230529_100441.out > ../results/chase_chatglm_6b_int8_case.result


# #  CHASE ChatGLM-6B
# python py3_evaluation.py \
#     --etype all \
#     --gold ../data/chase/gold_chase.out \
#     --table ../data/chase/Chase/chase_tables.json \
#     --db ../data/chase/database \
#     --skip_db_dir true \
#     --uni_cap false \
#     --pred ../output/20230601_192646_ChaseDataLoader_ChatGLM6B_API_MetadataMarkdown_CH_1_GLM.out > ../results/chase_chatglm_6b_case.result


# # CAHSE GPT-3.5-turbo
# python py3_evaluation.py \
#     --etype all \
#     --gold ../data/chase/gold_chase.out \
#     --table ../data/chase/Chase/chase_tables.json \
#     --db ../data/chase/database \
#     --skip_db_dir true \
#     --uni_cap false \
#     --pred ../output/20230531_204609_ChaseDataLoader_GPT35Turbo_API_MetadataMarkdown_EN_1.out > ../results/chase_gpt35_turbo_case.result


# # CHASE text-davinci-003 1041
# python py3_evaluation.py \
#     --etype all \
#     --gold ../data/chase/gold_chase_head.out \
#     --pred ../output/20230530_144105_ChaseDataLoader_TextDavinci003_API_MetadataPrompt_2.out \
#     --table ../data/chase/Chase/chase_tables.json \
#     --db ../data/chase/database \
#     --uni_cap false \
#     --skip_db_dir true > ../results/chase_text_davinci_003_1041_case.result


# # CoSQL ChatGLM-6B-int8
python py3_evaluation.py \
    --etype all \
    --gold ../data/cosql_dataset/sql_state_tracking/dev_gold.txt \
    --pred ../output/20230603_113841_CosqlLoader_ChatGLM6B_API_MetadataMarkdown_CH_1_GLM.out \
    --table ../data/cosql_dataset/tables.json \
    --db ../data/cosql_dataset/database \
    --uni_cap false \
    --skip_db_dir false > ../results/cosql_chatglm_6b_case.result



# # CoSQL gpt-3.5-turbo
# python py3_evaluation.py \
#     --etype all \
#     --gold ../data/cosql_dataset/sql_state_tracking/dev_gold.txt \
#     --pred ../output/20230530_204015_CosqlLoader_GPT35Turbo_API_MetadataMarkdown_EN_1.out \
#     --table ../data/cosql_dataset/tables.json \
#     --db ../data/cosql_dataset/database \
#     --uni_cap false \
#     --skip_db_dir false > ../results/cosql_gpt35_turbo_case.result


# # CoSQL text-davinci-003
# python py3_evaluation.py \
#     --etype all \
#     --gold ../data/cosql_dataset/sql_state_tracking/dev_gold.txt \
#     --pred ../output/20230601_114822_CosqlLoader_TextDavinci003_API_MetadataMarkdown_EN_1.out \
#     --table ../data/cosql_dataset/tables.json \
#     --db ../data/cosql_dataset/database \
#     --uni_cap false \
#     --skip_db_dir false > ../results/cosql_text_davinci_003_case.result
