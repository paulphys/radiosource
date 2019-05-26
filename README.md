# RRGG - Random Radio Galaxy Generator
![mosaik](/mosaik.png) 

### ***RRGG*** uses the open-source [Astropy](https://www.astropy.org/) library (A Community Python Library for Astronomy) to generate a pseudorandom radio source of maximum 1000x1000 pixel. It utilizes the Gaussian2D modeling function to simulate a radio stream emitted by a variety of differently shaped galaxies. 
#### > *Disclaimer: This is not a scientific simulation but more a proof of concept on generating random radio noise*


### Requirements
  * Python 3.6 or higher
  * Pip
  * Jupyter Notebook  // *recommended* but not mandatory
  * Numpy
  * Astropy
  * Matplotlib
### Installation

```python
pip3 install numpy
pip3 install astropy
pip3 install matplotlib
pip3 install numpy
python3 -m pip install jupyter
```
### Usage
```python
python executable.py
```
Enter the amount of random sources you wish to generate

## Release History

* 0.2.0
    * ADD: Added `postprocessing.py`Automated post processing with fits coloring and export to image file
    * CHANGE: Adjusted random range of source from 80 to 50
    
* 0.1.0
    * Work in progress
    * The first release
    
### Important notes
* use the Jupyter Notebook for ease of operation
* create a subfolder for the fits files called 'fits'
* create a subfolder for the exported image files called 'export'
* ~~for post processing fits files i recommend using the [fv FITS Viewer](https://heasarc.gsfc.nasa.gov/ftools/fv/) provided by NASA HEASARC~~ 

### To Do
- [x] Automate post processing
- [x] Export to img file (tiff,png,jpg)
- [ ] GUI
- [ ] Let user change parameters

#### Example Images 
![collage](/collage4x3.png) 
![collage](/mosaik5x5.png) 
