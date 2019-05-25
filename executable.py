import os

print('Random Radio Galaxy Generator')
amount = int(input('How many radio sources do you wish to generate?'))
for i in range(amount):
    os.system('python generate.py')

os.system('python postprocessing.py')

print('Done')

