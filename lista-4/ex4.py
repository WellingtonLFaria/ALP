def ex4(statement):
    statement = statement.replace('.', '').replace(',', '').replace(':', '').lower().split()
    palavras = []
    for palavra in statement:
        if palavra[0] in 'python' or palavra[-1] in 'python':
                palavras.append(palavra)
    return palavras

statement = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."

print(ex4(statement))
