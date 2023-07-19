import filework

# Функция создания заметки.
def newnote():
    note_name = input('Введите название заметки' + '\n')
    selectedfiles = filework.selectnote(note_name)
    if (len(selectedfiles) == 1):
        print('Заметка с таким именем уже существует \n')
        selectdoing(selectedfiles[0])
    else :
        text_of_note = inputlongtext()
        filework.writenote((note_name + '.json'), text_of_note)

# Функция поиска заметки по имени.
def selectfilename():
    while True:
        note_name = input('Название заметки: ')
        selectedfiles = filework.selectnote(note_name)
        if (len(selectedfiles) == 1):
            return selectedfiles[0]
        if (len(selectedfiles) > 1):
           print("Найдено несколько вариантов: \n" + str(selectedfiles))
           print("\nКакой нужно выбрать? ")
        else : print("Такой заметки не найдено" + '\n')


def selectfiledate():
    target_text = input('Искомый текст: ')
    selectedfiles = filework.searchinnote(target_text)
    if (len(selectedfiles) == 1):
        return str(selectedfiles[0])
    if (len(selectedfiles) > 1):
        print("Найдено несколько вариантов: \n" + str(selectedfiles))
        print("\nКакой нужно выбрать? ")
        return selectfilename()
    else : print("Такой заметки не найдено" + '\n')


# Выбор действия с заметкой
def selectdoing(note_name):
    print(note_name)
    doing = input("Выберите действие: \n 1 Прочитать \n 2 Дополнить \n 3 Заменить \n 4 Удалить \n")
    if (doing == '1'):
        print(filework.readnote(note_name))
    if (doing == '2'):
        text = filework.readnote(note_name)
        print(text)
        adding = inputlongtext()
        text += adding
        filework.writenote(note_name, text)
    if (doing == '4'):
        doing = input(f"Удалить заметку {note_name}? \n 1 Да \n 2 Нет \n")
        if (doing == '1'):
            filework.delnote(note_name)
            print("Готово")
                
            
# Список всех заметок.
def showall():
    all_notes = filework.getallnotes()
    print(all_notes)

# Поиск заметки по дате
def searchdate():
    target = input("Укажите дату в формате дд.мм чч.мм.сс (можно частично): \n")
    selectedfiles = filework.searchdate(target)
    if (len(selectedfiles) == 1):
        temp = str(selectedfiles.values()).removeprefix("dict_values(['").removesuffix("'])")
        return temp
    if (len(selectedfiles) > 1):
        print("Найдено несколько вариантов: \n" + str(selectedfiles))
        print("\nКакой нужно выбрать? ")
        return selectfilename()
    else : print("Такой заметки не найдено" + '\n')
            


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


def wronginput():
    print("Нет такой команды")

def chosenote(selectedfiles):
    if (len(selectedfiles) == 1):
        return selectedfiles[0]
    if (len(selectedfiles) > 1):
        print("Найдено несколько вариантов: \n" + str(selectedfiles))
        print("\nКакой нужно выбрать? ")
        selectfilename()
    else : print("Такой заметки не найдено" + '\n')