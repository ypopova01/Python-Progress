words = ["dog", "talent", "loop", "aria", "tent", "choice"]

#this program should return all words that start and end with one and the same letter

words_matching_the_criteria = []

for x in words:
    if x[0] == x[-1]:
        words_matching_the_criteria.append(x)

print(words_matching_the_criteria)