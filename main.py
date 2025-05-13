import  streamlit as st
from utils import generate_script

st.title("视频脚本生成器")
with st.sidebar:
    deepseek_api_key = st.text_input("请输入Deepseek API密钥",type="password")
    st.markdown("[获取Deepseek API密钥](https://platform.deepseek.com/api_keys)")
subject = st.text_input("请输入视频的主题")
video_length = st.number_input("请输入视频的大致时长（单位：分钟）",min_value=0.1,step=0.1,value=None)
creativity = st.slider("请选择视频脚本的创造力（数字小说明更严谨，数字大说明更多样）"
                       ,min_value=0.0,max_value=1.0,value=0.2,step=0.1)
button_01 = st.button("生成脚本")
if button_01 and not deepseek_api_key:
    st.info("请提供你的deepseek API密钥")
    st.stop()
if button_01 and not subject:
    st.info("请输入视频主题")
    st.stop()
if button_01 and not video_length>=0.1:
    st.info("请确认视频时长(时长应大于0.1分钟)")
    st.stop()
if button_01:
    with st.spinner("AI思考中，请稍等片刻......"):
        title,script = generate_script(subject,video_length,creativity,deepseek_api_key)
    st.success("视频脚本生成成功")
    #副标题
    st.subheader("标题：")
    st.write(title)
    st.subheader("脚本内容：")
    st.write(script)