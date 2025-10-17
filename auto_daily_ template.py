import os
from  datetime import datetime

#日报模板
template = """
【今日工作内容】
- 完成了：
- 遇到问题：
- 明日计划：
"""

#获取当前日期
today = datetime.now().strftime('%Y-%m-%d')
filename = f"日报_{today}.txt"

#定义存放路径
folder = "daily_reports"
if not os.path.exists(folder):
    os.mkdir(folder)

filepath = os.path.join(folder, filename)

#写入模板内容
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(f"日期：: {today}\n")
    f.write(template)

print(f"✅ 日报已生成：{filepath}")
