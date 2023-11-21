import csv

# Read data from the input CSV file
with open("projects/gamer-score/gamer-data.csv", "r") as input_file:
    reader = csv.DictReader(input_file)
    data = [row for row in reader]

# Create a data structure to hold ID, name, and score
gamer = {
    "Name": "",
    "Score": 0 }

# Read through the file and keep track of everyone's scores
processed_data = {}
for row in data:
    # Create a new item if this gamer isn't already in the list
    if row["ID"] not in processed_data:
        processed_data[row["ID"]] = {
            "Name": row["Name"],
            "Score": 0
        }
    if row["Type"] == "Award":
        processed_data[row["ID"]]["Score"] += int(row["Points"])
    else:
        processed_data[row["ID"]]["Score"] -= int(row["Points"])

# Print out the summary
print("Player Name    Score")
print("-----------    -----")
for item in processed_data:
    print(f'{processed_data[item]["Name"]:>11}    {processed_data[item]["Score"]}')

# Write the processed data to the output CSV file
with open("gamer_score_data.csv", "w") as output_file:
    fieldnames = ["ID", "Name", "Score"]
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()
    for item in processed_data:
        writer.writerow({
            "ID": item,
            "Name": processed_data[item]["Name"],
            "Score": processed_data[item]["Score"]
        })