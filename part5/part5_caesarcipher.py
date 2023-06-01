def decode_message(message, shift):
    decoded_message = ""
    for char in message:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decoded_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decoded_message += decoded_char
        else:
            decoded_message += char
    return decoded_message


encoded_message = "Ymfy ujwxts nx htrnsl ktw rj! Nk dtz knsi ymnx styj, qttp fwtzsi rd uwtujwyd. Mnsy: N anxnyji ymj fwjf bnym rd ywtqqjd kwtr ymj lfwijs xmji."
decoded_message = decode_message(encoded_message, 5)
print(decoded_message)
