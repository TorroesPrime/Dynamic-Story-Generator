HumanTitles = ['Rogue Trader', 'Lord', 'Captain', 'Baron', 'Duke', 'Duchess', 'Dame', 'Lady', 'Baroness', 'Damme']
HumanTitles_m = [x for x in HumanTitles if x != "Duchess"]
HumanTitles_m = [x for x in HumanTitles_m if x != "Lady"]
HumanTitles_m = [x for x in HumanTitles_m if x != "Damme"]
HumanTitles_m = [x for x in HumanTitles_m if x != "Baroness"]
HumanTitles_m = [x for x in HumanTitles_m if x != "Dame"]
HumanTitles_f = [x for x in HumanTitles if x != "Duke"]
HumanTitles_f = [x for x in HumanTitles_f if x != "Lord"]
HumanTitles_f = [x for x in HumanTitles_f if x != "Baron"]
print("Human titles for male characters:")
print(HumanTitles_m)
print("Human titles for female characters:")
print(HumanTitles_f)
