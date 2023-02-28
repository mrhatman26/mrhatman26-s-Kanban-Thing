from gui import *
from version_handler import *
version_increase(0)
run = True
while run is True:
    run = gui_main()
    print(run)
