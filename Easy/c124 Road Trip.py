'''ROAD TRIP

You've decided to make a road trip across the country in a straight line. You
have chosen the direction you'd like to travel and made a list of cities in that
direction that have gas stations to stop at and fill up your tank. To make sure
that this route is viable, you need to know the distances between the adjacent
cities in order to be able to travel this distance on a single tank of gasoline,
(No one likes running out of gas.) but you only know distances to each city from
your starting point.

INPUT SAMPLE:
The first argument is a path to a filename. Each line in the file contains the
list of cities and distances to them, comma delimited, from the starting point
of your trip. You start your trip at point 0. The cities with their distances
are separated by semicolon. E.g.

Rkbs,5453; Wdqiz,1245; Rwds,3890; Ujma,5589; Tbzmo,1303;
Vgdfz,70; Mgknxpi,3958; Nsptghk,2626; Wuzp,2559; Jcdwi,3761;
Yvnzjwk,5363; Pkabj,5999; Xznvb,3584; Jfksvx,1240; Inwm,5720;
Ramytdb,2683; Voclqmb,5236;

OUTPUT SAMPLE:
Print out the distance from the starting point to the nearest city, and the
distances between two nearest cities separated by comma, in order they appear
on the route. E.g.

1245,58,2587,1563,136
70,2489,67,1135,197
1240,2344,1779,357,279
2683,2553
'''
def f(test='Rkbs,5453; Wdqiz,1245; Rwds,3890; Ujma,5589; Tbzmo,1303;'):
    test = test.rstrip().split()
    for i in range(len(test)):
        test[i] = test[i].split(',')
        test[i][1] = int(test[i][1][:-1])
    test = sorted(test, key=lambda x:x[1])
    position = 0
    result = []
    for city in test:
        result.append(str(city[1] - position))
        position = city[1]
    print(','.join(result))
