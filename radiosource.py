import os
import sys
def main():
    if not os.path.exists('fits/'):
        os.makedirs('fits/')
    if not os.path.exists('export/'):
        os.makedirs('export/')
    amount = int(sys.argv[1])
    if amount:
        print('Radiosource')
        print('Generating...')
        for i in range(amount):
            os.system('python generate.py')
        print("Generating Done")
        os.system('python postprocessing.py')
        print('Finished')
    else:
        sys.exit()
if __name__ == "__main__":
    main()
    
