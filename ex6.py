# 문제 6 — 특정 줄만 저장하기

f = open("text.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

f = open("line3.txt", "w", encoding="utf-8")
f.write(lines[2])  # 3번째 줄 (인덱스 2)
f.close()
