import csv
import tkinter as tk
from collections import Counter
from datetime import datetime

# --- LECTURE DU CSV ---
lignes = []
with open('pharmacie_bukavu_csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    print("Colonnes:", fieldnames)

    # trouver les noms de colonnes automatiquement
    col_nom = [c for c in fieldnames if 'nom' in c.lower()][0]
    col_qte = [c for c in fieldnames if 'quant' in c.lower()][0]
    col_prix = [c for c in fieldnames if 'prix' in c.lower()][0]
    col_date = [c for c in fieldnames if 'date' in c.lower() or 'exp' in c.lower()][0]

    for ligne in reader:
        lignes.append(ligne)

# --- CALCULS ---
total_qte = 0
total_valeur = 0
noms = []
expire_bientot = []

aujourdhui = datetime.now()

for ligne in lignes:
    try:
        qte = int(ligne[col_qte])
        prix = int(ligne[col_prix])
        total_qte += qte
        total_valeur += qte * prix
        noms.append(ligne[col_nom])

        date_peremption = datetime.strptime(ligne[col_date], "%Y-%m-%d")
        diff = (date_peremption - aujourdhui).days
        if diff < 90:
            expire_bientot.append([ligne[col_nom], diff, qte])
    except:
        pass

prix_moyen = total_valeur // total_qte if total_qte else 0
top_stock = Counter(noms).most_common(6)
expire_bientot.sort(key=lambda x: x[1])

# --- FENETRE ---
root = tk.Tk()
root.title("DASHBOARD PHARMACIE BUKAVU")
root.geometry("800x600")
root.configure(bg="white")

tk.Label(root, text="DASHBOARD PHARMACIE BUKAVU", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

# Haut : Chiffres
frame_haut = tk.Frame(root, bg="#f0f0f0")
frame_haut.pack(fill="x", padx=10, pady=5)

tk.Label(frame_haut, text="Qte totale: " + str(total_qte), font=("Arial", 11, "bold"), bg="#f0f0f0").pack(side="left", padx=20, pady=10)
tk.Label(frame_haut, text="Valeur stock: " + str(total_valeur) + " FC", font=("Arial", 11, "bold"), bg="#f0f0f0").pack(side="left", padx=20)
tk.Label(frame_haut, text="Prix moyen: " + str(prix_moyen) + " FC", font=("Arial", 11, "bold"), bg="#f0f0f0").pack(side="left", padx=20)

# Milieu : 2 colonnes
frame_mid = tk.Frame(root, bg="white")
frame_mid.pack(fill="both", expand=True, padx=10)

# Gauche : Graphique
frame_g = tk.Frame(frame_mid, bg="white")
frame_g.pack(side="left", fill="both", expand=True)
tk.Label(frame_g, text="Top Stock", font=("Arial", 12, "bold"), bg="white").pack()

canvas = tk.Canvas(frame_g, width=380, height=300, bg="white")
canvas.pack()

max_q = 1
for n, q in top_stock:
    if q > max_q: max_q = q

i = 0
for nom, qte in top_stock:
    y = 20 + i*45
    x_fin = (qte / max_q * 200)
    canvas.create_rectangle(10, y, 10 + x_fin, y+25, fill="#2E86AB")
    canvas.create_text(230, y+12, text=nom[:15] + " : " + str(qte), anchor="w", font=("Arial", 9))
    i += 1

# Droite : Alertes
frame_d = tk.Frame(frame_mid, bg="#fff5f5")
frame_d.pack(side="right", fill="both", expand=True, padx=10)
tk.Label(frame_d, text="ALERTE PEREMPTION < 90j", font=("Arial", 12, "bold"), bg="#fff5f5", fg="red").pack()

y = 0
for nom, jours, qte in expire_bientot[:10]:
    couleur = "red" if jours < 30 else "#CC5500"
    texte = nom[:20] + " -> " + str(jours) + "j (Qte " + str(qte) + ")"
    tk.Label(frame_d, text=texte, anchor="w", bg="#fff5f5", fg=couleur, font=("Arial", 9)).pack(fill="x", padx=5, pady=2)
    y+=1

if len(expire_bientot) == 0:
    tk.Label(frame_d, text="Stock OK, rien n'expire bientot", bg="#fff5f5", fg="green").pack()

root.mainloop()



