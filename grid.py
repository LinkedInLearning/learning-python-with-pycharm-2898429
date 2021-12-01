from cell import Cell

CELL_OFFSET = 2
PADDING = 7


class Grid:
    def __init__(self, screen_dimensions: tuple, surface, width: int, height: int):
        self.width = width
        self.height = height

        screen_width, screen_height = screen_dimensions
        effective_width, effective_height = screen_width - 2 * PADDING - (CELL_OFFSET * (width - 1)), screen_height - 2 * PADDING - (CELL_OFFSET * (height - 1))

        cell_width, cell_height = (effective_width / width, effective_height / height)
        self.cells = [
            [Cell((PADDING + x * (cell_width + CELL_OFFSET), PADDING + y * (cell_height + CELL_OFFSET)), (cell_width, cell_height)) for x in range(width)] for y in
            range(height)]

    def __str__(self):
        output = ""
        for row in self.cells:
            for cell in row:
                output += str(cell)
            output += "\n"
        return output

    def flip(self, col: int, row: int):
        if col < 0 or col >= self.width:
            raise RuntimeError(
                f"error updating cell at column {col}: expected column number between 0 and {self.width - 1}")
        if row < 0 or row >= self.height:
            raise RuntimeError(
                f"error updating cell at row {row}: expected column number between 0 and {self.height - 1}")

        self.cells[row][col].flip()

    def __compute_future_states(self):
        # navigate through the grid, for each cell find its valid neighbors
        for row_index, row in enumerate(self.cells):
            for col_index, cell in enumerate(row):
                cell.set_future_state(self.__count_living_neighbors(col_index, row_index))

    def update(self):
        self.__compute_future_states()
        for row in self.cells:
            for cell in row:
                cell.update()

    def draw(self, surface):
        for row in self.cells:
            for cell in row:
                cell.draw(surface)

    def check_clicks(self, pos):
        for row in self.cells:
            for cell in row:
                if cell.collidepoint(pos):
                    cell.flip()

    def reset(self):
        for row in self.cells:
            for cell in row:
                cell.set_inactive()

    def insert_shape(self, shape_name):
        match shape_name:
            case 'glider':
                self.flip(2, 1)
                self.flip(3, 2)
                self.flip(1, 3)
                self.flip(2, 3)
                self.flip(3, 3)
            case 'pentadecathlon':
                self.flip(5, 7)
                self.flip(6, 7)
                self.flip(7, 6)
                self.flip(7, 8)
                self.flip(8, 7)
                self.flip(9, 7)
                self.flip(10, 7)
                self.flip(11, 7)
                self.flip(12, 6)
                self.flip(12, 8)
                self.flip(13, 7)
                self.flip(14, 7)
            case 'lightweight':
                self.flip(0, 0)
                self.flip(3, 0)
                self.flip(4, 1)
                self.flip(0, 2)
                self.flip(4, 2)
                self.flip(1, 3)
                self.flip(2, 3)
                self.flip(3, 3)
                self.flip(4, 3)

    # cells have up to 8 neighbours, except cells in the boundary rows and columns.
    # this iterator yields a given position's neighbors
    def __count_living_neighbors(self, col: int, row: int):
        if col < 0 or col >= self.width:
            raise RuntimeError(
                f"error updating cell at column {col}: expected column number between 0 and {self.width - 1}")
        if row < 0 or row >= self.height:
            raise RuntimeError(
                f"error updating cell at row {row}: expected column number between 0 and {self.height - 1}")

        count = 0
        # top left
        if row > 0 and col > 0 and self.cells[row - 1][col - 1].active:
            count += 1
        # top
        if row > 0 and self.cells[row - 1][col].active:
            count += 1
        # top right
        if row > 0 and col < self.width - 1 and self.cells[row - 1][col + 1].active:
            count += 1
        # right
        if col < self.width - 1 and self.cells[row][col + 1].active:
            count += 1
        # bottom right
        if row < self.height - 1 and col < self.width - 1 and self.cells[row + 1][col + 1].active:
            count += 1
        # bottom
        if row < self.height - 1 and col < self.width - 1 and self.cells[row + 1][col].active:
            count += 1
        # bottom left
        if row < self.height - 1 and col < self.width - 1 and self.cells[row + 1][col - 1].active:
            count += 1
        # left
        if col < self.width - 1 and self.cells[row][col - 1].active:
            count += 1

        return count
