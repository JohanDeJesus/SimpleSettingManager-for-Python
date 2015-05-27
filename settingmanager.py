# SettingManager 0.1
# Simple configuration 
# Made by Johan De Jesus

import os
## File holding the settings. 
configurationFile = "config.txt";


## Do not edit beyond this point

## Dictionary array.
arrDict = {};


## Reads configuration file and loads it to arrDict[]
def loadConfiguration():
    try:
        with open(configurationFile,'r') as optionFile:
            for line in optionFile:
                if line[0] != '#':
                    #Line is not a comment.
                    if "=" in line: 
                        optionkey = line.split('=')[0];
                        optionvalue = line.split('=')[1].strip('\n');
                        arrDict[optionkey] = optionvalue;
    except IOError:
        print("Error while reading the specified file. Check your configuration file.")
                
## Returns the value of the specified key.
## If value does not exist, function returns ""
def opt(key):
    if key in arrDict:
        return arrDict[key]
    else:
        return ""



##Saves configuration
def saveConfiguration():
    #debugging reasons
    configFile = "config2.txt"
    try:
        with open(configurationFile,'r') as optionFile:
            with open(configFile,'w') as saveFile:
                for line in optionFile:
                    if ((line[0] != "#") and ("=" in line)):
                        key = line.split("=")[0]
                        buf = key+"="+opt(key)+"\n"
                        saveFile.write(buf)
                    else:
                        saveFile.write(line)

    except Exception as err:
        print("Error: "+err)

    os.remove(configurationFile)
    os.rename(configFile,configurationFile)
        
                        
                    
                
                

    

            
## End

    
## Script begins beyond this point

loadConfiguration();

