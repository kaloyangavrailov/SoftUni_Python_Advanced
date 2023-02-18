from collections import deque

colors_mismatched = deque(x for x in input().split())

main_colors_ex = {"red", "yellow", "blue"}

secondary_colors_ex = {"orange": {'red', 'yellow'},
                       "purple": {'red', 'blue'},
                       "green": {'yellow', 'blue'}
}

found_colors = []


while colors_mismatched:
    if len(colors_mismatched) > 1:
        for color in (colors_mismatched[0]+colors_mismatched[-1], colors_mismatched[-1]+colors_mismatched[0]):
            if color in main_colors_ex or color in secondary_colors_ex.keys():
                if color in main_colors_ex:
                    found_colors.append(color)
                elif color in secondary_colors_ex.keys():
                    found_colors.append(color)
                colors_mismatched.pop()
                colors_mismatched.popleft()
                break
        else:
            substring_a = colors_mismatched.popleft()
            substring_b = colors_mismatched.pop()
            substring_a = substring_a[:len(substring_a) - 1:]
            substring_b = substring_b[:len(substring_b) - 1:]
            if len(colors_mismatched) % 2 == 1:
                colors_mismatched.insert((len(colors_mismatched) // 2) + 1, substring_a)
                colors_mismatched.insert((len(colors_mismatched) // 2) + 1, substring_b)
            else:
                colors_mismatched.insert((len(colors_mismatched) // 2), substring_a)
                colors_mismatched.insert((len(colors_mismatched) // 2), substring_b)


    else:
        if len(colors_mismatched[0]) > 2:
            color = colors_mismatched.pop()
            if color in main_colors_ex or color in secondary_colors_ex.keys():
                if color in main_colors_ex:
                    found_colors.append(color)
                elif color in secondary_colors_ex.keys():
                    found_colors.append(color)
                colors_mismatched.pop()
            else:
                color = color[::len(color)-1]
                colors_mismatched.append(color)
        else:
            colors_mismatched.pop()
for color in found_colors:
    if color in secondary_colors_ex.keys():
        if secondary_colors_ex[color].issubset(set(found_colors)):
            continue
        else:
            found_colors.remove(color)

print(found_colors)