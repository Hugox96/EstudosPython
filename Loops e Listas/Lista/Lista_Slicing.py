# Slicing is yet another super practical aspect of Python. 
# It makes accessing strings, lists and tuples partially very effortless.

# Syntax
# 1) Follow the syntax notation [start:end:step]

# 2) If start is not given it will start from 0 (zero)

# 3) If end is not given it will go all the way to the end

# 4) If step is not given, steps will increase by 1


lista = [1,5,6,7,8,9]
# neste caso a variavel a receberá os numeros que correspondem a posição 1 e 3 da lista, já que o ultimo número(4) não conta
a= lista[1:5]
print(a)
print("4º posição da lista:", lista[4])
