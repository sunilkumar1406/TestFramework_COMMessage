"""
This modular class is to read input dict and write to CSV result file.

@author: Sunil
@date: 2015/07/12
"""

import serial
import time
import csv
import logger as logger

class Testresultwriter_csv:

    def __init__( self, in_csvoutpath ):
        self.in_csvoutpath = in_csvoutpath
        self.logger = logger.Logger("testresultwriter_csv")
        self.ofile = open(self.in_csvoutpath,"w",newline='')
        self.outwrite = csv.writer(self.ofile,'excel')
        header = ['Story_Specification_ID','Description','Input_Sendata','Output_receivedata_1','Output_receivedata_2','Output_receivedata_3','Output_receivedata_4','Actual_Output_receivedata','Result']
        self.outwrite.writerow(header) 
        
    def write_resultdict_into_csvfile( self, in_testcasedictresult ) :
        self.logger.log_string(in_testcasedictresult)
        for dictrow in in_testcasedictresult:
            self.logger.log_string(dictrow)
            data = [str(dictrow["Story_Specification_ID"]),str(dictrow["Description"]),str(dictrow["Input_Sendata"]),str(dictrow["Output_receivedata_1"]),str(dictrow["Output_receivedata_2"]),str(dictrow["Output_receivedata_3"]),str(dictrow["Output_receivedata_4"]),str(dictrow["Responsedata"]),str(dictrow["Result"])]
            self.outwrite.writerow(data)
        
    def __del__( self ):
        if self.ofile:
            self.ofile.close()
               
