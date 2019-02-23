# Centrality Variants

There are several ways of calculating the centrality of nodes in a graph. The idea of "centrality" is to reflect how connected/influential a node is on the structure of the graph as a whole. Each description is of the appropriate centrality measure for a node `n` in an undirected graph `G := (V, E)`.

References:
- https://en.wikipedia.org/wiki/Centrality
- chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/https://cs.brynmawr.edu/Courses/cs380/spring2013/section02/slides/05_Centrality.pdf
- http://complexitylabs.io/network-centrality/
- https://www.datacamp.com/community/tutorials/centrality-network-analysis-R
- https://aksakalli.github.io/2017/07/17/network-centrality-measures-and-their-visualization.html
- https://www.r-bloggers.com/network-centrality-in-r-an-introduction/


## Degree Centrality

The proportion of edges that `n` is a node of. This is the strength of `n`'s the _immediate_ influence of on `G`; the size of its immediate neighborhood.

## Eigenvector Centrality

The sum of the ranks of `n`'s direct neighbors, weighted by rank. This is like the degree centrality but weighting each connection by the rank of other node. Initial ranks are the degree centrality values.

## Closeness Centrality

The inverse of the average distance of `n` to every other node in `G`. This is the distance of `n` from the center of mass of `G`. 

## Betweenness Centrality

The proportion of shortest paths that `n` is a node of.
 This is the strength of `n` on the interaction of unconnected nodes in `G`. In other words, it is the proportional likelihood that a (random weighted by length) path of influence between two nodes will go through `n`.


# Notes

In order of short-to-long distance consideration:
- Degree: hyper-closeness (direct) collaboration
- Eigenvector centrality is like short-distance collaboration
- Betweenness/Closeness (which one?) is like long-distance influence/connectivity
