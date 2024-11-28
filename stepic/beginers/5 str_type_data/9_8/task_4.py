"""еобычное сравнение 📊
На вход программе подаются 2 строки. Вам необходимо сравнить эти строки посимвольно,
не учитывая регистр и игнорируя все небуквенные символы. Программа должна вывести «YES»,
если строки окажутся равны в результате такой проверки, или «NO» в противном случае.

Формат входных данных
На вход программе подаются 2 строки, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести «YES» или «NO» в соответствии с условием задачи."""
s1, s2 = input(), input()

str_s1 = [ord(i) for i in s1.lower() if i.isalpha()]
str_s2 = [ord(i) for i in s2.lower() if i.isalpha()]

cnt1 = 0
cnt2 = 0

for i in range(len(str_s1)):
    cnt1 += str_s1[i]

for i in range(len(str_s2)):
    cnt2 += str_s2[i]

if cnt1 == cnt2:
    print("YES")
else:
    print("NO")

# Второй способ решения - взято из форума решения
st_1 = [i.lower() for i in input() if i.isalpha()]
st_2 = [j.lower() for j in input() if j.isalpha()]

print("YES" if st_1 == st_2 else "NO")
