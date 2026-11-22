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