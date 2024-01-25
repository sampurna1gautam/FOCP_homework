# exercise .1

import sys
print(sys.platform)

# exercise .2

import sys
args = sys.argv[1:]
print(args)

# exercise .3 

import sys
args = sys.argv[1:]
print(sorted(list(map(float, args)))[0])

# exercise .4 

import sys
print(dir(sys))

# exercise .5

import sys
from statistics import mean
args = sys.argv[1:]
if len(args) == 0:
    print("No temperatures entered!")
else:
    temperatues = list(map(float, args))
    max_temp = max(temperatues)
    min_temp = min(temperatues)
    mean_temp = mean(temperatues)
    print(f"The max temperature is: {max_temp},\nThe min temperature is: {min_temp},\nThe mean temperature is: {mean_temp}")

    # exercise . 6 

import os
import sys
print(dir(os))