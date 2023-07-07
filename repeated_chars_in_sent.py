sentence = 'this is a common python interview question'

dict = {

}

for char in sentence:
    if char != ' ':
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1


sorted_dict = sorted(
    dict.items(), key=lambda listoftuple: listoftuple[1], reverse=True)

print(sorted_dict)
print(sorted_dict[0])
