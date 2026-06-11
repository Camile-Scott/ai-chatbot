from openai import OpenAI

client = OpenAI(
    api_key="sk-b4ea12a9c50e4704a15f2a7ad5010167",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

print("聊天机器人启动！输入 quit 退出")

history = []

while True:
    user_input = input("你：")
    if user_input == "quit":
        break
    
    history.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
        model="deepseek-v3",
        messages=history
    )
    
    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    
    print(f"AI：{reply}\n")