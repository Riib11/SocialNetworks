from tqdm import tqdm

class XML:

    indentation = "    "
    disallowed  = "&\"%<>"

    def __init__(self, name):
        self.name = name
        self.content = []
        self.current = ""
        self.indent_level = 0

    def add(self):
        self.content.append(self.current)
        self.current = ""

    def indent(self):
        self.current += self.indent_level * XML.indentation

    def indentIn(self):
        self.indent()
        self.indent_level += 1

    def indentOut(self):
        self.indent_level -= 1
        self.indent()

    def addHeader(self, tag, attributes=None):
        attributes = attributes or {}
        self.indentIn()
        header = "<"+tag
        for k,v in attributes.items():
            header += " "+k+"=\""+str(self.clean(v))+"\""
        header += ">"
        self.current += header + "\n"
        self.add()

    def addFooter(self, tag):
        self.indentOut()
        self.current += "</"+tag+">" + "\n"
        self.add()

    def addTag(self, tag, attributes=None):
        attributes = attributes or {}
        self.indent()
        tag = "<" + tag
        for k,v in attributes.items():
            tag += " "+k+"=\""+str(self.clean(v))+"\""
        tag += "/>"
        self.current += tag + "\n"
        self.add()

    def addTagSpan(self, tag, content, attributes=None):
        attributes = attributes or {}
        self.indentIn()
        self.indent_level -= 1
        header = "<"+tag
        for k,v in attributes.items():
            header += " "+k+"=\""+str(self.clean(v))+"\""
        header += ">"
        footer = "</"+tag+">"
        self.current += header + str(content) + footer + "\n"
        self.add()

    def write(self, directory):
        with open(directory + self.name, 'w+') as file:
            for line in tqdm(self.content):
                file.write(line)

    def clean(self, s):
        for c in XML.disallowed: s = str(s).replace(c,"")
        return s