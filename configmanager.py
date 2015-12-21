"""
This modular class is to Get INI parameters from INI.txt and Manipulate test configuration parameters

@author: Sunil
@date: 2015/07/12
"""
import re
import time
import random
from datetime import datetime
import serialcontrol
import os
import logger as logger


class Configmanager(object):
    def __init__(self, INI_Path):
        self.INI_Path = INI_Path
        self.logger = logger.Logger("configmanager")

    def get_ini_parameter (self):
        file_in = open(self.INI_Path, "r") 
        get_line = file_in.readline();
        initialtestvalues_dict = {}
        while get_line:
            dict_key = ""
            x = get_line.find("#")      # check if there is a comment in this line
            if x > -1 :
                get_line = get_line[:x]   # cut the comment part of the line
            get_line = get_line.strip()    
            x = get_line.find(":")
            if x > -1 :
                dict_key =get_line[:x]
                dict_key = re.sub ("\t","", dict_key.strip())
                dict_value = get_line[x+1:]                       
                dict_value = re.sub ("\t","",dict_value.strip())
                initialtestvalues_dict[dict_key] =  dict_value
            get_line = file_in.readline()  
        file_in = None   # close file   
        return initialtestvalues_dict

	
    def get_comport(self,ini_dict):
        comport = str(ini_dict["COMPORT"])
        return comport
	
    def get_reportpath(self,ini_dict):
        date=datetime.now().strftime( "%Y-%m-%d_%H_%M_%S" )
        reportfolder = "_".join( [date, ini_dict["ProjectName"], ini_dict["SW_Version"]] )
        reportpath = r"C:\\Bcd_access" + "\\" + reportfolder
        if not os.path.exists( reportpath) :
            os.makedirs(reportpath)
        time.sleep( 2 )
        return reportpath,reportfolder
		
