import random

fh = open('./data.csv', 'w')
random.seed()
fh.write('Getal\n')

for i in range(1000):
    fh.write(str(random.randint(0,1200)) + "\n")

fh.close()
