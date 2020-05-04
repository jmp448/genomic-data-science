library(tidyr)
library(ggplot2)
library(RColorBrewer)
library(randomForest)
library(enrichR)
source("helperFunctions_Proj3.R")

# this will be useful later
xcol <- colorRampPalette(rev(brewer.pal(n = 12,name = "Paired")))(11)
# data
expDat<-utils_loadObject("expDat_Proj3.rda")
expMean<-utils_loadObject("expMean_Proj3.rda")
sampTab<-utils_loadObject("sampTab_Proj3.rda")
slObj<-utils_loadObject("slObj_Proj3.rda")
grn<-utils_loadObject("grn_Proj3.rda")

find.converters <- function(curr.prof, init.prof, target.prof, pert, diff.thresh, simulator=simRegsProfilesPert, gene.net=grn, n=0, nIter=200) {
  corr.tg <- cor(curr.prof, target.prof)
  corr.init <- cor(curr.prof, init.prof)
  if (corr.tg - corr.init >= diff.thresh) {
    return(pert)
  } else {
    tf.changes <- target.prof - curr.prof
    
    # assign scores
    # for (i in 1:nrow(my.grn)) {
      # 1. weight changes by correlation, sum over grn edges
      # my.grn <- gene.net[!gene.net$TF %in% names(pert),]
      # my.grn[i, "score"] <- tf.changes[my.grn[i, "TG"]] * my.grn[i, "corr"]
      # my.grn[,c("TG", "corr", "zscore")] <- NULL
      # my.scores <- data.frame(data.table(my.grn)[, lapply(.SD, sum), by=list(TF)])
      
      # 2. just multiply by sign of correlation, sum over grn edges
      # my.grn <- gene.net[!gene.net$TF %in% names(pert),]
      # my.grn[i, "score"] <- tf.changes[my.grn[i, "TG"]] * sign(my.grn[i, "corr"])
      # my.grn[,c("TG", "corr", "zscore")] <- NULL
      # my.scores <- data.frame(data.table(my.grn)[, lapply(.SD, sum), by=list(TF)])
    # }
    # 3. just score based on tf differences
    # my.scores <- data.frame(tf.changes)
    # colnames(my.scores) <- c("score")
    # my.scores$TF <- rownames(my.scores)
    # my.scores <- my.scores[!my.scores$TF %in% names(pert),]
    
    # 4. weight tf differences by out-degree
    my.scores <- data.frame(tf.changes)
    colnames(my.scores) <- c("score")
    my.scores$TF <- rownames(my.scores)
    outdegs <- table(grn$TF)[order(match(names(table(grn$TF)), my.scores$TF))]
    my.scores <- data.frame(my.scores$score * outdegs)
    colnames(my.scores) <- c("TF", "score")
    my.scores <- my.scores[!my.scores$TF %in% names(pert),]
    
    my.scores$dir <- sign(my.scores$score)
    my.scores$score <- abs(my.scores$score)
    my.scores <- my.scores[order(my.scores$score, decreasing=T),]
    
    # take the top three, turn them into perturbations, and run a simulation
    pert <- c(pert, my.scores$dir[1])
    names(pert)[length(pert)] <- as.character(my.scores$TF[1])
    this.prof <- simulator(slObj, init.prof, pert, noise=n, iter=nIter)[,nIter]
    find.converters(this.prof, init.prof, target.prof, pert, diff.thresh, simulator, gene.net, n, nIter)
  }
}

# fib <- rowMeans(expDat[,which(sampTab$description1=='fibroblast')])
# esc <- rowMeans(expDat[,which(sampTab$description1=='esc')])
# 
# init.prof <- fib
# curr.prof <- fib
# target.prof <- esc
# diff.thresh <- 0.1
# its <- 500
# pert <- c()
# system.time(pert <- find.converters(curr.prof, init.prof, target.prof, pert, diff.thresh, nIter=its))

types = colnames(expMean)
corrs <- data.frame()
for (t.from in types) {
  corrs[t.from, t.from] <- 1
  for (t.to in types[types!=t.from]) {
    # find converting factors
    init.prof <- rowMeans(expDat[,which(sampTab$description1==t.from)])
    target.prof <- rowMeans(expDat[,which(sampTab$description1==t.to)])
    pert <- c()
    pert <- find.converters(init.prof, init.prof, target.prof, pert, diff.thresh=0.2, nIter=500)
    # find final similarities
    prod <- simRegsProfilesPert(slObj, init.prof, pert, iter=800, noise=0.1)[,800]
    corrs[t.from, t.to] <- cor(prod, target.prof)
    print(paste0("Completed for ", t.to))
    
  }
  print(paste0("Completed all for ", t.from))
}

saveRDS(corrs, file="data/corrs.rds")