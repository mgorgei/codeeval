'''SUGGEST GROUPS

You may have noticed that a new feature was added to our web site – user groups.
So, this challenge is about joining groups.

You are given a list of users of a social network, friends of each user, and
groups the user participates in.

To help users find the most interesting groups, we suggest them joining the
groups where ≥50% of their friends participate.

Your task is to write a program which finds a list of suggested groups for each
user.

INPUT SAMPLE:
The first argument is a file that contains the information about each user, one
user per line. The line is delimited by colon ‘:’ into three parts: user name,
list of friends, and list of groups. The items in each part are delimited by
comma ‘,’.
For example:

Amira:Isaura,Lizzie,Madalyn,Margarito,Shakira,Un:Driving,Mineral collecting
Elliot:Isaura,Madalyn,Margarito,Shakira:Juggling,Mineral collecting
Isaura:Amira,Elliot,Lizzie,Margarito,Verla,Wilford:Juggling
Lizzie:Amira,Isaura,Verla:Driving,Mineral collecting,Rugby
Madalyn:Amira,Elliot,Margarito,Verla:Driving,Mineral collecting,Rugby
Margarito:Amira,Elliot,Isaura,Madalyn,Un,Verla:Mineral collecting
Shakira:Amira,Elliot,Verla,Wilford:Mineral collecting
Un:Amira,Margarito,Wilford:
Verla:Isaura,Lizzie,Madalyn,Margarito,Shakira:Driving,Juggling,Mineral collecting
Wilford:Isaura,Shakira,Un:Driving

OUTPUT SAMPLE:
Print to stdout the list of suggested groups for each user. The list of users
and the list of groups for each user must be sorted alphabetically.
For example:

Isaura:Driving,Mineral collecting
Lizzie:Juggling
Madalyn:Juggling
Margarito:Driving,Juggling
Shakira:Driving,Juggling
Un:Driving,Mineral collecting
'''
from operator import attrgetter
class Person():
    def __init__(self, name, friends, interests):
        self.name = name
        self.friends = friends
        self.interests = interests

    def __repr__(self):
        return self.name + ':' + ','.join(self.friends) + ':' + ','.join(self.interests)

def f(test='t165.txt'):
    people = []
    with open(test) as file:
        for person in file:
            person = person.rstrip('\n').split(':')
            people.append( Person(person[0],
                                  person[1].split(','),
                                  person[2].split(',')) )
    people = sorted(people,key=attrgetter('name'))#may need
    result = ''
    for i in range(len(people)):
        n = len(people[i].friends)/2
        new_interest = {}
        for j in range(len(people)):
            if i != j:
                if (people[i].name in people[j].friends or
                    people[j].name in people[i].friends):
                    for interest in people[j].interests: 
                        new_interest[interest] = new_interest.get(interest,0) + 1
        line = []
        for k,v in new_interest.items():
            if v >= n:
                if not k in people[i].interests:
                    line.append(k)
        if line:
            result += people[i].name + ':' + ','.join(sorted(line)) + '\n'
    print(result[:-1])
