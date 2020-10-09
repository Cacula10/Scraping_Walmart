def def_cores(msg, cor):
    if cor == 'vermelho':
        print('')
        print("\033[0;31m", msg, "\033[m")
        print('')
    elif cor == 'amarelo':
        print('')
        print("\033[0;32m", msg, "\033[m")
        print('')
    elif cor == 'azul':
        print('')
        print("\033[0;34m", msg, "\033[m")
        print('')
    else:
        print('FAVOR CADASTRAR NOVA COR NA DEF')


