"""Maquette statique de l'arène WAKANDA CLASH (issue #6).

Camp du joueur en haut (bleu pâle), camp adverse en bas (rouge pâle),
ligne pointillée « Arène » au milieu, trois tours carrées par camp.
"""
import pygame

from config import (
    LARGEUR, HAUTEUR, HAUTEUR_ARENE, MILIEU, FPS,
    BLEU_PALE, ROUGE_PALE, BLEU_TOUR, ROUGE_TOUR, GRIS_LIGNE, FOND_HUD, TEXTE,
    TAILLE_TOUR, MARGE_TOUR, JOUEUR, ADVERSAIRE,
)
from tour import Tour


def dessiner_tour(ecran, tour, couleur):
    """Dessine une tour vivante sous forme de carré (l'affichage reste ici, pas dans Tour)."""
    rect = pygame.Rect(0, 0, TAILLE_TOUR, TAILLE_TOUR)
    rect.center = (tour.x, tour.y)
    pygame.draw.rect(ecran, couleur, rect, border_radius=6)


class Arene:
    """Dessine le terrain fixe et ses six tours (la logique des tours est dans tour.py)."""

    def __init__(self):
        colonnes = [LARGEUR // 4, LARGEUR // 2, 3 * LARGEUR // 4]
        y_joueur = MARGE_TOUR + TAILLE_TOUR // 2
        y_adverse = HAUTEUR_ARENE - MARGE_TOUR - TAILLE_TOUR // 2
        self.tours_joueur = [Tour(i, JOUEUR, x, y_joueur) for i, x in enumerate(colonnes)]
        self.tours_adverses = [Tour(3 + i, ADVERSAIRE, x, y_adverse) for i, x in enumerate(colonnes)]
        self.police = pygame.font.SysFont("arial", 18)

    def _ligne_pointillee(self, ecran):
        longueur, espace = 12, 8
        for x in range(0, LARGEUR, longueur + espace):
            pygame.draw.line(ecran, GRIS_LIGNE, (x, MILIEU), (min(x + longueur, LARGEUR), MILIEU), 2)

    def draw(self, ecran):
        ecran.fill(BLEU_PALE, (0, 0, LARGEUR, MILIEU))
        ecran.fill(ROUGE_PALE, (0, MILIEU, LARGEUR, HAUTEUR_ARENE - MILIEU))
        self._ligne_pointillee(ecran)
        label = self.police.render("Arène", True, TEXTE)
        ecran.blit(label, label.get_rect(midbottom=(LARGEUR // 2, MILIEU - 4)))
        for tour in self.tours_joueur:
            if tour.vivante:
                dessiner_tour(ecran, tour, BLEU_TOUR)
        for tour in self.tours_adverses:
            if tour.vivante:
                dessiner_tour(ecran, tour, ROUGE_TOUR)
        # zone HUD vide (élixir et boutons viendront plus tard)
        ecran.fill(FOND_HUD, (0, HAUTEUR_ARENE, LARGEUR, HAUTEUR - HAUTEUR_ARENE))
        pygame.draw.line(ecran, GRIS_LIGNE, (0, HAUTEUR_ARENE), (LARGEUR, HAUTEUR_ARENE), 1)


def main():
    pygame.init()
    ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
    pygame.display.set_caption("WAKANDA CLASH — maquette arène")
    horloge = pygame.time.Clock()
    arene = Arene()

    en_cours = True
    while en_cours:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                en_cours = False
        arene.draw(ecran)
        pygame.display.flip()
        horloge.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    main()
