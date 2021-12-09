import re
import sys

for line in sys.stdin:
    line = line.strip()
    pattern = r'\b(\w)(\w)+?'
    print(re.sub(pattern, r'\2\1', line))
    print(re.sub(r'\b(\w)(\w)', r"\2\1", line))
