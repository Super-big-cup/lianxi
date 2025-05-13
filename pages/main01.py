import streamlit as st
from utils_01 import generate_xiaohongshu
st.header("小红书文案生成器 📕")

with st.sidebar:
    deepseek_api_key = st.text_input("请输入Deepseek API密钥", type="password")
    st.markdown("[获取Deepseek API密钥](https://platform.deepseek.com/api_keys)")

theme_01 = st.text_input("主题:")
submit = st.button("提交")
if submit and not deepseek_api_key:
    st.info("请提供你的deepseek API密钥")
    st.stop()
if submit and not theme_01:
    st.info("请输入文案主题")
    st.stop()
if submit:
    with st.spinner("AI创作中，请稍等片刻......"):
        result = generate_xiaohongshu(theme_01,deepseek_api_key)
    st.divider()
    column01,column02 = st.columns(2)
    with column01:
        # st.markdown("##### 小红书标题1")
        # st.write(result.titles[0])
        # st.markdown("##### 小红书标题2")
        # st.write(result.titles[1])
        # st.markdown("##### 小红书标题3")
        # st.write(result.titles[2])
        # st.markdown("##### 小红书标题4")
        # st.write(result.titles[3])
        # st.markdown("##### 小红书标题5")
        # st.write(result.titles[4])
        for i in range(1,6,1):
            st.markdown(f"##### 小红书标题{i}")
            st.write(result.titles[i-1])
    with column02:
        st.markdown("##### 小红书正文")
        st.write(result.content)
