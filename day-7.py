import sys
from dataclasses import dataclass
from typing import Any

@dataclass
class Node:
    name: str
    size: int
    type: str
    children: list[str]

    def __init__(self, name: str, size: int, type: str, children: list[Any]):
        self.name = name
        self.size = size
        self.type = type
        self.children = []
    
    def update_size(self):
        if type == 'file':
            return
        else:
            for child in self.children:
                if child.type == 'dir':
                    child.update_size()
            self.size = sum([child.size for child in self.children])

@dataclass
class FileTree:
    root: Node
    current: Node
    stack: list[Node]

    def __init__(self):
        self.root = Node(name='/', size=0, type='dir', children=[])
        self.current = self.root
        self.stack = []
    
    def cd_root(self):
        self.current = self.root
        self.stack = []

    def cd(self, name: str):
        if name == '..':
            if self.current == self.root:
                pass
            else:
                self.current = self.stack.pop()
                return self.current

        elif name == '/':
            self.cd_root()
        else:
            self.stack.append(self.current)
            should_create = True
            for child in self.current.children:
                if child.name == name:
                    self.current = child
                    should_create = False
                    break
            # directory doesn't exist yet so we create it
            if should_create:
                self.current.children.append(Node(name=name, size=0, type='dir', children=[]))
                self.current = self.current.children[-1]

    def update(self, ls_output: str):
        first, name = ls_output.split()
        for child in self.current.children:
            if child.name == name:
                # item already exists
                break
        # item doesn't exist yet so we create it
        if first.isdigit():
            self.current.children.append(Node(name=name, size=int(first), type='file', children=[]))
        else:
            self.current.children.append(Node(name=name, size=0, type='dir', children=[]))
        self.root.update_size()

def find_small(root_node, threshold=100000) -> list[int]:
    '''
    Find all of the directories with a total size of at most 100000
    '''
    small_dirs = []
    if root_node.type == 'file':
        return [0]
    if root_node.type == 'dir':
        if root_node.size <= threshold:
            small_dirs.append(root_node.size)
        for child in root_node.children:
            small_dirs.extend(find_small(child, threshold))
    return small_dirs

def find_large(root_node, threshold) -> list[int]:
    '''
    Find all of the directories with a total size larger than threshold
    '''
    large_dirs = []
    if root_node.type == 'file':
        return []
    if root_node.type == 'dir':
        if root_node.size >= threshold:
            large_dirs.append(root_node.size)
        for child in root_node.children:
            large_dirs.extend(find_large(child, threshold))
    return large_dirs

def part_one(lines: list[str]):
    tree = FileTree()
    for line in lines:
        if line[0] == '$':
            _, command, *args = line.split()
            if command == 'cd':
                tree.cd(args[0])
            elif command == 'ls':
                # we don't actually process ls commands
                pass
        else:
            tree.update(ls_output=line)
    tree.root.update_size()
    return sum(find_small(tree.root))
    
def part_two(lines):
    tree = FileTree()
    for line in lines:
        if line[0] == '$':
            _, command, *args = line.split()
            if command == 'cd':
                tree.cd(args[0])
            elif command == 'ls':
                # we don't actually process ls commands
                pass
        else:
            tree.update(ls_output=line)
    tree.root.update_size()
    total_disk_space = 70000000
    free_space = total_disk_space - tree.root.size
    required_space = 30000000 - free_space
    possibilities = find_large(tree.root, required_space)
    return(min(possibilities))

def main():
    input_file = 'inputs/day-7-input'
    parsed_lines = [line.strip() for line in open(input_file).readlines()]

    part_one_ans = part_one(parsed_lines)
    print(f'Part 1 Answer: {part_one_ans}')
    part_two_ans = part_two(parsed_lines)
    print(f'Part 2 Answer: {part_two_ans}')

if __name__ == '__main__':
    sys.exit(main())