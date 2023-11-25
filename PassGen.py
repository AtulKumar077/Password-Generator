import string
import random

if __name__ == "__main__":
    str1 = string.ascii_lowercase
    str2 = string.ascii_uppercase
    str3 = string.digits
    str4 = string.punctuation
    plen = int(input("Enter password length: "))
    s = []
    s.extend(list(str1))
    s.extend(list(str2))
    s.extend(list(str3))
    s.extend(list(str4))
    print("Password: ")
    print("".join(random.sample(s, plen)))
