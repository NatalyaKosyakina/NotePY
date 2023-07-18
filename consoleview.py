import txtfilework

# Функция создания заметки. Памятка: обязательно добавить проверку на наличие такой заметки!
def newnote():
    note_name = input('Введите название заметки' + '\n')
    # Тут должна быть проверка на наличие заметки с таким именем и сообщение, что такая заметка уже есть.
    # Хотите отредактировать? Да - редактирование, нет - замена.
    selectedfiles = txtfilework.selectnote(note_name)
    if (len(selectedfiles) == 1):
        print('Заметка с таким именем уже существует \n')
        selectdoing(selectedfiles[0])
    else :
        text_of_note = inputlongtext()
        txtfilework.writenote((note_name + '.txt'), text_of_note)
        txtfilework.regnote(note_name)

# Функция поиска заметки по имени. Принимает название (приблизительно). Сверяет со списком файлов, сохраненных в папке. 
# Если совпадений нет, выводит сообщение, просит ввести данные повторно. 
# Если совпадений несколько, выводит их названия и просит указать точнее.
# Если совпадение одно, открывает файл. 

def selectfilename():
    while True:
        note_name = input('Название заметки: ')
        selectedfiles = txtfilework.selectnote(note_name)
        if (len(selectedfiles) == 1):
            return selectedfiles[0]
        if (len(selectedfiles) > 1):
           print("Найдено несколько вариантов: \n" + str(selectedfiles))
           print("\nКакой нужно выбрать? ")
        else : print("Такой заметки не найдено" + '\n')


def selectfiledate():
    note_name = input('Искомый текст: ')
    selectedfiles = txtfilework.searchinnote(note_name)
    if (len(selectedfiles) == 1):
        return selectedfiles[0]
    if (len(selectedfiles) > 1):
        print("Найдено несколько вариантов: \n" + str(selectedfiles))
        print("\nКакой нужно выбрать? ")
        selectfilename()
    else : print("Такой заметки не найдено" + '\n')


# Выбор действия с заметкой
def selectdoing(note_name):
    doing = input("Выберите действие: \n 1 Прочитать \n 2 Дополнить \n 3 Заменить \n 4 Удалить \n")
    if (doing == '1'):
        print(txtfilework.readnote(note_name))
    if (doing == '2'):
        text = txtfilework.readnote(note_name)
        print(text)
        adding = inputlongtext()
        text += adding
        txtfilework.writenote(note_name, text)
    if (doing == '4'):
        doing = input(f"Удалить заметку {note_name}? \n 1 Да \n 2 Нет \n")
        if (doing == '1'):
            txtfilework.delnote(note_name)
            print("Готово")
                
            
# Редактирование заметки (дополнение?). Должно открывать заметку для чтения 

# Вспомогательная функция: ввод текста заметки построчно.
def inputlongtext():
    print("Введите текст заметки. Для завершения введите END на отдельной строке")
    flag = True
    longtext = ''
    while flag:
        adding = input()
        if adding == 'END':
            flag = False
        else: 
            longtext += adding + '\n'
    return longtext