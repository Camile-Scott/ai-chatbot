# 我的AI助手 (My AI Assistant)

一个基于 DeepSeek / 通义千问 API 构建的全栈AI聊天应用，支持多对话管理、文档问答等功能。

## ✨ 功能特性

- 💬 **智能对话**：基于大语言模型的多轮对话
- 📁 **多对话管理**：类似ChatGPT的会话列表，支持新建、切换、删除
- 📄 **文档问答**：支持上传 PDF / Word / PPT，AI根据文档内容回答问题
- 💾 **数据持久化**：使用 SQLite 数据库，刷新页面历史记录不丢失
- 🎨 **Markdown渲染**：AI回复支持格式化展示（标题、列表、粗体等）
- 🚀 **一键启动**：双击 `start.bat` 自动启动并打开浏览器

## 🛠️ 技术栈

- **后端**：Python + Flask
- **数据库**：SQLite
- **前端**：HTML / CSS / JavaScript（原生，无框架）
- **AI模型**：DeepSeek-V3（通过阿里云百炼API）
- **文档解析**：PyPDF2、python-docx、python-pptx

## 📦 项目结构
ai-chat/

├── app.py              # Flask后端主程序

├── chat.py             # 命令行聊天版本

├── pdf_chat.py         # 命令行文档问答版本

├── start.bat           # 一键启动脚本

├── chat.db             # SQLite数据库（自动生成）

└── templates/

└── index.html      # 前端页面

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install openai flask pypdf2 python-docx python-pptx
```

### 2. 配置API Key

在 `app.py` 中填入你的 API Key：

```python
client = OpenAI(
    api_key="你的API Key",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
```

### 3. 启动项目

```bash
python app.py
```

访问 `http://127.0.0.1:5000` 即可使用。

或者在Windows上直接双击 `start.bat`。

## 📸 功能截图

（待补充）

## 📝 开发日志

这个项目是我从零开始学习AI应用开发的实践记录，完整开发过程记录在工作日志中。

## 🔮 未来计划

- [ ] 图片上传与识别
- [ ] 部署到云服务器
- [ ] 用户登录系统

## 📄 License

MIT