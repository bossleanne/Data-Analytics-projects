#a
salesdf = read.csv("sales.csv", header = T, na.strings = 'x')
salesdf = na.omit(salesdf)
summary(salesdf)

#b
mean_sales <- salesdf %>%
  select(level.of.education,sales)%>%
  group_by(level.of.education)%>%
  summarise(Sales = mean(sales))

ggplot(data=mean_sales, aes(x=level.of.education, y=Sales/1000)) +
  geom_bar(stat="identity", fill="steelblue",width=0.5)+
  geom_text(aes(label=round(Sales/1000)), vjust=-0.3, size=3.5)+
  theme_minimal()

#c
qplot(sales/1000, salary, colour = product.type, shape = product.type, 
      data = salesdf,main="Product.type.scatterplot",
      xlab="sales(k)", ylab="salary ")
levels(salesdf$product.type) # "computer hardware" "computer software" "office supplies"   "printers" 
par(mfrow=c(2,2))

#computer hardware
computer_hardware <- subset(salesdf, product.type == "computer hardware") 
plot(computer_hardware$salary,computer_hardware$sales/1000,col=("red")[computer_hardware$product.type],xlab ="salary",ylab = "sales(k)",main="Sales of computer hardware")

#computer software
computer_software <- subset(salesdf, product.type == "computer software")
plot(computer_software$salary,computer_software$sales/1000,col=computer_software$product.type,xlab ="salary",ylab = "sales(k)",main="Sales of computer software")
#office supplies
office_supplies <- subset(salesdf, product.type == "office supplies")
plot(office_supplies$salary,office_supplies$sales/1000,col=office_supplies$product.type,xlab ="salary",ylab = "sales(k)",main="Sales of office supplies")
#printers
printers <- subset(salesdf, product.type == "printers")
plot(printers$salary,printers$sales/1000,col=printers$product.type,xlab ="salary",ylab = "sales(k)",main="Sales of printers")

#d
model <- lm(sales ~ salary,data = salesdf)
summary(model)
par(mfrow=c(1,1))
plot(salesdf$salary,salesdf$sales,col="red",pch=16,xlab = "salary",ylab = "sales(k)")
abline(model,col="green")
# --------------------
# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept)  -1.716e+05  8.343e+03  -20.57   <2e-16 ***
#   salary  5.645e+00  9.156e-02   61.66   <2e-16 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Residual standard error: 49720 on 991 degrees of freedom
# Multiple R-squared:  0.7932,	Adjusted R-squared:  0.793 
# F-statistic:  3801 on 1 and 991 DF,  p-value: < 2.2e-16
# ---------------------

#e
#method1
library(dummies)
salesdf.new <- dummy.data.frame(salesdf, sep = ".")
model2 <- lm(sales ~ .,data = salesdf.new)
summary(model2)
plot(sales$salary,sales$sales,col="red",pch=16,xlab = "sales(k)",ylab = "salary")
abline(model2,col="green")
#method2
library(fastDummies)
results <- fastDummies::dummy_cols(salesdf, remove_first_dummy = TRUE)
model2 <- lm(sales ~ .,data = results)
summary(model2)
#what is knitr::kable(results)??

model2 <- lm(sales ~ .,data = salesdf)
summary(model2)



