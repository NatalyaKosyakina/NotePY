# Объект Приложение. 
# Содержит выбор действия, вызывает интерфейс  для работы с консолью и презентер.
import txtfilework.py

flag = True
while (flag):
    user_input = int(input('Выберите действие: \n 1 Добавление новой заметки \n 2 Редактирование \n 3 Поиск по дате \n 4 Удаление \n 5 Выход \n'))
    if (user_input == 1):
       print(1)
    if (user_input == 2):
       print(2)
    if (user_input == 3):
       print(3)
    if (user_input == 4):
       print(4)
    if (user_input == 5):
       flag = False