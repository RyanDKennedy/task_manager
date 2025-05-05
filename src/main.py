"""
Ryan Kennedy, Gabriel Walder
Cmdr. Schenk
Cloud Computing
7th Period
May 5, 2025
"""

import sys
from gui import GUI

def main():

    # initializes the gui
    gui = GUI()

    # starts the gui
    gui.run()

    # exit successfully
    sys.exit(0)

if (__name__=="__main__"):
    main()
