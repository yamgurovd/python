"""ФИО
На вход программе подаются три строки: имя, фамилия и отчество (именно в таком порядке). Напишите программу,
которая выводит инициалы человека.

Формат входных данных
На вход программе подаются три строки, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести ФИО человека.

Примечание. Гарантируется, что имя, фамилия и отчество начинаются с заглавной буквы."""
# Первый вариант решения
first_name = input()
last_name = input()
patronymic = input()

print(first_name[0], last_name[0], patronymic[0], sep='')

# Второй вариант решения
first_name = input()
last_name = input()
third_name = input()

for j in range(len(last_name)):
    if last_name[j] == last_name[0]:
        print(last_name[j], end="")
        break

for i in range(len(first_name)):
    if first_name[i] == first_name[0]:
        print(first_name[i], end="")
        break

for k in range(len(third_name)):
    if third_name[k] == third_name[0]:
        print(third_name[i])
        break
