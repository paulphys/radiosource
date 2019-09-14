import os
import sys
if not os.path.exists('fits/'):
    os.makedirs('fits/')
if not os.path.exists('export/'):
    os.makedirs('export/')
amount = int(sys.argv[1])
if amount:
    print('Random Radio Galaxy Generator')
    print('Generating...')
    for i in range(amount):
        os.system('python generate.py')
    print("Generating Done")
    os.system('python postprocessing.py')
    print('Finished')
else:
    sys.exit()
