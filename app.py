# Объект Приложение. 
# Содержит выбор действия, вызывает интерфейс  для работы с консолью и презентер.
import consoleview

flag = True
while (flag):
    user_input = input('Выберите действие: \n 1 Добавление новой заметки \n 2 Поиск заметки по названию \n 3 Поиск по содержимому \n 4 Список всех заметок \n 5 Поиск заметки по дате \n 0 Выход \n')
    if (user_input == '0'):
       flag = False
    if (user_input == '1'):
       consoleview.newnote()
    if (user_input == '2'):
       note = consoleview.selectfilename()
       consoleview.selectdoing(note)
    if (user_input == '3'):
       note = consoleview.selectfiledate()
       if (note != None):
         consoleview.selectdoing(note)
    if (user_input == '4'):
       consoleview.showall()
    if (user_input == '5'):
       note = consoleview.searchdate()
       if (note != None):
         consoleview.selectdoing(note)