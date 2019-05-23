# RRGG - Random Radio Galaxy Generator
![mosaik](/mosaik.png) 

### ***RRGG*** uses the open-source [Astropy](https://www.astropy.org/) Library (A Community Python Library for Astronomy) to generate a pseudorandom radio source of maximum 1000x1000 pixel. It utilizes the Gaussian2D modeling function inside of Astropy to simulate a radio source emitted by a variety of differently shaped galaxies. 
#### > *Disclaimer: This is not a scientific simulation but more a proof of concept on generating random radio noise*


### Requirements
  * Python 3.6 or higher
  * Jupyter Notebook  // *recommended* but not mandatory
  * Numpy
  * Astropy
  * Matplotlib
### Installation

```
pip3 install numpy
pip3 install astropy
pip3 install matplotlib
pip3 install numpy
python3 -m pip install jupyter
```
### Important notes
* use the Jupyter Notebook for ease of operation
* create a subfolder for the images called 'img'
* for post processing fits files i recommend using the [fv FITS Viewer](https://heasarc.gsfc.nasa.gov/ftools/fv/) provided by NASA HEASARC 

### To Do
- [ ] Automate post processing
- [ ] Export to img file (tiff,png,jpg)
- [ ] GUI
- [ ] Let user change parameters

#### Example Images 5x5 Mosaic
![mosaik](/mosaik5x5.png) 
