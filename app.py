#%%


##########################################################################
##########################################################################                                                     
### Class used to parse XML file from imports, proccess "records"      ###
### from XML file. Each Record will be turned into class object        ###
### and stored in a local class Dict. Record Objects will be added     ###
### to Company class object created from a list of companies in MFD    ###
### After dictionsaries are made, Record Objects will be added to      ###
### Company Object and stored, within their own "self.staff" dict      ###
### for further proccessing.                                           ###
##########################################################################
##########################################################################


from Record import *
from Company import *
from companies import *
from datetime import datetime as dt


# Python logging module, basic config to file
# Full implemintation forthcoming
import logging
logging.basicConfig(filename='test_logger.log',level=logging.INFO)

# Python xml module config and file location to be uploaded and parsed 
# ET.parse as ET, tree and root are used by convention
import xml.etree.ElementTree as ET
tree = ET.parse('/Users/jessemeekins/Documents/VS Code (original)/ROS11 MFD2023-01-27.xml')
root = tree.getroot()



# Stores all MFD Company Objects for further usage
companyDict = {}
# Stores all MFD XML roster records used for later analysis and use 
personnelDict = {}

class FileProccessing:
    # Initialization takes in no auguements, only defines two dictionaies for temp storage
    def __init__(self) -> None:
        pass
    
    ####################################################################
    ####    Class Function used by create_all_record_objects() to,  ####
    ####    to locate and extract text data from specific XML tags  ####
    ####################################################################

    def parse_record(self, record) -> dict:
        # Try/Except returns all data required or defaults to None type  
        try:
            # EID of employee in XML Record
            eid = record.find('RscEmployeeIDCh').text
            # Name of employee in XML Record
            name = record.find('RscMasterNameCh').text
            # Rank ef employee inXML Record
            rank = record.find('PosJobAbrvCh').text
            # Position of employee in XML Record 1.0 denotes paramedic
            position = record.find('PosFormulaIDCh').text
            # Unit abreviation located in XML Record
            comp = record.find('PUnitAbrvCh').text
            # Start date and time of Record inside XML record
            start = record.find('StaffingStartDt').text
        
            # Return a dictionary to be later added to the class dictionary self.personnelDict
            return {'EID':eid, 'NAME':name, 'RANK':rank, 'POSITION':position, 'COMP':comp, 'START':start}
        
        # If any values are not found or errors in parsing required data, 
        # program will continue collecting data without crashing.
        # Excpetion will be caught as variabble "e" as logged in log file
        except Exception as e:
            # Logging error to log file 
            logging.error(e)
            # Returning Nonetype, record will not be added to class dict
            return None
        
        
    ###############################################################################
    ####    Function for looping through all Apparatus List in comapnies.py,   ####
    ####  creating objects utilizing the Company class located in company.py   ####
    ###############################################################################

    def create_apparatus_objects(self) -> None:
        # For Loop through companies listed in "from companies import *" -> companies.py 
        for object in ALL_MFD_COMPANIES:
            # Creates Company object from company.py Company class
            company = Company(object)
            # Adds Company Object to Global Company Dictionary variable for later use
            companyDict[company.name] = company



    ############################################################################
    ####    Function for looping through all Records in a XML export and    ####
    #### creating objects utilizing the Records class located in records.py ####
    ############################################################################

    def create_all_record_objects(self) -> None:
        # For loop through children elements with tag <Record> in XML file import
        # root is defined above as apart XML package and tree manager refer to Python 3.11 Docs
        for child in root.iter('Record'):
            # Function from current class, defined 
            # above to return values with specific XML tags
            # Stores each Record instance as data 
            data = self.parse_record(child)
            # Checks that eack "data" is not None
            if data != None:
                # Creates new Record object that containes roster record data
                newRecord = Record(data['EID'] ,data['NAME'], data['RANK'], data['POSITION'], data['COMP'], data['START'])
                # Function from Record.py to check if record has 1.0 in roster record
                # 1.0 come from telestaff in profile FormulaID area
                newRecord.is_paramedic()
                # Adds record dict to Global personnelDict 
                personnelDict[data['EID']] = newRecord


class Get:
    def __init__(self):
        pass

    def get_company(self, company:str) -> object:
        comp = companyDict.get(company, None)
        return comp

    def get_record(self, EID:str) -> object:
        emp = personnelDict.get(EID, None)
        return emp
    

run = FileProccessing()
run.create_apparatus_objects()
run.create_all_record_objects()

getter = Get()
faulkner=getter.get_record('4783')
harris=getter.get_record('31857')
engine1 = getter.get_company('E1')

faulkner