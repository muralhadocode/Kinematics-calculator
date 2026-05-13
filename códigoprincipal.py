
import os

print("Bem vindo ao simulador de contas da cinemática!")
print("Aqui você pode calcular diversos parâmetros relacionados aos movimentos estudados na cinemática.")
print("Pequeno aviso, este programa está em desenvolvimento, então nem todas as opções estão disponíveis no momento e devo avisar que todas as unidades são de acordo com o SI (Sistema Internacional de Unidades), então para conseguir realizar as contas com facilidade, por favor, já converta todos os valores para as unidades de medida do SI.")
print("Digite o número da conta que deseja fazer: ")
print("1 - MU - Movimento Uniforme")
print("2 - MUV - Movimento Uniformemente Variado")
print("3 - MRUV - Movimento Retilíneo Uniformemente Variado (Queda Livre)")
print("4 - MCU - Movimento Circular Uniforme")
print("5 - MCUV - Movimento Circular Uniformemente Variado")
op = int(input("Selecione uma das opções acima: "))
sure = True

while sure == True:
    if op == 1:
        os.system('cls')
        print("Selecione qual conta deseja fazer: ")
        print("1 - Tempo (t) em segundos (s)")
        print("2 - Deslocamento (s) em metros (m)")
        print("3 - Velocidade média (v) em metros por segundo (m/s)")
        print("4 - Função horária do espaço")
        print("5 - Voltar para o menu de seleção principal")
        op1 = int(input("Selecione uma das contas acima: "))
        if op1 == 1:
            To = float(input("Digite o valor do tempo inicial (s): "))
            Tn = float(input("Digite o valor do tempo final (s): "))
            Tf = Tn - To
            print(f"O valor de Delta Tempo é: {Tf} s")
        elif op1 == 2:
            So = float(input("Digite o valor do deslocamento inicial (m): "))
            Sn = float(input("Digite o valor do deslocamento final (m): "))
            Sf = Sn - So
            print(f"O valor de Delta Deslocamento é: {Sf} m")
        elif op1 == 3:
            Ds = float(input("Digite o valor do Deslocamento (m): "))
            Dt = float(input("Digite o valor do Tempo (s): "))
            if Dt == 0:
                print("Erro: Tempo não pode ser zero.")
            else:
                Vm = Ds / Dt
            print(f"O valor da Velocidade Média é: {Vm} m/s")
        elif op1 == 5:
            os.system('cls')
            print("1 - MU - Movimento Uniforme")
            print("2 - MUV - Movimento Uniformemente Variado")
            print("3 - MRUV - Movimento Retilíneo Uniformemente Variado (Queda Livre)")
            print("4 - MCU - Movimento Circular Uniforme")
            print("5 - MCUV - Movimento Circular Uniformemente Variado")
            op = int(input("Selecione uma das opções acima: "))
        elif op1 == 4:
            os.system('cls')
            print("Função horária do espaço: Sn = So + V * t")
            print("1 - Sn (posição final) em metros (m)")
            print("2 - So (posição inicial) em metros (m)")
            print("3 - V  (velocidade) em metros por segundo (m/s)")
            print("4 - t  (tempo) em segundos (s)")
            inc = int(input("Selecione uma das opções acima: "))
            if inc == 1:
                So = float(input("Digite o valor da posição inicial (m): "))
                V = float(input("Digite o valor da velocidade (m/s): "))
                t = float(input("Digite o valor do tempo (s): "))
                Sn = So + V * t
                print(f"Sn = {So} m + {V} m/s * {t} s")
                print(f"Sn = {Sn} m")
            elif inc == 2:
                Sn = float(input("Digite o valor da posição final (m): "))
                V = float(input("Digite o valor da velocidade (m/s): "))
                t = float(input("Digite o valor do tempo (s): "))
                So = Sn - V * t
                print(f"{Sn} m = So + {V} m/s * {t} s")
                print(f"So = {Sn} m - {V} m/s * {t} s")
                print(f"So = {So} m")
            elif inc == 3:
                Sn = float(input("Digite o valor da posição final (m): "))
                So = float(input("Digite o valor da posição inicial (m): "))
                t = float(input("Digite o valor do tempo (s): "))
                if t == 0:
                    print("Erro: tempo não pode ser zero.")
                else:
                    V = (Sn - So) / t
                    print(f"{Sn} m = {So} m + V * {t} s")
                    print(f"V = ({Sn} m - {So} m) / {t} s")
                    print(f"V = {V} m/s")
            elif inc == 4:
                Sn = float(input("Digite o valor da posição final (m): "))
                So = float(input("Digite o valor da posição inicial (m): "))
                V = float(input("Digite o valor da velocidade (m/s): "))
                if V == 0:
                    print("Erro: velocidade não pode ser zero.")
                else:
                    t = (Sn - So) / V
                    print(f"{Sn} m = {So} m + {V} m/s * t")
                    print(f"t = ({Sn} m - {So} m) / {V} m/s")
                    print(f"t = {t} s")
    if op == 2:
        os.system('cls')
        print("Selecione qual conta deseja fazer: ")
        print("1 - Equação da velocidade")
        print("2 - Equação do espaço")
        print("3 - Equação de Torricelli")
        print("4 - Voltar para o menu de seleção principal")
        op2 = int(input("Selecione uma das contas acima: "))
        if op2 == 1:
            os.system('cls')
            print("1 - V (velocidade final)")
            print("2 - Vo (velocidade inicial)")
            print("3 - a (aceleração)")
            print("4 - t (tempo)")
            inc = int(input("Selecione a incógnita: "))
            if inc == 1:
                Vo = float(input("Digite Vo (m/s): "))
                a = float(input("Digite a (m/s²): "))
                t = float(input("Digite t (s): "))
                V = Vo + a * t
                print(f"V = {V} m/s")
            elif inc == 2:
                V = float(input("Digite V (m/s): "))
                a = float(input("Digite a (m/s²): "))
                t = float(input("Digite t (s): "))
                Vo = V - a * t
                print(f"Vo = {Vo} m/s")
            elif inc == 3:
                V = float(input("Digite V (m/s): "))
                Vo = float(input("Digite Vo (m/s): "))
                t = float(input("Digite t (s): "))
                if t == 0:
                    print("Erro: tempo não pode ser zero.")
                else:
                    a = (V - Vo) / t
                    print(f"a = {a} m/s²")
            elif inc == 4:
                V = float(input("Digite V (m/s): "))
                Vo = float(input("Digite Vo (m/s): "))
                a = float(input("Digite a (m/s²): "))
                if a == 0:
                    print("Erro: aceleração não pode ser zero.")
                else:
                    t = (V - Vo) / a
                    print(f"t = {t} s")
        elif op2 == 2:
            os.system('cls')
            print("1 - S (posição final)")
            print("2 - So (posição inicial)")
            print("3 - Vo (velocidade inicial)")
            print("4 - a (aceleração)")
            print("5 - t (tempo)")
            inc = int(input("Selecione a incógnita: "))
            if inc == 1:
                So = float(input("Digite So (m): "))
                Vo = float(input("Digite Vo (m/s): "))
                a = float(input("Digite a (m/s²): "))
                t = float(input("Digite t (s): "))
                S = So + Vo * t + (a * t**2) / 2
                print(f"S = {S} m")
            elif inc == 2:
                S = float(input("Digite S (m): "))
                Vo = float(input("Digite Vo (m/s): "))
                a = float(input("Digite a (m/s²): "))
                t = float(input("Digite t (s): "))
                So = S - Vo * t - (a * t**2) / 2
                print(f"So = {So} m")
            elif inc == 3:
                S = float(input("Digite S (m): "))
                So = float(input("Digite So (m): "))
                a = float(input("Digite a (m/s²): "))
                t = float(input("Digite t (s): "))
                if t == 0:
                    print("Erro: tempo não pode ser zero.")
                else:
                    Vo = (S - So - (a * t**2) / 2) / t
                    print(f"Vo = {Vo} m/s")
            elif inc == 4:
                S = float(input("Digite S (m): "))
                So = float(input("Digite So (m): "))
                Vo = float(input("Digite Vo (m/s): "))
                t = float(input("Digite t (s): "))
                if t == 0:
                    print("Erro: tempo não pode ser zero.")
                else:
                    a = 2 * (S - So - Vo * t) / (t**2)
                    print(f"a = {a} m/s²")
            elif inc == 5:
                S = float(input("Digite S (m): "))
                So = float(input("Digite So (m): "))
                Vo = float(input("Digite Vo (m/s): "))
                a = float(input("Digite a (m/s²): "))
                A = a / 2
                B = Vo
                C = So - S
                if A == 0:
                    if B == 0:
                        print("Equação degenerada.")
                    else:
                        t = -C / B
                        print(f"t = {t} s")
                else:
                    discriminant = B**2 - 4*A*C
                    if discriminant < 0:
                        print("Não há solução real.")
                    elif discriminant == 0:
                        t = -B / (2*A)
                        print(f"t = {t} s")
                    else:
                        t1 = (-B + discriminant**0.5) / (2*A)
                        t2 = (-B - discriminant**0.5) / (2*A)
                        print(f"t = {t1} s ou t = {t2} s")
        elif op2 == 3:
            os.system('cls')
            print("1 - V (velocidade final)")
            print("2 - Vo (velocidade inicial)")
            print("3 - a (aceleração)")
            print("4 - S (deslocamento)")
            inc = int(input("Selecione a incógnita: "))
            if inc == 1:
                Vo = float(input("Digite Vo (m/s): "))
                a = float(input("Digite a (m/s²): "))
                dS = float(input("Digite S (m): "))
                V = (Vo**2 + 2 * a * dS)**0.5
                print(f"V = {V} m/s")
            elif inc == 2:
                V = float(input("Digite V (m/s): "))
                a = float(input("Digite a (m/s²): "))
                dS = float(input("Digite S (m): "))
                Vo = (V**2 - 2 * a * dS)**0.5
                print(f"Vo = {Vo} m/s")
            elif inc == 3:
                V = float(input("Digite V (m/s): "))
                Vo = float(input("Digite Vo (m/s): "))
                dS = float(input("Digite S (m): "))
                if dS == 0:
                    print("Erro: S não pode ser zero.")
                else:
                    a = (V**2 - Vo**2) / (2 * dS)
                    print(f"a = {a} m/s²")
            elif inc == 4:
                V = float(input("Digite V (m/s): "))
                Vo = float(input("Digite Vo (m/s): "))
                a = float(input("Digite a (m/s²): "))
                if a == 0:
                    print("Erro: aceleração não pode ser zero.")
                else:
                    dS = (V**2 - Vo**2) / (2 * a)
                    print(f"S = {dS} m")
        elif op2 == 4:
            os.system('cls')
            print("1 - MU - Movimento Uniforme")
            print("2 - MUV - Movimento Uniformemente Variado")
            print("3 - MRUV - Movimento Retilíneo Uniformemente Variado (Queda Livre)")
            print("4 - MCU - Movimento Circular Uniforme")
            print("5 - MCUV - Movimento Circular Uniformemente Variado")
            op = int(input("Selecione uma das opções acima: "))
    else:
        print("Opção inválida para MUV.")
    if op == 3:
        os.system('cls')
        print("Selecione o tipo de movimento: ")
        print("1 - Queda Livre")
        print("2 - Lançamento Vertical para Cima")
        print("3 - Lançamento Vertical para Baixo")
        print("4 - Voltar para o menu de seleção principal")
        op3 = int(input("Selecione uma das opções acima: "))
        if op3 == 1:
            os.system('cls')
            print("\nQUEDA LIVRE - Selecione a fórmula e a incógnita:")
            print("\n1 - Fórmula: v = g * t")
            print("   a) v (velocidade final)")
            print("   b) g (aceleração da gravidade)")
            print("   c) t (tempo)")
            print("\n2 - Fórmula: h = (g * t²) / 2")
            print("   a) h (altura)")
            print("   b) g (aceleração da gravidade)")
            print("   c) t (tempo)")
            print("\n3 - Fórmula: v² = 2 * g * h (Torricelli)")
            print("   a) v (velocidade final)")
            print("   b) g (aceleração da gravidade)")
            print("   c) h (altura)")
            print("\n4 - Fórmula: t = raiz(2 * h / g)")
            print("   a) t (tempo)")
            print("   b) h (altura)")
            print("   c) g (aceleração da gravidade)")
            escolha = input("\nSelecione a opção (ex: 1a, 2b, etc.): ").lower()
            g = 9.8
            if escolha == "1a":
                t = float(input("Digite t (s): "))
                v = g * t
                print(f"\nv = {g} * {t}")
                print(f"v = {v} m/s")
            elif escolha == "1b":
                v = float(input("Digite v (m/s): "))
                t = float(input("Digite t (s): "))
                if t == 0:
                    print("Erro: tempo não pode ser zero.")
                else:
                    g_calc = v / t
                    print(f"\ng = {v} / {t}")
                    print(f"g = {g_calc} m/s²")
            elif escolha == "1c":
                v = float(input("Digite v (m/s): "))
                t_calc = v / g
                print(f"\nt = {v} / {g}")
                print(f"t = {t_calc} s")
            elif escolha == "2a":
                t = float(input("Digite t (s): "))
                h = (g * t**2) / 2
                print(f"\nh = ({g} * {t}²) / 2")
                print(f"h = {h} m")
            elif escolha == "2b":
                h = float(input("Digite h (m): "))
                t = float(input("Digite t (s): "))
                if t == 0:
                    print("Erro: tempo não pode ser zero.")
                else:
                    g_calc = (2 * h) / (t**2)
                    print(f"\ng = (2 * {h}) / {t}²")
                    print(f"g = {g_calc} m/s²")
            elif escolha == "2c":
                h = float(input("Digite h (m): "))
                t_calc = (2 * h / g)**0.5
                print(f"\nt = raiz(2 * {h} / {g})")
                print(f"t = {t_calc} s")
            elif escolha == "3a":
                g_val = float(input("Digite g (m/s²): "))
                h = float(input("Digite h (m): "))
                v = (2 * g_val * h)**0.5
                print(f"\nv = raiz(2 * {g_val} * {h})")
                print(f"v = {v} m/s")
            elif escolha == "3b":
                v = float(input("Digite v (m/s): "))
                h = float(input("Digite h (m): "))
                if h == 0:
                    print("Erro: altura não pode ser zero.")
                else:
                    g_calc = (v**2) / (2 * h)
                    print(f"\ng = {v}² / (2 * {h})")
                    print(f"g = {g_calc} m/s²")
            elif escolha == "3c":
                v = float(input("Digite v (m/s): "))
                g_val = float(input("Digite g (m/s²): "))
                h = (v**2) / (2 * g_val)
                print(f"\nh = {v}² / (2 * {g_val})")
                print(f"h = {h} m")
            elif escolha == "4a":
                h = float(input("Digite h (m): "))
                t_calc = (2 * h / g)**0.5
                print(f"\nt = raiz(2 * {h} / {g})")
                print(f"t = {t_calc} s")
            elif escolha == "4b":
                t = float(input("Digite t (s): "))
                h = (g * t**2) / 2
                print(f"\nh = ({g} * {t}²) / 2")
                print(f"h = {h} m")
            elif escolha == "4c":
                t = float(input("Digite t (s): "))
                h = float(input("Digite h (m): "))
                if t == 0:
                    print("Erro: tempo não pode ser zero.")
                else:
                    g_calc = (2 * h) / (t**2)
                    print(f"\ng = (2 * {h}) / {t}²")
                    print(f"g = {g_calc} m/s²")
        elif op3 == 2:
            os.system('cls')
            print("\nLANÇAMENTO VERTICAL PARA CIMA - Selecione a fórmula e a incógnita:")
            print("\n1 - Fórmula: v = v0 - g * t")
            print("   a) v (velocidade final)")
            print("   b) v0 (velocidade inicial)")
            print("   c) g (aceleração da gravidade)")
            print("   d) t (tempo)")
            print("\n2 - Fórmula: h = v0 * t - (g * t²) / 2")
            print("   a) h (altura)")
            print("   b) v0 (velocidade inicial)")
            print("   c) g (aceleração da gravidade)")
            print("   d) t (tempo)")
            print("\n3 - Fórmula: v² = v0² - 2 * g * Dh (Torricelli)")
            print("   a) v (velocidade final)")
            print("   b) v0 (velocidade inicial)")
            print("   c) g (aceleração da gravidade)")
            print("   d) Dh (deslocamento)")
            print("\n4 - t_subida = v0 / g")
            print("   a) t_subida (tempo de subida)")
            print("   b) v0 (velocidade inicial)")
            print("   c) g (aceleração da gravidade)")
            print("\n5 - h_max = v0² / (2 * g)")
            print("   a) h_max (altura máxima)")
            print("   b) v0 (velocidade inicial)")
            print("   c) g (aceleração da gravidade)")
            print("\n6 - t_total = 2 * v0 / g")
            print("   a) t_total (tempo total)")
            print("   b) v0 (velocidade inicial)")
            print("   c) g (aceleração da gravidade)")
            escolha = input("\nSelecione a opção (ex: 1a, 2b, etc.): ").lower()
            g = 9.8
            if escolha == "1a":
                v0 = float(input("Digite v0 (m/s): "))
                t = float(input("Digite t (s): "))
                v = v0 - g * t
                print(f"\nv = {v0} - {g} * {t}")
                print(f"v = {v} m/s")
            elif escolha == "1b":
                v = float(input("Digite v (m/s): "))
                t = float(input("Digite t (s): "))
                v0 = v + g * t
                print(f"\nv0 = {v} + {g} * {t}")
                print(f"v0 = {v0} m/s")
            elif escolha == "1c":
                v = float(input("Digite v (m/s): "))
                v0 = float(input("Digite v0 (m/s): "))
                t = float(input("Digite t (s): "))
                if t == 0:
                    print("Erro: tempo não pode ser zero.")
                else:
                    g_calc = (v0 - v) / t
                    print(f"\ng = ({v0} - {v}) / {t}")
                    print(f"g = {g_calc} m/s²")
            elif escolha == "1d":
                v = float(input("Digite v (m/s): "))
                v0 = float(input("Digite v0 (m/s): "))
                if g == 0:
                    print("Erro: gravidade não pode ser zero.")
                else:
                    t = (v0 - v) / g
                    print(f"\nt = ({v0} - {v}) / {g}")
                    print(f"t = {t} s")
            elif escolha == "2a":
                v0 = float(input("Digite v0 (m/s): "))
                t = float(input("Digite t (s): "))
                h = v0 * t - (g * t**2) / 2
                print(f"\nh = {v0} * {t} - ({g} * {t}²) / 2")
                print(f"h = {h} m")
            elif escolha == "2b":
                h = float(input("Digite h (m): "))
                t = float(input("Digite t (s): "))
                if t == 0:
                    print("Erro: tempo não pode ser zero.")
                else:
                    v0 = (h + (g * t**2) / 2) / t
                    print(f"\nv0 = ({h} + ({g} * {t}²) / 2) / {t}")
                    print(f"v0 = {v0} m/s")
            elif escolha == "2c":
                h = float(input("Digite h (m): "))
                v0 = float(input("Digite v0 (m/s): "))
                t = float(input("Digite t (s): "))
                if t == 0:
                    print("Erro: tempo não pode ser zero.")
                else:
                    g_calc = (2 * (v0 * t - h)) / (t**2)
                    print(f"\ng = (2 * ({v0} * {t} - {h})) / {t}²")
                    print(f"g = {g_calc} m/s²")
            elif escolha == "2d":
                h = float(input("Digite h (m): "))
                v0 = float(input("Digite v0 (m/s): "))
                A = g / 2
                B = -v0
                C = h
                discriminant = B**2 - 4*A*C
                if discriminant < 0:
                    print("\nNão há solução real.")
                elif discriminant == 0:
                    t = -B / (2*A)
                    print(f"\nt = {t} s")
                else:
                    t1 = (-B + discriminant**0.5) / (2*A)
                    t2 = (-B - discriminant**0.5) / (2*A)
                    print(f"\nt = {t1} s ou t = {t2} s")
            elif escolha == "3a":
                v0 = float(input("Digite v0 (m/s): "))
                Dh = float(input("Digite Dh (m): "))
                v_squared = v0**2 - 2 * g * Dh
                if v_squared < 0:
                    print("\nNão há solução real (v² negativo).")
                else:
                    v = v_squared**0.5
                    print(f"\nv = raiz({v0}² - 2 * {g} * {Dh})")
                    print(f"v = {v} m/s")
            elif escolha == "3b":
                v = float(input("Digite v (m/s): "))
                Dh = float(input("Digite Dh (m): "))
                v0_squared = v**2 + 2 * g * Dh
                v0 = v0_squared**0.5
                print(f"\nv0 = raiz({v}² + 2 * {g} * {Dh})")
                print(f"v0 = {v0} m/s")
            elif escolha == "3c":
                v = float(input("Digite v (m/s): "))
                v0 = float(input("Digite v0 (m/s): "))
                dh = float(input("Digite Δh (m): "))
                if dh == 0:
                    print("Erro: deslocamento não pode ser zero.")
                else:
                    g_calc = (v0**2 - v**2) / (2 * Dh)
                    print(f"\ng = ({v0}² - {v}²) / (2 * {Dh})")
                    print(f"g = {g_calc} m/s²")
            elif escolha == "3d":
                v = float(input("Digite v (m/s): "))
                v0 = float(input("Digite v0 (m/s): "))
                g_val = float(input("Digite g (m/s²): "))
                Dh = (v0**2 - v**2) / (2 * g_val)
                print(f"\nDh = ({v0}² - {v}²) / (2 * {g_val})")
                print(f"Dh = {Dh} m")
            elif escolha == "4a":
                v0 = float(input("Digite v0 (m/s): "))
                t_subida = v0 / g
                print(f"\nt_subida = {v0} / {g}")
                print(f"t_subida = {t_subida} s")
            elif escolha == "4b":
                t_subida = float(input("Digite t_subida (s): "))
                v0 = t_subida * g
                print(f"\nv0 = {t_subida} * {g}")
                print(f"v0 = {v0} m/s")
            elif escolha == "4c":
                v0 = float(input("Digite v0 (m/s): "))
                t_subida = float(input("Digite t_subida (s): "))
                g_calc = v0 / t_subida
                print(f"\ng = {v0} / {t_subida}")
                print(f"g = {g_calc} m/s²")
            elif escolha == "5a":
                v0 = float(input("Digite v0 (m/s): "))
                h_max = v0**2 / (2 * g)
                print(f"\nh_max = {v0}² / (2 * {g})")
                print(f"h_max = {h_max} m")
            elif escolha == "5b":
                h_max = float(input("Digite h_max (m): "))
                v0 = (2 * g * h_max)**0.5
                print(f"\nv0 = raiz(2 * {g} * {h_max})")
                print(f"v0 = {v0} m/s")
            elif escolha == "5c":
                v0 = float(input("Digite v0 (m/s): "))
                h_max = float(input("Digite h_max (m): "))
                g_calc = v0**2 / (2 * h_max)
                print(f"\ng = {v0}² / (2 * {h_max})")
                print(f"g = {g_calc} m/s²")
            elif escolha == "6a":
                v0 = float(input("Digite v0 (m/s): "))
                t_total = 2 * v0 / g
                print(f"\nt_total = 2 * {v0} / {g}")
                print(f"t_total = {t_total} s")
            elif escolha == "6b":
                t_total = float(input("Digite t_total (s): "))
                v0 = t_total * g / 2
                print(f"\nv0 = {t_total} * {g} / 2")
                print(f"v0 = {v0} m/s")
            elif escolha == "6c":
                v0 = float(input("Digite v0 (m/s): "))
                t_total = float(input("Digite t_total (s): "))
                g_calc = 2 * v0 / t_total
                print(f"\ng = 2 * {v0} / {t_total}")
                print(f"g = {g_calc} m/s²")
        elif op3 == 3:
            os.system('cls')
            print("\nLANÇAMENTO VERTICAL PARA BAIXO - Selecione a fórmula e a incógnita:")
            print("\n1 - Fórmula: v = v0 + g * t")
            print("   a) v (velocidade final)")
            print("   b) v0 (velocidade inicial)")
            print("   c) g (aceleração da gravidade)")
            print("   d) t (tempo)")
            print("\n2 - Fórmula: h = v0 * t + (g * t²) / 2")
            print("   a) h (altura)")
            print("   b) v0 (velocidade inicial)")
            print("   c) g (aceleração da gravidade)")
            print("   d) t (tempo)")
            print("\n3 - Fórmula: v² = v0² + 2 * g * Dh (Torricelli)")
            print("   a) v (velocidade final)")
            print("   b) v0 (velocidade inicial)")
            print("   c) g (aceleração da gravidade)")
            print("   d) Dh (deslocamento)")
            escolha = input("\nSelecione a opção (ex: 1a, 2b, etc.): ").lower()
            g = 9.8
            if escolha == "1a":
                v0 = float(input("Digite v0 (m/s): "))
                t = float(input("Digite t (s): "))
                v = v0 + g * t
                print(f"\nv = {v0} + {g} * {t}")
                print(f"v = {v} m/s")
            elif escolha == "1b":
                v = float(input("Digite v (m/s): "))
                t = float(input("Digite t (s): "))
                v0 = v - g * t
                print(f"\nv0 = {v} - {g} * {t}")
                print(f"v0 = {v0} m/s")
            elif escolha == "1c":
                v = float(input("Digite v (m/s): "))
                v0 = float(input("Digite v0 (m/s): "))
                t = float(input("Digite t (s): "))
                if t == 0:
                    print("Erro: tempo não pode ser zero.")
                else:
                    g_calc = (v - v0) / t
                    print(f"\ng = ({v} - {v0}) / {t}")
                    print(f"g = {g_calc} m/s²")
            elif escolha == "1d":
                v = float(input("Digite v (m/s): "))
                v0 = float(input("Digite v0 (m/s): "))
                if g == 0:
                    print("Erro: gravidade não pode ser zero.")
                else:
                    t = (v - v0) / g
                    print(f"\nt = ({v} - {v0}) / {g}")
                    print(f"t = {t} s")
            elif escolha == "2a":
                v0 = float(input("Digite v0 (m/s): "))
                t = float(input("Digite t (s): "))
                h = v0 * t + (g * t**2) / 2
                print(f"\nh = {v0} * {t} + ({g} * {t}²) / 2")
                print(f"h = {h} m")
            elif escolha == "2b":
                h = float(input("Digite h (m): "))
                t = float(input("Digite t (s): "))
                if t == 0:
                    print("Erro: tempo não pode ser zero.")
                else:
                    v0 = (h - (g * t**2) / 2) / t
                    print(f"\nv0 = ({h} - ({g} * {t}²) / 2) / {t}")
                    print(f"v0 = {v0} m/s")
            elif escolha == "2c":
                h = float(input("Digite h (m): "))
                v0 = float(input("Digite v0 (m/s): "))
                t = float(input("Digite t (s): "))
                if t == 0:
                    print("Erro: tempo não pode ser zero.")
                else:
                    g_calc = 2 * (h - v0 * t) / (t**2)
                    print(f"\ng = 2 * ({h} - {v0} * {t}) / {t}²")
                    print(f"g = {g_calc} m/s²")
            elif escolha == "2d":
                h = float(input("Digite h (m): "))
                v0 = float(input("Digite v0 (m/s): "))
                A = g / 2
                B = v0
                C = -h
                discriminant = B**2 - 4*A*C
                if discriminant < 0:
                    print("\nNão há solução real.")
                elif discriminant == 0:
                    t = -B / (2*A)
                    print(f"\nt = {t} s")
                else:
                    t1 = (-B + discriminant**0.5) / (2*A)
                    t2 = (-B - discriminant**0.5) / (2*A)
                    print(f"\nt = {t1} s ou t = {t2} s")
            elif escolha == "3a":
                v0 = float(input("Digite v0 (m/s): "))
                Dh = float(input("Digite Dh (m): "))
                v = (v0**2 + 2 * g * Dh)**0.5
                print(f"\nv = raiz({v0}² + 2 * {g} * {Dh})")
                print(f"v = {v} m/s")
            elif escolha == "3b":
                v = float(input("Digite v (m/s): "))
                Dh = float(input("Digite Dh (m): "))
                v0_squared = v**2 - 2 * g * Dh
                if v0_squared < 0:
                    print("\nNão há solução real (v0² negativo).")
                else:
                    v0 = v0_squared**0.5
                    print(f"\nv0 = raiz({v}² - 2 * {g} * {Dh})")
                    print(f"v0 = {v0} m/s")
            elif escolha == "3c":
                v = float(input("Digite v (m/s): "))
                v0 = float(input("Digite v0 (m/s): "))
                Dh = float(input("Digite Dh (m): "))
                if Dh == 0:
                    print("Erro: deslocamento não pode ser zero.")
                else:
                    g_calc = (v**2 - v0**2) / (2 * Dh)
                    print(f"\ng = ({v}² - {v0}²) / (2 * {Dh})")
                    print(f"g = {g_calc} m/s²")
            elif escolha == "3d":
                v = float(input("Digite v (m/s): "))
                v0 = float(input("Digite v0 (m/s): "))
                g_val = float(input("Digite g (m/s²): "))
                Dh = (v**2 - v0**2) / (2 * g_val)
                print(f"\nDh = ({v}² - {v0}²) / (2 * {g_val})")
                print(f"Dh = {Dh} m")
        elif op3 == 4:
            os.system('cls')
            print("1 - MU - Movimento Uniforme")
            print("2 - MUV - Movimento Uniformemente Variado")
            print("3 - MRUV - Movimento Retilíneo Uniformemente Variado (Queda Livre)")
            print("4 - MCU - Movimento Circular Uniforme")
            print("5 - MCUV - Movimento Circular Uniformemente Variado")
            op = int(input("Selecione uma das opções acima: "))
    if op == 4:
        os.system('cls')
        print("Opção MCU ainda não disponível.")
        print("Digite 1 para voltar para o menu de seleção principal.")
        if int(input("Digite sua escolha: ")) == 1:
            os.system('cls')
            print("1 - MU - Movimento Uniforme")
            print("2 - MUV - Movimento Uniformemente Variado")
            print("3 - MRUV - Movimento Retilíneo Uniformemente Variado (Queda Livre)")
            print("4 - MCU - Movimento Circular Uniforme")
            print("5 - MCUV - Movimento Circular Uniformemente Variado")
            op = int(input("Selecione uma das opções acima: "))
        else:
            print("Opção invalida.")
    if op == 5:
        os.system('cls')
        print("Opção MCUV ainda não disponível.")
        print("Digite 1 para voltar para o menu de seleção principal.")
        if int(input("Digite sua escolha: ")) == 1:
            os.system('cls')
            print("1 - MU - Movimento Uniforme")
            print("2 - MUV - Movimento Uniformemente Variado")
            print("3 - MRUV - Movimento Retilíneo Uniformemente Variado (Queda Livre)")
            print("4 - MCU - Movimento Circular Uniforme")
            print("5 - MCUV - Movimento Circular Uniformemente Variado")
            op = int(input("Selecione uma das opções acima: "))
        else:
            print("Opção invalida.")
