import csv
import random
from datetime import datetime, timedelta

medicaments = ["Paracetamol", "Amoxicilline", "Quinine", "Metronidazole", "Ibuprofen", "Arthemeter"]

with open('pharmacie_bukavu_csv', 'w', newline='', encoding='utf_8') as f:
    writer = csv.writer(f)
    writer.writerow(["Nom", "Quantite", "Prix_achat", "Prix_vente", "Date_peremption","Fournisseur"])

    for i in range(300):
        nom = random.choice(medicaments) + f" {random.randint(100, 500)}mg"
        quantite = random.randint(5, 200)
        prix_achat = random.randint(500, 5000)
        prix_vente = prix_achat + random.randint(200, 2000)
        date_exp = (datetime.now() + timedelta(days=random.randint(30, 700))).strftime("%Y-%m-%d")

        writer.writerow([nom, quantite, prix_achat, prix_vente, date_exp])

print("Fichier pharmacie_bukavu.csv créé avec 300 medicaments !")
