
# probability of sensor being correct or miss
pHit = 0.6
pMiss = 0.2

#Probability of robot movement
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

# Setup initial array with equal probability
p=[]
n=5
#p=[0, 1, 0, 0, 0]
for x in range(0, n):
    p.append(1./n)

#Setup world with 3 rooms of 2 different colors
world=['green', 'red', 'red', 'green', 'green']
#Continious measurements
measurements = ['red', 'green']
#continious movement/motion
motions = [1, 1]
#Sense function that updates probabilities depending on measurements
#Posterio measurements
def sense(p, Z):
    q=[]
    for x in range(0,len(p)):
        if world[x] == Z:
            q.append(p[x]*pHit)
        else:
            q.append(p[x]*pMiss)
    qSum = sum(q)
    for x in range(0,len(p)):
        q[x] = q[x]/qSum
    return q

#Moving the robot from room to room we shift the array
def move(p, U):
    q = []
    for x in range (len(p)):
        k = pExact * p[x-U] % len(p) #We multiply exact with the value
        k = k + p[x-U-1] % len(p) * pOvershoot #We multiply the next value with overshoot probability
        k = k + p[x-U+1] % len(p) * pUndershoot  # We multiply the value before with the undershoot probability
        q.append(k)
    return q

for x in range(0,len(measurements)):
    p = sense(p,measurements[x]) 
    p = move(p, motions[x])   

print p