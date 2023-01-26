from urllib import request
import xml.etree.ElementTree as XMLElementTree

address = "http://127.0.0.1:8089/import"

clipObject = XMLElementTree.Element("Clip")
XMLElementTree.SubElement(clipObject, "Path").text = r"C:\Users\joe\Pictures\capybara.jpg"
xmlDataString = XMLElementTree.tostring(clipObject)

headers = {"Content-Type": "application/xml"}

newRequest = request.Request(address, data=xmlDataString, headers=headers)
resp = request.urlopen(newRequest).read().decode("utf-8")
