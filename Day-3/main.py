import re

with open("input.txt", "r") as file:
    text = file.read()

part1 = 0
part2 = 0

pattern = re.compile(r"mul\((-?\d+),(-?\d+)\)|(do\(\))|(don't\(\))")
matches = pattern.findall(text.strip())

do = True
for a, b, doInstr, dontInstr in matches:
  if doInstr or dontInstr:
    do = bool(doInstr)
  else:
    res = int(a) * int(b)
    part1 += res
    part2 += res * do

print("Part 1: ", part1)
print("Part 2: ", part2)