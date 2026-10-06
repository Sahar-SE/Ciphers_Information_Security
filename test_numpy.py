
# Name: Sahar Saba Amiri
# CMS ID: 578321

import numpy as np

#       Task One
scores = np.array([
	[88, 92, 79, 95, 70],
	[65, 70, 60, 55, 80],
	[90, 85, 88, 91, 89],
])
players = np.array(['Player A', 'Player B', 'Player C'])

bonus_scores = scores + 5
print('Bonus scores:')
print(bonus_scores)

totals = bonus_scores.sum(axis=1)
print('Totals:', totals)

winner_index = np.argmax(totals)
print('Winner:', players[winner_index])

passed_rounds = (bonus_scores >= 75).sum(axis=1)
print('Rounds passed:', passed_rounds)

ranking = np.argsort(totals)[::-1]
print('Final ranking:', players[ranking])

#     Task Two

cities = np.array(['Islamabad', 'Lahore', 'Karachi', 'Multan'])
temps = np.array([
	[22, 24, 23, 40, 25, 24, 23],
	[30, 31, 33, 32, 31, 30, 34],
	[28, 29, 28, 30, 29, 28, 27],
	[35, 36, 5, 37, 36, 35, 36],
])

means = temps.mean(axis=1)
std_dev = temps.std(axis=1)
print('\nCity means:', means)
print('City standard deviations:', std_dev)

stable_city = np.argmin(std_dev)
print('Most stable city:', cities[stable_city])

lbl = np.where(temps >= 33, 'Hot', 'Normal')
print('\nTemperature labels:')
print(lbl)

hot_days = (temps >= 33).sum(axis=1)
print('\nHot days per city:', hot_days)

hotest_city = np.argmax(hot_days)
print('City with the most hot days:', cities[hotest_city])


#       task three

stg = np.array(['Stage 1', 'Stage 2', 'Stage 3', 'Stage 4'])
fuel_used = np.array([1200, 950, 800, 500])
duration = np.array([5, 8, 12, 20])
fuel_tank = 4000

burn_rate = fuel_used / duration
print('\nBurn rates (litres/minute):', np.round(burn_rate, 2))
fastest_stage = np.argmax(burn_rate)
slowest_stage = np.argmin(burn_rate)
print('Fastest-burning stage:', stg[fastest_stage])
print('Slowest-burning stage:', stg[slowest_stage])

cum_fuel = np.cumsum(fuel_used)
remaining_fuel = fuel_tank - cum_fuel
print('\nCumulative fuel burned:', cum_fuel)
print('Fuel remaining:', remaining_fuel)
print('Does the tank ever go negative?', np.any(remaining_fuel < 0))

reserve = np.full(fuel_used.shape, 200)
fuel_reserve = np.vstack((fuel_used, reserve))
stage_requirements = fuel_reserve.sum(axis=0)
print('\nFuel and reserve stacked array:')
print(fuel_reserve)
print('New per stage fuel requirements:', stage_requirements)

