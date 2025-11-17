# 문제 2 — 숫자 파일의 합 구하기
f = open("numbers.txt", "r")
total = 0
for line in f:
    total += int(line.strip())
f.close()
print(total)
