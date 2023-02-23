#%%

# Class to take individual Records from XML export and turn each record into an object. 
# These Objects will be added to Company objects list of staff. This will provide a list,
# of object that can be intereacted with via the functions below. In addition, the variables 
# and parameters of each Record object will directly effect the variable and parameters of
# the company object. 

# New future versions of this prgram will utilize log journals which is a built in python,
# library. Reference to the logging module and other python libraries can be found at,
# https://docs.python.org/3/ currently python is on version 3.11.2, I am currently,
# using Python 3.10.8. 

# Python built in library
# will be implimented further in the near future
import logging

# Record class that creates objects from individual "<record>" tags in a XML file export.
# These object represent staffing records added into telestaff during daily operations
class Record:
    # initalize the class and outlines positional arguments needed to create a Record Object
    # Verbose will be later used in conjucntion with debug to toggle between print and logging 
    def __init__(self, eid:str|int, name:str, rank:str, position:str, company:str, time:str, verbose=False):
        # "<RscEmployeeIDCh>"
        self.eid = eid
        # "<RscMasterNameCh>"
        self.name = name
        # "<PosJobAbrvCh>"
        self.rank = rank
        # "<PosFormulaIDCh>"
        self.position = position
        # Checks for "1.0" in position name
        self.paramedic = False
        # "<PUnitAbrvCh>"
        self.company_abr = company
        # "<ShiftStartDt>"
        self.time = time
        # Immidiatly checks record for "1.0",
        try:
            # 1.0 will appaear in position,
            # ** troubleshoot in telestaff formula ID section **
            if '1.0' in self.position:
                # automatically change paramedic to True
                self.paramedic = True
        # Handles error if a NoneType in XML file is encountered        
        # captures error message in a variable called "e"
        except TypeError as e:
            # will record "e" variable text to log file
            logging.ERROR(e)
            # allows program to continue
            pass
    
    # Pronounced Repper, provides a human readable string to,
    # see what information the Object stores. Can be fully,
    # customized using basic python syntax.
    def __repr__(self) -> str:
        # All values need to be declared above
        return f"""
        COMPANY: {self.company_abr}
        EID: {self.eid}
        NAME: {self.name}
        RANK: {self.rank}
        POSITION: {self.position}
        PARAMEDIC: {self.paramedic}
        TIME: {self.time}
        """
    
    
    # Below are "getter" methods. Theyre simply called that because
    # the intention is to get something back from them. Names of,
    # mthods can be changed to anything, "get" is used by convention.

    # Return eid of Object as a string. example "Object.get_id()"
    def get_eid(self) -> str:
        return self.eid
    # returns Objects name as a string
    def get_name(self) -> str:
        return self.name
    # returns Objects rank as a string
    def get_rank(self) -> str:
        return self.rank
    #returns Objects position as a string
    def get_position(self) -> str:
        return self.position
    # returns bool value of is paramedic
    def get_paramedic(self) -> bool:
        return self.paramedic
    # return Objects name as string
    def get_company_abr(self) -> str:
        return self.company_abr
    # return objects start time as a string
    def get_time(self) -> str:
        return self.time


