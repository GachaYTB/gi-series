"""A library to support python with the GiS\n
Usage:\n
import gislib\n
gisapp = gis.GiS((appname), (r, g, b of app menu app color), (r, g, b of app menu app title color), (app startup title), (r, g, b of app startup title color))"""

def string_to_hex(input_str):
    return ''.join(hex(ord(char))[2:].upper() for char in input_str)
def rgb_to_hex(rgb):
    r, g, b = rgb
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    hex_color = "{:02X}{:02X}{:02X}".format(r, g, b)
    return hex_color
def number_to_hex(num):
    hex_representation = '{:04X}'.format(num)
    return hex_representation

class GiS:
    def __init__(self, appname:str="Custom App", appmenuappcolor:tuple=(255, 255, 255), appmenuapptitlecolor:tuple=(0, 0, 0), appstartuptitle:str="Custom App", appstartuptitlecolor:tuple=(255, 255, 255)):
        """Initializes the GiS app\n
        Usage:\n
        gisapp = gis.GiS((appname), (r, g, b of app menu app color), (r, g, b of app menu app title color), (app startup title), (r, g, b of app startup title color))"""
        a = string_to_hex(appname)
        b = rgb_to_hex(appmenuappcolor)
        c = rgb_to_hex(appmenuapptitlecolor)
        d = string_to_hex(appstartuptitle)
        e = rgb_to_hex(appstartuptitlecolor)
        self.filecontent = a + "FF05FE" + b + "FF05FE" + c + "FF05FE" + d + "FF05FE" + e

    def export(self, exportpath: str):
        """Exports the GiS App\n
        NOTE: Your file name NEEDS to end with .gisapp\n
        Usage:\n
        gisapp.export((exportpath))"""
        with open(exportpath, "w") as exportfile:
            exportfile.write(self.filecontent)
    
    def print(self, text: str, x:int=0, y:int=0, color:tuple=(255, 255, 255)):
        """Prints some text to the screen\n
        Usage:\n
        gisapp.print((text to print), (x position of the text), (y position of the text), (r, g, b of the text's color))"""
        self.filecontent = self.filecontent + "\n00000000" + rgb_to_hex(color) + number_to_hex(x) + number_to_hex(y) + string_to_hex(text)
    
    def gotomenu(self):
        """Goes to the menu of the console\n
        Usage:\n
        gisapp.gotomenu()"""
        self.filecontent = self.filecontent + '\n000002'