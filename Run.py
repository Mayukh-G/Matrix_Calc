# Author : Mayukh Gautam
# Main File Entry Point
from Calculator import Mat

X_F = 2.643 / 4.547
Y_F = 3.7 / 4.547
SUPP_Y = 876.9  # kN
SUPP_X = 0

m = Mat([
    [1, 0, 0, 8],
    [0, 0, 1, 7],
    [3, 3, 0, 9]
])
m.row_reduce(show_steps=True)
print(m)
