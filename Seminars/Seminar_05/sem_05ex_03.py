# Напишите программу, удаляющую из текста все слова, содержащие "абв".
text_string = ['абв', 'абвгд', 'абвг', 'рпвд', 'абв']
answer = [i for i in text_string if i.find('абв')]
# for i in text_string:
#     if i.find('абв')==-1:
#         answer.append(i)
print(answer)