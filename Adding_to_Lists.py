def spelling_bee(word):
    result = []
    result.append(word)
    result.extend(list(word))
    result.append(word)
    return result

# Example usage
word1 = input("Input a word: ")

output1 = spelling_bee(word1)


print(output1)
