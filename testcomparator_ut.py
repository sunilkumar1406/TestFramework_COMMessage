import unittest
import testcomparator as testcomparator
import csv
story_dictlist_result= [{'Output_receivedata_4': '', 'Input_Sendata': '', 'Result': '', 'Story_Specification_ID': '', 'Output_receivedata_3': '', 'Output_receivedata_1': '', 'Output_receivedata_2': '', 'Responsedata': '', 'Description': ''}, {'Output_receivedata_4': '', 'Input_Sendata': 'C1 SET 41 01', 'Result': 'Passed', 'Story_Specification_ID': 'Story_CAN Set protocol_1', 'Output_receivedata_3': '', 'Output_receivedata_1': 'C1 ACK 0', 'Output_receivedata_2': '', 'Responsedata': 'C1 ACK 0', 'Description': ''}, {'Output_receivedata_4': '', 'Input_Sendata': 'C1 SET 41 02', 'Result': 'Passed', 'Story_Specification_ID': 'Story_CAN Set protocol_2', 'Output_receivedata_3': '', 'Output_receivedata_1': 'C1 ACK 1', 'Output_receivedata_2': '', 'Responsedata': 'C1 ACK 1', 'Description': ''}, {'Output_receivedata_4': '', 'Input_Sendata': 'C1 SET 41 03', 'Result': 'Passed', 'Story_Specification_ID': 'Story_CAN Set protocol_3', 'Output_receivedata_3': '', 'Output_receivedata_1': 'C1 ACK 0', 'Output_receivedata_2': '', 'Responsedata': 'C1 ACK 0', 'Description': ''}, {'Output_receivedata_4': '', 'Input_Sendata': 'C1 SET 41 04', 'Result': 'Passed', 'Story_Specification_ID': 'Story_CAN Set protocol_4', 'Output_receivedata_3': '', 'Output_receivedata_1': 'C1 ACK 0', 'Output_receivedata_2': '', 'Responsedata': 'C1 ACK 0', 'Description': ''}, {'Output_receivedata_4': '', 'Input_Sendata': 'C1 SET 41 05', 'Result': 'Failed', 'Story_Specification_ID': 'Story_CAN Set protocol_5', 'Output_receivedata_3': '', 'Output_receivedata_1': 'C1 ACK 0', 'Output_receivedata_2': '', 'Responsedata': 'C1 ACK 1', 'Description': ''}, {'Output_receivedata_4': '', 'Input_Sendata': 'C1 SET 41 06', 'Result': 'Passed', 'Story_Specification_ID': 'Story_CAN Set protocol_6', 'Output_receivedata_3': '', 'Output_receivedata_1': 'C1 ACK 1', 'Output_receivedata_2': '', 'Responsedata': 'C1 ACK 1', 'Description': ''}, {'Output_receivedata_4': '', 'Input_Sendata': '', 'Result': '', 'Story_Specification_ID': '', 'Output_receivedata_3': '', 'Output_receivedata_1': '', 'Output_receivedata_2': '', 'Responsedata': '', 'Description': ''}, {'Output_receivedata_4': '', 'Input_Sendata': 'W1 DBG 01', 'Result': 'Passed', 'Story_Specification_ID': 'Story_Advanced Id logging_1', 'Output_receivedata_3': '', 'Output_receivedata_1': 'W1 DBG 01 00 06', 'Output_receivedata_2': '', 'Responsedata': 'W1 DBG 01 00 06', 'Description': ''}, {'Output_receivedata_4': '', 'Input_Sendata': 'W1 DBG 02', 'Result': 'Failed', 'Story_Specification_ID': 'Story_Advanced Id logging_2', 'Output_receivedata_3': '', 'Output_receivedata_1': 'W1 DBG 02 05 00 00', 'Output_receivedata_2': '', 'Responsedata': 'W1 DBG 02 04 09 00', 'Description': ''}, {'Output_receivedata_4': '', 'Input_Sendata': 'W1 DBG 05', 'Result': 'Failed', 'Story_Specification_ID': 'Story_Advanced Id logging_3', 'Output_receivedata_3': '', 'Output_receivedata_1': 'W1 DBG 05 00 00 28 bd d6 fc', 'Output_receivedata_2': '', 'Responsedata': 'W1 DBG 05 00 01 28 bd d6 fc', 'Description': ''}, {'Output_receivedata_4': '', 'Input_Sendata': 'W1 DBG 07', 'Result': 'Passed', 'Story_Specification_ID': 'Story_Advanced Id logging_4', 'Output_receivedata_3': '', 'Output_receivedata_1': 'W1 DBG 07 15100600000 0273.600.009 3690', 'Output_receivedata_2': '', 'Responsedata': 'W1 DBG 07 15100600000 0273.600.009 3690', 'Description': ''}, {'Output_receivedata_4': '', 'Input_Sendata': '', 'Result': '', 'Story_Specification_ID': '', 'Output_receivedata_3': '', 'Output_receivedata_1': '', 'Output_receivedata_2': '', 'Responsedata': '', 'Description': ''}, {'Output_receivedata_4': '', 'Input_Sendata': 'C1 CON 1', 'Result': 'Passed', 'Story_Specification_ID': 'Story_CAN Diax Firewall_1', 'Output_receivedata_3': '', 'Output_receivedata_1': 'C1 ACK 0', 'Output_receivedata_2': '', 'Responsedata': 'C1 ACK 0', 'Description': ''}, {'Output_receivedata_4': '', 'Input_Sendata': 'C1 SET 41 01', 'Result': 'Passed', 'Story_Specification_ID': 'Story_CAN Diax Firewall_2', 'Output_receivedata_3': '', 'Output_receivedata_1': 'C1 ACK 0', 'Output_receivedata_2': '', 'Responsedata': 'C1 ACK 0', 'Description': ''}, {'Output_receivedata_4': '', 'Input_Sendata': 'C1 REQ 02 10 01', 'Result': 'Failed', 'Story_Specification_ID': 'Story_CAN Diax Firewall_3', 'Output_receivedata_3': 'C1 RDY 2', 'Output_receivedata_1': 'C1 ACK 0', 'Output_receivedata_2': 'C1 RSP 7e8 10 50 2 0 0 0 0 0', 'Responsedata': 'C1 ACK 0C1 RDY 3', 'Description': ''}]
in_testcasedict= [[{'Output_receivedata_1': 'C1 ACK 0', 'Description': '', 'Story_Specification_ID': 'Story_CAN Set protocol_1', 'Input_Sendata': 'C1 SET 41 01', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Output_receivedata_4': ''}, {'Output_receivedata_1': 'C1 ACK 1', 'Description': '', 'Story_Specification_ID': 'Story_CAN Set protocol_2', 'Input_Sendata': 'C1 SET 41 02', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Output_receivedata_4': ''}, {'Output_receivedata_1': 'C1 ACK 0', 'Description': '', 'Story_Specification_ID': 'Story_CAN Set protocol_3', 'Input_Sendata': 'C1 SET 41 03', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Output_receivedata_4': ''}, {'Output_receivedata_1': 'C1 ACK 0', 'Description': '', 'Story_Specification_ID': 'Story_CAN Set protocol_4', 'Input_Sendata': 'C1 SET 41 04', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Output_receivedata_4': ''}, {'Output_receivedata_1': 'C1 ACK 0', 'Description': '', 'Story_Specification_ID': 'Story_CAN Set protocol_5', 'Input_Sendata': 'C1 SET 41 05', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Output_receivedata_4': ''}, {'Output_receivedata_1': 'C1 ACK 1', 'Description': '', 'Story_Specification_ID': 'Story_CAN Set protocol_6', 'Input_Sendata': 'C1 SET 41 06', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Output_receivedata_4': ''}], [{'Output_receivedata_1': 'W1 DBG 01 00 06', 'Description': '', 'Story_Specification_ID': 'Story_Advanced Id logging_1', 'Input_Sendata': 'W1 DBG 01', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Output_receivedata_4': ''}, {'Output_receivedata_1': 'W1 DBG 02 05 00 00', 'Description': '', 'Story_Specification_ID': 'Story_Advanced Id logging_2', 'Input_Sendata': 'W1 DBG 02', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Output_receivedata_4': ''}, {'Output_receivedata_1': 'W1 DBG 05 00 00 28 bd d6 fc', 'Description': '', 'Story_Specification_ID': 'Story_Advanced Id logging_3', 'Input_Sendata': 'W1 DBG 05', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Output_receivedata_4': ''}, {'Output_receivedata_1': 'W1 DBG 07 15100600000 0273.600.009 3690', 'Description': '', 'Story_Specification_ID': 'Story_Advanced Id logging_4', 'Input_Sendata': 'W1 DBG 07', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Output_receivedata_4': ''}], [{'Output_receivedata_1': 'C1 ACK 0', 'Description': '', 'Story_Specification_ID': 'Story_CAN Diax Firewall_1', 'Input_Sendata': 'C1 CON 1', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Output_receivedata_4': ''}, {'Output_receivedata_1': 'C1 ACK 0', 'Description': '', 'Story_Specification_ID': 'Story_CAN Diax Firewall_2', 'Input_Sendata': 'C1 SET 41 01', 'Output_receivedata_3': '', 'Output_receivedata_2': '', 'Output_receivedata_4': ''}, {'Output_receivedata_1': 'C1 ACK 0', 'Description': '', 'Story_Specification_ID': 'Story_CAN Diax Firewall_3', 'Input_Sendata': 'C1 REQ 02 10 01', 'Output_receivedata_3': 'C1 RDY 2', 'Output_receivedata_2': 'C1 RSP 7e8 10 50 2 0 0 0 0 0', 'Output_receivedata_4': ''}]]
comport="COM7"
class TestTestcomparator(unittest.TestCase):
    def testsend_and_receive_Commsgs(self): 
        testcomparator_obj=testcomparator.Testcomparator(in_testcasedict,comport)
        response=testcomparator_obj.send_and_receive_Commsgs("C1 SET 41 01")
        self.assertEqual(response,"C1 ACK 0\r" )
        del testcomparator_obj
    def testcreate_resultdict_from_responsedatareceieved(self):
        testcomparator_obj1=testcomparator.Testcomparator(in_testcasedict,comport)        
        response1=testcomparator_obj1.create_resultdict_from_responsedatareceieved()
        self.assertEqual(response1,story_dictlist_result)
        del testcomparator_obj1
        
    
if __name__ == "__main__":
    unittest.main()