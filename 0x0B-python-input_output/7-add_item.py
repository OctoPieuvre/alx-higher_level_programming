#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

# Load existing items from file or create empty list
try:
    items = load_from_json_file('add_item.json')
except:
    items = []

# Add new items to the list
for arg in sys.argv[1:]:
    items.append(arg)

# Save the updated list to file
save_to_json_file(items, 'add_item.json')
