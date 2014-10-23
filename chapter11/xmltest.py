import xml.etree.ElementTree as ET

xml = '''<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
'''


def basic_usage(root):
    print('root.tag: %s' % root.tag)
    for child in root:
        print(child.tag, child.attrib)
    print('data.country[0].year: %s' % root[0][1].text)

    for neighbor in root.iter('neighbor'):
        print('neighbor:', neighbor.attrib)


def xpath_usage(root):
    for neighbor in root.findall(".//neighbor"):
        print('neighbor:', neighbor.attrib)

    for country in root.findall(".//year/..[@name='Singapore']"):
        print('country:', country.attrib['name'])


if __name__ == '__main__':
    root = ET.fromstring(xml)
    basic_usage(root)
    xpath_usage(root)
