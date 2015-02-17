#!/usr/bin/env python

class Element(object):


    tag = "html"
    indent = "  "


    def __init__(self, content=None):
        self.content = []

        if content is not None:
            self.content.append(content)

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, file, ind=""):

        file.write("<" + self.tag + ">")
        file.write('\n')
        for line in self.content:
            file.write(self.indent + line)
            file.write('\n')
        file.write("</" + self.tag + ">")
