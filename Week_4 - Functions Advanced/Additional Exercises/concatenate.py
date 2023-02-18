def concatenate(*args, **kwargs):
    strng = ''.join(args)
    for key, value in kwargs.items():
        if key in strng:
            strng = strng.replace(key, value)

    return strng



print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))