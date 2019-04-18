setwd("~/SocialNetworks/systems-papers/python/authors_network/")
correlations_fn = "data/correlations_vA1_c_cc-rank=0.csv"

data_table = read.csv(correlations_fn)

winsorize <- function(x) {
    Min <- which.min(x)
    Max <- which.max(x)
    ord <- order(x)
    x[Min] <- x[ord][2]
    x[Max] <- x[ord][length(x)-1]
    x
}

values = data_table[2:length(data_table)]

pruned_values = mapply(winsorize, values)

mode = "Correlation"
suffix = "(cc-rank = 0)"

calculations = cor(
  values,
  use = "pairwise.complete.obs",
  method = "pearson"
)

write.csv(
  calculations,
  file = paste("numbers/Author Features",mode,"Calculations.csv",suffix, sep=" "))
