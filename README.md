
---

# ⚙️ Python Auto —— 自动化工作流合集

> 用 Python 解放双手，让重复的工作一键自动完成。
> 打工人的理想工具箱 🧰✨

---

## 🚀 项目简介

**Python Auto** 是一个持续更新的自动化脚本合集项目，目标是打造一个 **“全能办公自动化实验室”**。
无论是生成日报、批量处理文件、爬取数据、RPA 自动化操作，还是和 AI API 结合的智能助手，这里都会陆续集成。

📦 **一句话概括：**

> 「写给所有不想浪费时间在重复劳动上的人」

---

## 🧩 当前已实现功能

| 模块        | 文件                       | 功能简介                      |
| --------- | ------------------------ | ------------------------- |
| 📝 日报自动生成 | `ai_auto_daily_temp.py`  | 一句话调用 DeepSeek API 自动生成日报 |
| 📄 模板定义   | `auto_daily_template.py` | 自定义日报模板，统一输出格式            |

---

## 🔮 未来规划

| 阶段      | 模块方向    | 简介                                     |
| ------- | ------- | -------------------------------------- |
| 📈 阶段一  | 自动化办公   | 批量重命名文件、Excel 处理、日报自动生成                |
| 🤖 阶段二  | AI 集成   | 接入 DeepSeek、OpenAI、Qwen 等 API 实现智能生成任务 |
| 🕸️ 阶段三 | 数据采集    | 爬虫脚本、API 抓取工具、网站监控                     |
| 🧱 阶段四  | RPA 自动化 | 模拟点击操作、n8n 工作流节点集成                     |
| ☁️ 阶段五  | 云端自动化   | 部署到服务器，实现定时任务与Webhook触发                |

---

## 🛠️ 环境配置

```bash
# 1️⃣ 克隆项目
git clone https://github.com/Tom-python0121/python_auto.git
cd python_auto

# 2️⃣ 安装依赖
pip install -r requirements.txt  # （后续会更新依赖清单）

# 3️⃣ 运行示例脚本
python ai_auto_daily_temp.py
```

---

## 🧠 核心理念

> 「重复的事交给机器，创造的事留给人类。」

* 自动化是最好的时间复利。
* 让每一个程序员都能轻松搭建自己的“小型工作机器人”。
* 每一个 demo 都是可复制、可扩展、可集成的。

---

## 📂 项目结构

```
python_auto/
│
├── ai_auto_daily_temp.py       # 使用 DeepSeek API 自动生成日报
├── auto_daily_template.py      # 日报模板生成器
├── /scripts/                   # （预留）文件批处理脚本、爬虫脚本等
├── /rpa/                       # （预留）RPA 自动化模块
├── /api_tools/                 # （预留）AI 接口封装
└── README.md                   # 项目说明文档
```

---

## 🌟 示例展示

```bash
📝 输入你今天的工作简述：今天优化了n8n节点逻辑，还写了日报生成脚本。
🤖 正在调用 DeepSeek 生成日报，请稍候...
✅ 日报已生成：日报_2025-10-18.txt
```

生成效果👇

```
**工作日报**
日期：2025年10月18日
汇报人：Tom

今日工作内容：
1. 优化 n8n 节点逻辑；
2. 编写自动日报脚本，接入 DeepSeek API。

明日计划：
- 优化输出模板；
- 添加批量生成功能。
```

---

## 🔧 技术栈

| 分类    | 技术                     |
| ----- | ---------------------- |
| 语言    | Python 3.10+           |
| AI 接口 | DeepSeek, OpenAI（规划中）  |
| 自动化工具 | n8n, 影刀, 八爪鱼（规划中）      |
| 数据处理  | pandas, requests, json |
| 文件输出  | Markdown / txt / Excel |

---

## 📬 联系方式

👨‍💻 **作者：Tony Wei（盼哥）**
📧 Email: [weipan15679363796@163.com](mailto:weipan15679363796@163.com)
🌐 GitHub: [Tom-python0121](https://github.com/Tom-python0121)
📱 微信公众号：**盼哥PyAI实验室**
🎯 关键词：Python 自动化 · AI 编程 · 工作效率提升

---

## 🏷️ Topics

`python` · `automation` · `deepseek` · `rpa` · `ai` · `n8n` · `auto-daily-report` · `workflow` · `productivity`

---
