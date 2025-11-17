# 문제 8 — 이메일 주소만 추출하기

f = open("contacts.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

f = open("emails.txt", "w", encoding="utf-8")
for line in lines:
    parts = line.split()
    for p in parts:
        if "@" in p:
            f.write(p + "\n")
f.close()
