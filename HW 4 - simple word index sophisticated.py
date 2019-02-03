text = '''
apple and banana one apple one banana
a red apple and a green apple'''

words_list=text.split()
print(words_list)

unique_words = []
for x in words_list:
    if x not in unique_words:
        unique_words.append(x)

length = []
for x in words_list:
    length.append(len(x))
k = max(length)
print(k)

for x in unique_words:
    print(f"|%{k}s |%d |" % (x,words_list.count(x)))