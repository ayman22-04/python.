sentence = input("Enter a long sentence: ")

unique_characters = set(sentence)

unique_characters.discard(" ")

print("Unique Characters:", unique_characters)
print("Total Unique Characters:", len(unique_characters))