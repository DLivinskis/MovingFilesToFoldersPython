import os
import shutil
dir_list = os.listdir('C:/Users/dlivi/OneDrive/Desktop/Folder/FilesToMove')
print(dir_list[0])
NameToCheck = str(dir_list[0])
print(NameToCheck)
LetterToCheck = NameToCheck[0]
print(LetterToCheck)
if LetterToCheck == 'A':
    print ('Goes to A')
    pathToMove = 'C://Users//dlivi//OneDrive//Desktop//Folder//'
    PathToMovePart2 = str(LetterToCheck)
    pathToMoveCombined = pathToMove + PathToMovePart2
    pathToFileFolder = 'C:/Users/dlivi/OneDrive/Desktop/Folder/FilesToMove/'
    pathToFile = pathToFileFolder + NameToCheck
    print(pathToMoveCombined)
    print(pathToFile)
    shutil.move(pathToFile,pathToMoveCombined)
elif LetterToCheck == 'B':
    print ('Goes to B')
    pathToMove = 'C://Users//dlivi//OneDrive//Desktop//Folder//'
    PathToMovePart2 = str(LetterToCheck)
    pathToMoveCombined = pathToMove + PathToMovePart2
    pathToFileFolder = 'C:/Users/dlivi/OneDrive/Desktop/Folder/FilesToMove/'
    pathToFile = pathToFileFolder + NameToCheck
    print(pathToMoveCombined)
    print(pathToFile)
    shutil.move(pathToFile,pathToMoveCombined)
elif LetterToCheck == 'C':
    print ('Goes to C')
    pathToMove = 'C://Users//dlivi//OneDrive//Desktop//Folder//'
    PathToMovePart2 = str(LetterToCheck)
    pathToMoveCombined = pathToMove + PathToMovePart2
    pathToFileFolder = 'C:/Users/dlivi/OneDrive/Desktop/Folder/FilesToMove/'
    pathToFile = pathToFileFolder + NameToCheck
    print(pathToMoveCombined)
    print(pathToFile)
    shutil.move(pathToFile,pathToMoveCombined)
elif LetterToCheck == 'D':
    print ('Goes to D')
    pathToMove = 'C://Users//dlivi//OneDrive//Desktop//Folder//'
    PathToMovePart2 = str(LetterToCheck)
    pathToMoveCombined = pathToMove + PathToMovePart2
    pathToFileFolder = 'C:/Users/dlivi/OneDrive/Desktop/Folder/FilesToMove/'
    pathToFile = pathToFileFolder + NameToCheck
    print(pathToMoveCombined)
    print(pathToFile)
    shutil.move(pathToFile,pathToMoveCombined)
