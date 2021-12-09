import re
import sys

for line in sys.stdin:
    line = line.strip()
    pattern = r'(\w)\1+'
    print(re.sub(pattern, r'\1', line))
