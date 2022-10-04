with open('Opgaven.csv', 'r', encoding="utf-8") as input:
    data = input.read()
    print(data)

result = ''

with open('Result.csv', 'w', encoding="utf-8") as output:
    output.write(result)