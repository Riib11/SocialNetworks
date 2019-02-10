# Scripts in progress: Grepping for group B

It takes an average of 5.5 minutes per grep, where each grep searches for 20 papers from group B. So, the total search will take a little over 90 hours (a little less than 4 days).

And it finished! Hooray! Here's the stats:

Papers searched: 38,138
Papers found: 11,731

This seems like it couldn't possibly be right though, since almost every group B search query found all of its targets. I need to see what I can make of it. THe 11,731 number comes from a `wc` on the tmp/gB* files.

Found what happened: ran out of space :(((( Left off around 500 something, about halfway through, so my original estimates were not bad. But it'll have to run for the rest of the week probably.

- Ask Eitan or more space

# Finding Missing from Group A

The `missing_gA` papers are defined to be the papers that are in our original source for group A, but were not found in the SS corpus. Fortunately, there are only about 200 or so of these papers! To find them, I've been trying an algorithm for finding edit distance, but it looks like thats not working yet because of memory problems, I tried with threshold 5.
