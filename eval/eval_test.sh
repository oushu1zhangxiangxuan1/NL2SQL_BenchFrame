python py3_evaluation.py \
    --etype all \
    --gold ../data/chase/gold_chase_test.out \
    --pred ../output/predict_ChaseDataLoader_ChatGLM6B_API_MetadataPrompt_1_20230526_102909.out \
    --table ../data/chase/Chase/chase_tables.json \
    --db ../data/chase/database \
    --skip_db_dir true
