# - Deve receber 3 parametros (operation, num1, num2)
# - Validar os parametros e todos devem ser validos, do contrario retornaremos uma 
# excecao com a mensagem do erro
# - Deve retornar o resultado da operaao quando os parametros forem validos

def calculator(operation, num1, num2):

    validate(operation, num1, num2)

    if operation == 'add':
        return num1 + num2
    elif operation == 'sub':
        return num1 - num2
    elif operation == 'mult':
        return num1 * num2
    elif operation == 'div':
        try:
            return num1 / num2
        except ZeroDivisionError as ze:
            raise ZeroDivisionError('Voce nao pode dividir um numero por 0')
    
def validate(operation, num1, num2):
    if operation is None:
        raise Exception('Operacao nao pode ser nulo')
    
    if num1 is None or num2 is None:
        raise Exception('Informe dois numeros validos para realizar a operacao')
    
    if operation not in ['add', 'sub', 'mult', 'div']:
        raise Exception("informe uma operacao valida (add, sub, mult, div)")