encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

message = ""
for i in range(len(encrypted_message)):
    if i%2 == 0:
        message += encrypted_message[i:i+1]
    else:
        message += encrypted_message[len(encrypted_message) -i -1: len(encrypted_message)-1]
print(message)