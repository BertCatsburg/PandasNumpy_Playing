import pandas as pd
import random

# Base first names
first_names = [
    "Anna", "Bram", "Charlotte", "Daan", "Emma", "Finn", "Gwen", "Hugo", "Iris", "Jasper",
    "Kim", "Lars", "Maud", "Noah", "Olivia", "Pim", "Quinty", "Ravi", "Sanne", "Timo",
    "Ursula", "Victor", "Willem", "Xander", "Yara", "Zoe"
]

# Generate 50 unique names by appending random initials
unique_names = set()
while len(unique_names) < 50:
    name = random.choice(first_names) + " " + chr(random.randint(65, 90)) + "."
    unique_names.add(name)

# UK cities
uk_cities = [
    "London", "Manchester", "Birmingham", "Leeds", "Glasgow", "Liverpool", "Bristol",
    "Sheffield", "Edinburgh", "Leicester", "Coventry", "Bradford", "Cardiff", "Belfast",
    "Newcastle", "Nottingham", "Southampton", "Portsmouth", "Derby", "Brighton"
]

# Generate data
data = {
    "Naam": list(unique_names),
    "Plaats": [random.choice(uk_cities) for _ in range(50)],
    "Leeftijd": [random.randint(18, 65) for _ in range(50)],
    "Salaris": [random.randint(20000, 100000) for _ in range(50)]
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("personen_uk_data.csv", index=False)
print("CSV file 'personen_uk_data.csv' with UK cities and 50 unique names has been created.")
