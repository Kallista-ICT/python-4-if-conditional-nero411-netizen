generationinput = int(input("Enter your birth year: "))

if generationinput < 1946:
    Generation = "Silent Generation"
elif generationinput < 1965:
    Generation = "Baby Boomer"
elif generationinput < 1981:
    Generation = "Generation X"
elif generationinput < 1997:
    Generation = "Millenials"
elif generationinput < 2013:
    Generation = "Generation Z"
else:
    Generation = "Generation Alpha"

print(f"You belong to: {Generation}")   