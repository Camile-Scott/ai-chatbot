@echo off
cd /d C:\Users\M00053440\ai-chat
start py app.py
timeout /t 3
start http://127.0.0.1:5000