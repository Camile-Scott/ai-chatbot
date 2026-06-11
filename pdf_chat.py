from openai import OpenAI
import PyPDF2

client = OpenAI(
    api_key="sk-b4ea12a9c50e4704a15f2a7ad5010167",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

def read_pdf(file_path):
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
    return text

def ask_pdf(pdf_text, question):
    response = client.chat.completions.create(
        model="deepseek-v3",
        messages=[
            {"role": "system", "content": f"你是一个文档助手。以下是文档内容：\n\n{pdf_text}"},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

# 主程序
pdf_path = input("请输入PDF文件路径：")
print("正在读取PDF...")
pdf_text = read_pdf(pdf_path)
print(f"读取完成！共 {len(pdf_text)} 个字符\n")

while True:
    question = input("你的问题：")
    if question == "quit":
        break
    answer = ask_pdf(pdf_text, question)
    print(f"AI：{answer}\n")