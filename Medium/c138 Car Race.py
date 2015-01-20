'''CAR RACE

In this challenge you need to find out how fast each car goes around a given
track. A track is represented by a sequence of float and integer numbers, each
float number is a length of a straight section in miles, followed by an integer
number which represents an angle of the turn in degrees. Each car is described
by its top speed in MPH, the time to reach the top speed from 0 MPH, and the
time to brake from its top speed to 0 MPH. The rules:

1. A car is weightless, it is just a point. 
2. A car accelerates and brakes with a constant acceleration. 
3. Turn speed is linearly dependent on the turn degree and can be obtained from
the following proportion: 
A car can pass through a 0 degree turn with its top speed, and it must brake to
0 MPH if a turn degree is 180. 
4. A car starts with 0 MPH speed, accelerates to its top speed, after that goes
at the top speed as long as possible, then brakes as late as possible to reach
the allowed turn speed and after the turn immediately accelerates from the turn
speed to the top speed and so on. 
5. No time is needed to pass a turn, it's just a point and at that point the
speed of a car must be exactly the same as the allowed turn speed. 
6. A length of a track section will always allow a car to reach it's top speed.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. The first
line of the file contains a track, represented by a sequence of numbers
separated by a single whitespace. Then there are N lines of cars. Each car is a
line with parameters in the next order: car number, top speed, time to
accelerate form 0 to a top speed, time to brake from a top speed to 0, separated
by a single whitespace. E.g.

1.029 115 1.122 125 1.185 100 0.53 110 0.751 95 1.242 85 0.533 85 1.003 120 0.465 110 0.546 125 0.446 90 0.582 70 0.878 45 0.49 30 1.016 130 1.047 140 1.146 75 0.496 85 0.857 125 0.971 0
1 266 8.1 1.4
2 178 8.7 4.8
3 251 8.0 3.4
4 215 6.8 3.8
5 220 5.9 3.3
6 262 4.5 1.5
7 267 5.4 2.6
8 268 7.8 3.8
9 225 4.7 1.8
10 266 4.0 1.9

OUTPUT SAMPLE:
Print out the car number with it's lap time separated by a single whitespace.
Each car must be printed in a new line in order from fastest to slowest lap. The
lap time must be in seconds rounded to the hundredth of a second. E.g.

10 241.05
6 244.98
7 247.32
1 254.07
8 258.67
3 273.02
9 283.52
5 298.28
4 309.22
2 375.86
'''
class Car():
    def __init__(self, number, top_spd, tt_acc, tt_dec):
        self.number = int(number)
        self.top_spd = int(top_spd) / 3600.0
        self.tt_acc = float(tt_acc)
        self.tt_dec = float(tt_dec)
        
    def __repr__(self):
        return ' '.join([str(self.number),str(self.top_spd),str(self.tt_acc),str(self.tt_dec)])

class Track():
    def __init__(self, distance, degree):
        self.distance = float(distance)
        self.degree = float(degree)
        
    def __repr__(self):
        return ' '.join([str(self.distance),str(self.degree)])

def f(test='''1.029 115 1.122 125 1.185 100 0.53 110 0.751 95 1.242 85 0.533 85 1.003 120 0.465 110 0.546 125 0.446 90 0.582 70 0.878 45 0.49 30 1.016 130 1.047 140 1.146 75 0.496 85 0.857 125 0.971 0
1 266 8.1 1.4
2 178 8.7 4.8
3 251 8.0 3.4
4 215 6.8 3.8
5 220 5.9 3.3
6 262 4.5 1.5
7 267 5.4 2.6
8 268 7.8 3.8
9 225 4.7 1.8
10 266 4.0 1.9'''):
    race_track, *cars = test.rstrip('\n').split('\n')
    race_track = race_track.split()
    track = []
    for i in range(0, len(race_track), 2):
        track.append(Track(race_track[i], race_track[i+1]))
    for i in range(len(cars)):
        cars[i] = cars[i].split()
        cars[i] = Car(cars[i][0], cars[i][1], cars[i][2], cars[i][3])
    finish = []
    for c in cars:
        acc = c.top_spd / c.tt_acc
        dec = c.top_spd / c.tt_dec
        time = 0
        last_velocity = 0
        for t in track:
            velocity = (180 - t.degree) / 180 * c.top_spd
            
            tacc = (c.top_spd - last_velocity) / acc
            dacc = last_velocity * tacc + .5 * acc * tacc**2
            
            tdec = (c.top_spd - velocity) / dec
            ddec = c.top_spd * tdec - .5 * dec * tdec**2
            
            tmid = (t.distance - dacc - ddec) / c.top_spd 
            time += tacc + tmid + tdec
            last_velocity = velocity
        finish.append([str(c.number) , '{:.2f}'.format(time)])
    finish = sorted(finish, key=lambda x:x[1])
    finish = list(map(' '.join, finish))
    print('\n'.join(finish))
