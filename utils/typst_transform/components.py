import re

'''
Components can be designed to represent either
whole blocks, or substructures of blocks.

For example, suppose we have a block:
::: rect
=== Title
Content
:::

`=== Title` could be considered a substructure of
the rectangle block. In general, all you need is 
to create a component with a pattern 
'''

'''
from words import WORDS

dropdown_display_component = Component(name="dropdown_display_component", pattern=re.compile(r"::: rect\n(.*?)\n:::"))
dropdown_display_component.sub(WORDS[word_replacement_name], )
'''

'''
Would it be better if this was a regular class and
the callable was an instance method?

Probably would make it easier to automate, because 
then all the relevant methods would be grouped under 
that component... but it would make *creating* 
components more difficult and less general. I'm leaning
more towards using regular classes since there could be
lots of extra processing a component has to do relative 
to other components.

Still want to maintain that components use each other

I think the methods need to be static to make it as
convenient as possible to call the replacements
=> Rather than instantiating the components with a pattern
    at runtime, do it here with a static pattern (since it's
    true the patterns won't change)
'''

class Component:
    _cname: str
    _cpattern: str

    def __init__(self, name: str, pattern: str):
        self.name = name
        self.pattern = re.compile(pattern, re.DOTALL+re.MULTILINE)

    def replacement(self, match: re.Match) -> str:
        pass

    def run(self, source: str):
        return self.pattern.sub(self.replacement, source)


class MdToHtml(Component):
    _cname = "md_to_html"
    _cpattern = r"(^|\s)([\*\_]{1,2})(.+?)[\*\_]{1,2}"

    def __init__(self):
        super().__init__(self._cname, self._cpattern)

    def replacement(self, match: re.Match) -> str:
        md_char = match.group(2)
        content = match.group(3)

        if md_char in ["_", "*"]:
            return f" <i>{content}</i>"
        elif md_char == "**":
            return f" <b>{content}</b>"
        return f"{md_char}"


class DetailsContent(Component):
    _cname = "details_content"
    _cpattern = r"### ([\w\s]+)\n(.+)"

    def __init__(self):
        super().__init__(self._cname, self._cpattern)

    def replacement(self, match: re.Match) -> str:
        title = match.group(1).strip()
        content = match.group(2).strip()
        return f"<summary>{title}</summary>\n<p>\n{content}\n</p>"

class BlockQuotes(Component):
    _cname = "block_quotes"
    _cpattern = r"^(\> .+?\n)$"

    def __init__(self):
        super().__init__(self._cname, self._cpattern)
        
    def replacement(self, match: re.Match) -> str:
        quote_lines = match.group(1).split(">")
        quote_content = " ".join([
            line.strip() 
            for line in quote_lines 
            if len(line) > 0 and line != "\n"
        ])

        return f"<blockquote>{quote_content}</blockquote>"

class Details(Component):
    _cname = "details"
    _cpattern = r"::: rect\n(.*?)\n:::"

    def __init__(self):
        super().__init__(self._cname, self._cpattern)

    def replacement(self, match):
        content = match.group(1)

        md_to_html = MdToHtml()
        details_content = DetailsContent()

        res = details_content.pattern.sub(details_content.replacement, content)
        res = md_to_html.pattern.sub(md_to_html.replacement, res)
        return f"<details>\n{res}\n</details>"


class AlignedLineBreaks(Component):
    _cname = "aligned_line_breaks"
    _cpattern = r"\s\\{2}\s"

    def __init__(self):
        super().__init__(self._cname, self._cpattern)

    def replacement(self, _: re.Match) -> str:
        return " \\\\\\\\\n"


class MathBlock(Component):
    _cname = "math_block"
    _cpattern = r"\$\$(.*?)\$\$"

    def __init__(self):
        super().__init__(self._cname, self._cpattern)

    def replacement(self, match: re.Match) -> str:
        aligned_line_breaks = AlignedLineBreaks()

        mt = aligned_line_breaks.pattern.sub(aligned_line_breaks.replacement, match.group(1))
        return f"$${mt}$$"


class RemoveSingleLineBreaks(Component):
    _cname = "remove_single_line_breaks"
    _cpattern = r"\n\\\n"

    def __init__(self):
        super().__init__(self._cname, self._cpattern)

    def replacement(self, _: re.Match) -> str:
        return ""
    
class RemoveUnwantedCharacters(Component):
    _cname = "remove_unwanted_characters"
    _cpattern = r"\s?(℄)\s?"

    def __init__(self):
        super().__init__(self._cname, self._cpattern)

    def replacement(self, _: re.Match) -> str:
        return ""
    
class FixLinks(Component):
    _cname = "fix_links"
    _cpattern = r"\[(\[[.\s\S]+)\]\{\.\w+\}"

    def __init__(self):
        super().__init__(self._cname, self._cpattern)

    def replacement(self, match: re.Match) -> str:
        link: str = match.group(1)
        link = link.replace("\n", " ")
        return link
    
class CreateHeadingSpace(Component):
    _cname = "create_heading_space"
    _cpattern = r"## [\w\s]+"

    def __init__(self):
        super().__init__(self._cname, self._cpattern)
    
    def replacement(self, match: re.Match) -> str:
        heading = match.group(0)
        return f"<br>\n\n{heading}"