import sys

def part_one(grid):
    visible = 0
    y_max = len(grid)
    x_max = len(grid[0])
    for x in range(0, x_max):
        for y in range(0, y_max):
            # edges
            if x == 0 or x == x_max - 1 or y == 0 or y == y_max - 1:
                visible += 1
            # interior
            else:
                tree = grid[y][x]
                left_visible = tree > max(grid[y][0:x])
                right_visible = tree > max(grid[y][x+1:])
                top_visible = tree > max([grid[y][x] for y in range(0, y)])
                bottom_visible = tree > max([grid[y][x] for y in range(y+1, y_max)])
                if any([left_visible, right_visible, top_visible, bottom_visible]):
                    visible += 1
    return visible

def part_two(grid):
    scores = []
    y_max = len(grid)
    x_max = len(grid[0])
    for x in range(0, x_max):
        for y in range(0, y_max):
            # edges
            if x == 0 or x == x_max - 1 or y == 0 or y == y_max - 1:
                scores.append(0)
            # interior
            else:
                tree = grid[y][x]
                # look left
                left_score = 0
                for i in range(x-1, -1, -1):
                    if grid[y][i] >= tree:
                        left_score += 1
                        break
                    else:
                        left_score +=1
                # look right
                right_score = 0
                for i in range(x+1, x_max):
                    if grid[y][i] >= tree:
                        right_score += 1
                        break
                    else:
                        right_score +=1
                # look up
                up_score = 0
                for i in range(y-1, -1, -1):
                    if grid[i][x] >= tree:
                        up_score += 1
                        break
                    else:
                        up_score +=1
                # look down
                down_score = 0
                for i in range(y+1, y_max):
                    if grid[i][x] >= tree:
                        down_score += 1
                        break
                    else:
                        down_score +=1
                score = left_score * right_score * up_score * down_score
                # print(f'x: {x}, y: {y}, score: {score}')
                scores.append(score)
    return max(scores)

def main():
    input_file = 'inputs/day-8-input'
    parsed_grid = [
        [int(x) for x in line.strip()]
        for line in
        open(input_file).readlines()
    ]
    part_one_ans = part_one(parsed_grid)
    print(f'Part 1 Answer: {part_one_ans}')
    part_two_ans = part_two(parsed_grid)
    print(f'Part 2 Answer: {part_two_ans}')

if __name__ == '__main__':
    sys.exit(main())