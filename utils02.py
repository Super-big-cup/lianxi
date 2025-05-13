from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain

def get_chat_response(prompt,memory,api_key):
    model = ChatOpenAI(model="gpt-3.5-turbo",
                       api_key=api_key,
                       base_url="https://api.aigc369.com/v1")

    chain = ConversationChain(llm=model,memory=memory)

    response=chain.invoke({"input":prompt})
    return response["response"]