import os #os module imported here
location = os.getcwd() # get present working directory location here
counter = 0 #keep a count of all files found
csvfiles = [] #list to store all csv files found at location
filebeginwithhello = [] # list to keep all files that begin with 'hello'
otherfiles = [] #list to keep any other file that do not match the criteria

for file in os.listdir('Parts'):
    try:
        if file.endswith(".mxl"):
            print ("mxl file found:\t", file)
            csvfiles.append(str(file))
            counter = counter+1
    except Exception as e:
        raise e
        print ("No files found here!")

print ("Total files found:\t", counter)
