# Space Invaders : Comment Fonctionne Notre Code

> **Guide Pratique — Projet de Groupe**  
> *Explication simple étape par étape, pensée même pour ceux qui n'ont jamais programmé auparavant.*

---

## Commençons par les bases : les personnages du jeu

Si vous y réfléchissez, **Space Invaders** comporte très peu d'éléments à l'écran, moins que les doigts d'une main. En informatique, on les appelle des **entités** :

* **Le `player` (canon)** : notre vaisseau en bas qui se déplace vers la droite et vers la gauche.
* **Le `laser`** : le projectile. Il est séparé du canon car, une fois tiré, il doit voler tout seul pendant que nous continuons à bouger.
* **Les `aliens`** : toute l'équipe ennemie, regroupée dans une seule grande liste.
* **Le Boss final** : nous l'ajouterons plus tard. Pour ce week-end, nous nous concentrons uniquement sur les 3 premiers.

---

### Comment nous construisons les personnages : les Dictionnaires

Pour créer chaque personnage, nous utilisons un **dictionnaire**. Imaginez-le comme la fiche de statistiques (*stats*) d'un jeu vidéo : à chaque étiquette — appelée **clé** — on associe une **valeur**.

La fonction `player(x, y)` crée et nous renvoie cette fiche avec 4 clés (les deux vitesses `v_x` et `v_y` démarrent à `0.0`, tandis que `x` et `y` sont les coordonnées de départ) :

```python
# Création du dictionnaire player (lignes 112-119 et 183)
# Patrick - S2600934
def player(x, y):
    return {
        "v_x": 0.0,
        "v_y": 0.0,
        "x": x,
        "y": y
    }

player_1 = player(100.0, 400.0)