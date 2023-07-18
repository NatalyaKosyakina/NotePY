import os
import datetime
from os import listdir


path_to_notes = r'notesfolder/'
path_to_list_of_notes = r'noteslist.txt'
# Функция для чтения записки по номеру файла. 
# Принимает номер файла, по идее должна возвращать прочитанную строку.
def readnote(note_name):
    file_path = path_to_notes + str(note_name)   
    with open(file_path, 'r') as f:
        return(f.read())
        f.close

# Функция для создания нового файла. Принимает: имя файла, дату создания/изменения, текст файла. Нужна ли дата? Нужна проверка на имя
def createnote(note_name, text_of_note):
    file_path = path_to_notes + str(note_name) + '.txt'
    date_of_change = datetime.datetime.now().strftime('%m.%d.%Y %H:%M:%S')
    with open(file_path, 'w') as f:
        f.write(date_of_change + '\n')
        f.write(text_of_note + '\n')
        f.close
    with open(path_to_list_of_notes, 'w+') as f:
        f.write(note_name + '\n')
        f.write(date_of_change + '\n')
        f.close
    

# Поиск файла по названию
def selectnote(note_name):
    result = []
    for note in listdir(path_to_notes):
        if (note_name in note):
            result.append(note)
    return result

# Поиск файла по дате.

# Функция удаления файла будет в презентере.
def delnote(note_name):
    os.remove(path_to_notes + note_name)
# Функция изменения файла (дозаписи) тоже будет в презентере: сначала ищем файл, затем читаем его, отбрасываем дату, и добавляем новый текст
def editnote(note_name):
    file_path = path_to_notes + str(note_name) 
    flag = True
    with open(file_path, 'r+') as f:
        print(f.read())
        while flag:
            user_input = input()
            else :
                f.write(input())
        f.close