def balanced_brackets(my_string: str):
    cleared_string = ""
    for i in my_string:
        if i in "()[]":
            cleared_string += i
    if len(cleared_string) == 0:
        return True
    if cleared_string[0] not in "[]()" and cleared_string[-1] not in "[]()":
        return balanced_brackets(cleared_string[1:-1])
    if cleared_string[0] == '(' and cleared_string[-1] == ')':
        return balanced_brackets(cleared_string[1:-1])
    elif cleared_string[0] == '[' and cleared_string[-1] == ']':
        return balanced_brackets(cleared_string[1:-1])

    if not (cleared_string[0] == '(' and cleared_string[-1] == ')'):
        return False
    elif not (cleared_string[0] == '[' and cleared_string[-1] == ']'):
        return False
    # remove first and last character
    return balanced_brackets(cleared_string[1:-1])


ok = balanced_brackets("([([])])")
print(ok)

ok = balanced_brackets("(python version [3.7]) please use this one!")
print(ok)

# this is no good, the closing bracket doesn't match
ok = balanced_brackets("(()]")
print(ok)

# different types of brackets are mismatched
ok = balanced_brackets("([bad egg)]")
print(ok)
