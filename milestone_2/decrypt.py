step = int(input("Enter step: "))
message = input("Enter message: ")
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
encrypted_message = ''
def encrypt(user_message, step=step, new_message=encrypted_message):
    for i in user_message:
            alphabet_index = alphabet.index(i)
            new_i = (alphabet_index + step) % len(alphabet)
            new_message += alphabet[new_i]
    return new_message

print(encrypt(message))