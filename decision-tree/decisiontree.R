library(RWeka)
library(partykit)
input = read.csv("G:/Academic/4/4-1/DM Lab/decision-tree/R_input.csv",
                 header=TRUE,
                 sep =",")
result = J48(buys_computer~age+income+student+credit_rating, data=input)
summary(result)
plot(result, type="simple")