from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain

def pa_chain(api_key,memory,uploaded_file,question):
    model = ChatOpenAI(model="gpt-3.5-turbo",
                       api_key=api_key,
                       base_url="https://api.aigc369.com/v1")
    file_uploaded = uploaded_file.read()
    temp_file_path = "temp.pdf"
    with open(temp_file_path,"wb") as temp_file:
        temp_file.write(file_uploaded)
    loder = PyPDFLoader(temp_file_path)
    docs = loder.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size= 1000,
        chunk_overlap=50,
        separators=["\n","。","！","？","，","、",""]
    )
    text = text_splitter.split_documents(docs)
    embeddings_model = OpenAIEmbeddings()
    db = FAISS.from_documents(text,embeddings_model)
    retriever = db.as_retriever()
    qa = ConversationalRetrievalChain.from_llm(
        llm=model,
        retriever=retriever,
        memory=memory
    )
    response = qa.invoke({"chat_history":memory,"question":question})
    return response

