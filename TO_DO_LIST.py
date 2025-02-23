from tkinter import *

# Fonction pour marquer une tâche comme terminée
def mark_done():
    try:
        selected_index = listbox.curselection()[0]  # Récupérer l'index de la tâche sélectionnée
        task = listbox.get(selected_index)
        if not task.startswith("✔ "):  # Vérifier si la tâche n'est pas déjà marquée comme faite
            listbox.delete(selected_index)
            listbox.insert(selected_index, f"✔ {task}")  # Ajouter la coche
    except:
        label.config(text="Sélectionnez une tâche à terminer")

# Fonction pour ajouter une tâche
def add():
    task = entryBox.get().strip()
    if task:
        listbox.insert(END, task)
        listbox.config(height=listbox.size())
        entryBox.delete(0, END)

# Fonction pour supprimer une tâche
def delete():
    try:
        listbox.delete(listbox.curselection())
        listbox.config(height=listbox.size())
    except:
        label.config(text="Sélectionnez une tâche à supprimer")

# Création de la fenêtre principale
window = Tk()
window.title("TO-DO List avec Python")
window.geometry("600x400")

# Liste des tâches
listbox = Listbox(window, bg="#f7ffde", font=("Arial", 14), width=40, height=6)
listbox.pack(pady=10)

# Ajouter quelques tâches par défaut
tasks = ["Faire une application mobile", "Développer un site web", "Organiser les dossiers du projet", "Réunion","Suivre un cours en ligne sur SQL","Faire une entretien","Pratiquer des exercices sur HackerRank"]
for task in tasks:
    listbox.insert(END, task)

listbox.config(height=listbox.size())

# Champ de saisie pour ajouter une nouvelle tâche
entryBox = Entry(window, font=("Arial", 14))
entryBox.pack(pady=5)

# Boutons
button_add = Button(window, text="Ajouter", command=add, bg="#a0d995", font=("Arial", 12))
button_add.pack(pady=2)

button_delete = Button(window, text="Supprimer", command=delete, bg="#f68b8b", font=("Arial", 12))
button_delete.pack(pady=2)

button_done = Button(window, text="Terminer", command=mark_done, bg="#FFD700", font=("Arial", 12))
button_done.pack(pady=2)

# Label pour afficher les messages d'information
label = Label(window, text="", font=("Arial", 12))
label.pack(pady=5)

# Lancement de la fenêtre
window.mainloop()
