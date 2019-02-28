# Done

## February 22 - February 28

- for AuthorsNetwork:
  - separate connected components into their own gexf files (via `AuthorsGraph.isolate_component(cc_rank)`)
  - do centrality measurements for each component separately (via `AuthorsGraph.fill_all_centralities(calculate = True)` after `AuthorsGraph.isolate_component(cc_rank)`)

## February 15-21

- "one-sentence" explanations of centrality measurements: `notes/Centralities.md`

- for AuthorsNetwork and PapersNetwork: made 4 colorings of networks by centrality measurements

- in authors network, colored connected components by component size (measured in number of nodes)

- convert centrality measures to log-log scale

- colored PapersNetwork in Gephi by each centrality measure

- make PapersNetwork in which each node is a paper and nodes are connected if they share authors.

## February 8-14

- think of interesting semantic questions for network
  - wrote descriptions in `notes/Research Questions.md`

- think about what centrality means, go through each of the measures so far
  - degree centrality: how many authors collaborated with an author
  - eigenvector centrality: how many connected authors collaborated with an author
  - closeness centrality: how efficiently an author is connected to the rest of the network (where not being connected at all is counted as bad)
  - betweenness centrality: how many efficient connections between authors are facilitated by an author; how many efficiency-bridges this author is part of

- explore conn-comps (graph colors top 10ish), and dist of sizes
  - make Gephi graph where the top 10 components are colored, and others are gray
  - seems to really help visually in interpreting the graph

- change axis to log scale
  - changed all to log scale

- change axis to absolute (degree)
  - changed degree centrality to absolute. other centrality measures are relative by definition, so multiplying by #nodes doesn't really make sense

- remove TPU paper (Google), and outline
  - restricted x-range to have maximum. each centrality measure found its own sweet spot that captured a reasonable majority of the data

## January 31 - February 7

- measure centralities
  - created graph object and use networkx library to calculate degree, eigenvector, closeness, and betweeness centralities. implemented in python/authors_network/authors_network.py

- used data from Semantic Scholar for group A rather that probably-poorly disambiguated data from the pdf-to-xmls.
