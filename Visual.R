#getwd()
#setwd('/Users/user/Documents/OUCRU/Graph_Genome')
#--------------------------------- INSTALL AND CALL PACKAGES ---------------------------#
library(ggplot2)
library(tidyr)
library(devtools)

#--------------------------------- INSTALL AND CALL PACKAGES ---------------------------#

report1=read.csv('test.csv',sep='\t',header=F)
colnames(report1)=c("gene","read_count","length","coverage")
#report1$acc_no = 

t=separate(data = report1, col = gene, into = c("left", "right"), sep = "_")
t=as.data.frame(table(t$left))
colnames(t) = c("Gene","No_of_detected_prot")
t$tot_prot = c(11,11)
t$pct_detect=round(t$No_of_detected_prot/t$tot_prot*100,2)

t

write.csv(table(t$left),file = "t.csv")
install.packages("rmarkdown", type = "source")
library(rmarkdown)


