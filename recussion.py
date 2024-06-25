# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)

# x=factorial(6)
# print(x)

# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# for i in range(10):
#     print(fibonacci(i))


# def sum_list(n):
#     if not n:
#         return 0
#     else:
#         return n[0] + sum_list(n[1:])

# numbers = [1, 2, 3, 4, 5]
# print(sum_list(numbers))


# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     else:
#         return s[-1] + reverse_string(s[:-1])

# s = "hello"
# print(reverse_string(s))


# def power(a,b):
#     if exp == 0:
#         return 1
#     else:
#         return a * power(a,b- 1)

# print(power(2, 3))



# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)

# print(gcd(48, 18))

