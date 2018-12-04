input = data.frame(x=c(1,1,0,2,3), y=c(1,0,2,4,5))
set.seed(1)
result = kmeans(input, 2)
plot(input, 
     col=result$cluster+1, 
     pch=16)