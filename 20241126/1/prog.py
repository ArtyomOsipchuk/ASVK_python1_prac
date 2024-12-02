import sys

s = sys.stdin.buffer.read()
n = s[0]
r = []
shift = (len(s) - 1) // n
if not shift:
    shift = 1
for i in range(1, len(s), shift):
    r.append(s[i:i + shift])
r.sort()
sys.stdout.buffer.write(s[0:1] + b"".join(r))
