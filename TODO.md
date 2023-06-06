1. 处理CHASE的gold.out  DONE

2. 处理超时Fallback    DONE

3. evaluation 无法区分大小写  DONE

4. evaluation 没有明确输出IM和QM

5. 两次timeout后infer脚本直接挂了？

3. 优化Prompt
   1. 降低输入次数，Mode改为Single    DONE
   
   2. 通过Prompt控制，精简模型输出，从而降低history的累积  DONE
   
   3. 每次都处理history，精简history
   
      1. 只保留模型输出的sql
      2. 直接将输出设置为空字符串
   
   4. 直接不要history，把init prompt 和 每次的问题合并，让其输出一个sql
   
   5. Catorygol类型的列需要把值列出来，并加上释义
   
   6. 把query history全部拼接成一个query，或者把history中的response置空
   
      ![image-20230526134701360](/Users/johnsaxon/Library/Application Support/typora-user-images/image-20230526134701360.png)
   
7. 6B 在长输入下OOM，或者超时

   - [ ] 直接通过CLI访问MODEL，避免timeout
   - [ ] 但是如果这样会导致需要装不同的conda虚拟环境以支持不同的model
   - [ ] 可以尝试使用websocket进行连接尝试
   - [ ] 尝试将模型平均分布到两张卡上，减轻0卡压力，1卡算力目前也没利用起来

### Benchmark

- Spider
- CoSQL
- CHASE  



### Model

##### ChatGLM-6B 

   - int4
   - int8
   - raw

##### OpenAI

- GPT-4
- TextDavinci003
- GPT-3.5-Turbo

##### Prompt

- 无Prompt
- Metadata Prompt
  - ddl
  - NL(自然语言)
- 单轮Prompt VS 每轮Prompt

##### History

    - 不加history
        - 加history
      - 单加问题
      - 问题加模型response



- [ ] evaluation的EX下的QM和IM可能不太准？需要看代码，特别是all的时候，一直是0
- [x] ChatGLM-6B 解决OOM问题
- [ ] 不通过API访问，通过CLI访问，避免TIMEOUT
- [x] 去掉大小写转换，可能会导致EX结果偏低



#### OpenAI 模型评估费用预测(Prompt 中带元数据跑一轮完成的评估)

| 模型             | 单价            | CHASE | CoSQL | Spider |
| ---------------- | --------------- | ----- | ----- | ------ |
| text-davinci-003 | 0.02/1K tokens  | 25$   | 25$   | 25$    |
| GPT-3.5-turbo    | 0.002/1K tokens | 2.5$  | 2.5$  | 2.5$   |
| GPT-4            | 0.2/1K tokens   | 250$  | 250$  | 250$   |



#### 评估结果

见 Benckmarks.xlsx

