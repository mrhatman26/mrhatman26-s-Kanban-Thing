from gui_main import *
from gui_project import *
from version_handler import *
version_increase(0)
run = True
while run is True:
    run = gui_project()#gui_main()
    print(run)
