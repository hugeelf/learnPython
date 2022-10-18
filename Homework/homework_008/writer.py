def write_to_base(a):
    with open('base.txt', 'a', encoding='utf-8') as base:
        base.write(f'{a}\n')

def edit_base(old_string,new_string):
    with open ('base.txt', 'r', encoding='utf-8') as base:
        a=[]
        for i in base:
            if len(i)<=1:
                continue
            else:
                a.append(i)
    old_data = old_string
    a[a.index(old_data)] = new_string
    with open ('base.txt', 'w',encoding='utf-8') as base:
        for i in a:
            write_to_base(i)
            