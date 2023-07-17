import txtfilework

# Функция создания заметки. Памятка: обязательно добавить проверку на наличие такой заметки!
def newnote():
    note_name = input('Введите название заметки' + '\n')
    text_of_note = input('Введите текст заметки' + '\n')
    # Тут должна быть проверка на наличие заметки с таким именем и сообщение, что такая заметка уже есть.
    # Хотите отредактировать? Да - редактирование, нет - замена.
    txtfilework.createnote(note_name, text_of_note)

# Функция поиска заметки по имени. Принимает название (приблизительно). Сверяет со списком файлов, сохраненных в папке. 
# Если совпадений нет, выводит сообщение, просит ввести данные повторно. 
# Если совпадений несколько, выводит их названия и просит указать точнее.
# Если совпадение одно, открывает файл. 

def selectfilename():
    flag = True
    while flag:
        note_name = input('Название заметки: ')
        selectedfiles = txtfilework.selectnote(note_name)
        if (len(selectedfiles) == 1):
            return selectedfiles[0]
        if (len(selectedfiles) > 1):
           print("Найдено несколько вариантов: \n" + selectedfiles)
           print("\nКакой нужно выбрать? ")
        else : print("Такой заметки не найдено" + '\n')


#def selectfiledate():


# Выбор действия с заметкой
def selectdoing(note_name):
    user_input = input("Выберите действие: \n 1 Прочитать \n 2 Дополнить \n 3 Удалить \n")
    if (user_input == 1):
       txtfilework.readnote(note)
    if (user_input == 2):
       
       print(note)
    if (user_input == 3):
        print(note)
    
# Функция удаления заметки.
