# txt = str(input("Matin kiriting:"))
# arr = txt.split(" ")
# same_words = ''
# checker_word_index = 0
# for i in arr:
#     if arr.count(arr[checker_word_index]) >=2:
#         same_words=arr[checker_word_index]
#         break
#     else:
#         checker_word_index+=1
# print(same_words if same_words else "takrorlangan so'z yo'q")

# txt = input("Matn kiriting:")
# arr = txt.split(" ")
# checker_word_index = arr[0]
# word_len = True
# for i in arr:
#     if len(i) > len(checker_word_index):
#         checker_word_index = i
#         word_len = False
#
# if word_len:
#     print("barcha so'zlarning uzunligi bir xil")
# else:
#     print(checker_word_index)

# txt = input("Matin kiriting:")
# arr = txt.split(" ")
# words = 0
#
# words_len= len("")
# for i in arr:
#     words += 1
#     print(f'Sozlar uzunligi:{len(i)}')
# print(f"So'zlar soni: {words}ta")

# txt = "hello world"
# arr = txt.split(" ")
# arr1 = ""
# for i in arr:
#     arr1 += f"{i[::-1]} "
# print(arr1)


# matn = input("Matnni kiriting: ")
#
# sozlar = matn.split()
# almashtirilgan_matn = ""
#
# for soz in sozlar:
#     if len(soz) > 1:
#         almashtirilgan_sozi = soz[-1] + soz[1:-1] + soz[0]
#     else:
#         almashtirilgan_sozi = soz
#     almashtirilgan_matn += almashtirilgan_sozi + " "
#
# print("Almashtirilgan natija:", almashtirilgan_matn)

# 2 - masala: Berilgan satrdagi har bir so'zning birinchi va oxirgi harfini almashtiring.
# Masalan, "hello world" uchun natija "oellh dorlw" bo'lishi kerak.

# txt = input("Matin kiriting:")
# arr = txt.split(" ")
# changed_words = ""
# for i in arr:
#     if len(i)>1:
#         changing_word = i[-1]+i[1:-1]+i[0]
#     else:
#         changing_word=i
#     changed_words+=changing_word+" "
# print(f"Almashgan matin: {changed_words}" )

# 3 - masala: Berilgan satrdan barcha belgilarni (@,#,$,%,^,& kabi) o'chirib, bar bir belgining tartib raqamini
# qo'ying yani:--- "h@ll@ wo#ld" >>> "h1ll2 wo3ld"

# txt = input("Matinni kiriting: ")
# signs = "!@#$%^&"
# arr2 = signs.split()
# arr = txt.split(" ")
# changed_words = ""
# for i in arr:
#     for a in arr2:
#         if i == a:
#             changing_words= a=i.index()
#         else:
#             changing_words=i
#             changed_words+changing_words+" "
# print(changed_words)


# Foydalanuvchidan bir son olish va uni kvadratini chop etish.
# number = int(input("enter a number:  "))
# print(number*number)

# 2 - Biror matnni foydalanuvchidan olish va uni 5 marta takrorlash.
# txt = input("matn kirit:")
# for i in range(5):
#     print(txt)

# 3 - Foydalanuvchidan bir son olish va agar u musbat bo'lsa, "Musbat" deb, aks holda "Manfiy" deb chop etish.
# a = int(input("enter anum:"))
# if a <0:
#     print("manfiy")
# else:
#     print("musbat")

# 4 - Foydalanuvchidan bir son olish va u juft bo'lsa, "Juft", toq bo'lsa, "Toq" deb chop etish.
# num = int(input("Enter a number:"))
# if num %2 == 0:
#     print("Even")
# else:
#     print("Odd")

# 5 - 1 dan 20 gacha bo'lgan juft sonlarni chop etish (for loop ammo if yordamisiz)
# for i  in  range(0,21,2):
#     print(i)


# 6 - Foydalanuvchidan bir matn olish va har bir harfini yangi qatorda chop etish.
# txt = input("matn kirit:")
# for i in txt:
#     print(i)

# 7 - Foydalanuvchidan ikki son olish va ulardan kattasini chop etish.
# a=int(input("enter a num:"))
# b=int(input("enter another num:"))
# if a>b:
#     print("a is greater")
# elif b>a:
#     print("b is greater")
# else:
#     print("equal")

# 8 - Foydalanuvchidan bir so'z olish va agar u "Python" so'zi bilan bir xil bo'lsa,
# "To'g'ri javob!" deb, aks holda "Xato javob" deb chop etish.

# print("bu qaysi dastur")
# txt = input().lower()
# if txt == "python":
#     print("To'gri")
# else:
#     print("xato")

# 9 - Foydalanuvchidan bir son olish va u 10 dan kichik bo'lsa, "Kichik", aks holda "Katta" yoki "teng" deb chop etish.
# a=int(input("enter a num:"))
#
# if a>10:
#     print("a is greater")
# elif 10>a:
#     print("b is greater")
# else:
#     print("equal")

# 10 - 5 dan 15 gacha bo'lgan sonlarni chop etish, lekin 10 ga yetganda, "O'n" deb chop etish (for loop va if yordamida).
# num =  5,6,7,8,9,10,11,12,13,14,15
# print(num)
# for i in num:
#     if i==10:
#         print("o'n")
#     else:
#         print(i)

# 11 - Foydalanuvchidan bir matn olish va uning ichidagi barcha "a" harflarini "o" harfi bilan almashtirish.
# txt = input()
# txt2 = txt.replace("a","o")
# print(txt2)

# 12 - Foydalanuvchidan 3 ta son olish va ulardan eng kichigini chop etish.
# a=int(input("enter a num:"))
# b=int(input("enter another num:"))
# c=int(input("enter another num:"))
# if a>b:
#     print(a)
# elif c<a:
#     print(a)
# elif a<b:
#     print(b)
# elif c<b:
#     print(b)
# elif a<c:
#     print(c)
# elif b<c:
#     print(c)
# else:
#     print("equal")

# 13 - Foydalanuvchidan bir son olish va u 5 yoki 7 ga bo'linadigan bo'lsa,
# "Bo'linadi", aks holda "Bo'linmaydi" deb chop etish.
# num = int(input("enter a num:"))
# if num % 5  == 0:
#     print("bolinadi")
# elif num % 7 ==0:
#     print("bolinadi")
# else:
#     print("bolinmaydi")

# 14 - Foydalanuvchidan bir jumla oling va har bir so'zning bosh harfini katta harfga o'zgartiring.
# a=input()
# arr = a.split()
# for i in arr:
#     print(i.capitalize())

# 15 - Foydalanuvchidan bir qator so'zlar oling (masalan, vergul bilan ajratilgan)
# va ular orasidan palindrom so'zlarni topib, chop eting.
# user_input = input("So'z kiriting kiriting: ")
# words = user_input.split(", ")
# palindromes = []
# for word in words:
#     if word == word[::-1]:
#         palindromes.append(word)
# print("Palindrom so'zlar:")
# for palindrome in palindromes:
#     print(palindrome)
