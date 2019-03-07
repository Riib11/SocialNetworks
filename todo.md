# To Do

# !!!

- Cleaning up data:
  - find original paper titles data
  - to find conference names, match papers in SS to raw paper titles this solves the previous problem:
    - there are a few rogue "venue" values that are pointed out in `papers_network/papesr_network.py` in the definition of `venues` that I added but weren't found among the papers that I looked through (`/systems-papers/sys-papers/`)

# !!

- find authors for high eigenvector group in AuthorsNetwork

# !
- color pixels by connected component (look this up: stacked bar chart)
- compare to control conferences: SIGIR, KDD, SLE, OOPSLA, PLDI, IDCM, SPAA
- this would amount to just changing the coloring so that the non-control and control conferences are different colors.
