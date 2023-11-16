# Izveidojiet Python programmu, kas saskaita no 1 līdz lietotāja ievadītam skaitlim, izmantojot for ciklu.

ievaditais_skaitlis = int(input("Ievadiet skaitli: "))
summa=0

# for cikls, kas saskaita no 1 līdz ievadītajam skaitlim
for skaitlis in range(ievaditais_skaitlis):
    summa = skaitlis

# Pasaka cik japieskaita 1, lai iegutu so skaitli
print("No 1 līdz ievadītajam skaitlim", ievaditais_skaitlis, "ir:", summa)
