import sys
def part_one():
    input_file = '/Users/amytsai/Code/advent-of-code/inputs/day-1-input'
    lines = [line.strip() for line in open(input_file).readlines()]
    elfs = []
    tmp_line = []
    for line in lines:
        if line.isnumeric():
            tmp_line.append(int(line))
        else:
            elfs.append(tmp_line)
            tmp_line = []
    
    max_cal = float('-inf')
    for elf in elfs:
        if sum(elf) > max_cal:
            max_cal = sum(elf)
    return max_cal

def part_two():
    input_file = '/Users/amytsai/Code/advent-of-code/inputs/day-1-input'
    lines = [line.strip() for line in open(input_file).readlines()]
    elfs = []
    tmp_line = []
    for line in lines:
        if line.isnumeric():
            tmp_line.append(int(line))
        else:
            elfs.append(tmp_line)
            tmp_line = []
    
    sums = [sum(x) for x in elfs]
    sums = sorted(sums, reverse=True)
    return sum(sums[0:3])

def main():
    part_one_ans = part_one()
    print(f'Part 1 Answer: {part_one_ans}')
    part_two_ans = part_two()
    print(f'Part 2 Answer: {part_two_ans}')


if __name__ == '__main__':
    sys.exit(main())