count = 0
while True:
    try:
        document = input()

        document_list = list(document)

        for index, cher in enumerate(document):
            if cher == '"':
                if count == 0:
                    count = 1
                    document_list[index] = "``"
                else:
                    count = 0
                    document_list[index] = "''"

        print(''.join(document_list)) #list to string

    except EOFError:
        break