input = data.frame(x=c(151,174,138,186,128,136,179,163,152,131),
                   y=c(63,81,56,91,47,57,76,72,62,48))
plot(input$y,input$x,
     col="blue",
     main="Height & Weight regression",
     abline(lm(input$x~input$y)),
     cex=1.3,
     pch=16,
     xlab="Weight in kg",
     ylab="Height in cm")