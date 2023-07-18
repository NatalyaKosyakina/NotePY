# Объект Приложение. 
# Содержит выбор действия, вызывает интерфейс  для работы с консолью и презентер.
import consoleview

flag = True
while (flag):
    user_input = int(input('Выберите действие: \n 1 Добавление новой заметки \n 2 Поиск заметки по названию \n 3 Поиск заметки по дате \n 4 Выход \n'))
    if (user_input == 1):
       consoleview.newnote()
    if (user_input == 2):
       note = consoleview.selectfilename()
       consoleview.selectdoing(note)
    if (user_input == 3):
       print(3)    
    if (user_input == 4):
       flag = False