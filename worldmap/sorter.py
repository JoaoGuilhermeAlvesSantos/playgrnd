import json

# Load the JSON data
with open('data.json', 'r') as file:
    data = json.load(file)

# Extract the dictionary
events_by_country = data["total_events_by_country"]

# Sort the dictionary by values in descending order
sorted_events = dict(sorted(events_by_country.items(), key=lambda item: item[1], reverse=True))

# Save the sorted dictionary to a new JSON file
with open('sorted_data.json', 'w') as sorted_file:
    json.dump({"total_events_by_country": sorted_events}, sorted_file, indent=4)

print("Sorted data has been saved to 'sorted_data.json'.")