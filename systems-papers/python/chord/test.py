import matplotlib.pyplot as plt
import numpy as np
import chord

plt.figure(figsize=(6,6))
chord.chordDiagram(
    np.array([
        [1,1,1],
        [1,1,1],
        [1,1,1]
    ]),
    plt.axes([0,0,1,1])
)
plt.show()


# def chordDiagram(X, ax, colors=None, width=0.1, pad=2, chordwidth=0.7):
"""Plot a chord diagram

Parameters
----------
X :
    flux data, X[i, j] is the flux from i to j
ax :
    matplotlib `axes` to show the plot
colors : optional
    user defined colors in rgb format. Use function hex2rgb() to convert hex color to rgb color. Default: d3.js category10
width : optional
    width/thickness of the ideogram arc
pad : optional
    gap pad between two neighboring ideogram arcs, unit: degree, default: 2 degree
chordwidth : optional
    position of the control points for the chords, controlling the shape of the chords
"""