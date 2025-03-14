import numpy
import pandas
import time

#This is benchmark to test if caching an array before running through it is faster on pandas
#For me it make sense, as it avoids a cache every call I think, but need to make sure :P

N = 1000000



dataframe = pandas.DataFrame({"A": range(1,N), "B": range(1,N), "C": range(1,N), "D": range(1,N), "E": range(1,N), "F": range(1,N), "G": range(1,N)})


#First we run the dumb way
start_time = time.time()
sum = 0
for i in range(1,N-1):
	sum += dataframe["A"][i]

print("total sum " + str(sum))

end_time = time.time()

total_time = end_time - start_time

print("The dumb method takes " + str(total_time))



#Then we run teh smart way
start_time = time.time()
sum = 0
A_column = dataframe["A"]
for i in range(1,N-1):
	sum += A_column[i]

print("total sum " + str(sum))

end_time = time.time()
total_time = end_time - start_time

print("The smart method takes " + str(total_time))

#In my computer the second method takes HALF THE TIME :P. I thought it was going to be a bigger difference, but still!