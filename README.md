# pyAB2json
Script for using pylogix to save all controller and program tags into a .json format with file based version control (ipadress_date.json) and view through pyJSONViewer tree heirarchy for Allen Bradley compactlogix,controllogix, and micro800(controller tags only)

download python3.1
pip install pylogix https://github.com/dmroeder/pylogix
pip install pyJSONViewer https://pypi.org/project/PyJSONViewer/

Run pyAB2json.py 

input IP Address of target Allan Bradley Controller

if Micro800 series plc input "y" at next prompt otherwise press any key

printout of filename and location is found at end of script printout

open command prompt and run pyJSONViewer

open file in pyJSONViewer

