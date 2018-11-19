import os
import sys
import numpy as np
arg1 = sys.argv[0]
arg2 = sys.argv[1]


#directory = "T4500_AC7.0"
#print(directory)
print(arg2)
files = os.listdir(arg2)

for afile in files:
    thing = afile.strip().split(".csv")[0].split("z")[1].split("c")

    print(np.array(thing, dtype=float).sum() + 8.43)
