from os import listdir


path_to_notes = r'notesfolder/'
# Функция для чтения записки по номеру файла. 
# Принимает номер файла, по идее должна возвращать прочитанную строку.
def readnote(note_name):
    file_path = path_to_notes + str(note_name) + '.txt'   
    with open(file_path, 'r') as f:
        return(f.read())
        f.close

# Функция для создания нового файла. Принимает: имя файла, дату создания/изменения, текст файла. Нужна ли дата? Нужна проверка на имя
def createnote(note_name, text_of_note):
    file_path = path_to_notes + str(note_name) + '.txt'
    date_of_change = date_of_change = datetime.datetime.now().strftime('%m.%d.%Y %H:%M:%S')
    with open(file_path, 'w') as f:
        f.write(date_of_change + '\n')
        f.write(text_of_note + '\n')
        f.close

# Поиск файла
def selectnote(note_name):
    result = []
    for note in listdir(path_to_notes):
        if (note_name in note):
            print(note_name + note)
            result.append(note)
    return result

selectnote('4.txt')


# Функция удаления файла будет в презентере.
# Функция изменения файла (дозаписи) тоже будет в презентере: сначала ищем файл, затем читаем его, отбрасываем дату, и добавляем новый текст