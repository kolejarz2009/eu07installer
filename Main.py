import os
import requests
#def ScriptReader(filename)
    ## Open the file with read only permit
InstallScriptName=input("r_i:")
if os.path.exists(InstallScriptName)==False:
	print("Nie ma takiego pliku\nFile does not exist")
	quit()
f = open(InstallScriptName, "r")
    ## use readlines to read all lines in the file
    ## The variable "lines" is a list containing all lines

lines = f.readlines()

	## close the file after reading the lines.
f.close()

if (lines[1])=="purpose=eu07\n" or (lines[2])=="purpose=eu07\n":
	#print(lines) # Pokaż wszystkie linie
	#print("")
	#print(lines.index("[INFO]\n")) # Jaki numer ma ta linia
	DnHeader=int(lines.index("[DOWNLOAD]\n"))
	#print(DnHeader)	
	DnLineNr=int(DnHeader + 1) 
	#print(DnLineNr, "Numer lini z URL")	
	#print(lines[DnLineNr])
	URL_Line=(lines[DnLineNr])
	#print(URL, "Samo URL")
	DnList=URL_Line.split("=") #Split DnList into two sections, URL [0], and SaveFileAs_PreMod[1]
	URL=DnList[0]
	print(URL)	
	SaveFileAs_PreMod=DnList[1].split("\n")	#Get rid of \n at the end of the line
	SaveFileAs=SaveFileAs_PreMod[0]	
	#print(SaveFileAs)
	print("URL:", URL, "will be saved as:", SaveFileAs)

def DownloadFile(URL, SaveFileTo):
    r = requests.get(URL, stream=True)
    with open(SaveFileTo, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)

DownloadFile(URL, SaveFileAs)



