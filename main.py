import xml.sax
import gzip
import xml.etree.ElementTree as ET


class MyHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_element = ""
        self.text = ""
        self.mdate = ""

    def startElement(self, name, attrs):
        self.current_element = name
        if name == "article":
            self.mdate = attrs.get("mdate", "")  # Get the mdate attribute

    def characters(self, content):
        self.text += content

    def endElement(self, name):
        if name == "title":
            print("Title:", self.text)
        elif name == "author":
            print("Author:", self.text)
        elif name == "year":
            print("Year:", self.text)
        elif name == "journal":
            print("Journal:", self.text)
        elif name == "ee":
            print("EE URL:", self.text)
        elif name == "article":
            print("MDate:", self.mdate)
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

