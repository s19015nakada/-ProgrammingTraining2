import random

def Typoglycemia(target):

    result = []
    for word in target.split(' '):
        if len(word) <= 4:
            result.append(word)
        else:
            chr_list = list(word[1:-1])
            random.shuffle(chr_list)
            result.append(word[0] + ''.join(chr_list) + word[-1])

            return ' '.join(result)

target = input('文字列を入力してください>')

result = Typoglycemia(target)
print('結果>>' + result)
