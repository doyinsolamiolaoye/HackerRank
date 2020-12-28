# def factorial(n):
#     if n <= 1 :
#         result = 1
#     else:
#         result = n
#         i = 1
#         while i < n:
#             result *= i
#             i += 1
#     return result

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n* factorial(n - 1)

	
	
print(factorial(int(input())))