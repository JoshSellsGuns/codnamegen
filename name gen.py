import random
namelist1 = ["Legit", "Xtreme", "FaZe", "Total", "Fly", "OG", "Complete", "Im", "Killer", "Swift", "Krazy", "Super", ]
namelist2 = ["Scopes", "Clips", "Clipz", "Sounds", "Wolf", "Dragon", "Ownage", "Mastery", "Prestige", "Spaceman", "Apex", "Frags"]
name1 = namelist1[random.randint(0,len(namelist1))]
name2 = namelist2[random.randint(0,len(namelist2))]
name = name1 + " " + name2
print(name)
input("Press enter when you are finished... ")