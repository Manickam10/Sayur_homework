def encode_message(message, pattern):
    # Remove spaces from the message
    message = message.replace(" ", "")

    encoded_message = []
    message_index = 0

    for char in pattern:
        if char == "*":
            if message_index < len(message):
                encoded_message.append(message[message_index])
                message_index += 1
        else:
            encoded_message.append(char)

    return "".join(encoded_message)

# Test example
message = "I Love India"
pattern = "*** **** ** **********     *****"
output = encode_message(message, pattern)
print(output)
