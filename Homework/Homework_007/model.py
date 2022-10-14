def find(name):
    with open('phone_book.txt', 'r', encoding='utf-8') as pb:
        book = (pb.readlines())
        answer = [i.strip('\n')
                  for i in book if i.lower().find(name.lower()) >= 0]
        return answer
