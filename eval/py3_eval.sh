# CHASE
# python py3_evaluation.py \
#     --etype all \
#     --gold ../data/chase/gold_chase_head.out \
#     --pred ../output/20230530_144105_ChaseDataLoader_TextDavinci003_API_MetadataPrompt_2.out \
#     --table ../data/chase/Chase/chase_tables.json \
#     --db ../data/chase/database \
#     --uni_cap true \
#     --skip_db_dir true

# CoSQL gpt-3.5-turbo
# python py3_evaluation.py \
#     --etype all \
#     --gold ../data/cosql_dataset/sql_state_tracking/dev_gold.txt \
#     --pred ../output/20230530_204015_CosqlLoader_GPT35Turbo_API_MetadataMarkdown_EN_1.out \
#     --table ../data/cosql_dataset/tables.json \
#     --db ../data/cosql_dataset/database \
#     --uni_cap true \
#     --skip_db_dir false


#  CHASE ChatGLM-6B-int8
# python py3_evaluation.py \
#     --etype all \
#     --gold ../data/chase/gold_chase.out \
#     --table ../data/chase/Chase/chase_tables.json \
#     --db ../data/chase/database \
#     --skip_db_dir true \
#     --uni_cap true \
#     --pred ../output/predict_ChaseDataLoader_ChatGLM6B_API_MetadataPrompt_1_20230529_100441.out



#  CHASE ChatGLM-6B
# python py3_evaluation.py \
#     --etype all \
#     --gold ../data/chase/gold_chase.out \
#     --table ../data/chase/Chase/chase_tables.json \
#     --db ../data/chase/database \
#     --skip_db_dir true \
#     --uni_cap true \
#     --pred ../output/20230601_192646_ChaseDataLoader_ChatGLM6B_API_MetadataMarkdown_CH_1_GLM.out



# CAHSE GPT-3.5-turbo
# python py3_evaluation.py \
#     --etype all \
#     --gold ../data/chase/gold_chase.out \
#     --table ../data/chase/Chase/chase_tables.json \
#     --db ../data/chase/database \
#     --skip_db_dir true \
#     --uni_cap true \
#     --pred ../output/20230531_204609_ChaseDataLoader_GPT35Turbo_API_MetadataMarkdown_EN_1.out


# CoSQL ChatGLM-6B-int8
python py3_evaluation.py \
    --etype all \
    --gold ../data/cosql_dataset/sql_state_tracking/dev_gold.txt \
    --pred ../output/20230603_113841_CosqlLoader_ChatGLM6B_API_MetadataMarkdown_CH_1_GLM.out \
    --table ../data/cosql_dataset/tables.json \
    --db ../data/cosql_dataset/database \
    --uni_cap true \
    --skip_db_dir false



# CoSQL text-davinci-003
# python py3_evaluation.py \
#     --etype all \
#     --gold ../data/cosql_dataset/sql_state_tracking/dev_gold.txt \
#     --pred ../output/20230601_114822_CosqlLoader_TextDavinci003_API_MetadataMarkdown_EN_1.out \
#     --table ../data/cosql_dataset/tables.json \
#     --db ../data/cosql_dataset/database \
#     --uni_cap true \
#     --skip_db_dir false