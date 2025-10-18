import os
import requests
from datetime import datetime

#设置DeepSeek API Key
DEEPSEEK_API_KEY = "sk-b7a6969c6b554a93ab89aff9f7765c23"

#DeepSeek API 调用函数
def generate_report(prompt):
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "你是一名认真写日报的上班族，请根据输入生成一份格式规范、语气自然的日报。"},
            {"role": "user", "content": f"请根据提示生成日报：{prompt}"}
        ],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        raise Exception(f"请求失败：{response.text}")

# 日报模板包装
def format_report(content):
    today = datetime.now().strftime("%Y-%m-%d")
    template = f"""
日期：{today}

【今日工作内容】
{content}

【遇到问题】
暂无特殊问题。

【明日计划】
- 继续优化自动化脚本；
- 研究 AI 工具结合 Python 的写作效率。
"""
    return template

#写入文件
def save_report(content):
    today = datetime.now().strftime("%Y-%m-%d")
    folder = f"daily_reports"
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, f"日报_{today}.txt")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅日报已经生成：{filepath}")

#主程序入口
if __name__ == "__main__":
    prompt = input("📝 输入你今天的工作简述：")
    print("🤖 正在调用 DeepSeek 生成日报，请稍候...\n")

    try:
        ai_content = generate_report(prompt)
        final_report = format_report(ai_content)
        save_report(final_report)
    except Exception as e:
        print("❌ 出错啦：", e)