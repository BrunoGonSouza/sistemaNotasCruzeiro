'''Universidade Cruzeiro do sul
   Bruno Gonçalves de Souza
   RGM : 29078989
   06.04.22
   Escreva um programa que calcule a nota final do aluno, para
   determinar se ele está aprovado ou reprovado, caso reprovado,
   faça AF para sustituir a menor nota'''

while(True):    
    a1 = float(input("Digite a nota de A1 [1 - 5]: "))
    a2 = float(input("Digite a nota de A2 [1 - 5]: "))

    presenca = int(input("Digite com a presença [%]: "))
    if a1 < 0 or a1 > 5 or a2 < 0 or a2 > 5:
        print("Nota inválida (entre 0 e 5)")
    else:    
            if (presenca < 75):
                print("Reprovado por faltas")
            else:
                resultadoParcial = a1 + a2
                print(f"Nota Parcial: ({resultadoParcial:.1f})")

                if (resultadoParcial >= 6):
                    print("Aprovado")
                else:
                    if (a1 < 1 and a2 < 1):
                        print("Reprovado pois não teve uma nota minima de 1 ponto")
                    if (a1 >= 1 or a2 >= 1):
                        aF = float(input("Digite a nota de Recuperação [AF]: "))
                        if(a1 >= a2):
                            notaMaior = a1
                        else:
                            notaMaior = a2
                        resultadoFinal = notaMaior + aF
                        if (resultadoFinal >= 6):
                            print(f"Maior nota entre a1 e a2: ({notaMaior}) | Nota de recuperação AF: ({aF})")
                            print(f"Nota Final: ({resultadoFinal}): Aprovado com AF")
                        else:
                            print(f"Maior nota entre a1 e a2: ({notaMaior}) | Nota de AF: ({aF}) = Nota Final: ({resultadoFinal})")
                            print("Reprovado com AF")
                

    print("---------------------------------------------")

  
    


