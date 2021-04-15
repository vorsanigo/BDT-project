import pandas as pd
import numpy as np
import requests
import xml.etree.cElementTree as ET
from xml.parsers import expat
from lxml import etree

# url stations anagrafica
url_stations_anagrafica = "http://dati.meteotrentino.it/service.asmx/listaStazioni"
# request get
resp_stat = requests.get(url_stations_anagrafica)
#print(resp_stat.content)

# create xml file
with open('stations.xml', 'wb') as f:
    f.write(resp_stat.content)

# create tree
tree = ET.parse("file.xml")

# get root element
root = tree.getroot()

# initialize interesting lists -> code, name, short name of all the stations
codes = []
names = []
short_names = []

# get all the codes
for code in root.findall('.//{http://www.meteotrentino.it/}codice'):
    codes.append(code.text)
# get all the names
for name in root.findall('.//{http://www.meteotrentino.it/}nome'):
    names.append(name.text)
# get all the short names
for short_name in root.findall('.//{http://www.meteotrentino.it/}nomebreve'):
    short_names.append(short_name.text)

print(codes)
print(names)
print(short_names)



















'''xmlstr = ET.tostring(root, encoding='utf8', method='xml')

root = fromstring(xmlstr)
for actor in root.findall('{http://people.example.com}actor'):
    name = actor.find('{http://people.example.com}name')
    print(name.text)
    for char in actor.findall('{http://characters.example.com}character'):
        print(' |-->', char.text)'''





'''inputfile = 'file.xml'
target_ns = '{http://www.meteotrentino.it/}'
nsmap = {None: target_ns}

tree = etree.parse(inputfile)
root = tree.getroot()
'''
# here we set the namespace of all elements to target_ns
'''for elem in root.getiterator():
    tag = etree.QName(elem.tag)
    elem.tag = '{%s}%s' % (target_ns, tag.localname)

# create a new root element and set the namespace map, then
# copy over all the child elements
new_root = etree.Element(root.tag, nsmap=nsmap)
new_root[:] = root[:]

# create a new elementtree with new_root so that we can use the
# .write method.
tree = etree.ElementTree()
tree._setroot(new_root)

tree.write('done.xml',
           pretty_print=True, xml_declaration=True, encoding='UTF-8')'''

'''print(root.tag)
for x in root.findall('{http://www.meteotrentino.it/}ArrayOfAnagrafica'):
    code = x.find('{http://www.meteotrentino.it/}codice')
    print(code.text)'''
'''for child in root.iter():
    from r in document.Descendants(ns + "Credential")
    select(string)
    r.Element(target_ns + "Username");
    print(child)
    #print(child.tag, child.attrib)
    print(child.tag, child.attrib[target_ns + 'codice'])'''



'''
# Remove namespace prefixes
for elem in root.getiterator():
    elem.tag = etree.QName(elem).localname
# Remove unused namespace declarations
etree.cleanup_namespaces(root)

print(etree.tostring(root).decode())

url_stations_anagrafica = "http://dati.meteotrentino.it/service.asmx/listaStazioni"
resp_stat = requests.get(url_stations_anagrafica)
#print(resp_stat.content)

with open('stations.xml', 'wb') as f:
    f.write(resp_stat.content)

class DisableXmlNamespaces:
    def __enter__(self):
            self.oldcreate = expat.ParserCreate
            expat.ParserCreate = lambda encoding, sep: self.oldcreate(encoding, None)
    def __exit__(self, type, value, traceback):
            expat.ParserCreate = self.oldcreate

def parseXML(xmlfile):
    # create element tree object
    with DisableXmlNamespaces():
        tree = ET.parse("file.xml")

    # get root element
    root = tree.getroot()

    print(root.findall('{http://www.meteotrentino.it/}codice'))
    # create empty list for news items
    newsitems = []

    for child in root.iter():
        print(child)
        #print(child.tag, child.attrib)
        #print(child.tag, child.attrib['codice'])

parseXML('stations.xml')

root = ET.fromstring(resp_stat.content)

for child in root.iter('*'):
    print(child.tag, child.attrib['codice'])

#root = tree.getroot()
#tree = ET.ElementTree(root)
#tree.write("file.xml")
#print(root.text)


for code in root.iter("ns0:codice"):
    print(code)
    codes.append(code.text)

print(codes)
'''


