class Prompt:
    def __init__(
        self, prefix="", suffix="", metadata="", template="", **kwargs
    ) -> None:
        self.prefix = prefix
        self.suffix = suffix
        self.metadata = metadata
        self.template = template

    def generate_input(self, query):
        return "%s%s%s" % (self.prefix, query, self.suffix)

    def raw_prompt(self):
        return "%s%s" % (self.prefix, self.suffix)

    def getInitPrompy(self, metadata):
        return self.init_prompt % metadata


class MetadataPrompt:
    def __init__(
        self, init_prompt="", prefix="", suffix="", metadata="", template="", **kwargs
    ) -> None:
        self.init_prompt = init_prompt
        self.prefix = prefix
        self.suffix = suffix
        self.metadata = metadata
        self.template = template

    def generate_input(self, query):
        return "%s%s%s" % (self.prefix, query, self.suffix)

    def raw_prompt(self):
        return "%s%s" % (
            self.prefix,
            self.suffix,
        )

    def getInitPrompt(self, metadata):
        return self.init_prompt % metadata


MetadataPrompt_1 = MetadataPrompt(
    init_prompt="%s\n根据上面的几个表结构，在后续的对话中将自然语言查询转换为SQL语句，仅以markdown形式输出SQL，不要生成其他无关内容，且确保SQL是完整且正确的。\n 本次只需回答'好的'",
    prefix="结合上下文，将这句自然语言查询转换为完整的SQL语句，仅以markdown形式输出SQL，不要生成其他无关内容，且确保SQL是完整且正确的:",
)


# class BaseSqlPrompt(Prompt):
#     pass


# class BaseSqlPromptEn(Prompt):
#     pass


BaseSqlPrompt_1 = Prompt(prefix="将下列需求转换为SQL: ")

BaseSqlPrompt_2 = Prompt(prefix="请不要修改我提供的字段的大小写，将这句自然语言查询转换为SQL语句: ")

BaseSqlPrompt_2_1 = Prompt(prefix="请不要修改我提供的字段的大小写，将这句自然语言查询转换为完整的SQL语句: ")

BaseSqlPrompt_2_2 = Prompt(prefix="请不要修改我提供的字段的大小写，将这句自然语言查询转换为完整的SQL语句，请简洁回答，无需作出解释: ")

BaseSqlPrompt_2_2 = Prompt(
    prefix="将这句自然语言查询转换为完整的SQL语句，仅以markdown形式输出SQL，不要生成其他无关内容，且确保SQL是完整且正确的:"
)

BaseSqlPrompt_3 = Prompt(
    prefix="当给出一个输入问题时，使用正确的语法回答，并编写相应的SQL代码。在保持创意的同时，确保 SQL 代码是完整且正确的: "
)

BaseSqlPrompt_3_pg = Prompt(
    prefix="当给出一个输入问题时，使用正确的语法回答，并编写相应的 PostgreSQL 代码。在保持创意的同时，确保 SQL 代码是完整且正确的: "
)

# RolePlay
BaseSqlPrompt_4 = Prompt(
    prefix="你是一个精通SQL的高级工程师，当给出一个输入问题时，使用正确的语法回答，并编写相应的 PostgreSQL 代码。在保持创意的同时，确保 SQL 代码是正确的: "
)

BaseSqlPromptEn_1 = Prompt(
    prefix="Given an input question, respond with syntactically correct PostgreSQL. Be creative but the SQL must be correct: "
)

# Single Prompt
SinglePrompt_1 = Prompt(
    prefix="将我后续每轮输入的自然语言查询都转换为SQL语句，不要修改我提供的字段的大小写，请简洁回答，无需作出解释；在保持创意的同时，确保 SQL 代码是完整且正确的"
)

SinglePrompt_SqlOnly = Prompt(
    prefix="将我后续每轮输入的自然语言查询都转换为SQL语句，不要修改我提供的字段的大小写，请简洁回答，仅输出SQL，不要生成其他无关内容；在保持创意的同时，确保SQL代码是完整且正确的"
)


if "__main__" == __name__:
    print(MetadataPrompt_1.getInitPrompt("这里是元数据----------"))
