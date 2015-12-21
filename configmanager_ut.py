import unittest
import configmanager as configmanager
initialtestvalues_dict = {'Project': 'BCD', 'CanSimu': 'NoSimu', 'TesterName': 'SunilKumar', 'COMPORT': 'COM7', 'ProjectName': 'BCD_SmartConnectivity', 'SW_Version': '4.9.0', 'SelectedTest': 'SpecialTest', 'AddInfo': 'Python Frame work Trial test'}
class TestConfigmanager(unittest.TestCase):
    def testget_ini_parameter(self):
        configmanager_obj=configmanager.Configmanager(r"C:\Bcd_access\INI.txt" )
        self.assertEqual(configmanager_obj.get_ini_parameter(),initialtestvalues_dict )
    def testget_comport(self):
        configmanager_obj=configmanager.Configmanager(r"C:\Bcd_access\INI.txt" )
        comport = configmanager_obj.get_comport(initialtestvalues_dict)
        self.assertEqual(comport,"COM7" )

if __name__ == "__main__":
    unittest.main()
