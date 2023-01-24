from random import randint
a = randint(1,10)
n = int(input('Eu pensei em um número de 1 a 10, digite o seu palpite: '))
c = 0
d = 5
while n != a:
    n = int(input(f'Tente de novo, você terá mais {d} chances: '))
    if n != a:
        dica = str((input('Você quer uma dica? [S/N]: '))).upper().strip()
    if dica == 'S':
        if n < a:
            print('Tente um valor maior.')
        if n > a:
            print('Tente um valor menor.')
    if dica == 'N':
        print('Então vamos continuar..')
    c += 1
    d -= 1
    if c == 5 and n != a:
        break
if n == a:
    print(f'Você acertou!Com {c} tentativas!')
if n != a:
    print(f'Eu pensei no número {a}!')
    print('Tchau!')
    