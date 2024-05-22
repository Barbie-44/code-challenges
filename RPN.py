"""
Problem Statement

Reverse Polish Notation: It is a mathematical notation in which operators follow their operands. Watch this video for more detailed explanation.

For example, given 3 4 + 2 * 1 +, the operation would be: (3+4) *2 +1 = 15. 
Whenever we see a number, we push to stack and if an operator, pop and perform the calculation and push it back to stack.

Example
Example 1

Input: "3 4 + 2 * 1 +"
Output: 15

Example 2

Input: "3 5 + 7 2 - *"
Output: 40

"""

"""
GOAL:
    Return the result of the operations by stacking the operands
-----------------------------------------------------------------
THIKING:
    Recibes un str
    Es necesario analizar si se trata de un número o de un operador
    Si se trata de un número, lo saltas y pasas al siguiente elemento
    Si el siguiente elemento es un operador, se aplica la operación (+,-,*,/) a los dos últimos dígitos antes de su aparición
    El resultado de la operación se 'adhiere' al resultado final
-----------------------------------------------------------------
CODE APPROACH:
    1. Define a function RNP that accepts an str as arg
    2. Transform the str to a list with split() method, using whitespaces as dividers
    3. Iterate through each element of the list
    4. Make a condition to check whether the item is an int number or an operator
    5. If the item is a number, don't do anything
    6. If the item is an operator, get it's index and apply the operator to the previous two elements in the list
    7. Save the result in a variable.
    8. Repeat the process
    9. Return the result.-
"""


def get_RNP_result(str_arg: str):
    original_list = str_arg.split()
    print("ORIGINAL_LIST: ", original_list)
    result = []

    for item in original_list:
        if item not in ["*", "/", "+", "-"]:
            result.append(item)
        else:
            second_operand = result.pop()
            first_operand = result.pop()
            print("IS STRING? ", first_operand + item + second_operand)
            curr_result = eval(first_operand + item + second_operand)
            print("CURRENT_RESULT: ", curr_result, type(curr_result))
            result.append(str(curr_result))
    print("RESULT: ", result[-1])
    return result[-1]


# example_1 = "3 4 + 2 * 1 +"
# get_RNP_result(example_1)

example_2 = "3 5 + 7 2 - *"
get_RNP_result(example_2)

"""
Challenge completed in: 53min
"""
