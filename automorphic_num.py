def is_automorphic(n):
    return str(n**2).endswith(str(n))

num = int(input())
if is_automorphic(num):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
