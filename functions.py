# 1. Գրել ֆունկցիա, որը կվերդարձնի ստացած արգումենտներից թվերի
# գումարը։

# def count_func(*args):
#     count = 0
#     for el in args:
#         count += el
#     return count
#
# print(count_func(1,5,3,6))

# 2. Գրել ֆունկցիա, որը կվերդարձնի ստացած արգումենտներից տողերի
# քանակը։

# def count_lines(text):
#     lines = text.split("\n")
#     return len(lines)
# print(count_lines("hello\nworld\nejhr"))


# 3. Գրել ֆունկցիա, որը կվերադարձնի ստասած արգումենտների միջին
# թվաբանականը։
# def average(*args):
#     res = sum(args) / len(args)
#     return res
# print(average(1,2,3))

# 4. Գրել ֆունկցիա, որը կստանա 2 արգումենտ և կվերադարձնի այդ
# արգումենտերի հետ կատարած մաթեմատիկական գործողությունների
# արդյունքները

# def math_func(num1,num2,operator="+"):
#     if operator == "+":
#         return num1 + num2
#     elif operator == "-":
#         return num1 - num2
#     elif operator == "*":
#         return num1 * num2
#     elif operator == "/":
#         return num1 / num2
#     else:
#         return "operator is not defined"
#
# print(math_func(5,5,"*"))

# 5. Գրել ֆունկցիա, որը որպես արգումենտ կստանա տողը և կվերադարձնի
# այն դարձված ամբողջությամբ մեծատառ (upper ֆունկցիան օգտագործել չի
# կարելի)։
#
# def my_upper(text):
#     for el in text:
#         if "a" <= el <= "z":
#             el_up = ord(el) - 32
#             text = text.replace(el, chr(el_up))
#             # print(chr(el))
#         # if el.isalpha():
#         #
#         else:
#             continue
#     return text
#
#
# print(my_upper("helHPl__l1"))

# 6. Գրել ֆունկցիա, որը որպես արգումենտ կստանա տողը և կվերադարձնի
# այն դարձված ամբողջությամբ փոքրատառ (lower ֆունկցիան օգտագործել չի
# կարելի)։

# def my_lower(text):
#     for el in text:
#         if "A" <= el <= "Z":
#             el_low = ord(el) + 32
#             text = text.replace(el, chr(el_low))
#         else:
#             continue
#     return text
#
#
# print(my_lower("helHPl__l1ZF"))

# 7. Գրել ֆունկցիա, որը որպես արգումենտ կստանա տողը և կվերադարձնի
# այն դարձված բոլոր բառերի առաջին տառերը մեծատառ (title ֆունկցիան
# օգտագործել չի կարելի)։

# def my_title(text):
#     text = text.split(" ")
#     text = [el[0].upper() + el[1::] for el in text ]
#     return " ".join(text)
# print(my_title("heh jdsf"))

# 8. Գրել ֆունկցիա, որը որպես արգումենտ կստանա տողը և կվերադարձնի
# այն դարձված հակառակ։
# def my_revers(text):
#      return  text[::-1]
# print(my_revers("hello workd"))


# 9. Գրել ֆունկցիա, որը որպես արգումենտ կստանա տող և 2 թիվ։ Այն պետք է
# վերադարձնի տրված 2 թվերի արանքում եղած ենթատողը։

# def cut_sentence(text, start=0, end=0):
#     text = text[start:end:]
#     return text
#
#
# print(cut_sentence("hellooowosofsd fhsjdk", 1, 7))

# 10. Գրել ֆունկցիա, որը կվերադարձնի նախադասության ամենաերկար
# բառը։

# def longest_word(sentence):
#     tmp = ""
#     for word in sentence.split():
#         if len(word) > len(tmp):
#             tmp = word
#         else:
#             continue
#     return tmp
# print(longest_word("hel hello world hj k"))

# 11. Գրել ֆունկցիա, որը կվերադարձնի նախադասության ամենաշատ
# օգտագործված տառը։

# def most_used_letter(sentence):
#     md = {}
#
#     for el in sentence:
#         if el.isalpha():
#
#             if el in md:
#                 md[el] += 1
#             else:
#                 md[el] = 1
#         else:
#             continue
#         max_count = max(md.values())
#         max_us_letters = [f"{k} it was used {v} times"
#         for k,v in md.items() if v == max_count]
#
#
#     return max_us_letters
#
#
# print(most_used_letter("hhhрррррellojf"))

# 12. Գրել ֆունկցիա, որը կվերադարձնի նախադասության ամենաերկար
# բառում ամենաշատ օգտագործված տառը։

# def count_func(sentence):
#
#     tmp = ""
#     for word in sentence.split():
#         if len(word) > len(tmp):
#             tmp = word
#         else:
#             continue
#     md = {}
#
#     for el in tmp:
#         if el.isalpha():
#             if el in md:
#                 md[el] += 1
#             else:
#                 md[el] = 1
#         max_count = max(md.values())
#         max_us_letters = [f"{k} it was used {v} times"
#             for k,v in md.items() if v == max_count]
#     return max_us_letters
#
# print(count_func("this is my happy day"))


