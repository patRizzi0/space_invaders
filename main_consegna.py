import pygame

#@Patrick
#@S2600934
#Configuration initiale


#Size
WIDTH = 800
HEIGHT = 500
FPS = 60

# Entities
SQUARE_SIZE = 50 # Sostituisci con la grandezza reale del tuo quadrato

# Boundaries
LIMIT_TOP = 0.0
LIMIT_LEFT = 0.0
LIMIT_BOTTOM = float(HEIGHT - SQUARE_SIZE)
LIMIT_RIGHT = float(WIDTH - SQUARE_SIZE)

LIMIT_LEFT_ALIENS = 100
LIMIT_RIGHT_ALIENS = float(WIDTH - 100)

#Colors
BLACK = (0, 0, 0)
RED = (100, 0, 0)
WHITE = (255, 255, 255)

#Grandezze
WIDTH_ALIEN = 25
HEIGHT_ALIEN = 25

WIDTH_LASER = 5
HEIGHT_LASER = 10

WIDTH_RECT = 50
HEIGHT_RECT = 30

#Physique de jeu
# s = s0 + v * dt
def mru_1D_horizontal_player(player_1,dt):
    player_1["x"] += player_1["v_x"] * dt

def mru_1D_horizontal_aliens(aliens_1,dt):
    aliens_1["x"] += aliens_1["v_x"] * dt

def mru_1D_vertical(laser_1,dt_laser):
    #@Patrick
    #ça c'est pour les laser. Mouvement verical
    laser_1["y"] += laser_1["v_y"] * dt_laser

#Mechanique du clavier
def input_handler(player_1, laser_1):
    running = True
    for event in pygame.event.get():
        if event_quit(event):
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player_1["v_x"] = -270
            if event.key == pygame.K_d:
                player_1["v_x"] = 270
            # @Patrick
            # Activation de l'état du laser et assignation de la vitesse verticale lors de l'appui sur la touche G.
            if event.key == pygame.K_g:
                if laser_1["is_fired"] == False:
                    laser_1["is_fired"] = True
                    laser_1["v_y"] = -300

        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_a, pygame.K_d):
                player_1["v_x"] = 0.0
    return running


# @Patrick
# Initialise et retourne la fenêtre principale de Pygame avec les dimensions spécifiées.
def create_window(width, height):
    pygame.init()
    return pygame.display.set_mode((width, height))

# @Patrick
# Vérifie si l'événement actuel correspond à la fermeture de la fenêtre (clic sur la croix).
def event_quit(event):
    return event.type == pygame.QUIT

# @Patrick
# S2600934
#Fonction dediées à la creation de toute objet qui viens sur écran.
def draw_aliens(window,x,y):
    pygame.draw.rect(window, WHITE,(int(x),int(y), WIDTH_ALIEN, HEIGHT_ALIEN))

def draw_laser(window,x,y):
    pygame.draw.rect(window, WHITE,(int(x),int(y), WIDTH_LASER, HEIGHT_LASER))

def draw_rect(window,x,y):
    pygame.draw.rect(window, RED,(int(x),int(y), WIDTH_RECT, HEIGHT_RECT))


#Initialisation de la fenetre
window = create_window(WIDTH, HEIGHT)


#Définition des entités - dict{}
#Player
#Patrick - S2600934
def player(x,y):
    #Hadjer fait le système de score, commence par ici.
    return {
        "v_x": 0.0,
        "v_y": 0.0,
        "x": x,
        "y": y
    }
def laser(x,y):
    return {
        "v_x": 0.0,
        "v_y": 0.0,
        "x": x,
        "y": y,
        # @Patrick
        # État du laser : True = en vol/visible, False (au sommet) = rechargé.
        "is_fired": False
    }
def aliens(x,y, points):
    return {
        "v_x": 20.0,
        "v_y": 0.0,
        "x": x,
        "y": y,
        "points": points
    }

def set_barriers(player_1, laser_1):
    if player_1["x"] >= LIMIT_RIGHT:
        player_1["x"] = LIMIT_RIGHT
        player_1["v_x"] = 0.0

    elif player_1["x"] <= 0.0:
        player_1["x"] = 0.0
        player_1["v_x"] = 0.0
    # @Patrick
    # Réinitialisation du laser (machine à états) lorsqu'il atteint la limite supérieure de la fenêtre.
    if laser_1["y"] <= 0.0:
        laser_1["is_fired"] = False
        laser_1["v_y"] = 0.0

def set_barriers_aliens(alien_list):
    #@Patrick
    #@S2600934

    if len(alien_list) == 0:
        return

    left_alien = alien_list[0]["x"]
    right_alien = alien_list[0]["x"]

    for alien in alien_list:
        if alien["x"] < left_alien:
            left_alien = alien["x"]
        if alien["x"] > right_alien:
            right_alien = alien["x"]


    if right_alien + WIDTH_ALIEN >=WIDTH or left_alien <= 0:
        for alien in alien_list:
            alien["v_x"] = -alien["v_x"]
            alien["y"] += 20

#Creation de laser - le laser prend les memes valeurs initiales que le player evidemment
player_1 = player(100.0, 400.0)
laser_1 = laser(player_1["x"], player_1["y"])
#Creation des aliens
alien_list = []
espace_x = 0
espace_y = 0

# TÂCHE 2 (à faire après la tâche 1) : des points différents selon l'alien.
#J'ai rangé pour toi un petit peu le code, maintenant le dict alien il a aussi un clé "points" (ligne 126)
#En fait, je t'ai pas encore expliqué les conditions. Pour mieux comprendre le code qui va de ligne 187 à 196, utilise l'AI.
# (regarde la fonction aliens et la boucle qui crée la grille d'aliens).

# À faire : au lieu d'ajouter 1 indipendemment de l'alien qu'on touche, ajoute les points de l'alien touché.
# Indice : alien["points"] te donne la valeur de l'alien qui vient d'être touché.
# Si tout fonctionne, toucher un alien de la rangée du haut rapporte
# plus de points que toucher un alien de la rangée du bas.

for i in range(5):
    for j in range(11):
        if i == 0:
            points = 5
        elif i == 1:
            points = 3
        elif i == 2:
            points = 2
        else:
            points = 1
        new_alien = aliens(100 + espace_x, 100 + espace_y, points)
        alien_list.append(new_alien)
        espace_x += 50

    espace_y += 35
    espace_x = 0


#Ici on initalise le score
score = 0
time = pygame.time.Clock()
running = True
while running:
    running = input_handler(player_1, laser_1)

    dt_ms = time.tick(FPS)
    dt = dt_ms / 1000
    #Toute la partie physique
    mru_1D_horizontal_aliens(player_1,dt) 

    if(laser_1["is_fired"] == False):
        laser_1["x"] = player_1["x"]
        laser_1["y"] = player_1["y"]
    else:
        mru_1D_vertical(laser_1,dt)


    

    #Patrick
    #@S2600934
    #Collisione alieno laser
    for alien in alien_list:
        if laser_1["is_fired"] == True:
            if alien["x"] + WIDTH_ALIEN > laser_1["x"] and alien["x"] < laser_1["x"] + WIDTH_LASER and alien["y"] + HEIGHT_ALIEN > laser_1["y"] and alien["y"] < laser_1["y"] + HEIGHT_LASER:
                alien_list.remove(alien)
                # Hadjer, travaille dans cette boucle. Pour mardi, fais le système de score :
                # c'est un bon moyen de te familiariser avec le code.
                # Tout ce dont tu as besoin se trouve dans cette boucle.
                # À faire : quand un laser touche un alien, ajoute 1 à la variable score.
                # Indice : regarde comment `+=` est utilisé dans les fonctions de physique.
                # Si tout fonctionne, le score en haut à droite de la fenêtre augmente
                # à chaque alien touché. Pour tirer, appuie sur G.
                laser_1["is_fired"] = False
                laser_1["v_y"] = 0.0



    set_barriers_aliens(alien_list)
    set_barriers(player_1, laser_1)

    #Remplir la fenetre
    window.fill((0, 0, 0))
    police = pygame.font.SysFont('monospace', HEIGHT//12, True)

    for alien in alien_list:
        mru_1D_horizontal_aliens(alien, dt)
        draw_aliens(window, alien["x"], alien["y"])

    #Dessiner les entités
    draw_rect(window,player_1["x"],player_1["y"])
    if(laser_1["is_fired"] == True):
        draw_laser(window, laser_1["x"], laser_1["y"])

    #Ici on initialise le score que tu vois dans la partie en haut à droite de la fenetre.
    marquoir = police.render(str(score), True, WHITE)
    window.blit(marquoir, (7 * WIDTH // 8, HEIGHT // 10))

    pygame.display.flip()