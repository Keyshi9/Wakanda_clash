"""Configuration centrale de WAKANDA CLASH (issue #7).

Tous les réglages du jeu sont ici : dimensions, couleurs, élixir, troupes,
tours, combat et vagues. Aucune autre partie du code ne doit contenir de
« nombre magique » : pour équilibrer le jeu, on modifie seulement ce fichier.

Les valeurs de combat sont des PROPOSITIONS du cahier des charges (à ajuster).
"""

# ---------------------------------------------------------------------------
# Fenêtre et arène (fenêtre verticale)
# ---------------------------------------------------------------------------
LARGEUR = 480                      # largeur de la fenêtre en pixels
HAUTEUR = 800                      # hauteur de la fenêtre en pixels
HAUTEUR_ARENE = 640                # hauteur de l'arène ; le reste (en bas) est le HUD
MILIEU = HAUTEUR_ARENE // 2        # y de la ligne pointillée centrale
FPS = 60                           # images par seconde

# ---------------------------------------------------------------------------
# Joueurs (identifiants)
# ---------------------------------------------------------------------------
JOUEUR = 1                         # le joueur humain : camp bleu, en haut
ADVERSAIRE = 2                     # l'ordinateur : camp rouge, en bas

# ---------------------------------------------------------------------------
# Couleurs (rouge, vert, bleu)
# ---------------------------------------------------------------------------
BLANC = (255, 255, 255)
NOIR = (30, 30, 30)
GRIS = (110, 110, 110)
GRIS_LIGNE = (150, 150, 150)
TEXTE = (90, 90, 90)
FOND_HUD = (250, 250, 250)
BLEU_PALE = (224, 234, 250)        # fond du camp du joueur
ROUGE_PALE = (245, 228, 228)       # fond du camp adverse
BLEU_TOUR = (66, 133, 222)
ROUGE_TOUR = (212, 83, 83)
BLEU_BOUTON = (224, 234, 250)
BLEU_BORD = (40, 110, 210)

COULEURS_JOUEUR = {JOUEUR: BLEU_TOUR, ADVERSAIRE: ROUGE_TOUR}

# ---------------------------------------------------------------------------
# Tours (3 par camp, identiques)
# ---------------------------------------------------------------------------
NB_TOURS = 3                       # tours par camp
PV_TOUR = 1000                     # points de vie d'une tour (proposition)
TAILLE_TOUR = 44                   # côté du carré dessiné, en pixels
MARGE_TOUR = 40                    # distance entre la tour et le bord haut/bas de l'arène

# ---------------------------------------------------------------------------
# Élixir
# ---------------------------------------------------------------------------
ELIXIR_MAX = 10                    # la jauge s'arrête à 10 ; le surplus est perdu
ELIXIR_DEPART = 5                  # élixir au début de la partie
ELIXIR_PAR_SECONDE = 0.5           # 1 élixir toutes les 2 secondes

# ---------------------------------------------------------------------------
# Troupes : coût (élixir), PV, dégâts par coup, vitesse (pixels/seconde)
# ---------------------------------------------------------------------------
TROUPES = {
    "Soldat": {"cout": 3, "pv": 100, "degats": 20, "vitesse": 40},   # polyvalent
    "Tank":   {"cout": 5, "pv": 300, "degats": 30, "vitesse": 20},   # résistant et lent
    "Rapide": {"cout": 2, "pv": 60,  "degats": 10, "vitesse": 70},   # mobile et fragile
}
TYPES_TROUPES = tuple(TROUPES)     # ordre des boutons : Soldat, Tank, Rapide

RAYON_TROUPE = 8                   # rayon du point dessiné, en pixels

# ---------------------------------------------------------------------------
# Combat (identique pour toutes les troupes)
# ---------------------------------------------------------------------------
PORTEE = 24                        # distance (px) à laquelle une troupe s'arrête pour frapper
COUPS_PAR_SECONDE = 1              # cadence d'attaque : un coup par seconde

# ---------------------------------------------------------------------------
# Vagues ennemies (l'adversaire n'a pas d'élixir)
# ---------------------------------------------------------------------------
# (secondes après le début, composition)
VAGUES = [
    (15,  {"Soldat": 2}),
    (40,  {"Soldat": 3}),
    (65,  {"Soldat": 3, "Rapide": 1}),
    (90,  {"Soldat": 2, "Tank": 1}),
    (115, {"Soldat": 3, "Rapide": 1, "Tank": 1}),
]
INTERVALLE_VAGUES = 25             # ensuite : une vague toutes les 25 secondes...
VAGUE_CROISSANCE = {"Soldat": 1}   # ...qui ajoute ces troupes à chaque nouvelle vague
