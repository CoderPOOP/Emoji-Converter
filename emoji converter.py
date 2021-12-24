#Emoji Converter

message = input(">")
words = message.split(" ")
emojis = {
    ":)": "😄",
    ":(": "😔",
    "Hi": "👋"
    # like this we can add more
}

output = ""

for word in words:
    output += emojis.get(word, word) + " "

print(output)