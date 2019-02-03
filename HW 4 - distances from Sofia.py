distances_from_sofia = [
    ("Bansko", 97),
    ("Brussels", 1701),
    ("Alexandria", 1403),
    ("Nice", 1307),
    ("Szeged", 469),
    ("Dublin", 2479),
    ("Palermo", 987),
    ("Moscow", 1779),
    ("Oslo", 2098),
    ("London", 2019),
    ("Madrid", 2259),
]

#print(distances_from_sofia[0][1])
# [0][1] <1500
# [1][1] <1500

below_1500 = []

for k in distances_from_sofia:
    if k[1] < 1500:
        print(f"{k[0]} - {k[1]} ")

