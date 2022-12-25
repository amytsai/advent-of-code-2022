import sys
def part_one(pairs):
    total = 0
    for first, second in pairs:
        f1, f2 = first
        s1, s2 = second
        all_nums = [f1, f2, s1, s2]
        max_val = max(all_nums)
        min_val = min(all_nums)
        if (f1 == min_val and f2 == max_val) or (s1 == min_val and s2 == max_val):
            total += 1
    return total

def part_two(pairs):
    total = 0
    for first, second in pairs:
        f1, f2 = first
        s1, s2 = second
        if not(f2 < s1 or s2 < f1):
            total += 1
    return total

def main():
    input_file = '/Users/amytsai/Code/advent-of-code-2022/inputs/day-4-input'
    parsed_lines = [line.strip() for line in open(input_file).readlines()]
    parsed_pairs = [
        [
            [int(x) for x in t.split('-')]
            for t in line.split(',')
        ] 
        for line in parsed_lines
    ]

    part_one_ans = part_one(parsed_pairs)
    print(f'Part 1 Answer: {part_one_ans}')
    part_two_ans = part_two(parsed_pairs)
    print(f'Part 2 Answer: {part_two_ans}')


if __name__ == '__main__':
    sys.exit(main())