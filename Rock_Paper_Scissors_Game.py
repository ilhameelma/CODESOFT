from tkinter import *
import random

# Liste des choix possibles avec leurs émojis
choices = {
    "rock": "✊",
    "paper": "🖐",
    "scissors": "✌"
}

score = 0  # Score du joueur

# Fonction pour ouvrir la fenêtre du score
def open_score_window():
    score_window = Toplevel(window)  # Créer une nouvelle fenêtre secondaire
    score_window.title("Score Window")
    score_window.geometry("300x200")

    # Ajouter un label pour afficher le score
    label_score_window = Label(score_window, text=f"🏆 Score: {score}", font=("Arial", 14))
    label_score_window.pack(pady=20)

    # Ajouter des boutons "Yes" et "No"
    label_jouer= Label(score_window,text="you want play again")
    label_jouer.pack()
    Button(score_window, text="Yes", command=game, fg="green").pack(side=LEFT, padx=50, pady=10)
    Button(score_window, text="No", command=window.quit, fg="red").pack(side=RIGHT, padx=50, pady=10)

# Fonction principale du jeu
def game():
    global score  # Utilisation de la variable globale score

    # Vérifier la sélection de l'utilisateur via les checkboxes
    if var_rock.get() == 1:
        choice_user = "rock"
    elif var_paper.get() == 1:
        choice_user = "paper"
    elif var_scissors.get() == 1:
        choice_user = "scissors"
    else:
        label_result.config(text="Please select an option (Rock, Paper, Scissors)", fg="red")
        return

    choice_computer = random.choice(list(choices.keys()))  # Choix aléatoire de l'ordinateur

    # Mettre à jour l'affichage des choix avec des émojis
    label_resultat.config(text=f"You: {choices[choice_user]}")
    label_computer.config(text=f"Computer: {choices[choice_computer]}")

    # Déterminer le résultat
    if (choice_computer == "rock" and choice_user == "scissors") or \
       (choice_computer == "paper" and choice_user == "rock") or \
       (choice_computer == "scissors" and choice_user == "paper"):
        label_result.config(text="❌ You lost!", fg="red")

    elif choice_computer == choice_user:
        label_result.config(text="🔄 It's a tie!", fg="blue")

    else:
        score += 1  # Augmenter le score
        label_result.config(text="✅ You won!", fg="green")

    # Mettre à jour le score affiché
    label_score.config(text=f"🏆 Score: {score}")

    # Ouvrir la fenêtre du score
    open_score_window()

# Création de la fenêtre principale
window = Tk()
window.title("Rock Paper Scissors Game")
window.geometry("500x600")  # Augmenter la taille de la fenêtre pour avoir plus d'espace

# Variables pour stocker l'état des checkbox (coché ou décoché)
var_rock = IntVar()
var_paper = IntVar()
var_scissors = IntVar()

# Labels et boutons
Label(window, text="🎮 Rock Paper Scissors!", font=("Arial", 14)).pack(pady=10)
Label(window, text="Select your choice (rock, paper, scissors):").pack(pady=5)

# Affichage des images et checkbox
frame = Frame(window)
frame.pack(pady=20)

image_rock = PhotoImage(file="rock1.png").subsample(5, 5)
image_paper = PhotoImage(file="paper.png").subsample(5, 5)
image_scissors = PhotoImage(file="scisor.png").subsample(5, 5)

# Labels pour les images
label_rock = Label(frame, image=image_rock)
label_rock.grid(row=0, column=0, padx=10)

label_paper = Label(frame, image=image_paper)
label_paper.grid(row=0, column=1, padx=10)

label_scissors = Label(frame, image=image_scissors)
label_scissors.grid(row=0, column=2, padx=10)

# Checkbuttons à côté des images
checkbox_rock = Checkbutton(frame, text="Rock", variable=var_rock)
checkbox_rock.grid(row=1, column=0)

checkbox_paper = Checkbutton(frame, text="Paper", variable=var_paper)
checkbox_paper.grid(row=1, column=1)

checkbox_scissors = Checkbutton(frame, text="Scissors", variable=var_scissors)
checkbox_scissors.grid(row=1, column=2)

# Bouton de validation
button = Button(window, text="Submit", command=game, fg="green")
button.pack(pady=5)

# Labels pour les résultats
label_resultat = Label(window, text="You: ❓", font=("Arial", 20))
label_resultat.pack(pady=10)

label_computer = Label(window, text="Computer: ❓", font=("Arial", 20))
label_computer.pack(pady=10)

label_result = Label(window, text="", font=("Arial", 14))
label_result.pack(pady=10)

# Label du score
label_score = Label(window, text="🏆 Score: 0", font=("Arial", 14))
label_score.pack(pady=5)

# Lancement de la fenêtre principale
window.mainloop()
