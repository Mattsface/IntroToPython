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

    def render_tag(self):
        pass

    def render(self, file, ind=""):
        # trying to render this shit


class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"