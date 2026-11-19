"""Maquette statique de l'arène WAKANDA CLASH (issue #6).

Camp du joueur en haut (bleu pâle), camp adverse en bas (rouge pâle),
ligne pointillée « Arène » au milieu, trois tours carrées par camp.
"""
import pygame

# --- Dimensions (fenêtre verticale) ---
LARGEUR = 480
HAUTEUR = 800
HAUTEUR_ARENE = 640          # le reste (en bas) est réservé au HUD
MILIEU = HAUTEUR_ARENE // 2

# --- Couleurs ---
BLEU_PALE = (224, 234, 250)
ROUGE_PALE = (245, 228, 228)
BLEU_TOUR = (66, 133, 222)
ROUGE_TOUR = (212, 83, 83)
GRIS_LIGNE = (150, 150, 150)
FOND_HUD = (250, 250, 250)
TEXTE = (90, 90, 90)

TAILLE_TOUR = 44
MARGE_TOUR = 40              # distance entre la tour et le bord haut/bas de l'arène


class Tour:
    """Tour carrée immobile (affichage seulement pour la maquette)."""

    def __init__(self, x, y, couleur):
        self.x = x
        self.y = y
        self.couleur = couleur

    def draw(self, ecran):
        rect = pygame.Rect(0, 0, TAILLE_TOUR, TAILLE_TOUR)
        rect.center = (self.x, self.y)
        pygame.draw.rect(ecran, self.couleur, rect, border_radius=6)


class Arene:
    """Dessine le terrain fixe et ses six tours."""

    def __init__(self):
        colonnes = [LARGEUR // 4, LARGEUR // 2, 3 * LARGEUR // 4]
        y_joueur = MARGE_TOUR + TAILLE_TOUR // 2
        y_adverse = HAUTEUR_ARENE - MARGE_TOUR - TAILLE_TOUR // 2
        self.tours_joueur = [Tour(x, y_joueur, BLEU_TOUR) for x in colonnes]
        self.tours_adverses = [Tour(x, y_adverse, ROUGE_TOUR) for x in colonnes]
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
        for tour in self.tours_joueur + self.tours_adverses:
            tour.draw(ecran)
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
        horloge.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()
