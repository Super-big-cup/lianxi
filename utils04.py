from langchain_openai import ChatOpenAI
from ts import PROMPT_TEMPLATE
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import json

def dataframe_agent(api_key,df,query):
    model = ChatOpenAI(api_key=api_key,
                       temperature=0,
                       model="gpt-3.5-turbo",
                       base_url="https://api.aigc369.com/v1",
                       max_retries=3
                       )
    agents = create_pandas_dataframe_agent(llm=model,
                                           df=df,
                                           verbose=True,
                                           agent_executor_kwargs={"handle_parsing_errors": True},
                                           allow_dangerous_code=True)
    prompt = PROMPT_TEMPLATE + query
    response = agents.invoke({"input":prompt})
    response_dict = json.loads(response["output"])
    return response_dict