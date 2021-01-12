# Zoom Scheduler

An automated script to open Zoom meetings at a given time on Mac OS, so you can always be on time. 

## Caveat

The script works by running in the background, which might be computationally expensive. 

## Requirements 
- [x] Installed python version above 3.5
- [x] Installed `schedule` package
- [x] Updated Zoom Software (Signed in)

#### To install the above packages :
+ To [Download Python](https://www.python.org/downloads/)
+ `pip install schedule`
+ To [Download Zoom Software](https://zoom.us/download#client_4meeting)

## How to run the program :

1. Clone this repository.
2. Install the `schedule` library with `pip install schedule`.
3. Add your own meetings in `config.py`.
3. Run `python main.py`. 

## Credits

*Originally forked from [https://github.com/prashanth-up/Zoom-Automation](https://github.com/prashanth-up/Zoom-Automation). That one used `pyautogui`, but I'm using `webbrowser` instead, to directly open the Zoom link, so that we don't have to depend on the screen resolution. Also, that script works for Windows, but this is for Mac. 
