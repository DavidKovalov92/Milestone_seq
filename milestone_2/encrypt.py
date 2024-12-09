from decrypt import encrypt, step, alphabet
old_message = ''
def decrypted(dec, enc=encrypt(), step=step):
    for i in enc:
            alphabet_index = alphabet.index(i)
            new_i = (alphabet_index - step) % len(alphabet)
            dec += alphabet[new_i]
    return dec

print(decrypted(old_message))