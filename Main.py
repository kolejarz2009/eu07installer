# -*- coding: utf-8 -*-
import os
import requests
from pyunpack import Archive

MaSzynaFolder="/home/m/MaSzyna/17.07" #Change this according to your case <!---------------------------
InstallFile="test"#input("Name of the install script:")

if os.path.exists(InstallFile)==False: #Check If given file exists
	print("File does not exist")
	quit()

def r_i_ReadScript(r_i_Name): #This works - Need to add decoder from Ansi!! #Works-NonAsni
	f = open(r_i_Name, "r")
	#f=g.decode('utf-8')
	lines = f.readlines()	
	f.close()
	if (lines[1])=="purpose=eu07\n":
		DnHeader=int(lines.index("[DOWNLOAD]\n"))	
		DnLineNr=int(DnHeader + 1) #Download URL is next line under the [DOWNLOAD] line
		URL_Line=(lines[DnLineNr]) #
		DnList=URL_Line.split("=") #Split DnList into two sections, URL [0], and SaveFileAs_PreMod[1]
		URL=DnList[0]
		SaveFileAs_PreMod=DnList[1].split("\n")	#Get rid of \n at the end of the line
		SaveFileAs=SaveFileAs_PreMod[0]	
		return URL, SaveFileAs 
		print("URL:", URL, "will be saved as:", SaveFileAs)
		print(lines[2])	
		DescriptionLine=(lines[2].split("="))
		#print(DescriptionLine[0].decode(utf-8))##Check
		print("Downloading file(s)...")		
		os.chdir(MaSzynaFolder)
		os.chdir("download") 
		r = requests.get(URL, stream=True)
		with open(SaveFileTo, 'wb') as fd:
			for chunk in r.iter_content(chunk_size=128):
				fd.write(chunk)
	else:
		print("Looks like this isn't a suitable install file. Please try doing it manually.")

def AskToContinue(): #Ask for permission to continue	#Works
	AskUser=input("Continue with the installation process? [y/N]")
	if AskUser=="Y" or AskUser=="y":
		print("Downloading files, please wait.")
	else:
		print("Installation aborted! Only y or Y continues the installation")
		quit()

def ArchiveExtraction(ArchiveName, ContentsDestination=MaSzynaFolder):
	ContentsDestination="/home/m/EU07Installer/pkg/"#Docelowo $MaSzynaFolder
	Archive(ArchiveName).extractall(ContentsDestination) 
	print("Extraction complete. Running post install jobs.")

def TexturesTxtProcess(): #Process that adds the required Textures.txt entries
	# Requires "r_i_ReadScript" to be run first!	
	WhichTexturesLine=int(lines.index("[TEXTURES.TXT]\n")+1)
	TexturesTxtLocation=lines[WhichTexturesLine].split("=")
	print(TexturesTxtLocation[0])
	EditTexturesTxtIn=TexturesTxtLocation[0]
	os.chdir(EditTexturesTxtIn)
	print(os.getcwd())
	TypeLine=(TexturesTxtLocation[1]).split("\n")
	print(TypeLine[0])#		ok
	Type=TypeLine[0]	
	print(Type)	#ok
	TextureTxtEntryHeading="["+Type+"]\n"
	print(TextureTxtEntryHeading) #ok
	ReadingTexturesNr=(int(lines.index(TextureTxtEntryHeading)))#		!!!
	print(ReadingTexturesNr)#ok
	ActualLine=int(ReadingTexturesNr)+2

def DetermineIfScriptOrArchive(InstallFile):
	IsScript=True #Debug only	
	if IsScript==True:	
		r_i_ReadScript(InstallName)
		AskToContinue()
		ArchiveExtraction(SaveFileAs, ContentsDestination)	
		if "[TEXTURES.TXT]\n" in lines:
			TexturesTxtProcess()

r_i_ReadScript(InstallFile)
