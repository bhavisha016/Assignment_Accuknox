import requests
import matplotlib.pyplot as plt

url = "http://127.0.0.1:5000/students"
response = requests.get(url)
students = response.json()

names = []
scores = []

for s in students:
    names.append(s["name"])
    scores.append(s["score"])

average = sum(scores) / len(scores)
print("Average Score:", average)

plt.bar(names, scores)
plt.axhline(average)
plt.xlabel("Students")
plt.ylabel("Total Score")
plt.title("Student Test Scores")
plt.show()
