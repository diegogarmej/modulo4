text = str(input())
word =str(input())
def search (text, word):
    if word in text :
        return ("Word Found")
    else:
        return ("Word no found")

print(search(text, word))

