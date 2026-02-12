banner = r"""
d8888b. d888888b d888888b  .d88b.  d8b   db 
88  `8D   `88'   `~~88~~' .8P  Y8. 888o  88 
88oodD'    88       88    88    88 88V8o 88 
88~~~      88       88    88    88 88 V8o88 
88        .88.      88    `8b  d8' 88  V888 
88      Y888888P    YP     `Y88P'  VP   V8P 
"""
print(banner)
print("Programa feito por APENAS Pablo Henrique Ferreira Loschi ©")
name = input("Nome do aluno -> ")

while True:
    try:
        test_grade = float(input("Nota da prova do 1º semestre -> "))
        ass_grade = float(input("Nota dos trabalhos do 1º semestre ->"))
        test_grade2 = float(input("Nota da prova do 2º semestre -> "))
        ass_grade2 = float(input("Nota dos trabalhos do 2º semestre ->"))
        
        final_grade = ((test_grade + ass_grade) / 2) + ((test_grade2 + ass_grade2) / 2)

        print(f"Sua nota final é", {final_grade})
        if final_grade >= 7:
            print("Você foi aprovado !")
        elif final_grade >= 5 and final_grade <= 6.9:
            print("Você está de recuperação !")
        else:
            print("Você foi reprovado !")
            
        retry = input("Você quer começar novamente ? (y/n) -> ").lower()
        if retry == 'y':
            continue
        else:
            break
    
    except ValueError:
        print("\nErro de input, por favor tente novamente")
        continue
    except KeyboardInterrupt:
        print("\nPrograma interrompido, desligando...")
        break
    except EOFError:
        print("\nProcesso interrompido, desligando...")
        break
    