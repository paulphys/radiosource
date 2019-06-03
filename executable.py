import os
if not os.path.exists('fits/'):
    os.makedirs('fits/')
if not os.path.exists('export/'):
    os.makedirs('export/')
print('Random Radio Galaxy Generator')
amount = int(input('How many radio sources do you wish to generate?'))
for i in range(amount):
    os.system('python generate.py')

print("Generating Done")
os.system('python postprocessing.py')
print('Finished')
