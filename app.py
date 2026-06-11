from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import PyPDF2
from docx import Document          # ← 改动1：新增，用于读取Word文件
from pptx import Presentation      # ← 改动2：新增，用于读取PPT文件

app = Flask(__name__)

client = OpenAI(
    api_key="sk-b4ea12a9c50e4704a15f2a7ad5010167",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

chat_history = []
pdf_docs = []

# ← 改动3：把原来写在upload函数里的PDF读取逻辑，单独抽出来成一个函数
def read_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# ← 改动4：新增，读取Word文件
def read_word(file):
    doc = Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

# ← 改动5：新增，读取PPT文件，并标注每一页页码
def read_pptx(file):
    prs = Presentation(file)
    text = ""
    for i, slide in enumerate(prs.slides):
        text += f"第{i+1}页：\n"
        for shape in slide.shapes:
            if shape.has_text_frame:
                for para in shape.text_frame.paragraphs:
                    text += para.text + "\n"
        text += "\n"
    return text

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    chat_history.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="deepseek-v3",
        messages=chat_history
    )
    reply = response.choices[0].message.content
    chat_history.append({"role": "assistant", "content": reply})
    return jsonify({"reply": reply})

@app.route("/upload", methods=["POST"])
def upload():
    global pdf_docs
    file = request.files["file"]        # ← 改动6：原来是 "pdf"，改成 "file"，更通用
    filename = file.filename.lower()    # ← 改动7：新增，获取文件名用于判断类型

    # ← 改动8：新增，根据文件类型调用不同的读取函数
    if filename.endswith(".pdf"):
        text = read_pdf(file)
    elif filename.endswith(".docx"):
        text = read_word(file)
    elif filename.endswith(".pptx"):
        text = read_pptx(file)
    else:
        return jsonify({"message": "不支持的文件格式"}), 400

    pdf_docs.append({"name": file.filename, "content": text})
    return jsonify({
        "message": f"上传成功！当前已加载 {len(pdf_docs)} 份文档：{', '.join([d['name'] for d in pdf_docs])}"
    })

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json.get("question")
    combined = "\n\n".join([f"【{d['name']}】\n{d['content']}" for d in pdf_docs])
    response = client.chat.completions.create(
        model="deepseek-v3",
        messages=[
            {"role": "system", "content": f"你是文档助手。以下是所有文档内容：\n\n{combined}"},
            {"role": "user", "content": question}
        ]
    )
    return jsonify({"answer": response.choices[0].message.content})

if __name__ == "__main__":
    app.run(debug=True)