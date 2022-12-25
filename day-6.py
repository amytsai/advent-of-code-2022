import sys
def part_one(line):
    for i in range(4, len(line)):
        seq = line[i-4:i]
        seq_set = set(seq)
        if len(seq_set) == 4:
            return i

def part_two(line):
    for i in range(14, len(line)):
        seq = line[i-14:i]
        seq_set = set(seq)
        if len(seq_set) == 14:
            return i


def main():
    input_file = 'inputs/day-6-input'
    parsed_lines = [line.strip() for line in open(input_file).readlines()]
    part_one_ans = part_one(parsed_lines[0])
    print(f'Part 1 Answer: {part_one_ans}')
    part_two_ans = part_two(parsed_lines[0])
    print(f'Part 2 Answer: {part_two_ans}')

if __name__ == '__main__':
    sys.exit(main())