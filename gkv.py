def to_camel_case(text):
    caps = text.upper()
    new = text[0].capitalize()
    for i in range(1 ,len(text)):
        if text[i] == "-" or text[i] == "_":
            new += text[i + 1].upper()
        elif text[i - 1] != "-" and text[i - 1] != "_":
            new += text[i]

    return new
print(to_camel_case("hello-my-friend"))