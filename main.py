# Autor: Micael Muniz de Oliveira Santos
# Componente Curricular: Algoritmos I
# Concluído em: 08/04/2022
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

'''
ITENS:
[1] açúcar                          1kg
[2] arroz                           4kg
[3] café                            2kg
[4] extrato de tomate               2un
[5] macarrão                        3un
[6] bolacha                         1pct
[7] óleo                            1,000cm³
[8] farinha de trigo                1kg
[9] feijão                          4kg
[10] sal                            1kg
[11] outros                         n/a
'''

# ciclo de repetição
process = "S"
app_running = "1"

# variaveis contadoras
sugar_pf = 0
sugar_pj = 0
rice_pf = 0
rice_pj = 0
coffee_pf = 0
coffee_pj = 0
tomato_pf = 0
tomato_pj = 0
pasta_pf = 0
pasta_pj = 0
biscuit_pf = 0
biscuit_pj = 0
oil_pf = 0
oil_pj = 0
flour_pf = 0
flour_pj = 0
bean_pf = 0
bean_pj = 0
salt_pf = 0
salt_pj = 0
others_pf = 0
others_pj = 0
times = 0

# variaveis pacotes
pack_sugar = 0
pack_rice = 0
pack_coffee = 0
pack_tomato = 0
pack_pasta = 0
pack_biscuit = 0
pack_oil = 0
pack_flour = 0
pack_bean = 0
pack_salt = 0
pack_others = 0
cesta_with_others = 0
cesta_without_others = 0
sugar = 0
rice = 0
coffee = 0
tomato = 0
pasta = 0
biscuit = 0
oil = 0
flour = 0
bean = 0
salt = 0
others = 0
cesta = 0


# FUNÇÃO QUE IMPRIME O RELATORIO (seja no final ou a qualquer momento solicitado)
def showReport():
    # times representa quantas vezes o programa contabilizou doações
    if times == 0:
        print(f"\n\n\n=================================================\n"
              f"{'NENHUM ITEM FOI RECEBIDO':^49}\n"
              f"=================================================\n")
    else:
        # Total de cada item recebido;
        print(f"\n\n\n=================================================\n"
              f"{'TOTAL DE CADA ITEM RECEBIDO:':^49}\n"
              f"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
              f"Açúcar: {sugar_pf + sugar_pj:.>39}kg\n"
              f"Arroz: {rice_pf + rice_pj:.>40}kg\n"
              f"Café: {coffee_pf + coffee_pj:.>41}kg\n"
              f"Extrato de tomate: {tomato_pf + tomato_pj:.>28}un\n"
              f"Pacotes de macarrão: {pasta_pf + pasta_pj:.>26}un\n"
              f"Pacotes de bolacha: {biscuit_pf + biscuit_pj:.>27}un\n"
              f"Óleo: {oil_pf + oil_pj:.>41}L\n"
              f"Farinha de trigo: {flour_pf + flour_pj:.>29}kg\n"
              f"Feijão: {bean_pf + bean_pj:.>39}kg\n"
              f"Sal: {salt_pf + salt_pj:.>42}kg\n"
              f"Outros: {others_pf + others_pj:.>39}\n"
              f"=================================================")

        # Total de itens (independente do tipo) doados por pessoas físicas e por pessoas jurídicas;
        print(f"\n=================================================\n"
              f"{'TOTAL DE ITENS POR PF E PJ:':^49}\n"
              f"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
              f"Total doado por Pessoas Fisicas: {rice_pf + coffee_pf + sugar_pf + tomato_pf + pasta_pf + biscuit_pf + oil_pf + flour_pf + bean_pf + salt_pf + others_pf}\n"
              f"Total doado por Pessoas Juridicas: {rice_pj + coffee_pj + sugar_pj + tomato_pj + pasta_pj + biscuit_pj + oil_pj + flour_pj + bean_pj + salt_pj + others_pj}\n"
              f"=================================================")

        # Quantas cestas básicas poderão ser formadas;
        print(f"\n=================================================\n"
              f"{f'TOTAL DE CESTAS BASICAS FORMADAS: {cesta}':^49}")
        print("================================================\n")

        # Quantas cestas básicas receberão um item extra (outros);
        print(f"\n=================================================\n"
              f"{f'TOTAL DE CESTAS BASICAS COM ITEM EXTRA: {cesta_with_others}':^49}")
        print("================================================\n")

        # Quantas cestas básicas não receberão um item extra (outros);
        print(f"\n=================================================\n"
              f"{f'TOTAL DE CESTAS BASICAS SEM ITEM EXTRA: {cesta_without_others}':^49}")
        print("================================================\n")

        # Após a montagem das cestas, quais foram os itens que sobraram.
        print(f"=================================================\n"
              f"{'TOTAL DE CADA ITEM SOBRADO:':^49}\n"
              f"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
              f"Açúcar: {pack_sugar*1+sugar:.>39}kg\n"
              f"Arroz: {pack_rice*4+rice:.>40}kg\n"
              f"Café: {pack_coffee*2+coffee:.>41}kg\n"
              f"Extrato de tomate: {pack_tomato*2+tomato:.>28}un\n"
              f"Pacotes de macarrão: {pack_pasta*3+pasta:.>26}un\n"
              f"Pacotes de bolacha: {pack_biscuit*1+biscuit:.>27}un\n"
              f"Óleo: {pack_oil*1+oil:.>41}L\n"
              f"Farinha de trigo: {pack_flour*1+flour:.>29}kg\n"
              f"Feijão: {pack_bean*4+bean:.>39}kg\n"
              f"Sal: {pack_salt*1+salt:.>42}kg\n"
              f"Outros: {pack_others+others-cesta_with_others:.>39}\n"
              f"=================================================")


# ciclo principal, ele encerra o programa
while app_running == "1":
    username = input("\n\nSeja bem vindo, como se chama?\n").strip().capitalize()

    pf_pj_repeat = True
    # VALIDAÇÃO: até o usuário escolher APENAS uma das opções (existem varias iguais a está ao longo do programa)
    while pf_pj_repeat:
        pf_pj = input(f"\n=================================================\n"
                      f"{f'{username}, sua doação será como Pessoa Física ou Pessoa Juridica?':^49}\n"
                      f"caso queira ver o relatorio, basta selecionar a opção 3\n"
                      f"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
                      f"[1] Pessoa Física\n"
                      f"[2] Pessoa Juridica\n"
                      f"[3] Exibir Relatorio\n"
                      f"=================================================\n")
        if pf_pj == "3":
            showReport()
        if pf_pj == "1" or pf_pj == "2":
            pf_pj_repeat = False

    # ciclo secundário, ele é repetido para cada doação
    while process == "S":
        # menu de doações
        print(f"\n=================================================\n"
              f"{f'Seja bem vindo(a) {username}!':^49}")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        main_quest = input("Escolha qual item deseja doar:\n"
                           "[1] Açúcar\n"
                           "[2] Arroz\n"
                           "[3] Café\n"
                           "[4] Extrato de tomate\n"
                           "[5] Macarrão\n"
                           "[6] Bolacha\n"
                           "[7] Óleo\n"
                           "[8] Farinha de trigo\n"
                           "[9] Feijão\n"
                           "[10] Sal\n"
                           "[11] Outros\n"
                           "[0] Cancelar\n"
                           "=================================================\n")

        # 'reset' de algumas validações logo de inicio, pois no final de cada ciclo provavelmente vão estar como True
        verification = False
        ask_process = False

        # começo dos if's para cada opção que o usuario pode selecionar no menu acima
        # Açúcar PESSOA FÍSICA
        if main_quest == "1" and pf_pj == "1":
            while not verification:
                quest = input(f"Digite quantos KG de açúcar deseja doar, {username}: ")
                if quest.isnumeric() and int(quest) > 0:
                    verification = True
                    sugar_pf += int(quest)
                    sugar += int(quest)

        # Açúcar PESSOA JURIDICA
        elif main_quest == "1" and pf_pj == "2":
            while not verification:
                quest = input(f"Digite quantos KG de açucar deseja doar, {username}: ")
                if quest.isnumeric() and int(quest) > 0:
                    verification = True
                    sugar_pj += int(quest)
                    sugar += int(quest)


        # Arroz PESSOA FÍSICA
        elif main_quest == "2" and pf_pj == "1":
            while not verification:
                quest = input(f"Digite quantos KG de arroz deseja doar, {username}: ")
                if quest.isnumeric() and int(quest) > 0:
                    verification = True
                    rice_pf += int(quest)
                    rice += int(quest)

        # Arroz PESSOA JURIDICA
        elif main_quest == "2" and pf_pj == "2":
            while not verification:
                quest = input(f"Digite quantos KG de arroz deseja doar, {username}: ")
                if quest.isnumeric() and int(quest) > 0:
                    verification = True
                    rice_pj += int(quest)
                    rice += int(quest)


        # Café PESSOA FÍSICA
        elif main_quest == "3" and pf_pj == "1":
            while not verification:
                quest = input(f"Digite quantos KG de café deseja doar, {username}: ")
                if quest.isnumeric() and int(quest) > 0:
                    verification = True
                    coffee_pf += int(quest)
                    coffee += int(quest)

        # Café PESSOA JURIDICA
        elif main_quest == "3" and pf_pj == "2":
            while not verification:
                quest = input(f"Digite quantos KG de café deseja doar, {username}: ")
                if quest.isnumeric() and int(quest) > 0:
                    verification = True
                    coffee_pj += int(quest)
                    coffee += int(quest)


        # Extrato de tomate PESSOA FÍSICA
        elif main_quest == "4" and pf_pj == "1":
            while not verification:
                quest = input(f"Digite quantas unidades de extrato de tomate deseja doar, {username}: ")
                if quest.isnumeric() and int(quest) > 0:
                    verification = True
                    tomato_pf += int(quest)
                    tomato += int(quest)

        # Extrato de tomate PESSOA JURIDICA
        elif main_quest == "4" and pf_pj == "2":
            while not verification:
                quest = input(f"Digite quantas unidades de extrato de tomate deseja doar, {username}: ")
                if quest.isnumeric() and int(quest) > 0:
                    verification = True
                    tomato_pj += int(quest)
                    tomato += int(quest)


        # Macarrão PESSOA FÍSICA
        elif main_quest == "5" and pf_pj == "1":
            while not verification:
                quest = input(f"Digite quantos pacotes de macarrão deseja doar, {username}: ")
                if quest.isnumeric() and int(quest) > 0:
                    verification = True
                    pasta_pf += int(quest)
                    pasta += int(quest)

        # Macarrão PESSOA JURIDICA
        elif main_quest == "5" and pf_pj == "2":
            while not verification:
                quest = input(f"Digite quantos pacotes de macarrão deseja doar, {username}: ")
                if quest.isnumeric() and int(quest) > 0:
                    verification = True
                    pasta_pj += int(quest)
                    pasta += int(quest)


        # Bolacha PESSOA FÍSICA
        elif main_quest == "6" and pf_pj == "1":
            while not verification:
                quest = input(f"Digite quantos pacotes de bolacha deseja doar, {username}: ")
                if quest.isnumeric() and int(quest) > 0:
                    verification = True
                    biscuit_pf += int(quest)
                    biscuit += int(quest)

        # Bolacha PESSOA JURIDICA
        elif main_quest == "6" and pf_pj == "2":
            while not verification:
                quest = input(f"Digite quantos pacotes de bolacha deseja doar, {username}: ")
                if quest.isnumeric() and int(quest) > 0:
                    verification = True
                    biscuit_pj += int(quest)
                    biscuit += int(quest)


        # Óleo PESSOA FÍSICA
        elif main_quest == "7" and pf_pj == "1":
            while not verification:
                quest = input(f"Digite quantos litros de óleo deseja doar, {username}: ")
                if quest.isnumeric() and int(quest) > 0:
                    verification = True
                    oil_pf += int(quest)
                    oil += int(quest)

        # Óleo PESSOA JURIDICA
        elif main_quest == "7" and pf_pj == "2":
            while not verification:
                quest = input(f"Digite quantos litros de óleo deseja doar, {username}: ")
                if quest.isnumeric() and int(quest) > 0:
                    verification = True
                    oil_pj += int(quest)
                    oil += int(quest)


        # Farinha de trigo PESSOA FÍSICA
        elif main_quest == "8" and pf_pj == "1":
            while not verification:
                quest = input(f"Digite quantos KG de farinha de trigo deseja doar, {username}: ")
                if quest.isnumeric() and int(quest) > 0:
                    verification = True
                    flour_pf += int(quest)
                    flour += int(quest)

        # Farinha de trigo PESSOA JURIDICA
        elif main_quest == "8" and pf_pj == "2":
            while not verification:
                quest = input(f"Digite quantos KG de farinha de trigo deseja doar, {username}: ")
                if quest.isnumeric() and int(quest) > 0:
                    verification = True
                    flour_pj += int(quest)
                    flour += int(quest)


        # Feijão PESSOA FÍSICA
        elif main_quest == "9" and pf_pj == "1":
            while not verification:
                quest = input(f"Digite quantos KG de feijão deseja doar, {username}: ")
                if quest.isnumeric() and int(quest) > 0:
                    verification = True
                    bean_pf += int(quest)
                    bean += int(quest)

        # Feijão PESSOA JURIDICA
        elif main_quest == "9" and pf_pj == "2":
            while not verification:
                quest = input(f"Digite quantos KG de feijão deseja doar, {username}: ")
                if quest.isnumeric() and int(quest) > 0:
                    verification = True
                    bean_pj += int(quest)
                    bean += int(quest)


        # Sal PESSOA FÍSICA
        elif main_quest == "10" and pf_pj == "1":
            while not verification:
                quest = input(f"Digite quantos KG de sal doar, {username}: ")
                if quest.isnumeric() and int(quest) > 0:
                    verification = True
                    salt_pf += int(quest)
                    salt += int(quest)

        # Sal PESSOA JURIDICA
        elif main_quest == "10" and pf_pj == "2":
            while not verification:
                quest = input(f"Digite quantos KG de sal deseja doar, {username}: ")
                if quest.isnumeric() and int(quest) > 0:
                    verification = True
                    salt_pj += int(quest)
                    salt += int(quest)


        # OUTROS, PESSOA FÍSICA
        elif main_quest == "11" and pf_pj == "1":
            while not verification:
                quest = input(f"Digite quantas unidades de um item não mencionado anteriormente você deseja doar , {username}: ")
                if quest.isnumeric() and int(quest) > 0:
                    verification = True
                    others_pf += int(quest)
                    others += int(quest)

        # OUTROS PESSOA JURIDICA
        elif main_quest == "11" and pf_pj == "2":
            while not verification:  # FIM DOS ITENS QUE POSSUEM VALIDAÇÃO DE INTEIRO
                quest = input(f"Digite quantas unidades de um item não mencionado anteriormente você deseja doar, {username}: ")
                if quest.isnumeric() and int(quest) > 0:
                    verification = True
                    others_pj += int(quest)
                    others += int(quest)
        else:
            print(f"{username}, você não escolheu um item entre 1 e 11, para finalizar responda \"N\" na proxima pergunta! ")

        if verification:
            times += 1

        while not ask_process:
            process = input(f"Deseja fazer outra doação como {username}? (S/N) ").upper()
            if process == "S" or process == "N":
                ask_process = True
                pf_pj_repeat = True
                # como é a mesma pessoa, ele valida o verificador de PF ou PJ com True para não perguntar novamente

    ask_app_running = False
    while not ask_app_running:
        app_running = input(f"\n=================================================\n"
                            f"{f'Como deseja prosseguir, {username}?':^49}\n"
                            f"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
                            f"[1] Fazer logoff como {username} e cadastrar um novo usuário\n"
                            f"[2] Finalizar a execução e exibir o relatorio final\n"
                            f"=================================================\n").upper()
        if app_running == "1" or app_running == "2":
            ask_app_running = True
            process = "S"

    # LOGICA PRINCIPAL DO CODIGO:
    # SEPARADOR DE ITENS - organizando em pacotes
    '''
    ele verifica se existe a quantidade necessaria de X item para uma cesta basica caso tenha, ele move essa informação 
    pra uma variavel pacote com o valor 1, deixando somente as sobras q n foram suficientes.
    eventualmente caso as sobras atinjam o valor necessario, elas passam para a varivel pacote também
    '''
    if sugar >= 1:
        pack_sugar += sugar // 1
        sugar = sugar % 1
    if rice >= 4:
        pack_rice += rice // 4
        rice = rice % 4
    if coffee >= 2:
        pack_coffee += coffee // 2
        coffee = coffee % 2
    if tomato >= 2:
        pack_tomato += tomato // 2
        tomato = tomato % 2
    if pasta >= 3:
        pack_pasta += pasta // 3
        pasta = pasta % 3
    if biscuit >= 1:
        pack_biscuit += biscuit // 1
        biscuit = biscuit % 1
    if oil >= 1:
        pack_oil += oil // 1
        oil = oil % 1
    if flour >= 1:
        pack_flour += flour // 1
        flour = flour % 1
    if bean >= 4:
        pack_bean += bean // 4
        bean = bean % 4
    if salt >= 1:
        pack_salt += salt // 1
        salt = salt % 1

    # SEPARADOR DE ITENS - organizando os pacotes em CESTA BASICA
    '''
    ele verifica se existe 1 pacote de cada item ao menos, se tiver, ele poem todos pacotes em uma lista 
    e pega o menor pacote como limitador, pois o menor pacote vai ser justamente a quantidade de cestas formadas,
    as sobras continuam la, até eventualmente poderem entrar na variavel de cesta também, caso os pacotes não entrem,
    no final eles vão ser multiplicados pelo valor q eles representam (por exemplo: 1 pack de feijão = 4kg) e exibidos
    como sobras, como os pacotes passaram pra dentro da variavel cesta, 
    o valor do pacote limitador (o menor) é subtraído de todos
    '''
    if pack_sugar >= 1 and pack_rice >= 1 and pack_coffee >= 1 and pack_tomato >= 1 and pack_pasta >= 1 and pack_biscuit >= 1 and pack_oil >= 1 and pack_flour >= 1 and pack_bean >= 1 and pack_salt >= 1:
        pack = [pack_sugar, pack_rice, pack_coffee, pack_tomato, pack_pasta, pack_biscuit, pack_oil, pack_flour,
                pack_bean, pack_salt]
        cesta += min(pack)
        pack_sugar -= min(pack)
        pack_rice -= min(pack)
        pack_coffee -= min(pack)
        pack_tomato -= min(pack)
        pack_pasta -= min(pack)
        pack_biscuit -= min(pack)
        pack_oil -= min(pack)
        pack_flour -= min(pack)
        pack_bean -= min(pack)
        pack_salt -= min(pack)

    if others > cesta:
        cesta_with_others = cesta
        cesta_without_others = 0
    if others <= cesta:
        cesta_with_others = others
        cesta_without_others = cesta - cesta_with_others
# FIM DOS CICLOS, O USUARIO ESCOLHEU FINALIZAR A EXECUÇÃO
showReport()
