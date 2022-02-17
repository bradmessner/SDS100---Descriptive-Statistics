# ***********************************************
# * Name:   Basic Statistics in R
# * Date:   Feb 17, 2022
# * Ver:    PR
# * Author: Brad D. Messner
# * Desc:   Importing a file and calculating basic
# *         descriptive analytics.
# ***********************************************

# Import Data

df<-myData$Price

length(df)
mean(df, na.rm = TRUE)
median(df, na.rm = TRUE)
min(df, na.rm = TRUE)
max(df, na.rm = TRUE)
max(df, na.rm = TRUE)-min(df, na.rm = TRUE)
quantile(df, na.rm = TRUE)
