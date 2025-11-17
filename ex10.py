# 문제 10 — 특정 문자열로 시작하는 줄만 저장하기

f = open("log.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

f = open("error.txt", "w", encoding="utf-8")
for line in lines:
    if line.startswith("ERROR"):
        f.write(line)
f.close()
