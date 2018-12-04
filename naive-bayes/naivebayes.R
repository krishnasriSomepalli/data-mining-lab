library(e1071)
input = read.csv("G:/Academic/4/4-1/DM Lab/naive-bayes/R_input.csv",
                 header=TRUE,
                 sep =",")
result = naiveBayes(buys_computer~age+income+student+credit_rating, data=input)
predict(result, data.frame(age="youth", 
                           income="medium", 
                           student="yes", 
                           credit_rating="fair"))