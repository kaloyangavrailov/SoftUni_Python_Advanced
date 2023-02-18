def rectangle(l, w):

    def area(l, w):
        return l * w

    def perimeter(l, w):
        return 2*(l + w)

    if type(l) == int and type(w) == int:
        return f"""Rectangle area: {area(l, w)}
Rectangle perimeter: {perimeter(l, w)}"""
    else:
        return f"Enter valid values!"


print(rectangle(2, 10))
print(rectangle('2', 10))
