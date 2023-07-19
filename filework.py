import os
import datetime
from os import listdir


path_to_notes = r'notesfolder/'
path_to_list_of_notes = r'noteslist.json'
time_format = r'%m.%d.%Y %H:%M:%S'
# Функция для чтения записки по номеру файла. 
# Принимает номер файла, по идее должна возвращать прочитанную строку.
def readnote(note_name):
    file_path = path_to_notes + str(note_name)   
    with open(file_path, 'r') as f:
        return(f.read())
        f.close

# Функция для создания нового файла. Принимает: имя файла, дату создания/изменения, текст файла.
def writenote(note_name, text_of_note):
    file_path = path_to_notes + str(note_name)
    date_of_change = datetime.datetime.now().strftime(time_format)
    with open(file_path, 'w') as f:
        f.write(date_of_change + '\n')
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

# Функция удаления файла будет в презентере. А нет, здесь, потому что пути все хранятся здесь.
def delnote(note_name):
    
    os.remove(path_to_notes + note_name)
# Функция изменения файла (дозаписи) тоже будет в презентере: сначала ищем файл, затем читаем его, отбрасываем дату, и добавляем новый текст
# Вспомогательная функция: при создании файла нужна регистрация во вспомогательном файле notelist, чтоб потом искать данные было проще.
def regnote(note_name):
    date_of_change = datetime.datetime.now().strftime(time_format)
    with open(path_to_list_of_notes, 'a') as f:
        f.write('\n{ "' + note_name + '": ')
        f.write('"' + date_of_change + '"}')
        f.close

# Вспомогательная функция поиска информации в файле:
def searchinnote(target_text):
    result = []
    for note in listdir(path_to_notes):
        print(note)
        with open((path_to_notes + str(note)), 'r') as f:
            text = f.read()
            if target_text in text:
                result.append(note)
            f.close
    return result    