student_scores = {
    "Ivan" : 5.00,
    "Alex" : 3.50,
    "Maria" : 5.50,
    "Georgi" : 5.00
}


best_score = max(student_scores.values())
#print(best_score)

for j,k in student_scores.items():
    if best_score == k:
        print(f"{j} - {k}")


worst_score = min(student_scores.values())
for l,m in student_scores.items():
    if worst_score == m:
        print(f"{l} - {m}")