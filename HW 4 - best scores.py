student_scores = {
    "Ivan" : 5.00,
    "Alex" : 3.50,
    "Maria" : 5.50,
    "Georgi" : 5.00
}

best_scores = []
for k,x in student_scores.items():
    if x > 4:
        best_scores.append(k)







print(best_scores)