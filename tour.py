"""Classe Tour (issue #8) : logique pure, sans Pygame.

Une tour est un carré immobile qui possède un propriétaire, une position,
des points de vie et un état vivante/détruite. Elle ne tire pas dans le MVP.
"""
from config import PV_TOUR


class Tour:
    """Tour d'un camp : reçoit des dégâts et signale sa destruction."""

    def __init__(self, id, joueur_id, x, y, pv_max=PV_TOUR):
        if pv_max <= 0:
            raise ValueError("pv_max doit être strictement positif")
        self.id = id                  # identifiant unique dans la partie
        self.joueur_id = joueur_id    # propriétaire (JOUEUR ou ADVERSAIRE)
        self.x = x                    # position du centre, en pixels
        self.y = y
        self.pv_max = pv_max
        self.pv = pv_max              # une tour neuve est à pleine vie

    @property
    def vivante(self):
        """True tant que la tour a des points de vie."""
        return self.pv > 0

    def recevoir_degats(self, degats):
        """Retire des PV (jamais en dessous de 0).

        Renvoie True si CE coup détruit la tour (signal de destruction),
        False sinon. Une tour déjà détruite ne subit rien et renvoie False.
        """
        if degats < 0:
            raise ValueError("les dégâts ne peuvent pas être négatifs")
        if not self.vivante:
            return False
        self.pv = max(0, self.pv - degats)
        return not self.vivante

    def __repr__(self):
        etat = f"{self.pv}/{self.pv_max} PV" if self.vivante else "détruite"
        return f"Tour(id={self.id}, joueur={self.joueur_id}, ({self.x}, {self.y}), {etat})"
