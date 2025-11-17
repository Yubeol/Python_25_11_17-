# 문제 7 — 빈 줄 제거 후 저장하기

f = open("messy.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

f = open("clean.txt", "w", encoding="utf-8")
for line in lines:
    if line.strip():  # 빈 줄 아니면
        f.write(line)
f.close()
