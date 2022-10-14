def add_contact(user_data):
    with open('phone_book.txt', 'a', encoding='utf-8') as pb:
        temp = user_data.split('+')
        user_data = temp[0]+'|| +'+temp[1]
        pb.write('\n' + user_data.title())
