library(arules)
txn = read.transactions(file = "G:/Academic/4/4-1/DM Lab/apriori/R_input.csv", 
                        rm.duplicates = TRUE,
                        format = "basket",
                        sep = ",",
                        cols = 1)
rules = apriori(txn, parameter = list(sup=0.5,conf=0.7,minlen=2,target="rules"))
inspect(rules)
itemFrequencyPlot(txn)