-------------------------
#code starts here

import yaml
print(path)
with open(path,'r') as f:
    data=yaml.load(f)
type_of_data = type(data)
print('Data type you are working with is : ', type_of_data)

# In which city, and at which venue the match was played and where was it played ?
city = data['info']['city']
print('City where the match was played is : ' + city)

# Which are all the teams that played in the tournament ? How many teams participated in total?
venue = data['info']['venue']
print('Venue of the match played is : ' + venue)

# Which team won the toss and what was the decision of toss winner ?
Teams = data['info']['teams']
print('Teams participated are : ' + Teams[0] , 'and' + ' ' + Teams[1] )
print('There are total of ' + str(len(Teams)) + ' teams that played in tournament')

toss = data['info']['toss']['winner'], data['info']['toss']['decision']
print('Team that won the toss is ' + toss[0], 'by ' + toss[1])

# Find the first bowler and first batsman who played the first ball of the first inning
first_bowler = data['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler']
first_batsman = data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']

print('First bowler who delivered first ball of the first inning was :' + first_bowler)
print('First bowler who played the first ball of the first inning was :' + first_batsman)

# How many deliveries were delivered in first inning ?
deliveries = len(data['innings'][0]['1st innings']['deliveries'])
print('First inning was consisting of' + ' ' + str(deliveries) + ' ' + 'deliveries delivered.')

import numpy as np
# Not every data format will be in csv there are other file formats also.
# This exercise will help you deal with other file formats and how toa read it.

data_ipl = np.genfromtxt(path, delimiter=',', skip_header=1, dtype=str)

# Number of unique matches 

# How many matches were held in total we need to know so that we can analyze further statistics keeping that in mind.
len(set(data_ipl[:,0]))

# Number of unique teams

# this exercise deals with you getting to know that which are all those six teams that played in the tournament.
team1_set = set(data_ipl[:, 3])
team2_set = set(data_ipl[:, 4])
unique_teams = team1_set.union(team2_set)
print(unique_teams)

# Sum of all extras

# An exercise to make you familiar with indexing and slicing up within data.
extras = data_ipl[:, 17]
extras_int = extras.astype(np.int16)
print(extras_int.sum())

# Delivery number when a given player got out

# Get the array of all delivery numbers when a given player got out. Also mention the wicket type.
wicket_filter = (data_ipl[:, 20] == 'SR Tendulkar')
wickets_arr = data_ipl[wicket_filter]
print(wickets_arr[:, 11])
print(wickets_arr[:, 21])

# Number of times Mumbai Indians won the toss

# this exercise will help you get the statistics on one particular team
team_records = data_ipl[data_ipl[:, 5] == 'Mumbai Indians']
unique_matches = set(team_records[:, 0])
print(len(unique_matches))

# Filter record where batsman scored six and player with most number of sixex

# An exercise to know who is the most aggresive player or maybe the scoring player 
sixes = data_ipl[data_ipl[:, 16].astype(np.int16) == 6]
from collections import Counter
most_sixes_scored = Counter(sixes[:,13],)
print(most_sixes_scored.most_common(3))


#code ends here

