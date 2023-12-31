import os
import datetime
from os import listdir


path_to_notes = r'notesfolder/'
time_format = r'%d.%m %H:%M:%S'

# Функция для чтения записки по номеру файла. 
def readnote(note_name):
    file_path = path_to_notes + str(note_name)   
    with open(file_path, 'r') as f:
        return(f.read())
        f.close

# Функция для создания нового файла. Принимает: имя файла, дату создания/изменения, текст файла.
def writenote(note_name, text_of_note):
    file_path = path_to_notes + str(note_name)
    # date_of_change = datetime.datetime.now().strftime(time_format)
    with open(file_path, 'w') as f:
        f.write(text_of_note + '\n')
        f.close
    

# Поиск файла по названию
def selectnote(note_name):
    result = []
    for note in listdir(path_to_notes):
        if (note_name in note):
            result.append(note)
    return result

# Поиск файла по дате.
def searchdate(target):
    result = {}
    for note in listdir(path_to_notes):
        t = os.path.getmtime(path_to_notes + str(note))
        t = str(datetime.datetime.fromtimestamp(t).strftime(time_format))
        if target in t:
            result[t] = note
    return result

# Функция удаления файла
def delnote(note_name):
    os.remove(path_to_notes + note_name)

# Вспомогательная функция поиска информации в файле:
def searchinnote(target_text):
    result = []
    for note in listdir(path_to_notes):
        with open((path_to_notes + str(note)), 'r') as f:
            text = f.read()
            if target_text in text:
                result.append(note)
            f.close
    return result 

def getallnotes():
    result = []
    for note in listdir(path_to_notes):
        result.append(note)
    return result    