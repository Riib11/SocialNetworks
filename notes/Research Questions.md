# Research Questions

## Conference Representation

__Background__: We know that most of these conferences can be considered as broadly belonging to the same sub-field of computer science called as "computer systems".

__Question__: Which conferences should be considered closely related to the main group of papers / topics, and which should be considered controls, belonging to related topics, but not quite as strongly related to the bulk of the papers?

__Method__: Create different graph variations of the conferences based on different connectivity approximations, and analyze connected components. The "systems" group should be one large, distinct connected component from the other connected components.

__Variation 1__: Connect conferences to each other based on whether they cite each other (directed graph). This is essentially the second graph from the summer, but with corrected conference names.

__Variation 2__: Connect conferences to each other when they share an author in our 2017 set (more shared authors, stronger the link).

__Notes__: Conferences come in many different sizes, which will affect the sizes of the edges (e.g., how many papers can cite to begin with?). Overcome by either making boolean edges (shares co-authors or not; cites or not), or with normalized, relative edges (10% of authors shared, also directed graph).

__Idea__: Connected components of paper collaborations seem to reflect a large center mass that could correlate with a "thematic center" for the the field of Computer Systems.

## Influence vs Centrality

__Background__: Most authors are assigned an "influence score" that intend to represent how influential a given author is on other authors. These scores use different calculations, and include `hindex`, `i10index`, and some others.

__Question__: How closely to various "influence scores" correlate to various centrality measurements in the 2017 authors' collaboration network?

__Method__: There are also several different measures of centrality: degree, eigenvector, closeness, and betweenness centralities. An analysis would take the form of a table that measures the correlation in each combination of an "influence score" and a centrality measurement.

__Note__: I have to research the best methods for measuring such a correlation; the correlation would be some measure on the distribution of differences between the normalized "influence score" and the centrality measure. 

__Note__: I have to research how different "influence scores" are meant to be interpreted relative to each other. E.g. does a 4x increase in `hindex` indicate a 4x increase in "influence"? Or perhaps is in logarithmic or sqrt growth? These measurements are likely informal and not well researched, so in that case I could try many different growth extrapolations and see if any work well.
