def ex5(statement):
    statement = statement.replace('.', '').replace(',', '').replace(':', '').lower().split()
    palavras = []
    for palavra in statement:
        if len(palavra) > 4:
            for letra in palavra:
                if letra in 'python':
                    palavras.append(palavra)
                    break
    return palavras

statement = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."

palavras = ex5(statement=statement)
print(palavras)