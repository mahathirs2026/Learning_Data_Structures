records = [
    ["Alice", "Math", 85],
    ["Bob", "Math", 78],
    ["Alice", "Physics", 92],
    ["Bob", "Physics", 88],
    ["Alice", "Chemistry", 79]
]

grades = {}
for name, subject, score in records:
    if name not in grades:
        grades[name] = []
    grades[name].append((subject,score))

print(grades)