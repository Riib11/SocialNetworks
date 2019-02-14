# Done

## February 14th

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
