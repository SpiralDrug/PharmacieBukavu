import csv
import tkinter as tk
from collections import Counter

#Lire le CSV
with open('pharmacie_bukavu_csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    noms = [ligne['Nom'].split()[0] for ligne in reader]

compte = Counter(noms).most_common(8)

#Dessiner avec tkinter
root = tk.Tk()
root.title("Stock Pharmacie Bukavu")

canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

max_val = max(valeur for nom, valeur in compte)

for i, (nom, qte) in enumerate(compte):
    x_debut = 20
    y_debut = 20 + i*45
    x_fin = 20 + (qte / max_val * 350)
    y_fin = y_debut + 30
    canvas.create_rectangle(x_debut, y_debut, x_fin, y_fin, fill="#2E86AB")
    canvas.create_text(400, y_debut + 15, text=nom + " : " + str(qte))

root.mainloop()

