# WAKANDA CLASH

Jeu de stratégie 2D vu de dessus (Python / Pygame) — projet ProjDev1.
Le joueur pose des troupes (Soldat, Tank, Rapide) pour protéger ses trois tours
et détruire les trois tours adverses. Version MVP : 1 joueur contre des vagues.

## Installation

Python 3.10 ou plus récent est nécessaire.

```bash
# 1. (conseillé) créer un environnement virtuel
python -m venv .venv

# 2. l'activer
#    Windows (PowerShell) : .venv\Scripts\Activate.ps1
#    Windows (cmd)        : .venv\Scripts\activate.bat
#    macOS / Linux        : source .venv/bin/activate

# 3. installer les dépendances
pip install -r requirements.txt
```

## Lancer le jeu

```bash
python accueil.py
```

## Organisation du dépôt

- `main` : version stable.
- `Develop` : branche d'intégration.
- `feature/...` : une branche par ticket, fusionnée dans `Develop` par pull request.
