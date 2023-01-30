'''
Escribe un programa que muestro por consola los números de 1 a 100
(ambos incluidos y con un salto de línea entre cada impresión),
sustituyendo los siguientes:
- Múltiplos de 3 - "fizz"
- Múltiplos de 5 - "buzz"
- Múltiplos de 3 y de 5 - "fizzbuzz"
'''

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print('fizzbuzz')
    elif num % 3 == 0:
        print('fizz')
    elif num % 5 == 0:
        print('buzz')
    else:
        print(num)

nums_list = list(i+1 for i in range(100))
print(nums_list)

for i in range(len(nums_list)):
    fizzbuzz(nums_list[i])

# ---------------------------------------------------------------------- #

'''
Escribe una función que reciba dos palabras y retorne verdadero o falso
según sean o no anagrmas. Un anagrama consiste en formar una palabra
reordenando TODAS las letras de otra palabra inicial. NO hace falta comprobar
que ambas palabras existan. Dos palabras exactamente iguales no son anagrama.
'''

def anagrama(word1, word2):
    
    word1 = word1.lower()
    word2 = word2.lower()
    
    if word1 == word2:
        return False
    
    return sorted(word1) == sorted(word2)

    '''
    word3 = list(range(len(word2)))
    
    
    for i in range(len(word1)):
        letter = word1[i]
        for j in range(len(word2)):
            if letter == word2[j]:
                word3[j] = letter
    
    if word3 == list(word2):
        return True
    else:
        return False
    '''


print(anagrama("Amor", "Roma"))