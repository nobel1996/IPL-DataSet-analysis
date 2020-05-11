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
