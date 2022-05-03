import re


class Calculator:
    """Supported input format: '1+1' or '(1+1)-1', etc..."""
    def calc(self, values):
        variable_value = 0
        result = 0
        stack = []
        sign = 1
        for value in values:
            if value.isdigit():
                variable_value = int(value) + 10*variable_value
            elif value in ['+', '-']:
                result += sign * variable_value
                variable_value = 0
                if value == '+':
                    sign = 1
                else:
                    sign = -1
            elif value == '(':
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif value == ')':
                result += variable_value * sign
                result *= stack.pop()
                result += stack.pop()
                variable_value = 0
            elif value in ['*', '/', '//']:
                print('Input is invalid :(((')
                break
        return result + variable_value * sign


operation = Calculator()
inp = ''
print("Let's start :-)"
      "\n!!!TO EXIT, type 'exit'!!!")
command_for_exit = 'exit'
while inp != command_for_exit:
    r = re.search('[A-Za-z]', inp)
    if r is not None:
        print('Value cannot be empty')
    inp = input('> ')
    res = operation.calc(inp)
    print(res)
print('Exit...')
