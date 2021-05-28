a, b, c, d = input().split()

pA = 2
pB = 3
pC = 4
pD = 1

media = (float(a)*pA + float(b)*pB + float(c)*pC + float(d)*pD) / (pA + pB + pC + pD)
mediaFormatada = float(format(media,".1f"))
print("Media:", mediaFormatada)

if mediaFormatada >= 7:
    print("Aluno aprovado.")
elif mediaFormatada < 5:
    print("Aluno reprovado.")
elif mediaFormatada >= 5 and mediaFormatada <=6.9:
    print("Aluno em exame.")
    exame = float(input("Nota do exame: "))
    novaNota = (mediaFormatada + exame) / 2
    if novaNota >= 5:
        print("Aluno aprovado.")
    elif novaNota <=4.9:
        print("Aluno reprovado.")
    print("Media final:", format(novaNota,".1f"))
print()