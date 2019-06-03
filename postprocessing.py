import os
from astropy.io import fits
import matplotlib.pyplot as plt

for filename in os.listdir('fits'):
    check = filename[:-5] + '.png'
    if (check not in os.listdir('export')):
        print(filename)
        path = 'fits/' + filename
        image_data = fits.getdata(path, ext=0)
        plt.grid(b=None)
        plt.figure(frameon=False)
        plt.imshow(image_data, cmap='bone')

        # Remove x,y axis labels
        metadata = plt.gca()
        metadata.axes.xaxis.set_ticklabels([])
        metadata.axes.yaxis.set_ticklabels([])
        # Remove grid
        metadata.grid(False)
        metadata.axis('off')

        export_path = 'export/' + filename[:-5] + '.png'
        plt.savefig(export_path,dpi=250, quality=95)

print('Post-Processing Done')
