'''

    This module contains class IniCreator()

'''


class IniCreator(object):
    ''' '''

    sections = ["[Allgemein]", "[Logging]", "[GUI]"]

    section_entries = {
            "[Allgemein]":["SprachID", "Konfigurationsverzeichnis", 
                           "Portnummer", "Kennung", "Kommando_Framing",
                           "Original Nachrichten Nr", "TimeOutKennung"
                           ],
            "[Logging]":["LogLevel", "LogVerzeichnis", "KomVerzeichnis",
                         "LogDateienLoeschen", "LoeschanAbAnzahlTage",
                ],
            "[GUI]":["x-Position", "y-Position", "Fensterbreite",
                     "Fensterhoehe", "Schriftgroesse", 
                ],
            }

    def __init__(self):
        ''' '''
        self.filename = None
        self.lines = None


    def write(self):
        ''' Print the complete ini content to file '''
        with open(self.filename, "w") as fout:
            for l in self.lines:
                print(l, file=fout)

    def __call__(self):
        return self.filename



