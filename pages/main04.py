import pandas as pd
import streamlit as st
from utils04 import dataframe_agent
import pandas

def create_chart(input_data,chart_type):
    df_data = pd.DataFrame(input_data["data"],columns=input_data["columns"])
    df_data.set_index(input_data["columns"][0],inplace=True)
    if chart_type == "bar":
        st.bar_chart(df_data)
    elif chart_type == "line":
        st.line_chart(df_data)
    elif chart_type == "scatter":
        st.scatter_chart(df_data)

st.header("CSV 智能分析工具 💡")
with st.sidebar:
    api_key = st.text_input("请输入您的api密钥",type="password")
    st.markdown("[获取API密钥](https://api.aigc369.com/v1)")
uploader_file = st.file_uploader("上传文件(csv文件)",type="csv")
if uploader_file:
    st.session_state.df = pd.read_csv(uploader_file)
    with st.expander("DataFrame 表格"):
        st.dataframe(st.session_state.df)
query = st.text_area("请输入你对以上表格的问题，或者数据提取要求，或者可视化要求(包括散点图、折线图、条形图):")
bt = st.button("生成回答")

if bt and not api_key:
    st.error("请输入您的API密钥")
    st.stop()
if bt and not uploader_file:
    st.info("请上传您的CSV数据文件")
    st.stop()
if bt and not query:
    st.info("请输入您想知道的问题")
    st.stop()
if bt and api_key and uploader_file and query:
    with st.spinner("AI正在生成回答......"):
        response_dict = dataframe_agent(api_key,st.session_state.df,query)
        if "answer" in response_dict:
            st.write(response_dict["answer"])
        if "table" in response_dict:
            st.table(pd.DataFrame(response_dict["table"]["data"],
                                  columns=response_dict["table"]["columns"]))
        if "bar" in response_dict:
            create_chart(response_dict["bar"],"bar")
        if "line" in response_dict:
            create_chart(response_dict["line"],"line")
        if "scatter" in response_dict:
            create_chart(response_dict["scatter"],"scatter")
