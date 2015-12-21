import unittest
import os.path
import sys
import sys
#sys.path.append('D:\drh8cob\auto_testing\SmartConnectivity\testresultwriter_csv.py')
from Smartconnectivity_BCD  import SmartConnectivity
import testresultwriter_csv as testresultwriter_csv


import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

csvoutpath ="C:\\Bcd_access\\unittest\\unittest.csv"
in_testcasedictresult= [{'Description': '', 'Story_Specification_ID': '', 'Output_receivedata_1': '', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Input_Sendata': '', 'Result': '', 'Output_receivedata_4': '', 'Responsedata': ''}, {'Description': '', 'Story_Specification_ID': 'Story_CAN Set protocol_1', 'Output_receivedata_1': 'C1 ACK 0', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Input_Sendata': 'C1 SET 41 01', 'Result': 'Passed', 'Output_receivedata_4': '', 'Responsedata': 'C1 ACK 0'}, {'Description': '', 'Story_Specification_ID': 'Story_CAN Set protocol_2', 'Output_receivedata_1': 'C1 ACK 1', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Input_Sendata': 'C1 SET 41 02', 'Result': 'Passed', 'Output_receivedata_4': '', 'Responsedata': 'C1 ACK 1'}, {'Description': '', 'Story_Specification_ID': 'Story_CAN Set protocol_3', 'Output_receivedata_1': 'C1 ACK 0', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Input_Sendata': 'C1 SET 41 03', 'Result': 'Passed', 'Output_receivedata_4': '', 'Responsedata': 'C1 ACK 0'}, {'Description': '', 'Story_Specification_ID': 'Story_CAN Set protocol_4', 'Output_receivedata_1': 'C1 ACK 0', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Input_Sendata': 'C1 SET 41 04', 'Result': 'Passed', 'Output_receivedata_4': '', 'Responsedata': 'C1 ACK 0'}, {'Description': '', 'Story_Specification_ID': 'Story_CAN Set protocol_5', 'Output_receivedata_1': 'C1 ACK 0', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Input_Sendata': 'C1 SET 41 05', 'Result': 'Failed', 'Output_receivedata_4': '', 'Responsedata': 'C1 ACK 1'}, {'Description': '', 'Story_Specification_ID': 'Story_CAN Set protocol_6', 'Output_receivedata_1': 'C1 ACK 1', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Input_Sendata': 'C1 SET 41 06', 'Result': 'Passed', 'Output_receivedata_4': '', 'Responsedata': 'C1 ACK 1'}, {'Description': '', 'Story_Specification_ID': '', 'Output_receivedata_1': '', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Input_Sendata': '', 'Result': '', 'Output_receivedata_4': '', 'Responsedata': ''}]

class TestTestresultwriter_csv(unittest.TestCase):
    def testwrite_resultdict_into_csvfile(self):
        #ini_dict = Configmanager.get_ini_parameter(self,r"C:\Bcd_access\INI.txt")
        #comport = Configmanager.get_comport(ini_dict)
        #reportpath,reportfolder = configmanager.get_reportpath(ini_dict)  
        #csvoutpath = reportpath + "\\Story_datasheet_Result_" + reportfolder + ".csv"
        testresultwriter_csv_obj=testresultwriter_csv.Testresultwriter_csv(csvoutpath)
        testresultwriter_csv_obj.write_resultdict_into_csvfile(in_testcasedictresult)
        del testresultwriter_csv_obj


if __name__ == "__main__":
    unittest.main()
