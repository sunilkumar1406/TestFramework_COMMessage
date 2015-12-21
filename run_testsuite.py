# -*- coding: iso-8859-15 -*-
#pylint: disable=C0301,W0702,W0703

#pylint: disable=W0614,W0401
"""
This is the TestSuite for executing Smartconnectivity Communication message testcases

@author: Sunil
@date: 2015/07/12
"""
import os
import traceback
import sys
import time
import random
from datetime import datetime
import win32pdhutil
import win32com.client
import subprocess
import re
import shutil
import csv

import configmanager as configmanager
import testsuiteparser_csv as testsuiteparser_csv
import testcomparator as testcomparator
import testresultwriter_csv as testresultwriter_csv
import logger as logger

#Initialize ConfigManager Module
configmanager = configmanager.Configmanager(r"C:\Bcd_access\INI.txt" )

#Initialize logger Module
logger = logger.Logger("run_testsuite")

#Get Config Manager inputs
ini_dict = configmanager.get_ini_parameter()
comport = configmanager.get_comport(ini_dict)
reportpath,reportfolder = configmanager.get_reportpath(ini_dict)

csvpath = r"C:/Bcd_access/Story_datasheet.csv"
csvoutpath = reportpath + "\\Story_datasheet_Result_" + reportfolder + ".csv"
print(csvoutpath)
print("csvoutpath!!!",csvoutpath)


#---------------------------------------------START TEST : ACTION--------------------------------------------------   
try:
    testsuiteparser_csv = testsuiteparser_csv.Testsuiteparser_csv(csvpath)
    testresultwriter_csv = testresultwriter_csv.Testresultwriter_csv(csvoutpath) 
    testcasedict = testsuiteparser_csv.read_inputs_from_csvfile()    
    logger.log_string(testcasedict)
    testcomparator = testcomparator.Testcomparator(testcasedict,comport)
    testcasedictresult = testcomparator.create_resultdict_from_responsedatareceieved()
    testresultwriter_csv.write_resultdict_into_csvfile(testcasedictresult)                    
    
except IOError:
    logger.log_string("ERROR:Test execution causes error, Please check!!!")
    
del configmanager
del testsuiteparser_csv
del testresultwriter_csv
del testcomparator 

    
