setwd("~/SocialNetworks/systems-papers/python/authors_network/")

################################################################################
# margins

# par(mar = c(5,5,5,5)) # doesn't seem to work...

################################################################################
# figure

# name = "Author Centralities Correlations Matrix"
name = "Author Features Correlations Matrix"
version = "A"
png(
  filename = paste("figs/",name,".png", sep=""),
  width = 2000, height = 2000, res = 150, units = "px"
)


################################################################################
# data

correlations = read.csv(paste("data/correlations_v",version,".csv", sep=""))

# labels

# names(correlations)

to_label = function(name) {
  return(paste(
    name,
    paste("\n(",length(correlations[[name]])," points)", sep="")
  ))
}

################################################################################
# plot

col_max = length(correlations)

pairs(
  correlations[2:col_max],
	
  main = name,

  # log = "xy", # causes 32 warnings
  na.action = na.omit,
  
  pch = 21,
  # bg = rainbow(col_max-1),
  # bg = colors,

  # upper.panel = NULL
  lower.panel = NULL,
  labels = mapply(to_label, names(correlations[2:col_max]))
)

# legend(
#   x = 0.5, y = 2,
# #   pt.bg = colors,
#   bty = "n"
# )

dev.off()
