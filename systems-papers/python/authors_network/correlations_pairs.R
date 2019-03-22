setwd("~/SocialNetworks/systems-papers/python/authors_network/")

################################################################################
# margins

# par(mar = c(5,5,5,5)) # doesn't seem to work...

################################################################################
# figure

name <- "Author-Features-Correlations-Matrix"
version <- "A"

winsorization_fraction <- 0.0

attributes <- paste(
  paste("wf",winsorization_fraction,sep="="),
  sep="-")

png(
  filename = paste("figs/",name,"_",attributes,".png", sep=""),
  width    = 2000, height = 2000, res = 150, units = "px"
)


################################################################################
# data

data_table <- read.csv(paste("data/correlations_v",version,".csv", sep=""))

# labels

to_label = function(name) {
  c <- data_table[[name]]
  return(paste(
    name,
    paste("\n(n = ",length(c[ !is.na(c) ]),")", sep="")
  ))
}

################################################################################
# prune

values <- data_table[2:length(data_table)]

# test <- function() {

#   x <- values[3][[1]]
#   frac <- 0.05
#   lim <- quantile(x, probs = c(frac, 1-frac), na.rm = TRUE)

#   print(paste("limits:", lim[1], lim[2]))

#   print(paste("mean:", mean(x, na.rm = TRUE)))
#   y <- x[ lim[1] <= x & x <= lim[2] ]
#   z <- x[ lim[2] < x ]

#   print(paste("total", length(x)))
#   print(paste("keep:", length(y)))
#   print(paste("drop:", length(z)))

#   quit()
# }
# test()

winsorize <- function (x, frac) {
  lim <- quantile(x, probs=c(frac, 1-frac), na.rm = TRUE)
  x[ is.na(x) | x < lim[1] | x > lim[2] ] <- NA 
  x
}

# dfw <- apply(df, 1, function(col) winsorize(col, frac))
# cor(dfw)

Z <- values

for (i in c(1:9)) {
  x <- Z[i][[1]]
  Z[i] <- winsorize(x, winsorization_fraction)
}

plot(Z[])

# values_winsorized[1:9] <- mapply(winsorize, values[1:9])

################################################################################
# plot

pairs(
  Z,
	
  main = name,

  # log = "xy", # causes 32 warnings
  na.action = na.omit,
  
  pch = 21,

  # upper.panel = NULL
  lower.panel = NULL,
  labels = mapply(to_label, names(data_table[2:length(data_table)]))
)

dev.off()
