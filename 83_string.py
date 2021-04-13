message = "This is a loren ipsum text."

print(message)
print(message[0], message[1], message[2], message[3])
print(len(message))
print(message[5:7])
print(message[5:])


print("index of fist space: ",message.index(' '))

first_space_index = message.index(' ')
print("text after first space:", message[first_space_index+1:])

last_space_index = message.rindex(' ')
print("text after first space:", message[first_space_index+1:])

words = message.split(" )
print(words)
