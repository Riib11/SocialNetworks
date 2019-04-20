# Done

## April 13 - April 19

- flush out report outline with more specifics in the Analysis and Conclusions sections
- summarize (more) thoughts on the social network analysis papers that I read

- made rough outline of Report Outline (`notes/Report Outline.md`)

- recreated authors features matrix with final data

- made authors features matrix for just the largest connected component individually

- made a final, good mapping `rawtitle => s2id` that contains the vast majority of database plus some things I had to manually search, for a total of 2430 entries.
  - this is in `find_missing/data/rawtitle_to_s2id.json` and `find_missing/data/rawtitle_to_s2id`
  - rawtitles that I still couldn't find are in `find_missing/data/unsearchable_rawtitles.txt`
  - there may be some issues, but its accurate for the most part

- debug finding keys for paper, then papers that don't have keys / map to same keys should be thrown out of gA

## April 6 - April 12

- recreated mappings as fully as possible
  - author_s2id => author_name, author_email
  - paper_s2id => paper_key
  - Jesus Christ this took a lot of work

## April 1 - April 5

- created proper and more validly-Winsorized pairs graph for authors features. only Winsorize first 9 (finely-grained) features, and found that Winsorize-fraction=0.02 is about good

- read: _On the Compliance of Women Engineers with a Gendered Scientific System_
  - information on social networks by gender in different disciplines
  - shows use of several centrality and feature measures in networks:
    - degree centrality
    - citations count
    - number of authors per paper
  - shows examples of co-authorship network visualizations:
    - style: _hairballs_
    - clustered by proximity of research subject or geographic proximity
  - classifying types of collaborations
  - references:
    - [37] Newman ME. The structure of scientific collaboration networks
      - collaborations across disciplines
    - [43,45,46] Whittington KCB. Gender and Scientific Dissemination in Public and Private Science: A Multivariate and Network Approach. 2006
    & Sugimoto CR, Ni C, West JD, Larivière V. Innovative women: an analysis of global gender disparities in patenting
    & Whittington KB, Smith-Doerr L. Gender and commercial science: Women’s patenting in the life sci- ences. J Technol Transf. 2005
      - gender disparity affected by where work is conducted
    - [14,50] Etzkowitz H, Kemelgor C, Uzzi B. Athena unbound: The advancement of women in science and tech- nology
    & Sagebiel F. New Initiatives in Science and Technology and Mathematics Education at the Formal Level: Masculinity cultures in engineering departments in institutions of higher education and perspec- tives for social change
      - engineering linked with masculinity
    - [52] Evetts J. Managing the technology but not the organization: Women and career in engineering. Women Manag Rev. 1998
      - women required to put extra effort into work for same respect
    - [22] Leahey E. Gender differences in productivity research specialization as a missing link. Gend Soc. 2006
      - women specialize less than men in research, perhaps resulting in less citations and influence

- read: _Scientific Collaboration_
  - subsection: Social Networks and Personal Factors
    - cross-disciplinary collaboration
    - personal connections lead to collaborations:
      - co-authorship network shortest path distance
      - geographic closeness
      - cultural closeness
      - types of research institution (industry/university)
    - subsection: Emergent Challenges
      - factors relevant for sustained funding
        - geographic proximity of collaborators
        - number of people in a given institution that are involved a given collaboration
        - size of collaboration (number of co-authors)
  - references:
    - Newman 2001 - The Structure of Scientific Collaborations
      - about which authors are likely to collaborate
    - Newman 2004 - Co-authorship networks and patterns of scientific collaboration
      - about collaboration facilitated across disciplines
    - Maglaughin, Sonnerwald 2005 - Factors that impact interdisciplinary natural science research collaboration in academia
      - how enjoyable successful collaborations can be
    - Lian, Guo, David 2002 - Collaborative patterns and age structures in Chinese publications
      - less mid-career scientists right now because of effects of Chinese Cultural Revolution

- discovered problem with idea to make conferences citation network more accurate with semantic scholar conference data:
  - the new data only tells us about paper=>conference in group A, but what the graph relies on is just as much the paper=>conference if group B.
  - the new data is that we have the semantic scholar id for each paper as well as its conference. But the semantic scholar data for conferences is not usable (not standardized). so since we don't have the conference data for papers in group B, there is no new data about group B's conferences and thus the group A -> group B conference citation network

- email Eitan the csv for author_id => (author_name, author_email mapping)
- emailed Eitan the csv for papers and authors networks adjacency matrices
- emailed Eitan the papers=>keys mapping

- redid that pairs matrix with properly parsed personsdata

- created adjacency matrices for AuthorsNetork and PapersNetwork
  - they are indexed by the semantic scholar ids for both authors and papers


## March 16 - March 22

- `Winsorize` function in r (removes outliers) (use `prob` interval)

- fixed error with reading `personsfeatures.csv` (missing quotes and leaving leading spaces), now it all is accessible

- color author network by
  - gender
  - country

- spend some time looking at correlations and pairs matrix and see what the relationship between different ones are somehow
- hypothesis: there is no relationship between how collaborative you are and your "influence score" (e.g. hindex, i10index)

- copy over semantic scholar id data to Eitan; mapping paper_key => s2id (PODC_10_001)

- export adjacency matrix for clustering (for PapersNetwork)

## March 9 - March 15

- colored papers graph by conferences
  - needed to match paper titles from s2 to original paper titles to get disambiguated conference names

- measure correlations between various author features:
    - " npubs"
    - " hindex"
    - " hindex5y"
    - " i10index"
    - " i10index5y"
    - " citedby"
    - " as_pc_chair"
    - " as_pc"
    - " as_session_chair"
    - " as_panelist"
    - " as_keynote_speaker"
    - " as_author" ]
- these correlations are graphed via `pairs` from R in `authors_network/figs/Author Features Correlations Matrix.png`; using the script `correlations_graph.R`
- these correlations are calculated via `cor`, `var`, and `cov` in `authors_network/numbers/Author Features Correlation Calculations.csv` extensively and a subtable in `authors_networks/numbers/Author Features Correlation Calculations.numbers`; using the script `correlations_calculations.R`

## February 29 - March 8

- added person's data to AuthorsNetwork (from `persons/persons.csv`)

- calculate correlations between centralities in AuthorsNetwork (scipy.piersonR, numpy.collf). In `authors_network/numbers/Centrality Correlations.numbers`)

## February 22 - February 28

- units for networkx centrality measurements:
  - __eigenvector__ is normalized by definition.
  - __closeness__ is default normalized by the number of nodes in the component, but I turned that off. so, the units now just are node^{-1} since the closeness is inverse of the distance (number of nodes along shortest path).
  - __betweenness__ is default normalized by `(2/((n-1)(n-2)))` where `n` is the number of nodes in the component.
  - __degree__ is default normalized by the number of nodes in the component.

- for PapersNetwork:
  - don't color centralities
  - color by conferences in papers graph

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
