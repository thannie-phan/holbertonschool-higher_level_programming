#!/usr/bin/python3
"""This module serialise and deserialise csv content"""


import csv
import json


def convert_csv_to_json(filename):
    """Convert a CSV file to JSON format and write the result to data.json."""

    data = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file)

        return True
    
    except FileNotFoundError:
        return False
