#!/usr/bin/python3
"""This module serialise and deserialise xml content"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Convert python dict into an xml file"""

    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, xml_declaration=True)


def deserialize_from_xml(filename):
    """Read XML file and convert it to dict"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        dictionary = {}

        for child in root:
            key = child.tag
            value = child.text
            dictionary[key] = value
        
        return dictionary
    
    except FileNotFoundError:
        return {}