# 🐟 FishReport - 摸鱼日报工厂

一款专为打工人打造的 AI 摸鱼日报生成工具。自动将你一天的摸鱼与工作内容，包装成一份高效、专业、可视化的日报，提升“摸鱼效率”，彰显“职场战斗力”。

## ✨ 核心功能

| 功能 | 描述 |
|------|------|
| 🧾 工作记录输入 | 多段工作内容或摸鱼内容输入（可语音拓展） |
| 🤖 AI 日报生成 | 使用 GPT 自动生成日报文本内容 |
| 📊 图表可视化 | 自动生成时间分布图表（饼图）展示任务分配比例 |
| 💬 摸鱼语录 | 每日报告附赠一句“摸鱼金句” |
| 📥 下载 & 复制 | 支持 Markdown 下载日报内容 |

## 📷 截图预览

> 可在部署后补充截图示意

## 🚀 在线访问（部署链接）

👉 https://你的部署地址.streamlit.app

或使用 AWS 免费服务器部署（下方提供指南）

## 💻 本地运行方式

1. 克隆项目：
```bash
git clone https://github.com/yourname/fishreport
cd fishreport
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 配置 OpenAI API 密钥（推荐使用 .env）
```env
OPENAI_API_KEY=your-api-key-here
```

4. 运行应用：
```bash
streamlit run app.py
```

## ☁️ 一键部署到 Streamlit Cloud

1. 打开 https://streamlit.io/cloud
2. 登录 GitHub 并连接你的项目仓库
3. 添加环境变量 OPENAI_API_KEY
4. 点击部署即可 🎉

## ✅ 使用 Amazon Q 记录

你可以在开发过程截图 Amazon Q 的使用，例如：

- 💡 代码优化建议：Q 对 app.py 的性能建议
- 🔐 安全提示：输入内容的 XSS 过滤提醒
- 🧠 架构建议：对图表组件和模块划分的调整建议

👉 截图一张你调用 Q 的建议内容即可，符合评审要求！

## 📄 License
MIT

> 项目由 ChatGPT 与你共同创作，开启摸鱼与生产力并存的新纪元 🧘
