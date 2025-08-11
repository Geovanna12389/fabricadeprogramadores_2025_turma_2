'''
try:
    divisão = 10/0
    print(divisão)
except:
    print(''não foi possível realizar essa operação!'')
'''   
def divide(x,y):
    try:
        resultado = x/y
    except ZeroDivisionError:
        print("por favor, não utilize zeros!")
    except:
        print("\033[9lm algo deu errado...")
    else:
        print(f"seu resultado é; {resultado}")
    finally:
        print("\033[92m vamos de novo?")
divide(13,0)