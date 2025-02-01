from sys import argv

# (script, filename) = argv

# fileName = 'D:\Work\Training\Training\Python\ex15_sample.txt'

txt = open('D:\Work\Training\Training\Python\ex15_sample.txt', "r")

print(f"Содержимое файла {txt.name}:")
print(txt.read())

print("Снова введите имя файла:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
