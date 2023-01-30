import re

# Match

my_string = "Esta es la lección número 7: Lección de Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I)
print(match)
start, end = match.span() 
print(my_string[start:end])

match = re.match("Esta no es la lección", my_other_string, re.I)
if match is not None:
    print(match)
    start, end = match.span() 
    print(my_other_string[start:end])

#print(re.match("Esta es la lección", my_string, re.I))
#print(re.match("Expresiones Regulares", my_string))

# Search

search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span() 
print(my_string[start:end])

# FindAll

findall = re.findall("lección", my_string) # re.I ignore uppercase and lowercase
print(findall)

# Split

split = re.split(" ", my_string)
print(split)

# Sub

sub = re.sub(" ", "_", my_string)
print(sub)
print(re.sub("lección|Lección", "LECCIÓN", my_string))
print(re.sub("[l|L]ección", "LECCIÓN", my_string))

# Patterns

pattern = r'[lL]ección'
print(re.findall(pattern, my_string))

pattern = r'[lL]ección|Expresiones'
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r'[a-z]'
print(re.findall(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r'[l].*'
print(re.findall(pattern, my_string))

# Email validation RegEx

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)

print(is_valid_email("eduardferresanchez@gmail.com"))