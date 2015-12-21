"""
This modular class is to read input data from CSV file from 'C:/Stabi_access/Story_datasheet.csv' and return a dict for the Test suite.

@author: Sunil
@date: 2015/07/12
"""

import serial
import time
import csv
import logger as logger

class Testsuiteparser_csv:

    def __init__( self, csvpath ):
        self.csvpath = csvpath
        self.ifile = open(self.csvpath,"r")
        self.inread = csv.reader(self.ifile)
        self.logger = logger.Logger("testsuiteparser_csv")
        next(self.inread) 
                
    def read_inputs_from_csvfile( self ) :
        self.logger.log_string('Read CSV file')        
        i = 0
        for row in self.inread:
            rowvalues = str(row[0]).split(';')
            if not rowvalues[0]:
                i = i + 1
        self.ifile.seek(0)
        next(self.inread)
        story_dictlist = []
        for x in range(0,i+1):
            story_dictlist.append([])
        m = 0
        for row in self.inread:
            rowvalues = str(row[0]).split(';')
            if rowvalues[0]:                
                story_dictlist[m].append({'Story_Specification_ID': str(rowvalues[0]),'Description': str(rowvalues[1]),'Input_Sendata': str(rowvalues[2]),'Output_receivedata_1': str(rowvalues[3]),'Output_receivedata_2': str(rowvalues[4]),'Output_receivedata_3': str(rowvalues[5]),'Output_receivedata_4': str(rowvalues[6])})                        
            else :
                m = m + 1
        return story_dictlist
    
    def __del__( self ):
        if self.ifile:
            self.ifile.close()
        
        
