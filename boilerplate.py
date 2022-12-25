import sys
def part_one(lines):
    return 0
def part_two(lines):
    return 0


def main():
    input_file = 'inputs/day-1-input'
    parsed_lines = [line.strip() for line in open(input_file).readlines()]

    part_one_ans = part_one(parsed_lines)
    print(f'Part 1 Answer: {part_one_ans}')
    part_two_ans = part_two(parsed_lines)
    print(f'Part 2 Answer: {part_two_ans}')


if __name__ == '__main__':
    sys.exit(main())