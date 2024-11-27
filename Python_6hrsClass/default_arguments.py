def greet(name, greeting = "Hello"): #預設引數為greeting的 Hello PS:預設引數須放在後面
    print(f"{greeting}, {name}")

greet("Joseph")

greet("Joseph", "Bonjour")