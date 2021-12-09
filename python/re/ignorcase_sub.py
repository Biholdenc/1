import re
import sys

for line in sys.stdin:
    line = line.strip()
    print(re.sub(r'\b(a+)\b', "argh", line, 1, flags=re.IGNORECASE))
