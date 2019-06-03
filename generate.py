import numpy as np
import matplotlib.pyplot as plt
import random
import uuid
from astropy.modeling.models import Gaussian2D
from astropy.nddata import CCDData

y,x = np.mgrid[0:4000, 0:4000]
data = (Gaussian2D(1,2000,2000,random.randint(50,1000),random.randint(50,1000), theta=random.randint(0,2))(x,y))
data += 0.006 * np.random.randn(4000,4000)
plt.imshow(data)
ccd = CCDData(data,meta={'object': 'random radio galaxy', 'filter': 'R'},unit='adu')
unique_filename = str(uuid.uuid4()) + '.fits'
ccd.write('fits/'+unique_filename)
