"""
This modular class is to create test result dict after sending input data and receiveing response from BT dongle.

@author: Sunil
@date: 2015/07/12
"""

import serial
import time
import serialcontrol
import logger as logger

class Testcomparator:

    def __init__( self, in_testcasedict,in_comport ):
        self.in_testcasedict = in_testcasedict
        self.in_comport = in_comport
        self.logger = logger.Logger("testcomparator")
        #Initialize SerialControl Module
        self.serial_obj = serialcontrol.Serialcontrol(self.in_comport)
        if self.serial_obj.initialized == False:
            self.logger.log_string('Info: COM port initialization failed') 
            
    def send_and_receive_Commsgs( self, senddata ) :
        self.serial_obj.sendcmd(senddata)
        result = self.serial_obj.readall()
        return result.decode()
                
    def create_resultdict_from_responsedatareceieved( self ) :
        story_dictlist_result = []
        for dictrow in self.in_testcasedict:
            story_dictlist_result.append({'Story_Specification_ID': '','Description': '','Input_Sendata': '','Output_receivedata_1': '','Output_receivedata_2': '','Output_receivedata_3': '','Output_receivedata_4': '','Responsedata': '','Result': ''})
    # Loop over columns.
            for dictcolumn in dictrow:
                self.logger.log_string(dictcolumn) 
                result = self.send_and_receive_Commsgs(str(dictcolumn["Input_Sendata"]))
                self.logger.log_string(str(dictcolumn["Output_receivedata_1"]) + str(dictcolumn["Output_receivedata_2"]) + str(dictcolumn["Output_receivedata_3"]) + str(dictcolumn["Output_receivedata_4"]))
                self.logger.log_string(str(result.replace('\r', '')))
                if str(result.replace('\r', '')) == str(dictcolumn["Output_receivedata_1"]) + str(dictcolumn["Output_receivedata_2"]) + str(dictcolumn["Output_receivedata_3"]) + str(dictcolumn["Output_receivedata_4"]):
                    story_dictlist_result.append({'Story_Specification_ID': str(dictcolumn["Story_Specification_ID"]),'Description': str(dictcolumn["Description"]),'Input_Sendata': str(dictcolumn["Input_Sendata"]),'Output_receivedata_1': str(dictcolumn["Output_receivedata_1"]),'Output_receivedata_2': str(dictcolumn["Output_receivedata_2"]),'Output_receivedata_3': str(dictcolumn["Output_receivedata_3"]),'Output_receivedata_4': str(dictcolumn["Output_receivedata_4"]),'Responsedata': str(result.replace('\r', '')),'Result': 'Passed'})
                else:
                    story_dictlist_result.append({'Story_Specification_ID': str(dictcolumn["Story_Specification_ID"]),'Description': str(dictcolumn["Description"]),'Input_Sendata': str(dictcolumn["Input_Sendata"]),'Output_receivedata_1': str(dictcolumn["Output_receivedata_1"]),'Output_receivedata_2': str(dictcolumn["Output_receivedata_2"]),'Output_receivedata_3': str(dictcolumn["Output_receivedata_3"]),'Output_receivedata_4': str(dictcolumn["Output_receivedata_4"]),'Responsedata': str(result.replace('\r', '')),'Result': 'Failed'})
        return story_dictlist_result
    
    def __del__( self ):
        if self.serial_obj.initialized:
            del self.serial_obj
