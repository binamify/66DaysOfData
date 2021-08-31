# # Specify c and alpha inside plt.scatter()
# plt.scatter(x = gdp_cap, y = life_exp,c = col, alpha = 0.8 ,s = np.array(pop) * 2)

# # Previous customizations
# plt.xscale('log') 
# plt.xlabel('GDP per Capita [in USD]')
# plt.ylabel('Life Expectancy [in years]')
# plt.title('World Development in 2007')
# plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# # Show the plot
# plt.show()

# dict = {
#     'Asia':'red',
#     'Europe':'green',
#     'Africa':'blue',
#     'Americas':'yellow',
#     'Oceania':'black'
# }

# i = 1000
# while i < 100000:
# 	print(i)
# 	i = i+1000

# error = 50000
# print("88888888888888888888888888888888888888888888888888888888888888888")
# while error > 1:
# 	error = error/4
# 	print(error)

# x = 1
# while x < 4 :
#     print(x)
#     x = x + 1
import pandas as pd
my_dict = {
	"height":10,
	"weight":20,
	"bmi":40,
	"ami":60
}
print(my_dict)

dataframe = pd.DataFrame(my_dict)
print(dataframe)


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab,row in cars.iterrows():
    cars.loc[lab,"COUNTRY"] = row['country'].upper()
#alternative
#cars["COUNTRY"] = cars["country"].apply(str.upper)

# Print cars
print(cars)


# //////////////////////////////////////////////////////////////////////////////