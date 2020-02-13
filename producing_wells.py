
# simulation for small production wells
import random
import numpy as np

# #############################################  Small Producers
# Creating the range for small producers
small_prod_random = []
for i_small in range(1, 6):  # from 1 to 5 (6 is not included)
    small_prod_random.append(i_small)  # range of small production numbers for "choice" function

# Generating the name for wells (for now they will be small 1, small 2, and so on ...)
# the production will be in barrels per day
num_small_wells = 5
numbering_wells_small = []
small_prod_numbers = []  # the numbers are based on barrels of oil per day
for i_num in range(1, num_small_wells + 1):
    numbering_wells_small.append("Small " + str(i_num))  # converting to string format
    # creating the random production for the small wells --- based on the # of wells considered small
    small_prod_numbers.append(random.choice(small_prod_random))  # random from range at the top

# converting lists into numpy arrays (for small producing wells)
small_num_np = np.asarray(numbering_wells_small)
small_production_np = np.asarray(small_prod_numbers)


# #############################################  Medium Producers
# Creating the range for medium producers
med_prod_random = []
for i_med in range(6, 11):  # from 1 to 10 (11 is not included)
    med_prod_random.append(i_med)  # range of small production numbers for "choice" function

# Generating the name for wells
num_med_wells = 5
numbering_wells_med = []
med_prod_numbers = []  # the numbers are based on barrels of oil per day
for i_num in range(1, num_med_wells + 1):
    numbering_wells_small.append("Medium " + str(i_num))  # converting to string format
    # creating the random production for the small wells --- based on the # of wells considered small
    med_prod_numbers.append(random.choice(med_prod_random))  # random from range at the top

# converting lists into numpy arrays (for Medium producing wells)
med_num_np = np.asarray(numbering_wells_med)
med_production_np = np.asarray(med_prod_numbers)


# #############################################  Large Producers
# Creating the range for Large producers
large_prod_random = []
for i_large in range(11, 21):  # from 11 to 20 (21 is not included)
    large_prod_random.append(i_large)  # range of small production numbers for "choice" function

# Generating the name for wells
num_large_wells = 5  # maybe will be less than med and small
numbering_wells_large = []
large_prod_numbers = []  # the numbers are based on barrels of oil per day
for i_num in range(1, num_large_wells + 1):
    numbering_wells_large.append("Large " + str(i_num))  # converting to string format
    # creating the random production for the small wells --- based on the # of wells considered small
    large_prod_numbers.append(random.choice(large_prod_random))  # random from range at the top

# converting lists into numpy arrays (for Medium producing wells)
large_num_np = np.asarray(numbering_wells_large)
large_production_np = np.asarray(large_prod_numbers)


# since the above are generated for barrels of oil in a day, we need to add a 'random' factor that will occur
# every day and bring the production either down or up by +- a number. The variation factor should not be
# too much as it is not experienced in the field unless well is down for maintenance or failures
variation_factor = 3

