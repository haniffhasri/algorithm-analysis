def decode_message(message, pattern):
    decoded_message = ""
    for char in message:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decoded_char = chr((ord(char) - ascii_offset - pattern) % 26 + ascii_offset)
            decoded_message += decoded_char
        else:
            decoded_message += char
    return decoded_message


def rabin_karp_decode(encoded_message):
    pattern = ""
    encoded_length = len(encoded_message)
    pattern_length = 0

    for i in range(encoded_length):
        if encoded_message[i].isdigit():
            pattern += encoded_message[i]
            pattern_length += 1
        elif pattern_length > 0:
            decoded_message = decode_message(encoded_message[:i], int(pattern)) + encoded_message[i:]
            return decoded_message

    return None

encoded_message = "Ymfy ujwxts nx htrnsl ktw rj! Nk dtz knsi ymnx styj, qttp fwtzsi rd uwtujwyd. Mnsy: N anxnyji ymj fwjf bnym rd ywtqqjd kwtr ymj lfwijs xmji -5."

decoded_message = rabin_karp_decode(encoded_message)
if decoded_message:
    print(decoded_message)
else:
    print("Pattern not found in the encoded message. Cannot decode the message")