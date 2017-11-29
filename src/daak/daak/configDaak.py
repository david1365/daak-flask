import xml.etree.ElementTree as ET
try:
    tree = ET.parse('config.py')
except ValueError:
    print ""