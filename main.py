from http.client import UPGRADE_REQUIRED
import xml.sax
import gzip
import xml.etree.ElementTree as ET
import csv
import os
from callback import Callback

paper_obj_list = []

class main(xml.sax.ContentHandler):
    def __init__(self):
        self.current_element = ""
        self.title = ""
        self.author = []
        self.year = ""
        self.journal = ""
        self.ee = ""
        self.text = ""
        self.mdate = ""
        self.key = ""
        self.publtype = ""

    def startElement(self, name, attrs):
        self.current_element = name
        if name == "article":
            self.mdate = attrs.get("mdate", "")  # Get the mdate attribute
            self.key = attrs.get("key","") # Get the key attribute
            self.publtype = attrs.get("publtype","") # Get the publtype attribute


    def characters(self, content):
        self.text += (content.strip())

    def endElement(self, name):
        if name == "title":
            self.title = self.text
        elif name == "author":
            self.author = self.author + [self.text]
        elif name == "year":
            self.year = self.text
        elif name == "journal":
            self.journal = self.text
        elif name == "ee":
            self.ee = self.text
        elif name == "article":
            current_obj_paper = {"Mdate": self.mdate, "Key": self.key, "Publtype": self.publtype, "Title":self.title, "Authors:":self.author, "Year":self.year, "Journal":self.journal, "EE":self.ee}
            paper_obj_list.append(current_obj_paper)
            self.title = ""
            self.author = []
            self.year = ""
            self.journal = ""
            self.ee = ""
            self.article = ""
            self.mdate = ""
            self.key = ""
            self.publtype = ""
        self.text = ""


if __name__ == "__main__":
    xml_file_path = "dblp.xml"
    parser = xml.sax.make_parser()
    handler = MyHandler()
    parser.setContentHandler(handler)
    try:
        parser.parse(open(xml_file_path, 'r'))
    except Exception as e:
        print("Error parsing XML:", str(e))
    callback_obj = Callback(paper_obj_list)
    callback_obj.print_paper()
    callback_obj.count_paper()
    
