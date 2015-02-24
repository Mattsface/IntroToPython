#!/usr/bin/env python

class Element(object):
    tag = "html"
    indent = "  "

    def __init__(self, content=None, **attributes):
        self.content = []
        self.attributes = attributes

        if content is not None:
            self.content.append(content)

    def append(self, new_content):
        self.content.append(new_content)

    def render_tag(self, indent="", closing=True):
        """
        Render a html tag
        """

        if self.attributes and closing == False:
            self.attributes = ''.join('{}="{}"'.format(key, val) for key, val in self.attributes.items())
            return "{}{}<{} {}>".format(indent, self.indent, self.tag, self.attributes)

        if not closing:
            return "{}{}<{}>".format(indent, self.indent, self.tag)
        else:
            return "{}{}</{}>".format(indent, self.indent, self.tag)

    def render(self, html_file, indent=""):
        """
        Let's try and fucking render this bullshit.

        Indentation isn't stacking correctly, I need to keep track of the current indent level for each tag, and
        then move back from it.
        """
        html_file.write(self.render_tag(indent, closing=False))
        html_file.write('\n')

        for con in self.content:
            try:
                html_file.write(indent + self.indent + con + "\n")
            except TypeError:
                con.render(html_file, (indent + self.indent))

        html_file.write(self.render_tag(indent))
        html_file.write('\n')


class Html(Element):
    tag = "html"
    indent = ""


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class Title(OneLineTag):
    tag = "title"


class OneLineTag(Element):
    def render(self, html_file, indent=""):
        html_file.write(self.render_tag(indent, closing=False))
        for con in self.content:
            try:
                html_file.write(indent + self.indent + con)
            except TypeError:
                con.render(html_file, (indent + self.indent))

        html_file.write(self.render_tag(indent))
        html_file.write('\n')


