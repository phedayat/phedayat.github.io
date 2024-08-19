from typing import List
from argparse import ArgumentParser

from components import (
    Details, 
    FixLinks,
    Component, 
    MathBlock,
    BlockQuotes,
    CreateHeadingSpace,
    RemoveSingleLineBreaks,
    RemoveUnwantedCharacters,
)

parser = ArgumentParser()
parser.add_argument("-i", "--input_file")
args = parser.parse_args()

with open(args.input_file, "r+") as f:
    source = f.read()

    transforms: List[Component] = [
        FixLinks(),
        BlockQuotes(),
        Details(), 
        MathBlock(), 
        RemoveSingleLineBreaks(),
        RemoveUnwantedCharacters(),
        CreateHeadingSpace(),
    ]
    for transform in transforms:
        source = transform.run(source)

    f.seek(0)
    f.flush()
    f.write(source)
