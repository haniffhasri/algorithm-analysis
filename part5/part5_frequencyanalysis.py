def decode_message(encoded_message, shift):
    decoded_message = ""

    for char in encoded_message:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decoded_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decoded_message += decoded_char
        else:
            decoded_message += char

    return decoded_message

def frequency_analysis(encoded_message):
    frequency_dict = {}

    for char in encoded_message:
        if char.isalpha():
            frequency_dict[char] = frequency_dict.get(char, 0) + 1

    sorted_freq = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
    most_frequent_char = sorted_freq[0][0]

    shift = (ord(most_frequent_char.lower()) - ord('e')) % 26

    return shift

# Encoded message
encoded_message = "Ymfy ujwxts nx htrnsl ktw rj! Nk dtz knsi ymnx styj, qttp fwtzsi rd uwtujwyd. Mnsy: N anxnyji ymj fwjf bnym rd ywtqqjd kwtr ymj lfwijs xmji."

# Perform frequency analysis to determine the shift
shift_value = frequency_analysis(encoded_message)

# Decode the message using the determined shift
decoded_message = decode_message(encoded_message, shift_value)

print("Decoded message:")
print(decoded_message)
