from tkinter import *

# Création de la fenêtre principale
window = Tk()
window.title("TO-DO List avec Python")
window.geometry("600x450")  # Ajustement de la taille pour inclure l'image

welcome_label = Label(window, text="Bienvenue dans votre TO-DO List !", 
                      font=("Arial", 16, "bold"), fg="blue")
welcome_label.pack(pady=10)

# Charger et afficher les images réduites
image = PhotoImage(file="brain2.png").subsample(5, 5)  # Réduire la taille de l'image
image1 = PhotoImage(file="cc2.png").subsample(5, 5)

frame_images = Frame(window)
frame_images.pack()

img_label = Label(frame_images, image=image)
img_label.pack(side=LEFT, padx=10)

img_label1 = Label(frame_images, image=image1)
img_label1.pack(side=RIGHT, padx=10)

# Fonction pour ajouter une tâche avec une case à cocher
def add():
    task_text = entryBox.get().strip()
    if task_text:
        frame = Frame(listbox, bg="#f7ffde")
        var = BooleanVar()
        check = Checkbutton(frame, variable=var, command=lambda: mark_done(var, label), bg="#f7ffde")
        check.pack(side=LEFT)
        label_task = Label(frame, text=task_text, font=("Arial", 14), bg="#f7ffde")
        label_task.pack(side=LEFT, padx=5)
        frame.pack(anchor='w', pady=2)
        tasks.append((var, frame))
        entryBox.delete(0, END)
        label.config(text="")  # Effacer les anciens messages
    else:
        label.config(text="Veuillez entrer une tâche", fg="red")

# Fonction pour marquer une tâche comme terminée
def mark_done(var, label):
    if var.get():
        label.config(text="Tâche terminée !", fg="green")
    else:
        label.config(text="")

# Fonction pour supprimer une tâche sélectionnée
def delete():
    for var, frame in tasks[:]:
        if var.get():
            frame.destroy()
            tasks.remove((var, frame))
    label.config(text="")

# Liste des tâches
listbox = Frame(window, bg="#f7ffde")
listbox.pack(pady=10)

tasks = []

# Ajouter quelques tâches par défaut
default_tasks = [
    "Faire une application mobile",
    "Développer un site web",
    "Organiser les dossiers du projet",
    "Réunion",
    "Suivre un cours en ligne sur SQL",
    "Faire un entretien",
    "Pratiquer des exercices sur HackerRank"
]

for task in default_tasks:
    frame = Frame(listbox, bg="#f7ffde")
    var = BooleanVar()
    check = Checkbutton(frame, variable=var, command=lambda v=var: mark_done(v, label), bg="#f7ffde")
    check.pack(side=LEFT)
    label_task = Label(frame, text=task, font=("Arial", 14), bg="#f7ffde")
    label_task.pack(side=LEFT, padx=5)
    frame.pack(anchor='w', pady=2)
    tasks.append((var, frame))

# Champ de saisie pour ajouter une nouvelle tâche
entryBox = Entry(window, font=("Arial", 14))
entryBox.pack(pady=5)

# Boutons
button_add = Button(window, text="Ajouter", command=add, bg="#a0d995", font=("Arial", 12))
button_add.pack(pady=2)

button_delete = Button(window, text="Supprimer les tâches cochées", command=delete, bg="#f68b8b", font=("Arial", 12))
button_delete.pack(pady=2)

# Label pour afficher les messages d'information
label = Label(window, text="", font=("Arial", 12))
label.pack(pady=5)

# Lancement de la fenêtre
window.mainloop()
