![mosaik](media/mosaik.png) 

# radiosource

> generate pseudorandom radio sources with [Astropy](https://www.astropy.org/)'s Gaussian2D modeling function

![Astropy](http://img.shields.io/badge/powered%20by-AstroPy-orange.svg?style=flat) ![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)

#### > *Disclaimer: This is not a scientific simulation but more a proof of concept on generating random radio sources*


### Requirements
  * Python 3
  * Numpy
  * Astropy
  * Matplotlib
### Installation

```python
pip3 install numpy
pip3 install astropy
pip3 install matplotlib
```
### Usage
```python
python3 rrgg.py -Amount
```


## Release History
* 1.2
    * ADD: pass amount as python script argument
* 1.1
    * ADD: Added `postprocessing.py` Automated post processing with fits coloring and export to image file
    * CHANGE: Adjusted random range of x_mean and y_mean from 80 to 50
* 1.0
    * initial commit
    
    

### To Do
- [x] Automate post processing
- [x] Export to img file (tiff,png,jpg)
- [ ] GUI

#### Example Imagery
![collage](media/collage4x3.png) 
![collage](media/mosaik5x5.png) 
