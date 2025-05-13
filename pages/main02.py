import streamlit as st
from utils02 import get_chat_response
from langchain.memory import ConversationBufferMemory

st.header("AI聊天模拟器 🤖")

with st.sidebar:
    api_key = st.text_input("输入 OpenAI API Key:", type="password")
    st.markdown("⚠️ 你的 API Key 不会保存在服务器上。")
if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"ai","content":"你好，我是你的ai助手有什么可以帮你的吗"}]

for message in st.session_state.messages:
    st.chat_message("ai").write(message["content"])

prompt = st.chat_input("你想聊些什么")

if prompt :
    # 检查 API Key
    if not api_key:
        st.error("请先在侧边栏输入 API Key！")
        st.stop()
    st.session_state["messages"].append({"role":"human","content":prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("AI正在思考，请稍等......"):
        response = get_chat_response(prompt,st.session_state["memory"],api_key)

    msg = {"role":"ai","content":response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)

