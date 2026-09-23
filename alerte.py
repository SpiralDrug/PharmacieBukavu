import csv
import tkinter as tk
from datetime import datetime

expire_bientot = []
aujourdhui = datetime.now()

with open('pharmacie_bukavu_csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for ligne in reader:
        date_peremption = datetime.strptime(ligne['Date_peremption'], "%Y-%m-%d")
        diff = (date_peremption - aujourdhui).days
        if diff < 90: # expire dans moins de 90 jours
            expire_bientot.append([ligne['Nom'], diff, ligne['Quantite']])

# Trier du plus urgent au moins urgent
expire_bientot.sort(key=lambda x: x[1])

root = tk.Tk()
root.title("ALERTE PEREMPTION - 90 jours")

canvas = tk.Canvas(root, width=650, height=400, bg="white")
canvas.pack()

canvas.create_text(20, 20, text="Medicaments qui expirent bientot :", anchor="w", font=("Arial", 12, "bold"))

y = 60
for nom, jours, qte in expire_bientot[:8]:
    couleur = "red" if jours < 30 else "orange"
    texte = nom + " - expire dans " + str(jours) + " jours - Qte: " + str(qte)
    canvas.create_text(20, y, text=texte, anchor="w", fill=couleur)
    y = y + 30

if len(expire_bientot) == 0:
    canvas.create_text(20, y, text="Aucun medicament ne va expirer, stock OK!", anchor="w", fill="green")

root.mainloop()
