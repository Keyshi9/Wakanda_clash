# Écran d'accueil de WAKANDA CLASH (issue #18)
# Affiche le titre et un bouton « Jouer ». Un clic sur le bouton lance la partie.

import pygame  # on importe la bibliothèque Pygame pour faire la fenêtre et les dessins
from arena import Arene  # on reprend l'arène de arena.py
from config import LARGEUR, HAUTEUR, FPS, BLANC, NOIR, GRIS, BLEU_BOUTON, BLEU_BORD  # tous les réglages viennent de config.py


class EcranAccueil:
    """Écran avec le titre du jeu et le bouton « Jouer »."""

    def __init__(self):
        self.police_titre = pygame.font.SysFont("arial", 40, bold=True)  # grande police pour le titre
        self.police_texte = pygame.font.SysFont("arial", 20)  # petite police pour le sous-titre et le bouton
        self.bouton = pygame.Rect(0, 0, 160, 50)  # rectangle du bouton : 160 px de large, 50 px de haut
        self.bouton.center = (LARGEUR // 2, HAUTEUR // 2 + 40)  # on place le bouton au milieu, un peu plus bas

    def clic_sur_jouer(self, position):
        """Renvoie True si la position de la souris est dans le bouton."""
        return self.bouton.collidepoint(position)  # collidepoint vérifie si le point est dans le rectangle

    def draw(self, ecran):
        """Dessine tout l'écran d'accueil."""
        ecran.fill(BLANC)  # on efface l'écran en le remplissant de blanc

        titre = self.police_titre.render("WAKANDA CLASH", True, NOIR)  # on crée l'image du texte du titre
        ecran.blit(titre, titre.get_rect(center=(LARGEUR // 2, HAUTEUR // 2 - 80)))  # on colle le titre en haut du centre

        sous_titre = self.police_texte.render("Un joueur contre des vagues", True, GRIS)  # on crée le sous-titre
        ecran.blit(sous_titre, sous_titre.get_rect(center=(LARGEUR // 2, HAUTEUR // 2 - 35)))  # on le colle sous le titre

        pygame.draw.rect(ecran, BLEU_BOUTON, self.bouton, border_radius=8)  # on dessine l'intérieur du bouton
        pygame.draw.rect(ecran, BLEU_BORD, self.bouton, width=2, border_radius=8)  # on dessine le bord du bouton

        texte = self.police_texte.render("Jouer", True, NOIR)  # on crée le texte « Jouer »
        ecran.blit(texte, texte.get_rect(center=self.bouton.center))  # on colle le texte au centre du bouton


def main():
    pygame.init()  # on démarre Pygame
    ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))  # on ouvre la fenêtre verticale
    pygame.display.set_caption("WAKANDA CLASH")  # on écrit le nom du jeu dans la barre de la fenêtre
    horloge = pygame.time.Clock()  # l'horloge sert à limiter le jeu à 60 images par seconde

    accueil = EcranAccueil()  # on crée l'écran d'accueil
    arene = Arene()  # on crée l'arène (l'écran de la partie)
    ecran_actuel = "accueil"  # on commence sur l'écran d'accueil

    en_cours = True  # tant que c'est True, le jeu continue
    while en_cours:  # boucle principale : elle tourne 60 fois par seconde
        for evenement in pygame.event.get():  # on regarde tout ce que le joueur a fait (clics, touches...)
            if evenement.type == pygame.QUIT:  # si le joueur ferme la fenêtre
                en_cours = False  # on arrête la boucle
            if evenement.type == pygame.MOUSEBUTTONDOWN and ecran_actuel == "accueil":  # clic pendant l'accueil
                if accueil.clic_sur_jouer(evenement.pos):  # si le clic est sur le bouton « Jouer »
                    ecran_actuel = "partie"  # on passe à l'écran de la partie

        if ecran_actuel == "accueil":  # si on est sur l'accueil
            accueil.draw(ecran)  # on dessine l'accueil
        else:  # sinon on est dans la partie
            arene.draw(ecran)  # on dessine l'arène

        pygame.display.flip()  # on affiche à l'écran tout ce qu'on vient de dessiner
        horloge.tick(FPS)  # on attend un peu pour rester au nombre d'images par seconde voulu

    pygame.quit()  # on ferme Pygame proprement


if __name__ == "__main__":  # ce bloc s'exécute seulement si on lance ce fichier directement
    main()  # on lance le jeu
