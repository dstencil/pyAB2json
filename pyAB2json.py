#!/usr/bin/env python3

import datetime
from pylogix import PLC
import json


IP = input('Enter AB PLC IP Address xxx.xxx.xxx.xxx \n')
microstatus = input('is PLC a Micro800 series? (y or n) def(n) \n')
if microstatus == 'y' or 'yes':
    microstatus = True
else:
    microstatus = False
dateformat = datetime.datetime.now()
files = "{}_{}.json".format(IP,dateformat.strftime("%m%d%y"))
with PLC(IP) as comm:
        
        comm.Micro800 = microstatus
       
        with open(files, 'w') as txt: 
            tags = comm.GetTagList()
            tagdict = {IP: []}
            
            for t in tags.Value:
                tagread = comm.Read(t.TagName)
                tagdict[IP].append({tagread.TagName: {'Value': tagread.Value,'Data Type':t.DataType,'Status':tagread.Status}})
                
                print('Writing: {} \n'.format(tagdict))
            json.dump(tagdict,txt, indent = 4)
            
  
        print('Tag Data written to {}'.format(files))
