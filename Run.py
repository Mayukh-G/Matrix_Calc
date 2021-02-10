# Author : Mayukh Gautam
# Main File Entry Point
from Calculator import Mat

X_F = 2.643 / 4.547
Y_F = 3.7 / 4.547
SUPP_Y = 876.9  # kN
SUPP_X = 0

m = Mat([
    [1, X_F, 0],
    [0, Y_F, SUPP_Y],
    [1, 3, 4]
])
m.row_reduce(show_steps=True)
print(m)
