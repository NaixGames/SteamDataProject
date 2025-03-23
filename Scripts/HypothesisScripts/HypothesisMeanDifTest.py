import pandas
import math
import scipy.stats as stats

data_path = "D:\Github\SteamDataProject\Data\cleaned_data.csv"
#data_path = "../../Data/shuffled_data.csv"
category = "Mac"
compare_output = "Average owners per day"

dataframe = pandas.read_csv(data_path)

yes_category = dataframe[dataframe[category] == 1][compare_output] 
no_category = dataframe[dataframe[category] == 0][compare_output] 

#compute the tes statistic
N_size = len(yes_category)
M_size = len(no_category)

mean_yes = yes_category.mean()
mean_no = no_category.mean()
var_yes = yes_category.var()
var_no = no_category.var()

estimated_var = ((N_size-1.0)*var_yes + (M_size-1.0)*var_no)/(N_size+M_size-2.0)
t_stats = (mean_yes+mean_no)/math.sqrt((estimated_var/N_size)+(estimated_var/M_size))

print(mean_yes)
print(mean_no)
print(estimated_var)
print(math.sqrt((1.0/N_size)+(1.0/M_size)))
print(t_stats)
#Compare with a t-student of N_size + M_size - 2 degrees of fredom!
freedom_deg = N_size+M_size-2
print(stats.t.cdf(t_stats, freedom_deg))
print(stats.t.cdf(-t_stats, freedom_deg))
print(stats.t.cdf(-abs(t_stats), freedom_deg) + 1 - stats.t.cdf(abs(t_stats),freedom_deg))