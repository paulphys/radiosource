![mosaik](media/mosaik.png) 

#### **radiosource** uses the open-source [Astropy](https://www.astropy.org/) library to generate a pseudorandom radio source of 1000x1000 pixels. It utilizes the Gaussian2D modeling function to simulate a radio stream emitted by a variety of differently shaped galaxies.
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
    * release
    
    

### To Do
- [x] Automate post processing
- [x] Export to img file (tiff,png,jpg)
- [ ] GUI

#### Example Images 
![collage](media/collage4x3.png) 
![collage](media/mosaik5x5.png) 
