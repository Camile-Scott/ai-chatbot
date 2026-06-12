import sqlite3

# 连接数据库(文件不存在会自动创建)
conn = sqlite3.connect("chat.db")
cursor = conn.cursor()

# 创建对话表
cursor.execute("""
CREATE TABLE IF NOT EXISTS conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
)
""")

# 创建消息表
cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conversation_id INTEGER,
    role TEXT,
    content TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
print("数据库表创建成功!")

# 测试:插入一条对话
cursor.execute("INSERT INTO conversations (title) VALUES (?)", ("测试对话",))
conn.commit()

# 测试:查询所有对话
cursor.execute("SELECT * FROM conversations")
print("所有对话:", cursor.fetchall())

conn.close()