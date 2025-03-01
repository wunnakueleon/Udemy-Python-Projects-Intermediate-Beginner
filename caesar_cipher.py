alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(word, num, decipher):
    word_list = list(word)
    message = []
    for i in word_list:
        if i in alphabet:
            space_num = alphabet.index(i)
            if decipher == 'encode':
                message += str(alphabet[(space_num + num) % 26])
            else:
                message += str(alphabet[(space_num - num) % 26])
        else:
            message += i
    string_message = ''.join(message)
    print(string_message)


user_word = input('Enter the word: ').lower()
shifters = int(input('Enter the number that you want to shift to: '))
encode_decode = input('Encode or Decode: ').lower()
encrypt(word=user_word, num=shifters, decipher=encode_decode)
