
from tkinter import *
import random

# Liste des caractères possibles
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '!', '@', '#', '$', '%', '&', '^', '?']

def generepassword():
    try:
        n = int(entry.get())  # Récupérer la taille depuis l'Entry
        tab = [random.choice(l) for _ in range(n)]  # Générer un mot de passe aléatoire
        password.set("".join(map(str, tab)))  # Afficher le résultat dans le Label
    except ValueError:
        password.set("Entrée invalide !")

# Création de la fenêtre
window = Tk()
window.title("Password Generator")
window.geometry("400x300")

# Champ d'entrée pour la taille du mot de passe
Label(window, text="Taille du mot de passe :",fg="blue",font=("Arial", 14)).pack(pady=5)
entry = Entry(window, font=("Arial", 14),fg="green")
entry.pack()

# Bouton pour générer le mot de passe
Button(window, text="Générer", font=("Arial", 14),fg="green", command=generepassword).pack(pady=10)

# Affichage du mot de passe généré
password = StringVar()
Label(window, textvariable=password, font=("Arial", 16, "bold"), fg="blue").pack(pady=10)

# Lancement de la fenêtre Tkinter
window.mainloop()
