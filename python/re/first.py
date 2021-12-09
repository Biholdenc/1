import re
import sys

for line in sys.stdin:
    line = line.strip()
    if re.search(r"cat.*cat", line):
        print(line)



for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(r"cat", line)) > 1:
        print(line)


while True:
    try:
        s = input()
    except EOFError:
        break
    r = r"cat"
    if len(re.findall(r, s)) >= 2:
        print(s)