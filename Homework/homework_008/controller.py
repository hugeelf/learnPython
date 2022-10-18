import ui
import model
import writer


def start_work():
    return ui.get_user_data()


def search_work():
    user_data = ui.get_user_data('Введите данные сотрудника для поиска: \n')
    search_result = model.search_data(user_data)
    return model.result_normalize(search_result)



def add_data_work():
    id = ui.get_user_data('Введите id сотрудника: ')
    name = ui.get_user_data('Введите ФИО сотрудника: ')
    phone = ui.get_user_data('Введите номер телефона сотрудника: ')
    post = ui.get_user_data('Введите должность сотрудника: ')
    cost = ui.get_user_data('Введите зарплату сотрудника: ')
    return (f'{id}||{name}||{phone}||{post}||{cost}')


def write_to_file(a):
    writer.write_to_base(a)

def beautify_edit_data(old_string):
    counter = 0
    for i in old_string:
        counter+=1
        ui.print_data(f'Запись {counter}: {i}')

def edit_info(old_string,string_number):
    temp_string = model.edit_string(old_string[int(string_number)-1])
    trigger = ui.get_user_data(f'Что будем менять?'
                    f'\n 1 - id'
                    f'\n 2 - ФИО'
                    f'\n 3 - Номер телефона'
                    f'\n 4 - Должность'
                    f'\n 5 - Зарплату'
                    f'\n'
                    )
    new_data = ui.get_user_data('Введите новое значение:\n')
    
    for_changes = [int(string_number)-1,model.changes(temp_string, trigger, new_data)]
    return for_changes


def edit_work():
    old_string = search_work()
    beautify_edit_data(old_string)
    old_list_index_and_new_list = edit_info(old_string, ui.get_user_data('Укажите номер записи для редактирования: '))
    new_list = model.list_to_string(old_list_index_and_new_list[1])
    string_to_change = str(old_string[int(old_list_index_and_new_list[0])])+'\n'
    # print (new_list)
    # print (old_list_index_and_new_list)
    # print(old_string)
    # print(new_string)
    writer.edit_base(string_to_change,new_list)


while True:
    mode = int(start_work())
    if mode == 1:
        for i in search_work():
            ui.print_data(i)
    elif mode == 2:
        write_to_file(add_data_work())
    elif mode == 3:
        edit_work()
    else:
        break
