import re
import argparse

from datetime import datetime

from components import Details, MathBlock, RemoveSingleLineBreaks

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input_file")
args = parser.parse_args()

# math_block_pattern = re.compile(r"\$\$(.*?)\$\$", re.DOTALL)

'''
Step 1:

Compile the pattern for the component-level pattern to edit in

We don't care about any text that isn't contained within some
sort of block, since that'll always be valid Markdown

Blocks include: `::: :::`, `$ $`, `$$ $$`, `<tag> </tag>`
'''
# rect_pattern = re.compile(r"::: rect\n(.*?)\n:::", re.DOTALL)

# metadata = {
#     "title": args.input_file.split(".")[0],
#     "date": datetime.now().date().isoformat(),
#     "math": True,
# }
# metadata_s = "\n".join([f"{key}: {value}" for (key, value) in metadata.items()])
# front_matter = f"---\n{metadata_s}\n---\n\n"

# def rds(match):
#     mt = re.sub(r"\\\\", r"\\\\\\\\", match.group(1))
#     return f"$${mt}$$"

# def mdToHTML(match):
#     '''
#     `group` refers to the capturing group, 
#     where group 0 is the whole matched string
#     '''
#     md_char = match.group(1)
#     content = match.group(2)

#     if md_char in ["_", "*"]:
#         return f"<i>{content}</i>"
#     elif md_char == "**":
#         return f"<b>{content}</b>"
#     return f"{md_char}"

'''
rect_component.sub(fixRect, source)

res = rect_title_component.sub(lambda x: x, content)
res = md_to_html_component.sub(mdToHTML, res)
return f"{res}"
'''

# def fixRect(match):
#     content = match.group(1)

#     res = re.compile(r"=== (.+)\n").sub(lambda x: f"<summary>{x.group(1)}</summary>\n", content)
#     res = re.compile(r"([\*\_]{1,2})(.+?)[\*\_]{1,2}").sub(mdToHTML, res)
#     return f"<details>\n{res}\n</details>"

with open(args.input_file, "r+") as f:
    source = f.read()
    # res = math_block_pattern.sub(rds, source)

    '''
    Here we call `component_pattern.sub(f, source)` to begin the replacements

    For each match, we call `f` and can extract more out with:
    ```
    re.compile(r"<inner_pattern>").sub(lambda x: x, content)
    ```

    The way this would be used is as follows:
    1. Identify components that could be converted
    2. For each component, compile a pattern
    3. Run component_pattern.sub(f, source) and for each match, run common subs on common patterns
        - Ex: Markdown --> HTML formatting
    4. The final result that gets returned by `f` is the correctly formatted component
    '''
    details = Details()
    mb = MathBlock()
    rmslb = RemoveSingleLineBreaks()

    # Imperative style
    res = details.pattern.sub(details.replacement, source)
    res = mb.pattern.sub(mb.replacement, res)
    res = rmslb.pattern.sub(rmslb.replacement, res)

    # Alternatively - functional style
    # res = math_block.pattern.sub(math_block.replacement, details.pattern.sub(details.replacement, source))

    '''
    # Multi-line functional style

    res = rmslb.pattern.sub(
        rmslb.replacement
        mb.pattern.sub(
            mb.replacement,
            details.pattern.sub(
                details.replacement,
                source,
            ),
        ),
    )
    '''
    
    print(res)
    # f.seek(0)
    # f.flush()
    # f.write(front_matter)
    # f.write(res)