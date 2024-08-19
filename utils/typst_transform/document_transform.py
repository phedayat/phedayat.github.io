from typing import List
from datetime import datetime
from argparse import ArgumentParser
from os.path import basename, extsep

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

metadata = {
    "title": basename(args.input_file).split(extsep)[0],
    "date": datetime.now().date().isoformat(),
    "math": True,
}
metadata_s = "\n".join([f"{key}: {value}" for (key, value) in metadata.items()])
front_matter = f"---\n{metadata_s}\n---\n\n"

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
    f.write(front_matter)
    f.write(source)
