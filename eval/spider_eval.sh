
# GPT_3.5_turbo
# python spider_evaluation.py \
#     --etype all \
#     --gold ../data/spider/dev_gold.sql \
#     --table ../data/spider/tables.json \
#     --db ../data/spider/database \
#     --pred ../output/20230531_111859_SpiderLoader_GPT35Turbo_API_MetadataMarkdown_EN_1.out



# chatglm_6b
python spider_evaluation.py \
    --etype all \
    --gold ../data/spider/dev_gold.sql \
    --table ../data/spider/tables.json \
    --db ../data/spider/database \
    --pred ../output/20230602_141350_SpiderLoader_ChatGLM6B_API_MetadataMarkdown_CH_1_GLM.out > ../results/spider_chatglm_6b.result


