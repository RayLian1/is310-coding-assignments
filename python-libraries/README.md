# CLI Data Entry Application

## Description
This Python CLI application allows users to enter movie data through the terminal. The program first displays example data using the Rich library. Then the user can enter new movie information.

After entering the data, the user confirms whether the information is correct. The program allows multiple entries and saves the final data to a CSV file.

## Data Collected
- Movie title
- Release date
- Box office earnings

## How to Run

Install required library:

pip install rich

Run the program:

python cli_data_entry.py

## Output

The program saves the data into:

movies.csv

It also prints the full file path so the user can find the file.