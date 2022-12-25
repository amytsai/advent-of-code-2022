import sys

def part_one(lines):
    shape_to_score = {
        'X': 1,
        'Y': 2,
        'Z': 3,
    }

    combo_to_score = {
        'C:X': 6, # scissors, rock
        'B:Z': 6, # paper, sci
        'B:Y': 3, # paper, paper
        'A:Z': 0, # rock, sci
        'A:Y': 6, # rock, paper
        'B:X': 0, # paper, rock
        'A:X': 3, # rock, rock
        'C:Z': 3, # sci, sci
        'C:Y': 0, # sci, paper
    }
    score = 0
    for round in lines:
        them, me = round.split(' ')
        score += shape_to_score[me]
        score += combo_to_score[f'{them}:{me}']
    return score

def part_two(lines):
    outcome_to_score = {
        'X': 0,
        'Y': 3,
        'Z': 6,
    }

    combo_to_score = {
        'C:X': 2, # scissors, lose, paper
        'B:Z': 3, # paper, win, scis
        'B:Y': 2, # paper, draw, paper
        'A:Z': 2, # rock, win, paper
        'A:Y': 1, # rock, draw, rock
        'B:X': 1, # paper, lose, rock
        'A:X': 3, # rock, lose, scis
        'C:Z': 1, # sci, win, rock
        'C:Y': 3, # sci, draw, sci
    }
    score = 0
    for round in lines:
        them, me = round.split(' ')
        score += outcome_to_score[me]
        score += combo_to_score[f'{them}:{me}']
    return score


def main():
    input_file = 'inputs/day-2-input'
    parsed_lines = [line.strip() for line in open(input_file).readlines()]

    part_one_ans = part_one(parsed_lines)
    print(f'Part 1 Answer: {part_one_ans}')
    part_two_ans = part_two(parsed_lines)
    print(f'Part 2 Answer: {part_two_ans}')

if __name__ == '__main__':
    sys.exit(main())