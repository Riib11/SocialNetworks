# Done

## February 14th

- think of interesting semantic questions for network
  - wrote descriptions in notes/Research Questions.md

- think about what centrality means, go through each of the measures so far
  - degree centrality: how many authors collaborated with an author
  - eigenvector centrality: how many connected authors collaborated with an author
  - closeness centrality: how efficiently an author is connected to the rest of the network (where not being connected at all is counted as bad)
  - betweenness centrality: how many efficient connections between authors are facilitated by an author; how many efficiency-bridges this author is part of

- explore conn-comps (graph colors top 10ish), and dist of sizes
  - make gephi graph where the top 10 components are colored, and others are gray
  - seems to really help visually in interpreting the graph

- change axis to log scale
  - changed all to log scale

- change axis to absolute (degree)
  - changed degree centrality to absolute. other centrality measures are relative by definition, so multiplying by #nodes doesn't really make sense

- remove TPU paper (Google), and outline
  - restricted x-range to have maximum. each centrality measure found its own sweet spot that captured a reasonable majority of the data

## February 17th

- measure centralities
  - created graph object and use networkx library to calculate degree, eigenvector, closeness, and betweeness centralities. implemented in python/authors_network/authors_network.py

- used data from Semantic Scholar for group A rather that probably-poorly disambiguated data from the pdf-to-xmls.
