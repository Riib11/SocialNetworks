import xml.etree.ElementTree as ET
import os

def parseXML(fn, do_raise=True):
    try:
        tree = ET.parse(fn)
        root = tree.getroot()
        return root
    except Exception as e:
        if do_raise: raise e

def getChildByTag(xml, tag, do_raise=True):
    for child in xml.getchildren():
        if child.tag == tag:
            return child
    if do_raise:
        raise Exception("couldn't find child of "+str(xml)+" with tag "+str(tag))

def getChildrenByTag(xml, tag):
    return [ child for child in xml.getchildren()
             if child.tag == tag ]

def getDescendantByTagPath(xml, tags, do_raise=True):
    try:
        for tag in tags:
            xml = getChildByTag(xml, tag)
        return xml
    except Exception as e:
        if do_raise: raise e

def XML_to_JSON(xml):
    return {
        "tag": xml.tag,
        "attrib": xml.attrib,
        "children": [XML_to_JSON(child) for child in xml.getchildren()]
    }
