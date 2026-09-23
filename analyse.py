import csv
from collections import Counter

with open('pharmacie_bukavu_csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    lignes = list(reader)

total_valeur = sum(int(l['Quantite']) * int(l['Prix_vente']) for l in lignes)
total_medicaments = sum(int(l['Quantite']) for l in lignes)
prix_moyen = total_valeur / total_medicaments if total_medicaments else 0

noms = [l['Nom'] for l in lignes]
plus_frequent = Counter(noms).most_common(3)

print(f"Nombre de types de médicaments: {len(lignes)}")
print(f"Quantite totale en stock: {total_medicaments}")
print(f"Valeur totale du stock: {total_valeur} FC")
print(f"Prix moyen de vente: {int(prix_moyen)} FC")
print(f"Top 3 medicaments les plus présents: {plus_frequent} ")
