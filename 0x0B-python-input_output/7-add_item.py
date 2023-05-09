#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

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
