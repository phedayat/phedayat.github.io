from typing import List
from argparse import ArgumentParser

from components import (
    Details, 
    FixLinks,
    Component, 
    MathBlock,
    BlockQuotes,
    RemoveSingleLineBreaks,
    RemoveUnwantedCharacters,
)

parser = ArgumentParser()
parser.add_argument("-i", "--input_file")
args = parser.parse_args()

with open(args.input_file, "r+") as f:
    source = f.read()

    # print("ORIGINAL: ", source, "\n----------\n")

    transforms: List[Component] = [
        FixLinks(),
        BlockQuotes(),
        Details(), 
        MathBlock(), 
        RemoveSingleLineBreaks(),
        RemoveUnwantedCharacters(),
    ]
    for transform in transforms:
        source = transform.run(source)

    # print("NEW: ", source, "\n----------\n")
    print(source)

    f.seek(0)
    f.flush()
    f.write(source)
