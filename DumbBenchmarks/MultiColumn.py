import numpy
import pandas
import time

#This is benchmark to test how slower it is to run through an array in different ways.

N = 10000000



dataframe = pandas.DataFrame({"A": range(1,N), "B": range(1,N), "C": range(1,N), "D": range(1,N), "E": range(1,N), "F": range(1,N), "G": range(1,N)})


A_column = dataframe["A"]
B_column = dataframe["B"]
C_column = dataframe["C"]


start_time = time.time()
sum = 0
for i in range(1,N-1):
	sum += A_column[i]
	sum += B_column[i]
	sum += C_column[i]

print("total sum " + str(sum))

end_time = time.time()

total_time = end_time - start_time

print("The first method takes " + str(total_time))




start_time = time.time()
sum = 0

for i in range(1,N-1):
	sum += A_column[i]

for i in range(1,N-1):
	sum += B_column[i]

for i in range(1,N-1):
	sum += C_column[i]

print("total sum " + str(sum))

end_time = time.time()
total_time = end_time - start_time

print("The second method takes " + str(total_time))

#In my computer both methods takes roughly the same time, with the second  one being SLIGHTLY faster. I think this
#is due to caches misses, but I think pandas is doing some weird stuff under the hood, because I would expect the 
#first method to be much slower (again, due to cache misses)