setwd("~/SocialNetworks/systems-papers/python/authors_network/")
version = "A"
data_table = read.csv(paste("data/correlations_v",version,".csv", sep=""))

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

calculations = cor(
  values,
  use = "pairwise.complete.obs",
  method = "pearson"
)

write.csv(
  calculations,
  file = paste("numbers/Author Features",mode,"Calculations.csv", sep=" "))
