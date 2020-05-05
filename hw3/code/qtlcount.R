trans <- read.delim("../data/transqtl.output.txt", header=T)

for ( snp in unique(trans$SNP) ) {
  correx <- sum(trans$SNP==snp)
  trans[trans$SNP==snp,"p.value"] <- trans[trans$SNP==snp,"p.value"]*correx
}

trans1 <- subset(trans, p.value <= 0.05)
trans2 <- subset(trans, p.value <= 0.2)
trans3 <- subset(trans, p.value <= 0.5)
trans4 <- subset(trans, p.value <= 0.9)

trans.matched <- read.delim("../data/transqtl.matched.txt", header=T)
for ( snp in unique(trans.matched$SNP) ) {
  correx <- sum(trans.matched$SNP==snp)
  trans.matched[trans.matched$SNP==snp,"p.value"] <- trans.matched[trans.matched$SNP==snp,"p.value"]*correx
}

transm1 <- subset(trans.matched, p.value <= 0.05)
transm2 <- subset(trans.matched, p.value <= 0.2)
transm3 <- subset(trans.matched, p.value <= 0.5)
transm4 <- subset(trans.matched, p.value <= 0.9)

# qq plots
height.mqtl <- readRDS("../data/matrixqtl.height.rds")
plot(height.mqtl, cex=0.2)

matched.mqtl <- readRDS("../data/matrixqtl.matched.rds")
plot(matched.mqtl, cex=0.2)