# A small tool for calculating and drawing the best function for given points.
# Copyright (C) 2021 ywa

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import math
import matplotlib.pyplot as plt

def func(x, a=1, b=0, c=0):
    fnc = (a * x ** exponent) + (b * x ** (exponent - 1)) + c
    return fnc


# gotta fix the rng problem
# fixed?
def set_up_graph(x_points, y_points, x_label="x", y_label="y"):
    rng = len(x_points)
    # labeling
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    # points
    for dot in range(len(x_points)):
        plt.scatter(x_points[dot] ** exponent, y_points[dot], color='black')
    # function
    plt.plot([func(i, exponent) for i in range(1, rng)], [func(i, exponent, a) for i  in range(1, rng)], color='black')
    # show everything
    plt.show()

def approx_var(orig_x_val, orig_y_val):
    best_approx = 9999999
    for z in range(-5000, 5001):
        a = z / 1000
        for y in range(-5000, 5001):
            temp_sum = 0
            b = y/1000
            for x in range(len(orig_x_val)):
                # actual formula
                temp_sum += (func(orig_x_val[x], a, b) - orig_y_val[x]) ** 2
            approx = math.sqrt(temp_sum / len(orig_x_val))
            if approx < best_approx: 
                result_a = a
                result_b = b
                best_approx = approx
                # print("deviation:%s ; constants%s" %(best_approx, (a, b)))
    return result_a, result_b

if __name__  == "__main__":
    # points
    orig_x_val = [2, 3, 4, 5, 6, 7]
    orig_y_val = [0.57, 0.52, 0.98, 1.3, 1.38, 2.07]
    exponent = 2
    
    # call everything
    a,b = approx_var(orig_x_val, orig_y_val)
    set_up_graph(orig_x_val, orig_y_val, a, b)
