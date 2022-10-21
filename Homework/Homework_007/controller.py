import model
import writer
import ui


def start_book():
    user_input = (ui.get_user_data(
        a='Вы хотите найти или добавить абонента?\n'))
    if user_input == 'добавить':
        writer.add_contact(ui.get_user_data(
            'Введите имя и номер телефона абонента (начните номер с +) \n'))
    elif user_input == 'найти':
        ui.view_data(model.find(
            (ui.get_user_data('Введите ФИО абонента для поиска\n'))))