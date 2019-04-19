setwd("~/SocialNetworks/systems-papers/python/authors_network/")

correlations_data_fn = "data/correlations_vA1_c_cc-rank=0.csv"

library(psych)

################################################################################
# figure

version <- "CR0"
name <- "Author-Features-Correlations-Matrix"

winsorization_fraction <- 0.02
winsorization_features <- c(1:9)
winsorization_features_str <- paste(
  winsorization_features[1],
  winsorization_features[length(winsorization_features)],
sep="to")

attributes <- paste(
  paste("wfrac", winsorization_fraction, sep="="),
  paste("wfeats", winsorization_features_str, sep="="),
  paste("v", version, sep="="),
sep="_")

png(
  filename = paste("figs/",name,"_",attributes,".png", sep=""),
  width    = 2000,
  height   = 2000,
  res      = 150,
  units    = "px"
)


################################################################################
# data


data_table <- read.csv(correlations_data_fn)

# labels

to_label = function(name) {
  c <- data_table[[name]]
  return(paste(
    name,
    paste("\n(n = ",length(c[ !is.na(c) ]),")", sep="")
  ))
}

################################################################################
# prune via winsorize

values <- data_table[2:length(data_table)]

winsorize <- function (x, frac) {
  lim <- quantile(x, probs=c(frac, 1-frac), na.rm = TRUE)
  x[ is.na(x) | x < lim[1] | x > lim[2] ] <- NA 
  x
}

# dfw <- apply(df, 1, function(col) winsorize(col, frac))
# cor(dfw)

Z <- values

for (i in winsorization_features) {
  x <- Z[i][[1]]
  Z[i] <- winsorize(x, winsorization_fraction)
}

################################################################################
# plot

psych::pairs.panels(
  Z,
  method  = "pearson",
  density = TRUE,
  lm      = F
)

dev.off()
