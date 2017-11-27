import xml.etree.ElementTree as ET
try:
    tree = ET.parse('daak.config.xml')
except ValueError:
    print ""