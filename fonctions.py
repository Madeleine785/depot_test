# Fonctions du programme de gestion de notes

def saisir_notes():
    """Demande des notes à l'utilisateur et renvoie une liste."""
    notes = []
    nb = int(input("Combien de notes ? "))
    for i in range(nb):
        note = float(input(f"Note {i + 1} : "))
        notes.append(note)
    return notes# Fonctions du programme de gestion de notes



def calculer_stats(notes):
    """Renvoie la moyenne, la note la plus basse et la plus haute."""
    moyenne = sum(notes) / len(notes)
    return moyenne, min(notes), max(notes)


def saisir_note(numero):
    """Redemande tant que la note n'est pas un nombre entre 0 et 20."""
    while True:
        texte = input(f"Note {numero} : ").replace(",", ".")
        try:
            note = float(texte)
        except ValueError:
            print("Erreur : tape un nombre (ex : 12.5).")
            continue
        if 0 <= note <= 20:
            return note
        print("Erreur : la note doit être entre 0 et 20.")


def saisir_notes():
    """Demande le nombre de notes puis chaque note, et renvoie une liste."""
    while True:
        try:
            nb = int(input("Combien de notes ? "))
            if nb > 0:
                break
        except ValueError:
            pass
        print("Erreur : tape un nombre entier supérieur à 0.")
    notes = []
    for i in range(nb):
        notes.append(saisir_note(i + 1))
    return notes


def calculer_stats(notes):
    """Renvoie la moyenne, la note la plus basse et la plus haute."""
    moyenne = sum(notes) / len(notes)
    return moyenne, min(notes), max(notes)