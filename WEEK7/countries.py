from cs50 import SQL

db = SQL("sqlite:///countries.db")

country = input("Specific country: ")

rows = db.execute("SELECT * FROM countries WHERE country = ?", country)

for row in rows:
    print(row)
print(type(rows))
