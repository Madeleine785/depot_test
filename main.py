# Programme principal : gestion de notes
print("=== Gestion de notes ===")
print("Programme en cours de développement.")

# Programme principal : gestion de notes
from fonctions import saisir_notes, calculer_stats

print("=== Gestion de notes ===")
notes = saisir_notes()
moyenne, note_min, note_max = calculer_stats(notes)
print(f"Moyenne : {moyenne:.2f}")
print(f"Note la plus basse : {note_min}")
print(f"Note la plus haute : {note_max}")

# Programme principal : gestion de notes
from fonctions import saisir_notes, calculer_stats

notes = []

while True:
    print("\n=== Gestion de notes ===")
    print("1. Saisir des notes")
    print("2. Afficher les statistiques")
    print("3. Quitter")
    choix = input("Ton choix : ")

    if choix == "1":
        notes = saisir_notes()
    elif choix == "2":
        if notes:
            moyenne, note_min, note_max = calculer_stats(notes)
            print(f"Notes : {notes}")
            print(f"Moyenne : {moyenne:.2f} | Min : {note_min} | Max : {note_max}")
        else:
            print("Aucune note saisie pour l'instant.")
    elif choix == "3":
        print("Au revoir !")
        break
    else:
        print("Choix invalide, tape 1, 2 ou 3.")