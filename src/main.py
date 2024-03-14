import os.path
from utils import get_file, get_operation_list, get_first_line, get_second_line, get_third_line

#Получаем путь к файлу operations.json
PATH = os.path.join(os.path.dirname(__file__), '..', 'operations.json')
#Формируем исходный список операций
lst = get_file(PATH)
#Получаем требуемый список операций, фильруем, сортируем по дате
operation_list = get_operation_list(lst)


#Вывод требуемой информации из списка операций
for i in operation_list[:5]:
    print(get_first_line(i))
    print(get_second_line(i))
    print(get_third_line(i), end= '\n\n')
