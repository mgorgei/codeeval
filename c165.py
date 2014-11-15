from operator import  attrgetter
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
