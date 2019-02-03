first_names = ["Ivan", "Maria", "Yana", "Petar"]
last_names = ["Ivanov", "Boyanova", "Popova", "Stoyanov"]

team_names = []

for x in range(len(first_names)):
    team_names.append(first_names[x])
    team_names.append(last_names[x])

print(team_names)
