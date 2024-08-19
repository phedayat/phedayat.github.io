import re
import argparse

from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input_file")
args = parser.parse_args()

math_block_pattern = re.compile(r"\$\$(.*?)\$\$", re.DOTALL)

metadata = {
    "title": args.input_file.split("/")[1].split(".")[0],
    "date": datetime.now().date().isoformat(),
    "math": True,
}
metadata_s = "\n".join([f"{key}: {value}" for (key, value) in metadata.items()])
front_matter = f"---\n{metadata_s}\n---\n\n"

def rds(match):
    mt = re.sub(r"\\\\", r"\\\\\\\\", match.group(1))
    return f"$${mt}$$"

def replace_rect(match):
    mt = re.sub(r"===", r"")

with open(args.input_file, "r+") as f:
    source = f.read()
    res = math_block_pattern.sub(rds, source)
    # res = 

    f.seek(0)
    f.flush()
    f.write(front_matter)
    f.write(res)