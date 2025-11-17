# 문제 1 — 파일 내용 줄 번호 붙여 출력하기
f = open("data1.txt", "r", encoding="utf-8")

for i, line in enumerate(f, start=1):
    print(f"{i}: {line.rstrip()}")

f.close()
