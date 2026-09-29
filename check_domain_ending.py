# На вход программе подаётся строка текста. Напишите программу, которая подсчитывает количество цифр в данной строке.
#www.google.com
# Формат входных данных
# На вход программе подаётся строка текста.
#
# Формат выходных данных
# Программа должна вывести количество цифр в данной строке.

s = input()
counter = 0
nums = '0123456789'
for _ in s:
    if _ in nums:
        counter += 1
print(counter)

site = input()
print('YES' if site.endswith('.ru') or site.endswith('.com') else 'NO')

# print(if (site.endswith('.ru') == True or site.endswith('.com') == True) == True 'YES' else 'NO')
