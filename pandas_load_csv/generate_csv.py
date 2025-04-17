import pandas as pd
import random

# Base first names
first_names = [
    "Anna", "Bram", "Charlotte", "Daan", "Emma", "Finn", "Gwen", "Hugo", "Iris", "Jasper",
    "Kim", "Lars", "Maud", "Noah", "Olivia", "Pim", "Quinty", "Ravi", "Sanne", "Timo",
    "Ursula", "Victor", "Willem", "Xander", "Yara", "Zoe"
]

# Generate unique names by appending a random letter or number
unique_names = set()
while len(unique_names) < 100:
    name = random.choice(first_names) + " " + chr(random.randint(65, 90)) + "."
    unique_names.add(name)

# Dutch cities
cities = [
    "Amsterdam", "Rotterdam", "Utrecht", "Eindhoven", "Groningen", "Maastricht", "Leiden",
    "Delft", "Nijmegen", "Arnhem", "Haarlem", "Zwolle", "Tilburg", "Breda", "Alkmaar",
    "Apeldoorn", "Amersfoort", "Den Bosch", "Enschede", "Leeuwarden"
]

# Generate data
data = {
    "Naam": list(unique_names),
    "Plaats": [random.choice(cities) for _ in range(100)],
    "Leeftijd": [random.randint(18, 65) for _ in range(100)],
    "Salaris": [random.randint(20000, 100000) for _ in range(100)]
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("personen_data.csv", index=False)
print("CSV file 'personen_data.csv' with unique names has been created.")
