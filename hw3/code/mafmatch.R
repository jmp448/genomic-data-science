height.snps <- read.delim("../data/height.snps.txt", header=T, row.names=1, stringsAsFactors=F)
bg.snps <- read.delim("../data/some.snps.txt", header=T, row.names=1, stringsAsFactors=F, na.strings="-")

height.mafs <- rowSums(height.snps)/838
bg.mafs <- rowSums(bg.snps)/838

find.closest <- function(height, bg) {
  i <- which.min(abs(height-bg))
  return(i)
}

closest.snps <- lapply(X=find.closest, FUN=height.mafs, bg=bg.mafs)

write.table(bg[closest.snps,], "matched.snps.txt", quote=FALSE)
