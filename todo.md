# To Do

## !!!

!!!
- go through `found_urls.txt` and get their semantic scholar paper objects from database


!!!
- run `find_missing_papers.py` to find all of the sub-5-edit-distance papers from the 947 that are not exact title matches
  - these resulting titles you need to look up in semantic scholar and manually download

- look at authors centralities and write explanation of how they relate and what the significances are, wrapping up!

- look up info on how centralities are used (in data science)
- say something summarizing about
  - what do centrality measures say about authors (noting don't correlate strongly with index values)
  - how related systems conferences are (systems-like)

- make notes on authors pairs matrix (raise Winsorize function)
<!-- revise: reproduce graph of conference citations (with new conference names) -->
- create conferences collaborations network
- created mapping between semantic scholar author ids and normalized author names (same way as the one I made for papers)

## !!

- find authors for high eigenvector group in AuthorsNetwork

## !

- color pixels by connected component (look this up: stacked bar chart) # maybe don't need to do this because I made the pairs matrix
- compare to control conferences: SIGIR, KDD, SLE, OOPSLA, PLDI, IDCM, SPAA
- this would amount to just changing the coloring so that the non-control and control conferences are different colors. (in which graph? i.e. Papers or Authors)
