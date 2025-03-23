from HypothesisTest import HypothesisTest
import pandas as pandas

print_level = 1

data_path = "D:\Github\SteamDataProject\Data\cleaned_data.csv"
dataframe = pandas.read_csv(data_path)

hypothesis_test = HypothesisTest(dataframe, print_level)

p_value = hypothesis_test.run_test("Mac", "Average owners per day", 1, 0)
print("P value for Mac category with Average owners per day " + str(p_value))

p_value = hypothesis_test.run_test("Mac", "Average owners", 1, 0)
print("P value for Mac category with Average owners " + str(p_value))

p_value = hypothesis_test.run_test("Linux", "Average owners", 1, 0)
print("P value for Linux category with Average owners " + str(p_value))

p_value = hypothesis_test.run_test("Windows", "Average owners", 1, 0)
print("P value for Windows category with Average owners " + str(p_value))