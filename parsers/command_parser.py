'''
    Der PDiag Distributor Command String besteht aus 9 Feldern, die jeweils durch ein ~ getrennt werden.


    CommandString class should help create the PDiag command string in multiple steps, e.g.:
        commandstring_inst = CommandString(kennung="01", inifile="testini", "scenarioname="testszenario")
        commandstring_inst(p1, p2, p3)


    Fields and description
    Feld   Name        Input               Beschreibung
    1      Kennung     01                  Scenario is run without any return value
                       02                  Scenario is run normally with all output 
                       03                  Scenario is not run, but info texts of the called messages are displayed

    2      Ini Datei   <name>              Name of the ini file to be used by the PDiag Distributor

    3      Szenario    <name>              Name of the scenario defined in the PDiag Dialog to be called

    4      Param 1     j/n/empty           Controls whether to return message content and the final result

    5      Param 2     j/n/empty           Controls whether to return messages as hex-strings

    6      Param 3     j/n/empty           Controls whether to return messages separated by message section

    7      Param 4     j/n/empty           Controls whether comment sections of the messages should also be returned

    8      Param 5     <list of messages>  Only process messages in the input list. List format is something like 2,5-7,10-12,15

    9      Param 6     L                   If this parameter is set, specific fields are reset to their initial values (see docs for more details)
                       L1                  Like L, but fewer values are reset
                       L2                  Like L, but different values are reset

'''

import yaml
from yaml.loader import SafeLoader

CMD_LIST = [
    "Kennung",
    "Ini Datei",
    "Szenario",
    "Param1",
    "Param2",
    "Param3",
    "Param4",
    "Param5",
    "Param6",
]

YAML_SETTINGS_FILENAME = "default_cmdstring_settings.yaml"

with open(YAML_SETTINGS_FILENAME) as yf:
    DEFAULT_SETTINGS = yaml.load(yf, Loader=SafeLoader)

    #print(DEFAULT_SETTINGS)

class DistributorCommand(object):
    ''' EMPTY DOC '''

    CSTRING_template = "{}~{}~{}~{}~{}~{}~{}~{}"

    def __init__(self, inputoptions={}):

        self._cmdstring = ""

        self._options = { optionkey:None for optionkey in CMD_LIST }
        #print(self._options)

        self.add_options( DEFAULT_SETTINGS )
        #print(self._options)

        self.add_options( inputoptions )
        #print(self._options)

        

    def print_options(self):
        ''' Prints out all options set '''

    def add_options(self, optionsdict):
        ''' Add missing options '''
        self._options.update(optionsdict)

    def get_string(self):
        ''' Returns command string with current command options set '''
        self._cmdstring = self._create_cmdstring()
        return self._cmdstring
    
    def get_string_with_options(self, options):
        ''' Creates command string without affecting class instance '''
        temp_cmdstring = self._create_cmdstring(options)
        return temp_cmdstring

    def _create_cmdstring(self, options={}):
        ''' This function creates the command string from all set parameters '''
        settingslist = [self._options[key] for key in CMD_LIST ]
        return self.CSTRING_template.format(*settingslist)


if __name__ == "__main__":

    dc = DistributorCommand()

    cmdstring = dc.get_string()

    print(cmdstring)



