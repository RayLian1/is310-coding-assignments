from rich.console import Console
from rich.table import Table
import csv
import os

console = Console()

console.print("Here is some example data:", style="bold cyan")

table = Table(title="Favorite Movies")
table.add_column("Title")
table.add_column("Release Date")
table.add_column("Box Office")

table.add_row("Star Wars", "1977", "$775M")
table.add_row("Avengers: Endgame", "2019", "$2.7B")

console.print(table)

entries = []

while True:

    console.print("\nEnter a movie", style="bold green")

    title = input("Movie title: ")
    date = input("Release date: ")
    money = input("Box office: ")

    console.print("\nYou entered:")
    console.print(title, date, money)

    confirm = input("Is this correct? (yes/no): ")

    if confirm == "yes":
        entries.append([title, date, money])

    again = input("Add another movie? (yes/no): ")

    if again != "yes":
        break


filename = "movies.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Release Date", "Box Office"])

    for e in entries:
        writer.writerow(e)

path = os.path.abspath(filename)

console.print("\nData saved!", style="bold green")
console.print("File location:", path)