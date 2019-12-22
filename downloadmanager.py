import os
import shutil

#Pad naar folder waar alle bestanden staan
Downloads_Folder_Path = os.path.join(os.path.expanduser('~'),'Downloads')

#Pad naar folders waarin alle bestanden worden gesorteerd
PDF_Folder_Path = os.path.join(Downloads_Folder_Path,'PDF_Files')
DOCX_Folder_Path = os.path.join(Downloads_Folder_Path,'DOCX_Files')
DEB_Folder_Path = os.path.join(Downloads_Folder_Path,'DEB_Files')
IM_Folder_Path = os.path.join(Downloads_Folder_Path,'IM_Files')
OVERIG_Folder_Path = os.path.join(Downloads_Folder_Path,'OVERIG_Files')

Folder_Paths = (PDF_Folder_Path, DOCX_Folder_Path, DEB_Folder_Path, IM_Folder_Path, OVERIG_Folder_Path)

#List alle bestanden in de Downloads Folder
Files_In_Dir = os.listdir(Downloads_Folder_Path)

#Maak lijst met pad naar objecten in downloads en lijst met pad naar
#daadwerkelijke bestanden zelf
Downloads_File_Paths = []
Files = []

#Loop die van de bestanden paden maakt
for File_Path in Files_In_Dir:
    File_Path = os.path.join(Downloads_Folder_Path, File_Path)
    Downloads_File_Paths.append(File_Path)

#Loop die checkt of het een bestand is en er vervolgens een lijst van maakt
for File_Path in Downloads_File_Paths:
    if os.path.isfile(File_Path) == True:
        Files.append(File_Path)


for File in Files:
    if File.find('.pdf') != -1:
        shutil.move(File, Folder_Paths[0])
    elif File.find('.docx') != -1:
        shutil.move(File, Folder_Paths[1])
    elif File.find('.deb') != -1:
        shutil.move(File, Folder_Paths[2])
    elif File.find('.jpg') != -1 or File.find('.png') != -1 or File.find('.jpeg') != -1:
        shutil.move(File, Folder_Paths[3])
    else:
        shutil.move(File, Folder_Paths[4])
