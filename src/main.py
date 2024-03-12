from os import path
import utils

#Получаем путь к файлу operations.json
PATH = path.join('..', 'operations.json')
#Формируем исходный список операций
lst = utils.get_file(PATH)
#Получаем требуемый список операций, фильруем, сортируем по дате
operation_list = utils.get_operation_list(lst)

#Вывод требуемой информации из списка операций
for i in operation_list[:5]:
    print(utils.get_first_line(i))
    print(utils.get_second_line(i))
    print(utils.get_third_line(i))
    print("")