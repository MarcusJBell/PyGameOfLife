import os
import sys
import time


class World:
    width = 0
    height = 0
    cells = []

    def __init__(self, width, height):
        self.width = width
        self.height = height

        for y in range(0, height):
            self.cells.append([])
            for x in range(0, width):
                self.cells[y].append(Cell())

    def render(self):
        cls = os.system('CLS')

        for row in self.cells:
            for cell in row:
                if cell.alive:
                    sys.stdout.write('X')
                else:
                    sys.stdout.write(' ')
            sys.stdout.write('\n')

    def update(self):
        for y, row in enumerate(self.cells):
            for x, tile in enumerate(row):
                neighbor_count = self.get_neighbor_count(x, y)
                if tile.alive:
                    if neighbor_count < 2 or neighbor_count > 3:
                        tile.next_state = False
                elif neighbor_count == 3:
                    tile.next_state = True

        for row in self.cells:
            for tile in row:
                tile.alive = tile.next_state

    def get_neighbor_count(self, x, y):
        count = 0
        for nx in range(x - 1, x + 2):
            for ny in range(y - 1, y + 2):
                if nx < 0 or nx > self.width - 1 or ny < 0 or ny > self.height - 1:
                    continue
                if nx == x and ny == y:
                    continue

                value = self.cells[ny][nx]
                if value.alive:
                    count = count + 1
        return count


class Cell:
    alive = False
    next_state = False


def load_world(world):
    project_path = os.path.abspath(os.path.dirname(__file__))
    file = open(os.path.join(project_path, 'world.txt'), mode='r')
    print(file)

    for y, line in enumerate(file.readlines()):
        for x, c in enumerate(list(line.rstrip('\n\r'))):
            if c == '1':
                world.cells[y][x].alive = True
                world.cells[y][x].next_state = True


def main():
    world = World(120, 60)
    load_world(world)

    count = 0
    while True:
        world.update()
        world.render()
        count = count + 1
        time.sleep(0.25)


main()
