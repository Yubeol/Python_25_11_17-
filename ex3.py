# 문제 3 — 특정 단어 개수 세기

f = open("story.txt", "r")
text = f.read().lower()
f.close()
count = text.count("python")
print(count)
