from template import system_template_text,user_template_text
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from xiaohongshu_model import Xiaohongshu
def generate_xiaohongshu(theme,api_key):
    prompt = ChatPromptTemplate.from_messages([
        ("system",system_template_text),
        ("user",user_template_text)
    ])
    model = ChatOpenAI(model="gpt-3.5-turbo",
                       api_key=api_key,
                       base_url="https://api.aigc369.com/v1")
    output_parser = PydanticOutputParser(pydantic_object=Xiaohongshu)
    chain = prompt | model | output_parser
    result = chain.invoke({
        "parser_instructions":output_parser.get_format_instructions(),
        "theme":theme
    })
    return result