library(rCBA)
txn = read.transactions(file = "G:/Academic/4/4-1/DM Lab/fp-growth/R_input.csv", 
                        rm.duplicates = TRUE,
                        format = "basket",
                        sep = ",",
                        cols = 1)
rules = fpgrowth(txn, support=0.5, confidence=0.7)
inspect(rules)
itemFrequencyPlot(txn)