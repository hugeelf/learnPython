def search_data():
    with open ('base.txt','r', encoding='utf-8') as base:
        user_data = input('Введите данные для поиска: ')
        for i in base:
            if i.find(user_data)!=-1:
                return i

def edit_data ():
    with open ('base.txt', 'r', encoding = 'utf-8') as base:
        a=[]
        for i in base:
            a.append(i)
    old_data = search_data()
    a[a.index(old_data)] = input('Введите новые данные:\n ')
    with open ('base.txt', 'w+', encoding = 'utf-8') as base: 
          for i in a:
            base.write(f'{i}\n')
     
