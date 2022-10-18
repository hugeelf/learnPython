def search_data(user_data):
    with open ('base.txt', 'r', encoding='utf-8') as base:
        a = []
        for i in base:
            if i.find(user_data)!=-1:
                a.append(i)
        return a

def result_normalize (search_result):
    a =[]
    for i in search_result:
        i = i.replace('\n','')
        a.append(i)
    return a

def edit_string(temp_string):
   return temp_string.split('||')

def changes (temp_string, index, new_data):
   temp_string.insert(int(index)-1, new_data)
   temp_string.pop(int(index))
   return temp_string

def list_to_string(temp_string):
    corrected_string = '||'.join(temp_string)
    return corrected_string
