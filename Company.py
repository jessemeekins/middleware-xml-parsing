#%%
#------------->   COMPANY.PY CLASS MODULE  <---------------
# Company class is ised to create Object froms a list of companies.
# The list of companies can be found in companies.py. It isnt 100%,
# correct but will surfice for the time being. The Company Class allows,
# Record objects to be added to the Company staff list. Additional functions,
# have been outlined to manipulate and change the Objects attributes.
# These attributes will be used in the app.py file to further proccess,
# the companies and personnel to provide a more robust application.
# Some of the below functions will appear abstract, but ill try to put,
# references to pythons documentation for followup. 


# Importing the Record class and all of its functionality
from Record import *

# Importing all nessecary packages
# logging will further developed in near future
import logging
from functools import singledispatch

# Defining the company class
class Company():
    # Initializing the company class
    # Only requires 1 argument to set up the Object
    # argument format should be "E69" or "T420"
    def __init__(self, name:str) -> None:
        # argument passed into this value
        self.name = name
        # Default empty staff list, will hold all Record Objects, that represent staffing records
        self.staff = []
        # Of the staffing records, how many have "1.0" in their position, representing paramedic
        self.medic_count =  0 
        # Default to false, will toggle to true once an Object with Paramedic is passed into the list
        # Trouble shoot this method within this class, under __add__() function
        self.is_als = False
        # Not yet functional within this class, mostly designed for comparer operators < > = in app.py
        self.overstaffed = False

    # Function returns a string representation of this Object. Fully Customizable.
    def __str__(self) -> str:
        return f"[{self.name} ALS: {self.is_als}] numParamedics: {self.medic_count} - overStaffed: {self.overstaffed}"
    
    # Defines a human readable representation of the Object if no other methods are called upon the Object
    # calling this method will launch a second func within this func to refresh if Objects values when, 
    # Record Objects are added and deleted
    def __repr__(self) -> str:
        # internal class method that auto refreshes and checks staffing list for paramedics and update counts
        self.refresher()
        # The actual formated string representation that is returned
        return f"""

        COMPANY: {self.name}
        # STAFF: {self.staff}
        # MEDICS: {self.medic_count}
        ALS: {self.is_als}

        """
    # This allows a Company Object to allow + operator to add a Record to the staff list
    # jesse = Record(...)
    # engine69 = Company(...)
    # engine69 + jesse
    # This will add a "jesse" object to the Company Objects list
    def __add__(self, obj:object, verbose=False) -> None:
        # Checks if passed "jesse" is an object, the object module is name "Record and length(staff List is less that 4)"
        if isinstance(obj, object) and obj.__module__ == "Record" and len(self.staff) <= 4:
            # Appends object to self.staff list
            self.staff.append(obj)
            # checks if object has paramedic set to true
            if obj.paramedic:
                # object i set to true, change is als to true
                self.is_als = True 
                # medic
                self.medic_count += 1
        else:
            if verbose:
                print('Did not meet screening criteria (Object, Classname: Record, or staff <= 4)')
            pass

    def __sub__(self, obj:object, verbose=False) -> None:
        if isinstance(obj, object):
            self.staff.remove(obj)
            if obj.paramedic:
                self.medic_count -= 1
            if self.medic_count == 0:
                self.is_als = False

        if verbose:
            print(obj)
            print(self.staff)

    def __eq__(self, obj:bool, verbose=False) -> bool:
        if isinstance(obj, bool):
            if self.is_als == obj:
                return True
            else:
                return False
        else:
            if verbose:
                print('Object needs to be a bool.')
            else:
                logging.DEBUG(f"{Company(__name__)} failed to execute '==' comp..." )
                
    def __gt__(self, obj: int, verbose=False):
        if isinstance(obj, int):
            if self.medic_count > 1:
                return True
            else:
                return False
        else:
            if verbose:
                print('need to pass a numerical value to thuis func')


                


    ######################################
    ###   Class "Getter" Methods for   ###
    ###   each variable in the class   ###
    ######################################
    
    def get_name(self, verbose=False) -> str:
        if verbose:
            print(self.name)
        return self.name
    
    def get_staff(self, verbose=False) -> list:
        if verbose:
            print(self.staff)
        return self.staff
        
    def get_medic_count(self, verbose=False) -> int:
        if verbose:
            print(self.medic_count)
        return self.medic_count

    def get_als(self, verbose=False) -> bool:
        if verbose:
            print(self.is_als)
        return self.is_als

    def refresher(self):
        if not self.is_als:
            for s in self.staff:
                if s.paramedic:
                    self.is_als = True
                    self.medic_count += 1
    
    
    
    
engine25 = Company('E25')

jesse = Record('21233', 'Jesse', 'BC', 'Chief of Staffing 1.0', 'E25', '2023-2-22 07:00:00')
lauren = Record('1234', 'Lauren', 'LT', 'Chief of Staffing 1.0', 'E25', '2023-2-22 07:00:00')
caroline = Record('69420', 'Caroline', 'DC', 'Chief of Beer', 'E25', '2023-2-22 07:00:00')
bryan = Record('18765', 'Brian', 'Dr', 'SORT', 'E25', '2023-2-22 07:00:00')
george = Record('12343', 'Gearoge', 'FFP', 'Nozzle', 'E25', '2023-2-22 07:00:00')

l = [jesse, lauren, caroline, bryan, george]

for i in l:
    engine25+i


ALS = True
MIN = 1



engine25.__str__()

engine25.get_staff()

for name in engine25.staff:
    print(name.name, name.rank, name.paramedic)