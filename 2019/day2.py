from typing import List

INPUT=[1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,19,5,23,2,6,23,27,1,6,27,31,2,31,9,35,1,35,6,39,1,10,39,43,2,9,43,47,1,5,47,51,2,51,6,55,1,5,55,59,2,13,59,63,1,63,5,67,2,67,13,71,1,71,9,75,1,75,6,79,2,79,6,83,1,83,5,87,2,87,9,91,2,9,91,95,1,5,95,99,2,99,13,103,1,103,5,107,1,2,107,111,1,111,5,0,99,2,14,0,0]

HALT=99
ADD=1
MULT=2

def calc(list : List[int]) -> None:
    pos = 0

    while list[pos] != 99:
        opcode, in1, in2, out = list[pos], list[pos+1], list[pos+2], list[pos+3]
        if opcode == ADD:
            list[out] = list[in1] + list[in2]
        elif opcode == MULT:
            list[out] = list[in1] * list[in2]
        else:
            raise ValueError(f"Error: {list[pos]}")
        pos += 4
    return list

assert calc([1,0,0,0,99]) == [2,0,0,0,99]
assert calc([2,3,0,3,99]) == [2,3,0,6,99]
assert calc([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
assert calc([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]

# part 1
def run(list: List[int], noun: int = 12, verb: int = 2) -> int:
    list = list[:]
    list[1] = noun
    list[2] = verb
    return calc(list)[0]

print(run(INPUT))

# part 2
TARGET = 19690720

for noun in range(100):
    for verb in range(100):
        output = run(INPUT, noun, verb)
        if output == TARGET:
            print(noun, verb, 100 * noun + verb)
            break



