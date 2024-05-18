
# Практическое задание по уроку "Строки и индексация строк"


#  1. Задача «Часть от целого».

sent = ('Сейчас на Земле появился новый вид роботов. '
       'Раньше их называли „железной оравой “, '
       'но это не очень точное определение')

print(sent[:44])



#  2. Задача «Палиндром».

word_1 = 'радар'
word_2 = 'норма'
pal_1 = word_1[::-1]
pal_2 = word_2[::-1]
check_1 = (word_1 == pal_1)
check_2 = (word_2 == pal_2)

print(pal_1, pal_2)
print(check_1, check_2)



#  3.  Задача «Равные части».

word = 'кенгуру'
l_part = word[:4]
r_part = word[4:]

print(r_part + l_part)



#  4.  Задача «Четные и нечетные».

string = 'нейропрограммирование'
even = string[::2]   # Чётные символы
odd = string[1::2]   # Нечётные символы

print(even)
print(odd)



#  5.  Задача «Обратный порядок».

word = 'нейропластичность'
word_len = len(word)              # вычисляем длину слова для удобства работы
word_abbrev = word[1:16]
word_invert = word_abbrev[::-1]

print(word_len)
print(word_invert)













