# SettingManager 0.1
# Simple configuration 
# Made by Johan De Jesus

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
        print("IOError. Check your configuration file.")
                
## Returns the value of the specified key.
## If value does not exist, function returns ""
def opt(key):
    if key in arrDict:
        return arrDict[key]
    else:
        return ""


            
## End

    
## Script begins beyond this point

loadConfiguration();
opt("hi")


