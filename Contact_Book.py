import csv
import os
from tkinter import *

FILENAME = "contacts.csv"

def get_new_id():
    if not os.path.exists(FILENAME):
        return 1
    with open(FILENAME, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)
        return int(rows[-1][0]) + 1 if rows else 1

def add_contact_window():
    def add_contact():
        name, phone, email, address = entry_name.get(), entry_phone.get(), entry_email.get(), entry_address.get()
        if name and phone:
            with open(FILENAME, mode="a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([get_new_id(), name, phone, email, address])
            status_label.config(text="Contact ajouté !", fg="green")
        else:
            status_label.config(text="Nom et téléphone requis!", fg="red")
    
    win = Toplevel()
    win.title("Ajouter un contact")
    Label(win, text="Nom").pack()
    entry_name = Entry(win)
    entry_name.pack()
    Label(win, text="Téléphone").pack()
    entry_phone = Entry(win)
    entry_phone.pack()
    Label(win, text="Email").pack()
    entry_email = Entry(win)
    entry_email.pack()
    Label(win, text="Adresse").pack()
    entry_address = Entry(win)
    entry_address.pack()
    Button(win, text="Ajouter", command=add_contact).pack()
    status_label = Label(win, text="")
    status_label.pack()

def search_contact_window():
    def search_contact():
        search_term = entry_search.get().strip()
        found = False
        with open(FILENAME, "r", encoding="utf-8") as file:
            for row in csv.reader(file):
                if row and (row[1].lower() == search_term.lower() or row[2] == search_term):
                    result_label.config(text=f"Trouvé: {row}", fg="blue")
                    found = True
                    break
        if not found:
            result_label.config(text="Contact introuvable", fg="red")
    
    win = Toplevel()
    win.title("Rechercher un contact")
    Label(win, text="Nom ou Téléphone").pack()
    entry_search = Entry(win)
    entry_search.pack()
    Button(win, text="Rechercher", command=search_contact).pack()
    result_label = Label(win, text="")
    result_label.pack()

def view_contacts_window():
    win = Toplevel()
    win.title("Liste des contacts")
    text_area = Text(win, height=15, width=60)
    text_area.pack()
    text_area.insert(END, "ID | Nom | Téléphone | Email | Adresse\n")
    text_area.insert(END, "-" * 50 + "\n")
    with open(FILENAME, "r", encoding="utf-8") as file:
        for row in csv.reader(file):
            if row:
                text_area.insert(END, " | ".join(row) + "\n")

def delete_contact_window():
    def delete_contact():
        contact_id = entry_delete.get().strip()
        if contact_id.isdigit():
            contact_id = int(contact_id)
            contacts, deleted = [], False
            with open(FILENAME, "r", encoding="utf-8") as file:
                for row in csv.reader(file):
                    if row and int(row[0]) == contact_id:
                        deleted = True
                    else:
                        contacts.append(row)
            if deleted:
                with open(FILENAME, "w", newline="", encoding="utf-8") as file:
                    csv.writer(file).writerows(contacts)
                status_label.config(text="Contact supprimé!", fg="green")
            else:
                status_label.config(text="ID introuvable!", fg="red")
    
    win = Toplevel()
    win.title("Supprimer un contact")
    Label(win, text="ID du contact").pack()
    entry_delete = Entry(win)
    entry_delete.pack()
    Button(win, text="Supprimer", command=delete_contact).pack()
    status_label = Label(win, text="")
    status_label.pack()

def update_contact_window():
    def update_contact():
        contact_id = entry_update.get().strip()
        if contact_id.isdigit():
            contact_id, contacts, updated = int(contact_id), [], False
            with open(FILENAME, "r", encoding="utf-8") as file:
                for row in csv.reader(file):
                    if row and int(row[0]) == contact_id:
                        new_name = entry_new_name.get() or row[1]
                        new_phone = entry_new_phone.get() or row[2]
                        new_email = entry_new_email.get() or row[3]
                        new_address = entry_new_address.get() or row[4]
                        row = [str(contact_id), new_name, new_phone, new_email, new_address]
                        updated = True
                    contacts.append(row)
            if updated:
                with open(FILENAME, "w", newline="", encoding="utf-8") as file:
                    csv.writer(file).writerows(contacts)
                status_label.config(text="Contact mis à jour!", fg="green")
            else:
                status_label.config(text="ID introuvable!", fg="red")
    
    win = Toplevel()
    win.title("Mettre à jour un contact")
    Label(win, text="ID du contact").pack()
    entry_update = Entry(win)
    entry_update.pack()
    Label(win, text="Nouveau Nom").pack()
    entry_new_name = Entry(win)
    entry_new_name.pack()
    Label(win, text="Nouveau Téléphone").pack()
    entry_new_phone = Entry(win)
    entry_new_phone.pack()
    Label(win, text="Nouvel Email").pack()
    entry_new_email = Entry(win)
    entry_new_email.pack()
    Label(win, text="Nouvelle Adresse").pack()
    entry_new_address = Entry(win)
    entry_new_address.pack()
    Button(win, text="Mettre à jour", command=update_contact).pack()
    status_label = Label(win, text="")
    status_label.pack()

window = Tk()
window.title("Gestion des Contacts")
Button(window, text="Ajouter Contact", command=add_contact_window,fg="blue").pack(pady =10)
Button(window, text="Rechercher Contact", command=search_contact_window,fg="blue").pack(pady =10)
Button(window, text="Voir Contacts", command=view_contacts_window,fg="blue").pack(pady =10)
Button(window, text="Supprimer Contact", command=delete_contact_window,fg="blue").pack(pady =10)
Button(window, text="Mettre à jour Contact", command=update_contact_window,fg="blue").pack(pady =10)
window.mainloop()
