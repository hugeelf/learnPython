def add_contact(user_data):
    with open('phone_book.txt', 'a', encoding='utf-8') as pb:
        pb.write('\n' + user_data.title())
