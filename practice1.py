def operation(op, num1, num2):
    if op == 'add':
        result = num1 + num2
        return result
    elif op=='division':
        result = num1 / num2
        return result
    else:
        print("enter right details.")
print(operation('add',1,2))
print(operation('division',2,3))