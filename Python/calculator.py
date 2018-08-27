#calculator
input1 = float(input("first number: "))
input2 = float(input("second number: "))
operationDict = {"sum" : (lambda num1, num2:num1+num2), "difference" : (lambda num1, num2:num1-num2), "product" : (lambda num1, num2:num1*num2), "quotient" : (lambda num1, num2:num1/num2), "modulo":(lambda num1, num2:num1%num2), "exponential":(lambda num1, num2:num1**num2)}
for operation in operationDict: #['sum', 'difference', 'product', 'quotient', 'modulo', 'exponential']:
    print(operation + ": " + str(operationDict[operation](input1, input2)))
