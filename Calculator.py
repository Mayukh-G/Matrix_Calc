# Author: Mayukh Gautam
# Calculates node equation using matrices
class Mat:
    def __init__(self, arr):
        if arr.__class__ != list or arr[0].__class__ != list:
            raise TypeError(f"Expected a double list. Instead got {arr}")
        self.matrix = arr
        self.rows = len(arr)
        self.columns = len(arr[0])
        self.step_count = 0

    def __str__(self):
        temp = [str(row) for row in self.matrix]
        start = "Matrix Object : "
        return start + "[\n" + "\n".join(temp) + "\n]"

    def __simplify(self, row_n, pivot_coord):
        div = self.matrix[row_n][pivot_coord]
        for i in range(self.rows + 1):
            self.matrix[row_n][i] /= div

    def __eliminate(self, main_r, pivot_coord):
        other = [i for i in range(self.rows)]
        other.remove(main_r)
        pivot = self.matrix[main_r][pivot_coord]
        for n in other:
            if self.matrix[n][pivot_coord] != 0:
                factor = -self.matrix[n][pivot_coord] / pivot
                for x in range(self.columns):
                    self.matrix[n][x] += self.matrix[main_r][x] * factor

    def row_reduce(self, show_steps=False):
        matrix = self.matrix
        for i in range(self.rows):
            pivot = None
            for j in range(self.columns):
                if not pivot:
                    pivot = matrix[i][j] if matrix[i][j] != 0 else None
                    pivot_coord = j if pivot else None
                    if pivot:
                        self.__simplify(row_n=i, pivot_coord=pivot_coord)
                        if show_steps:
                            print(f"Simplify : Step {self.step_count}\n", self)
                            self.step_count += 1
                        self.__eliminate(main_r=i, pivot_coord=pivot_coord)
                        if show_steps:
                            print(f"Eliminate : Step {self.step_count}\n", self)
                            self.step_count += 1
