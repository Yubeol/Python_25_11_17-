# 문제 5 — CSV 파일에서 점수 평균 구하기

f = open("score.csv", "r")
scores = []
for line in f:
    name, score = line.strip().split(",")
    scores.append(int(score))
f.close()
average = sum(scores) / len(scores)
print(f"평균나이는 {average:.1f}입니다.")
