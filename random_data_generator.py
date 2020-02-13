
# Creating a random data generator for monthly oil production from a list of wells.
# The generator will take into account several inputs to get a "desired" variation
# on the data. The user should be able to change the the variables with ease.

# Needed imports
import random  # for random number generations
import math  # to use for the rounding of numbers
from calendar import monthrange  # Determining the days in each month
import numpy as np  # for array handling and calculations
import matplotlib.pyplot as plt

# ####################################################
# #################################################### List of Variables
# data_points = 10  # How many data points are needed
low_boundary_variation = 1  # boundary values for the variations ( This is not the production!)
high_boundary_variation = 2  # boundary values for the variations
# Boundaries for production.
low_production_boundary = 1  # can be changed to any desired number as long as it is lower than high production
high_production_boundary = 4

number_of_wells = 6
name = 'Small '  # The naming of the wells ( for now they will be 'name 1', and so on
low_boundary_random = 1  # boundary values for the probability (how often) the production will
high_boundary_random = 5  # change ( Either up or down).
year = 2020  # Year
month = 1  # Number of month (ex: 1 = January)
##########################################################################################
##########################################################################################

#################################################### This can go in a function or ONE Loop
# Calculating the days in a given month
# month_days = monthrange(year, month)[1]  # calculating the days of a given month
# Testing to see if I can make more data points
month_days = 100
# Creating a range for the number of days in the given month.
days_in_month = []
for i0 in range(1, month_days + 1):
    days_in_month.append(i0)
# print(days_in_month)  # Checking to see if it worked.
# Converting to numpy array
days_in_month_np = np.asarray(days_in_month)
# print(days_in_month_np)  # Checking to see if worked.

# variation factor ( How much will the numbers alternate? )
# There will be a range of numbers to alternate. These numbers can be used to '+' or '-'
# to the data that needs to be altered.
random_variation = []  # Based on the # of days in a given month
for variation in range(1, month_days + 1):  # COULD USE "random.randint"! (Get rid of math.floor)
    random_variation.append(math.floor(random.uniform(low_boundary_variation, high_boundary_variation)))
    # Will be a list larger than the well_production. Every element on this list will be added/subtracted
    # to the 'well_production' list generated at the bottom in the loop.
#################################################################################

# Probability of alternating the 'well_production' - The well production will be a set of numbers that will be
# on a range (ex: 1 to 5). From these numbers, we will alternate then to generate a 'simulated' monthly production.
# Below is how often these numbers will change and how ( production going up or down)
one_in_what_probability = []  # how likely an event will occur.
for i1 in range(low_boundary_random, high_boundary_random + 1):
    one_in_what_probability.append(i1)
# print(one_in_what_probability)

range_of_values = []  # range for production of wells ( ex: 1 to 5). Meaning the production will be in between these #s
for i2 in range(low_production_boundary, high_production_boundary):
    # generating the random production
    range_of_values.append(i2)


# creating random production for the wells. This will be a 'master' key for creating the
# production for the wells. Can be used for small and large producers.
well_production = []
for i3 in range(0, number_of_wells):
    well_production.append(random.choice(range_of_values))
##########################################################################
# Adding a decline or increase to the data using a logarithmic function
a = 1  # The point where the graph starts in the Y - axis.
b = -0.01  # If "b" is negative the graph is decreasing.
x = []
for iii in range(1, month_days):
    x.append(iii)
y = a + b * np.log(x)
# How to add every element of one list to another. This is for the decrease or increase of the production.
################################################################################


# Combining all the list into loops that will take the 'well_production' numbers and add/subtract based on the
# variation numbers ( variation numbers will be length same as days in chosen month). Two loops are required for
# this task. The outer loop iterates over the well production (length < variation).
# The inner loop iterates over the variation numbers and adds/subtracts these #s from the production.
# The resulting 'data_per_month' should be mostly the same as the production. (If given low probability of change)
well_names = []
data_per_month = []  # to be populated with monthly data based on production
for i in well_production:  # naming the wells
    well_names.append(name + str(i))  # converting to strings for naming
    # Month variations that will be based on the well_production (Inside the loop)
    for ii in random_variation:
        event_will_occur = random.choice(one_in_what_probability)  # inside the loop since we need a new
        # variable every time the loop runs.
        one_two_prob = random.choice([1, 2])  # Helps decide whether to add or subtract in variation
        if event_will_occur > 1:  # CHANGE later to allow user to decide!!!!!!!!!!!!!!!!!!
            data_per_month.append(i * 1)  # The data will be the same as 'average' production
        else:
            if one_two_prob == 1:
                data_per_month.append(i + ii)  # Adding variations to the production
            elif one_two_prob == 2:
                # The result from subtracting could be that a negative # is formed. To deal with this, we need another
                # if/else statement to test the elements before appending to the list.
                if (i - ii) < 0:
                    data_per_month.append((i - ii) * -1)  # Deals with negative numbers
                else:
                    data_per_month.append(i - ii)  # of no negative #, then add the data
                # What to do about 0 values? For now we'll just let them be and say that is a day when the well did
                # not produce enough barrels or the well was down.


# Separate the list onto sub-sections. Each section will be will be -- the number of wells times the
# number of days in the chosen month. ( # wells x # days in month)
# Need to know how many times will the monthly production will be split
equal_num_parts = len(data_per_month) / month_days  # Number of parts to split monthly production
# print(equal_num_parts)

# Converting results (in list format) to numpy arrays.
well_production_np = np.asarray(well_production)
data_per_month_np = np.asarray(data_per_month)
# Need to reshape the numpy array into a x b array ( a = # of wells, b = number of days in month)
re_shape = data_per_month_np.reshape(number_of_wells, month_days)
# print(re_shape)  # Checking to see it it worked.
# Rotating the arry 90 degrees ( now the rows become columns and col become rows).
re_shape_rotate = np.rot90(re_shape)  # Had to rotate it to plot it!
# print(re_shape_rotate)  # Checking to see it it worked.

# Selecting rows from np array and summing values in a new array.
sum_production = []  # array will contain added production for each well.
for i4 in range(0, number_of_wells):  # Number of wells == # of rows in np array.
    sum_production.append(np.sum(re_shape[[i4], :]))
# print(sum_production)  # Checking to see if it works.

# Printing to visualize data.
print(" ")
# tt = np.asarray(re_shape_rotate[:, [0]])

# Tyring to automate the plots using for loop
plt.subplot(3, 2, 1)
plt.plot(np.asarray(re_shape_rotate[:, [0]]))
plt.subplot(3, 2, 2)
plt.plot(np.asarray(re_shape_rotate[:, [1]]))
plt.subplot(3, 2, 3)
plt.plot(np.asarray(re_shape_rotate[:, [2]]))
plt.subplot(3, 2, 4)
plt.plot(np.asarray(re_shape_rotate[:, [3]]))
plt.subplot(3, 2, 5)
plt.plot(np.asarray(re_shape_rotate[:, [4]]))
plt.subplot(3, 2, 6)
plt.plot(np.asarray(re_shape_rotate[:, [5]]))
# Show figure
plt.show()

# Checking to see if they worked.
# print(well_production)  # checking the well production 'average'
# print(random_variation)  # variation that will be used to alter the well_production
# print(data_per_month)  # the monthly produced data for each well
# print(len(data_per_month))

# Look into random.randint! Could reduce the lines of code! It also works with numpy arrays!





