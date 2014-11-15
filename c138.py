class Car():
    def __init__(self, number, top_spd, tt_acc, tt_dec):
        self.number = int(number)
        self.top_spd = int(top_spd)
        self.tt_acc = float(tt_acc)
        self.tt_dec = float(tt_dec)
        
    def __repr__(self):
        return ' '.join([str(self.number),str(self.top_spd),str(self.tt_acc),str(self.tt_dec)])

def f():
    with open('t138.txt') as file:
        test_case = file.read()
    track, *cars = test_case.rstrip('\n').split('\n')
    track = track.split()#(distance, degree)
    for i in range(len(cars)):
        cars[i] = cars[i].split()
        cars[i] = Car(cars[i][0], cars[i][1], cars[i][2], cars[i][3])
    print(track)

#start 0 mph at beginning, 
