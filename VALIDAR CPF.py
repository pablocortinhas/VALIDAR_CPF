while True:
    cpf_user = input('Informe o CPF que deseja validar: ')
    nove_dgt = cpf_user[:9]

    # VERIFICA PRIMEIRO DIGITO
    cont_1 = 10
    resultado_1 = 0

    for digito in nove_dgt:
        resultado_1 += int(digito) * cont_1
        cont_1 -= 1
    digito_1 = (resultado_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    # VERIFICA SEGUNDO DIGITO
    dez_dgt = nove_dgt + str(digito_1)
    cont_2 = 11
    resultado_2 = 0

    for digito in dez_dgt:
        resultado_2 += int(digito) * cont_2
        cont_2 -= 1
    digito_2 = (resultado_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_verif = f'{nove_dgt}{digito_1}{digito_2}'
    if cpf_user == cpf_verif:
        print(f'O CPF: {cpf_user} é válido\n')
    else:
        print('CPF inválido\n')