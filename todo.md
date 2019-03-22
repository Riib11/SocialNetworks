# To Do

## !!!

- `Winsorize` function in r (removes outliers) (use `prob` interval)
- spend some time looking at correlations and pairs matrix and see what the relationship between different ones are somehow
- hypothesis: there is no relationship between how collaborative you are and your "influence score" (e.g. hindex, i10index)

- color author network by gender, country, other personsfeatures

- reproduce graph of conference citations (with new conference names)

- copy over semantic scholar id data to Eitan; mapping paper_key => s2id (PODC_10_001)

- export adjacency matrix for clustering (for PapersNetwork)

- look up info on how centralities are used (in data science)


## !!

- say something summarizing about
  - what do centrality measures say about authors (noting don't correlate strongly with index values)
  - how related systems conferences are (systemy-like)
  - read paper from Eitan

- find authors for high eigenvector group in AuthorsNetwork

## !

- color pixels by connected component (look this up: stacked bar chart) # maybe don't need to do this because I made the pairs matrix
- compare to control conferences: SIGIR, KDD, SLE, OOPSLA, PLDI, IDCM, SPAA
- this would amount to just changing the coloring so that the non-control and control conferences are different colors. (in which graph? i.e. Papers or Authors)
