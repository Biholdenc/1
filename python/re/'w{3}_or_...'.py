import re
import sys
pattern = r"z...z", 'z.{3}z'
for line in sys.stdin:
    line = line.strip()
    if re.search(r"z\w{3}z", line):
        print(line)