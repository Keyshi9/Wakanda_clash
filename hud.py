# HUD de WAKANDA CLASH (issue #20)
# Affiché sous l'arène : la jauge d'élixir « X/10 » et les trois boutons de troupes.
# La troupe choisie est mise en surbrillance et son coût est affiché.

import pygame  # on importe Pygame pour dessiner
from config import LARGEUR, HAUTEUR_ARENE, ELIXIR_MAX, NOIR, BLANC  # réglages communs de config.py
from config import BLEU_BOUTON as BLEU_PALE, BLEU_BORD as BLEU  # couleurs du bouton sélectionné
from config import TROUPES as STATS_TROUPES, TYPES_TROUPES  # statistiques et ordre des troupes

# --- Couleurs propres au HUD (rouge, vert, bleu) ---
GRIS = (190, 190, 190)  # couleur du bord d'un segment vide et d'un bouton normal
VERT = (60, 180, 140)  # couleur d'un segment plein de la jauge

# Les trois troupes avec leur coût, dans l'ordre des boutons (coûts lus dans config.py)
TROUPES = [(nom, STATS_TROUPES[nom]["cout"]) for nom in TYPES_TROUPES]


class HUD:
    """Barre du bas : jauge d'élixir et boutons de troupes."""

    def __init__(self):
        self.police = pygame.font.SysFont("arial", 18)  # police normale
        self.petite_police = pygame.font.SysFont("arial", 14)  # petite police pour les coûts
        self.selection = None  # au départ, aucune troupe n'est choisie

        self.boutons = []  # liste des rectangles des trois boutons
        largeur_bouton = 120  # largeur d'un bouton en pixels
        espace = (LARGEUR - 3 * largeur_bouton) // 4  # espace égal entre les boutons et les bords
        for i in range(3):  # on crée les trois boutons, un par troupe
            x = espace + i * (largeur_bouton + espace)  # position horizontale du bouton numéro i
            self.boutons.append(pygame.Rect(x, HAUTEUR_ARENE + 70, largeur_bouton, 55))  # on ajoute le bouton

    def clic(self, position):
        """Si le clic tombe sur un bouton, on sélectionne cette troupe."""
        for i in range(3):  # on teste les trois boutons
            if self.boutons[i].collidepoint(position):  # si la souris est dans ce bouton
                self.selection = TROUPES[i][0]  # on retient le nom de la troupe choisie
                return True  # on dit que le clic a été utilisé
        return False  # le clic n'était sur aucun bouton

    def cout_selection(self):
        """Renvoie le coût de la troupe choisie, ou None si rien n'est choisi."""
        for nom, cout in TROUPES:  # on parcourt la liste des troupes
            if nom == self.selection:  # si c'est la troupe sélectionnée
                return cout  # on renvoie son coût
        return None  # aucune troupe n'est sélectionnée

    def draw(self, ecran, elixir):
        """Dessine la jauge (avec la valeur elixir) et les boutons."""
        # --- Jauge d'élixir ---
        texte = self.police.render("Élixir " + str(elixir) + "/10", True, NOIR)  # texte « Élixir X/10 »
        ecran.blit(texte, (20, HAUTEUR_ARENE + 25))  # on le place à gauche, en haut du HUD

        for i in range(ELIXIR_MAX):  # on dessine les 10 segments
            case = pygame.Rect(130 + i * 33, HAUTEUR_ARENE + 25, 28, 20)  # rectangle du segment numéro i
            if i < elixir:  # si ce segment est rempli
                pygame.draw.rect(ecran, VERT, case, border_radius=4)  # on le dessine en vert plein
            else:  # sinon le segment est vide
                pygame.draw.rect(ecran, GRIS, case, width=1, border_radius=4)  # on dessine juste son bord

        # --- Boutons des troupes ---
        for i in range(3):  # on dessine les trois boutons
            nom, cout = TROUPES[i]  # nom et coût de la troupe de ce bouton
            bouton = self.boutons[i]  # rectangle de ce bouton
            if nom == self.selection:  # si c'est la troupe sélectionnée
                pygame.draw.rect(ecran, BLEU_PALE, bouton, border_radius=8)  # fond bleu pâle
                pygame.draw.rect(ecran, BLEU, bouton, width=3, border_radius=8)  # bord bleu épais
            else:  # sinon c'est un bouton normal
                pygame.draw.rect(ecran, BLANC, bouton, border_radius=8)  # fond blanc
                pygame.draw.rect(ecran, GRIS, bouton, width=1, border_radius=8)  # bord gris fin

            titre = self.police.render(nom, True, NOIR)  # texte du nom de la troupe
            ecran.blit(titre, titre.get_rect(center=(bouton.centerx, bouton.y + 18)))  # en haut du bouton
            prix = self.petite_police.render("coût " + str(cout), True, NOIR)  # texte du coût
            ecran.blit(prix, prix.get_rect(center=(bouton.centerx, bouton.y + 40)))  # en bas du bouton

        # --- Coût de la troupe choisie ---
        if self.selection is not None:  # seulement si une troupe est choisie
            info = self.petite_police.render(self.selection + " choisi : coût " + str(self.cout_selection()), True, NOIR)
            ecran.blit(info, info.get_rect(center=(LARGEUR // 2, HAUTEUR_ARENE + 140)))  # sous les boutons
