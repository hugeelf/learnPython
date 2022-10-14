# ввод от пользователя и вывод в консоль
import model
import logger

def get_expression ():
    return input()

def show_result(a):
    print (a)


expression = get_expression() # получение данных от пользователя

answer = model.solution(expression) # сохранение решения

logger.log_expression(expression)
logger.log_answer(answer)
show_result(answer) # вывод ответа в консоль