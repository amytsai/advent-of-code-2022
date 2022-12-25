import sys
import copy

def part_one(board, moves):
    for move in moves:
        _, move_n, _, from_n, _, to_n = move.split()
        move_n = int(move_n)
        from_n = int(from_n)
        to_n = int(to_n)
        for _ in range(move_n):
            tmp = board[from_n].pop()
            board[to_n].append(tmp)
    
    output = ''
    for key in range(1, 10):
        output += board[key][-1]
    return output

def part_two(board, moves):
    for move in moves:
        _, move_n, _, from_n, _, to_n = move.split()
        move_n = int(move_n)
        from_n = int(from_n)
        to_n = int(to_n)

        tmp = board[from_n][-move_n:]
        board[from_n] = board[from_n][:len(board[from_n])-move_n]
        board[to_n].extend(tmp)
    
    output = ''
    for key in range(1, 10):
        output += board[key][-1]
    return output

def main():
    input_file = '/Users/amytsai/Code/advent-of-code-2022/inputs/day-5-input'
    parsed_lines = open(input_file).readlines()
    board = {
        key: list() for key in range(1, 10)
    }

    for key in range(1, 10):
        for line in range(7, -1, -1):
            item = parsed_lines[line][(key-1)*4+1]
            if item != ' ':
                board[key].append(item)
    moves = [line.strip() for line in parsed_lines[10:]]

    part_one_ans = part_one(copy.deepcopy(board), moves)
    print(f'Part 1 Answer: {part_one_ans}')
    part_two_ans = part_two(board, moves)
    print(f'Part 2 Answer: {part_two_ans}')

if __name__ == '__main__':
    sys.exit(main())