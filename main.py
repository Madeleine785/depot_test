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