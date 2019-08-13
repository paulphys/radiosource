import os
from astropy.io import fits
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

S1 = [1,2,3]
S2 = [1,2,3]
S3 = [1,2,3]
S4 = [1,2,3]
S5 = [1,2,3]

root = tk.Tk()
file_path = filedialog.askopenfilename()
root.withdraw()
root.geometry('500x500')
root.title('FITS FILE HANDLER')


tk.Label(root,text='FITS FILE HANDLER').grid(row=0)
var = tk.StringVar()

set1 = tk.OptionMenu(root,var,S1,S2,S3,S4,S5)
set1.configure(font=('Arial',30))
set1.grid(row=1, column=0)

tk.mainloop()





print(file_path)
file_path = file_path[33:]

print(file_path)
image_data = fits.getdata(file_path, ext=0)

plt.grid(b=None)
plt.figure(frameon=False)
plt.imshow(image_data, cmap='inferno')

# Remove x,y axis labels
metadata = plt.gca()
metadata.axes.xaxis.set_ticklabels([])
metadata.axes.yaxis.set_ticklabels([])
# Remove grid
metadata.grid(False)
metadata.axis('off')

export_path = 'export/' + file_path[5:-5] + '.png'
plt.savefig(export_path, dpi=250, quality=95)

print('Done')