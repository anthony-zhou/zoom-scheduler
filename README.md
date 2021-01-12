# Zoom Scheduler

An script that opens scheduled Zoom meetings automatically.

## Caveats

The script works by running in the background, which might be computationally expensive. It also only works on Mac OS right now, but the only OS-specific line is the part where we kill the Zoom process. 

## Requirements 
- [x] Installed Python version above 3.5
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
4. Run `python main.py`. 

## Credits

Originally forked from [https://github.com/prashanth-up/Zoom-Automation](https://github.com/prashanth-up/Zoom-Automation). That one used `pyautogui`, but I'm using `webbrowser` instead, to directly open the Zoom link, so that we don't have to depend on the screen resolution. Also, that script only works on Windows. 

## Contributing

While I don't plan to make a lot of edits here, feel free to open an issue or PR if there's anything you'd like to document or fix. Contributions are always appreciated!
