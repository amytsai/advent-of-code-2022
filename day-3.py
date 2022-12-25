import sys
from math import floor

def part_one(lines):
    score = 0
    for sack in lines:
        pivot = floor(len(sack)/2)
        first = set([x for x in sack[0:pivot]])
        second = set([x for x in sack[pivot:]])
        intersection = first.intersection(second)
        score += priority(intersection.pop())
    return score

def part_two(lines):
    score = 0
    while lines:
        first = set([x for x in lines.pop()])
        second = set([x for x in lines.pop()])
        third = set([x for x in lines.pop()])
        intersection = first.intersection(second).intersection(third)
        score += priority(intersection.pop())
    return score

def priority(intersection):
    if intersection.isupper():
        return ord(intersection) - 38
    else:
        return ord(intersection) - 96

def main():
    input_file = 'inputs/day-3-input'
    parsed_lines = [line.strip() for line in open(input_file).readlines()]

    part_one_ans = part_one(parsed_lines)
    print(f'Part 1 Answer: {part_one_ans}')
    part_two_ans = part_two(parsed_lines)
    print(f'Part 2 Answer: {part_two_ans}')

if __name__ == '__main__':
    sys.exit(main())