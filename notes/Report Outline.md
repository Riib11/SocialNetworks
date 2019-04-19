# Report Outline

## Introduction
- Sources of data
- Fields in data
- Purpose for data

## Background
- Context of work on social networks
- Recognized emergent features of social networks
- Context of questions raised about social networks

## Questions / Hypotheses
- How do conferences collaborate with / cite each other?
- How do authors collaborate with each other based on author features?
- How do papers' shared authors reflect other collaborations of authors?

## Papers Citation Network
- network: nodes are conferences, edges weighted by citations
- judgment: not very interesting

## Papers Collaboration Network
- network: nodes are papers, edges weighted by shared authors
- judgment: reveals some features, but better studied by Author Collaboration Network

## Author Collaboration Network
- network: nodes are authors, edges weighted by shared papers
- network can be colored by various author features
- node centralities can be measured of network
  - question: what does each centrality measure in terms of author features?
  - question: how do author features correlate with node centralities?
  - question: do node centralities measure the same kind of 'influence' as traditional 'influence' scores? e.g. hindex, i10index, etc.

## Analysis
- graph: author features pairs matrix
- centralities have a variety of types of correlations:
  - degree: TODO
  - eigenvector: TODO
  - betweeness: TODO
  - closeness: TODO

## Conclusions

- judgment of each centrality's significance: TODO
