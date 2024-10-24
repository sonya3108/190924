# 1
def count_brackets(s):
    brackets = {'(': 0, ')': 0, '[': 0, ']': 0, '{': 0, '}': 0}

    for char in s:
        if char in brackets:
            brackets[char] += 1

    return {'open brackets': brackets['('] + brackets['['] + brackets['{'],
            'closed brackets': brackets[')'] + brackets[']'] + brackets['}']}

string = "([]{})"
result = count_brackets(string)
print(result)


# 2

def is_balanced(s):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if not stack or bracket_map[char] != stack.pop():
                return False

    return not stack


string = "{}{}{}()()()[({})]"
result = is_balanced(string)
print(result)

# 3
def is_balanced_in_text(s):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if not stack or bracket_map[char] != stack.pop():
                return False

    return not stack


string = "Some text with brackets [] and {} and parentheses (test)."
result = is_balanced_in_text(string)
print(result)





