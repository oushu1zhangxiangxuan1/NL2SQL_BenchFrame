python py3_evaluation.py \
    --etype all \
    --gold ../gold/revert_gold_chase.out \
    --pred ../output/revert_predict_ChaseDataLoader_ChatGLM6B_API_BaseSqlPrompt_2_2_20230524_204343.out \
    --table ../data/chase/Chase/chase_tables.json \
    --db ../data/chase/database \
    --skip_db_dir true
