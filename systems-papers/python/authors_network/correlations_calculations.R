setwd("~/SocialNetworks/systems-papers/python/authors_network/")
version = "A"
correlations = read.csv(paste("data/correlations_v",version,".csv", sep=""))

mode = "Correlation"

calculations = NULL

if (mode == "Correlation") {
  calculations = cor(
    # without author_name column
    correlations[2:length(correlations)],
    use = "pairwise.complete.obs",
    method = "pearson"
  )
}
if (mode == "Covariance") {
  calculations = cov(
    # without author_name column
    correlations[2:length(correlations)],
    use = "pairwise.complete.obs",
    method = "pearson"
  )
}

write.csv(
  calculations,
  file = paste("numbers/Author Features",mode,"Calculations.csv", sep=" "))
