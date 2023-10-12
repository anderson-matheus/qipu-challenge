from ais_web import AisWeb

def main():
    aerodrome_code = input('Informe o código do aeródromo: ')
    message = None

    if not aerodrome_code:
        message = '\nCódigo não informado, tente novamente\n'
        print(message)
        return message

    try:    
        ais_web = AisWeb(aerodrome_code)
        result = ais_web.get_data()
        print(result)
        return result
    except:
        message = '\nNão foi possível coletar os dados, tente novamente\n'
        print(message)
        return message

if __name__ == '__main__':
    main()