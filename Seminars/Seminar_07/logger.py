# запись в файл

def log_expression (a):
    with open ('file.txt','w', encoding='utf-8') as file:
        file.write(f'Уравнение: {a} = 0 \n')
def log_answer(a):
    with open ('file.txt','a',encoding='utf-8') as file:
        file.write(f'Ответ на уравнение: {a} \n')