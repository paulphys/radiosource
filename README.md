# RRGG - Random Radio Galaxy Generator
![mosaik](media/mosaik.png) 

#### ***RRGG*** uses the open-source [Astropy](https://www.astropy.org/) to generate a pseudorandom radio source of 1000x1000 pixels. It utilizes the Gaussian2D modeling function to simulate a radio stream emitted by a variety of differently shaped galaxies.
#### > *Disclaimer: This is not a scientific simulation but more a proof of concept on generating random radio sources*


### Requirements
  * Python 3
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
python3 -m pip install jupyter
```
### Usage
```python
python3 rrgg.py -(Amount of random sources you wish to generate)
```



## Release History
* 1.0
    * proper release
    * ADD: pass amount as python script argument
* 0.2.1
    * ADD: Added ability to automatically make directories for fits files and exported images using *mkdir*
* 0.2.0
    * ADD: Added `postprocessing.py` Automated post processing with fits coloring and export to image file
    * CHANGE: Adjusted random range of x_mean and y_mean from 80 to 50
    
* 0.1.0
    * Work in progress
    * first release
    

### To Do
- [x] Automate post processing
- [x] Export to img file (tiff,png,jpg)
- [ ] GUI
- [ ] Let user change parameters

#### Example Images 
![collage](media/collage4x3.png) 
![collage](media/mosaik5x5.png) 
