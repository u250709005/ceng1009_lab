# def is_odd(n):
#     return n % 2 == 1
#
# print(is_odd(13))

# def is_leapyear(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False
#
# print(is_leapyear(2025))

# def print_triangle_number(n):
#     total = 0
#     for i in range(1, n + 1):
#         total = total + i
#         print(i, total)
#
# print_triangle_number(5)

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#         return True
#
# print(is_prime(29))

# def reverse_string(s):
#     result = ""
#     for ch in s:
#         result = ch + result
#     return result
#
# print(reverse_string("cristiano ronaldo"))
#
# def reverse_string(s):
#     return s[::-1]
# print(reverse_string("lionel messi"))

# def remove_all_occurences(sub, s):
#     return s.replace(sub, "")
#
# print(remove_all_occurences("ll", "hello world"))

# def substitute(message, key):
#     alphabet = "abcçdefghiıjklmnopqrstuüvwxyz"
#     result = ""
#     for ch in message:
#         index = alphabet.find(ch.lower())
#         if index == -1:
#             result += ch
#         elif ch.isupper():
#             result = result + key[index].upper()
#         else:
#             result = result + key[index].lower()
#     return result
#
# key = "qtgmsjeklrtyuıfgbnvmdsaqwerty"
# print(substitute("hello world", key))

def remove_dups(s):
    result = ""
    for ch in s:
        if ch.lower() not in result.lower():
            result = result + ch
    return result
print(remove_dups("hello world"))


















