import numpy as np

step = 64

colors = [ (r/256,g/256,b/256)
    for r in range(0, 256, step)
    for g in range(0, 256, step)
    for b in range(0, 256, step)
]