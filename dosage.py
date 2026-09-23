import csv
import random
import re

# VRAIS DOSAGES EN PHARMACIE
VRAIS_DOSAGES = {
    "Paracetamol": ["500mg", "1000mg"],
    "Ibuprofene": ["200mg", "400mg"],
    "Ibuprofen": ["200mg", "400mg"],
    "Amoxicilline": ["500mg", "1g"],
    "Amoxicillin": ["500mg", "1g"],
    "Ciprofloxacine": ["500mg"],
    "Metformine": ["500mg", "850mg", "1000mg"],
    "Omeprazole": ["20mg"],
    "Amlodipine": ["5mg", "10mg"],
    "Doliprane": ["500mg", "1000mg"],
    "Efferalgan": ["500mg"],
    "Augmentin": ["1g"],
    "Azithromycine": ["500mg"],
    "Chloroquine": ["100mg"],
    "Quinine": ["500mg"],
    "Artemether": ["80mg"],
    "Arthemeter": ["20/120mg"],
    "Diclofenac": ["50mg", "100mg"],
    "Metronidazole": ["250mg", "500mg"]
}

# Ouvre l'ancien CSV
with open('pharmacie_bukavu_csv', 'r', encoding='utf-8') as f:
    reader = list(csv.DictReader(f))
    fieldnames = reader[0].keys()

# Corrige
for ligne in reader:
    nom_complet = ligne['Nom']
    # on cherche le nom de base
    for vrai_nom, dosages in VRAIS_DOSAGES.items():
        if vrai_nom.lower() in nom_complet.lower():
            # remplace le dosage par un vrai
            nouveau_dosage = random.choice(dosages)
            # remplace " 327mg" par " 400mg"
            ligne['Nom'] = re.sub(r'\d+mg|\d+g|\d+/\d+mg', nouveau_dosage, nom_complet)
            # si pas de remplacement, ajoute le dosage
            if ligne['Nom'] == nom_complet:
                ligne['Nom'] = vrai_nom + " " + nouveau_dosage
            break

# Sauvegarde le nouveau CSV propre
with open('pharmacie_bukavu_csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(reader)

print("CORRIGE! Maintenant les dosages sont realistes : 500mg, 400mg, 1g, etc.")

