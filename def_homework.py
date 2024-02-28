# def my_replace(text, old_value="", new_value=""):
#     result = ""
#     for el in range(len(text)):
#         if text[el] != old_value:
#             result += text[el]
#         else:
#             result += new_value
#     return result
#
#
# print(my_replace("Hello world", "l", "p"))

# def my_split(input_text, delimiter=" "):
#     res = []
#     tmp = ""
#     for el in input_text:
#         if el != delimiter:
#             tmp += el
#         else:
#             res.append(tmp)
#             tmp = ""
#     if tmp:
#         res.append(tmp)
#     return res
#
#
# print(my_split("hello world"))

# def my_upper(input_text):
#     tmp = ""
#     for el in input_text:
#         if el.isalpha():
#             if el.lower():
#                 tmp += el.upper()
#         else:
#             tmp += el
#     return tmp
#
#
# print(my_upper("HellooooO WOrld -="))

# def my_lower(inp_text):
#     tmp = ""
#     for el in inp_text:
#         if el.isalpha():
#             if el.upper():
#                 tmp += el.lower()
#         else:
#             tmp += el
#     return tmp
#
#
# print(my_lower("HellooooO WOrld -="))

#
# def my_join(enter_list, delipetrs=" "):
#     tmp = ""
#     for el in enter_list:
#         tmp += el + delipetrs
#     return tmp
#
#
# test_list = ["Hello", "you", "are", "big", "human"]
# print(my_join(test_list))

# def my_startswith(inp_text, sample=""):
#     len_sample = len(sample) + 1
#     if sample in inp_text[:len_sample]:
#         print("yes")
#         return sample
#     else:
#         print("no surch value")
#
#
# test_text = "hellooo"
# print(my_startswith(test_text, "hel"))

# def my_swapcase(inp_text):
#     tmp = ""
#     for el in inp_text:
#         if el.isalpha():
#             if el == el.lower():
#                 tmp += el.upper()
#             else:
#                 tmp += el.lower()
#         else:
#             tmp += el
#     return tmp
#
#
# print(my_swapcase("hElojf,.  "))

# def my_factorial(x):
#     if x == 0:
#         return 1
#     else:
#         res = 1
#         for i in range(1, x + 1):
#             res *= i
#             print(i)
#     return res
#
# 
# print(my_factorial(3))
