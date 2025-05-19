from openai import OpenAI
from datetime import date
import os
import time
from dotenv import load_dotenv

time.sleep(2)
# 加载环境变量
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def generate_report(tasks: str, selected_date: date) -> str:
    prompt = f"""
你是一位职场日报助手。请根据以下任务内容，生成一篇有条理、显得高效但不浮夸的日报。
日期：{selected_date}
任务：
{tasks}
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你是一位精通写日报的 AI 职场秘书。"},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=600
    )
    return response.choices[0].message.content.strip()
