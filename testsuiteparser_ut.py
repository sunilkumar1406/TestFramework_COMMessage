import unittest
import os
import sys
import testsuiteparser_csv as testsuiteparser_csv



csvoutpath ="C:\\Bcd_access\\unittest\\unittest1.csv"
#in_testcasedictresult= [{'Description': '', 'Story_Specification_ID': '', 'Output_receivedata_1': '', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Input_Sendata': '', 'Result': '', 'Output_receivedata_4': '', 'Responsedata': ''}, {'Description': '', 'Story_Specification_ID': 'Story_CAN Set protocol_1', 'Output_receivedata_1': 'C1 ACK 0', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Input_Sendata': 'C1 SET 41 01', 'Result': 'Passed', 'Output_receivedata_4': '', 'Responsedata': 'C1 ACK 0'}, {'Description': '', 'Story_Specification_ID': 'Story_CAN Set protocol_2', 'Output_receivedata_1': 'C1 ACK 1', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Input_Sendata': 'C1 SET 41 02', 'Result': 'Passed', 'Output_receivedata_4': '', 'Responsedata': 'C1 ACK 1'}, {'Description': '', 'Story_Specification_ID': 'Story_CAN Set protocol_3', 'Output_receivedata_1': 'C1 ACK 0', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Input_Sendata': 'C1 SET 41 03', 'Result': 'Passed', 'Output_receivedata_4': '', 'Responsedata': 'C1 ACK 0'}, {'Description': '', 'Story_Specification_ID': 'Story_CAN Set protocol_4', 'Output_receivedata_1': 'C1 ACK 0', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Input_Sendata': 'C1 SET 41 04', 'Result': 'Passed', 'Output_receivedata_4': '', 'Responsedata': 'C1 ACK 0'}, {'Description': '', 'Story_Specification_ID': 'Story_CAN Set protocol_5', 'Output_receivedata_1': 'C1 ACK 0', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Input_Sendata': 'C1 SET 41 05', 'Result': 'Failed', 'Output_receivedata_4': '', 'Responsedata': 'C1 ACK 1'}, {'Description': '', 'Story_Specification_ID': 'Story_CAN Set protocol_6', 'Output_receivedata_1': 'C1 ACK 1', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Input_Sendata': 'C1 SET 41 06', 'Result': 'Passed', 'Output_receivedata_4': '', 'Responsedata': 'C1 ACK 1'}, {'Description': '', 'Story_Specification_ID': '', 'Output_receivedata_1': '', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Input_Sendata': '', 'Result': '', 'Output_receivedata_4': '', 'Responsedata': ''}]
story_dict= [[{'Output_receivedata_3': '', 'Output_receivedata_4': '', 'Description': '', 'Story_Specification_ID': 'Story_CAN Set protocol_1', 'Output_receivedata_2': '', 'Input_Sendata': 'C1 SET 41 01', 'Output_receivedata_1': 'C1 ACK 0'}, {'Output_receivedata_3': '', 'Output_receivedata_4': '', 'Description': '', 'Story_Specification_ID': 'Story_CAN Set protocol_2', 'Output_receivedata_2': '', 'Input_Sendata': 'C1 SET 41 02', 'Output_receivedata_1': 'C1 ACK 1'}, {'Output_receivedata_3': '', 'Output_receivedata_4': '', 'Description': '', 'Story_Specification_ID': 'Story_CAN Set protocol_3', 'Output_receivedata_2': '', 'Input_Sendata': 'C1 SET 41 03', 'Output_receivedata_1': 'C1 ACK 0'}, {'Output_receivedata_3': '', 'Output_receivedata_4': '', 'Description': '', 'Story_Specification_ID': 'Story_CAN Set protocol_4', 'Output_receivedata_2': '', 'Input_Sendata': 'C1 SET 41 04', 'Output_receivedata_1': 'C1 ACK 0'}, {'Output_receivedata_3': '', 'Output_receivedata_4': '', 'Description': '', 'Story_Specification_ID': 'Story_CAN Set protocol_5', 'Output_receivedata_2': '', 'Input_Sendata': 'C1 SET 41 05', 'Output_receivedata_1': 'C1 ACK 0'}, {'Output_receivedata_3': '', 'Output_receivedata_4': '', 'Description': '', 'Story_Specification_ID': 'Story_CAN Set protocol_6', 'Output_receivedata_2': '', 'Input_Sendata': 'C1 SET 41 06', 'Output_receivedata_1': 'C1 ACK 1'}]]

class TestTestsuiteparser_csv(unittest.TestCase):
    def testread_inputs_from_csvfile(self):
    
        testsuiteparser_csv_obj=testsuiteparser_csv.Testsuiteparser_csv(csvoutpath)
        response=testsuiteparser_csv_obj.read_inputs_from_csvfile()
        self.assertEqual(response,story_dict)
        del testsuiteparser_csv_obj

if __name__ == "__main__":
    unittest.main()
