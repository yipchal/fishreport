import streamlit as st
import datetime
from utils import generate_report


st.set_page_config(page_title="摸鱼日报工厂", layout="centered")
st.title("🐟 摸鱼日报工厂 FishReport")

st.markdown("""
> 帮你把平平无奇的一天，包装成高产高效的职场奇迹。每天一份日报，摸鱼也显得很专业！
""")

# 输入区
st.header("🧾 今天你做了什么？")
tasks = st.text_area("输入你今天的工作内容（换行分隔每一项）",
    placeholder="例如：\n- 回复了客户邮件\n- 修复了页面 bug\n- 看了半小时知乎")

with st.expander("📅 选择日期（默认今天）"):
    date = st.date_input("日报日期", value=datetime.date.today())

# 提交按钮
if st.button("📄 生成日报"):
    if not tasks.strip():
        st.warning("请先输入今天做了什么内容！")
    else:
        with st.spinner("AI 正在生成日报中..."):
            report = generate_report(tasks, date)
            quote = get_random_moyu_quote()
            chart_fig = generate_chart(tasks)

        st.success("✅ 日报生成完毕！")
        st.subheader("🎯 自动生成日报：")
        st.markdown(report, unsafe_allow_html=True)

        st.subheader("📊 时间分布图")
        st.pyplot(chart_fig)

        st.subheader("🤖 摸鱼金句")
        st.info(f"“{quote}”")

        st.download_button("📥 下载日报 Markdown 文件", report, file_name="moyu_report.md")
