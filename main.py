import calendar

annee=int(input("Entrer une annee(ex:2024):"))
mois=int(input("Entrer un mois(1-12):"))

print('\nAfficher le calendrier:')
print(calendar.month(annee,mois))