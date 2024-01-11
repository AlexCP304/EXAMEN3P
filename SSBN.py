import pygame
import sys
import random

class Personaje(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = personaje = pygame.image.load("p.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(0, 300)
        self.muerto = 0
        self.jumping = False
        self.jump_count = 2
        self.gravity = 1
        self.player_y_change = 0
        self.invulnerable = False
        self.invulnerable_timer = 0

    def update(self):
        teclas = pygame.key.get_pressed()
        # Verifica si el personaje está en modo invulnerable y actualiza el temporizador
        if self.invulnerable:
            self.invulnerable_timer -= 1
            if self.invulnerable_timer <= 0:
                self.invulnerable = False

        # Si el personaje no está en modo invulnerable, permite el movimiento
        if not self.invulnerable:
            if teclas[pygame.K_a]:
                self.image = personaje = pygame.image.load("piz.png").convert_alpha()
                if self.rect.x > 0:
                    self.rect.x -= 2.5
            elif teclas[pygame.K_d]:
                self.image = personaje = pygame.image.load("pd.png").convert_alpha()
                if self.rect.x < 1260:
                    self.rect.x += 2.5

        # Verifica si ninguna tecla de movimiento está presionada
        if not any([teclas[pygame.K_a], teclas[pygame.K_d], teclas[pygame.K_SPACE]]):
            self.image = personaje = pygame.image.load("p.png").convert_alpha()

        if not self.invulnerable:
            # Verifica si la tecla de espacio está presionada y no está actualmente saltando
            if teclas[pygame.K_SPACE] and not self.jumping:
                self.player_y_change = -10  # Velocidad vertical inicial del salto
                self.jumping = True

        # Aplicar gravedad y actualizar posición vertical del salto
        if self.jumping:
            self.player_y_change += self.gravity
            self.rect.y += self.player_y_change

            # Si ha alcanzado una altura máxima de salto, comienza a descender
            if self.jump_count <= 0:
                self.jumping = False
            self.jump_count -= 1
        else:
            # Si no está saltando, aplica gravedad normal
            self.player_y_change += self.gravity
            self.rect.y += self.player_y_change

            # Evitar que el jugador caiga fuera de la pantalla
            if self.rect.y > 300:
                self.rect.y = 300
                self.player_y_change = 0
            if self.rect.y < 0:
                self.rect.y = 0
                self.player_y_change = 0

    def make_invulnerable(self, duration):
        # Activa el modo invulnerable y establece el temporizador
        self.invulnerable = True
        self.invulnerable_timer = duration


class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemigo = pygame.image.load("pro.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(1000, 300)
        self.speed = 12  # Ajusta la velocidad del enemigo

    def update(self, personaje_invulnerable):
        # Si el personaje está invulnerable, no se mueve
        if not personaje_invulnerable:
            # Mueve al enemigo de izquierda a derecha
            self.rect.x += self.speed
            # Si el enemigo alcanza los bordes de la pantalla, invierte la dirección
            if self.rect.x <= 100 or self.rect.x >= 1300 - self.rect.width:
                self.speed = -self.speed


class Mos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = mos = pygame.image.load("mos.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(0, 180)
        self.speed = 8  # Ajusta la velocidad del enemigo

    def update(self, personaje_invulnerable):
        # Si el personaje está invulnerable, no se mueve
        if not personaje_invulnerable:
            # Mueve al enemigo de izquierda a derecha
            self.rect.x += self.speed
            # Si el enemigo alcanza los bordes de la pantalla, invierte la dirección
            if self.rect.x <= 0 or self.rect.x >= 1300 - self.rect.width:
                self.speed = -self.speed


class Ara(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ara = pygame.image.load("ara.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(650, 60)
        self.speed = 8  # Ajusta la velocidad del enemigo

    def update(self, personaje_invulnerable):
        # Si el personaje está invulnerable, no se mueve
        if not personaje_invulnerable:
            # Mueve al enemigo de izquierda a derecha
            self.rect.x += self.speed
            # Si el enemigo alcanza los bordes de la pantalla, invierte la dirección
            if self.rect.x <= 500 or self.rect.x >= 1300 - self.rect.width:
                self.speed = -self.speed

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)  # Color para la plataforma
        self.rect = self.image.get_rect(topleft=(x, y))

class Nar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = nar = pygame.image.load("nar.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(400, 125)
        self.speed = 9  # Ajusta la velocidad del enemigo

    def update(self, personaje_invulnerable):
        # Si el personaje está invulnerable, no se mueve
        if not personaje_invulnerable:
            # Mueve al enemigo de izquierda a derecha
            self.rect.x += self.speed
            # Si el enemigo alcanza los bordes de la pantalla, invierte la dirección
            if self.rect.x <=400 or self.rect.x >= 950 - self.rect.width:
                self.speed = -self.speed


class D(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = d = pygame.image.load("d.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(0,-35)

class Ene(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ene = pygame.image.load("ene.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(1000, 300)
        self.speed = 25  # Ajusta la velocidad del enemigo

    def update(self, personaje_invulnerable):
        # Si el personaje está invulnerable, no se mueve
        if not personaje_invulnerable:
            # Mueve al enemigo de izquierda a derecha
            self.rect.x += self.speed
            # Si el enemigo alcanza los bordes de la pantalla, invierte la dirección
            if self.rect.x <= 100 or self.rect.x >= 1300 - self.rect.width:
                self.speed = -self.speed

def main0():
    pygame.init()

    screen = pygame.display.set_mode((100, 100))
    fondo = pygame.image.load("es.png").convert()
    jugando = True

    while jugando:
        pygame.time.delay(100)
        pygame.display.flip()
        break
    pygame.quit()

def main():
    pygame.init()
    pygame.mixer.music.load("mu_1.ogg")
    pygame.mixer.music.play(1)
    pygame.init()

    # variables
    jugando = True

    screen = pygame.display.set_mode((1300, 400))
    pygame.display.set_caption("RÁPIDO Y ESTUDIOSO")

    fondo = pygame.image.load("es.png").convert()

    hasperdido = pygame.image.load("Hasperdido.png").convert_alpha()

    d = D()
    ara = Ara()
    enemigo = Enemigo()
    mos = Mos()
    personaje = Personaje()
    plataforma = Plataforma(340, 218.5, 125, 10, (224, 153, 115))  # Ejemplo de plataforma, ajusta las coordenadas y el tamaño según tus necesidades
    plataforma2 = Plataforma(550, 132, 100, 10, (248, 0, 0))
    plataforma3 = Plataforma(720, 132, 100, 10, (248, 0, 0))
    plataforma4 = Plataforma(869, 250, 72.5, 10, (248, 0, 0))
    plataformas = [plataforma, plataforma2, plataforma3, plataforma4]
    temporizador = pygame.time.Clock()
    tiempo_fin_juego = None
    # ANCHO = 1300
    # ALTO = 400
    # ventana = pygame.display.set_mode((ANCHO, ALTO))
    fuente2 = pygame.font.SysFont("Segoe print", 30)
    # Después de inicializar tus variables y antes del bucle principal
    posicion_transicion = 1260  # Establece la posición en el eje x para la transición
    # Colores
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)

    while jugando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jugando = False

        personaje.update()
        enemigo.update(personaje.invulnerable)  # Actualiza la posición del enemigo
        ara.update(personaje.invulnerable)
        mos.update(personaje.invulnerable)
        d.update(personaje.invulnerable)

        # Colisiones con Ara
        if pygame.sprite.collide_rect(ara, personaje):
            personaje.make_invulnerable(120)  # 60 frames = 1 segundo
            personaje.rect.x = 0
            personaje.rect.y = 300

        # Colisiones con Enemigo
        if pygame.sprite.collide_rect(enemigo, personaje):
            personaje.make_invulnerable(120)
            personaje.rect.x = 0
            personaje.rect.y = 300

        # Colisiones con mos
        if pygame.sprite.collide_rect(mos, personaje):
            personaje.make_invulnerable(120)
            personaje.rect.x = 0
            personaje.rect.y = 300

        # Colisiones con d
        if pygame.sprite.collide_rect(d, personaje):
            personaje.make_invulnerable(120)
            personaje.rect.x = 0
            personaje.rect.y = 300

        # Colisiones con la plataforma
        for plataforma in plataformas:
            if pygame.sprite.collide_rect(personaje, plataforma):
                personaje.rect.y = plataforma.rect.y - personaje.rect.height
                personaje.player_y_change = 0
                personaje.jump_count = 2
                personaje.jumping = False

        if personaje.rect.x > posicion_transicion:
            break  # Sale del bucle para cambiar de nivel

        # actualizacion grafica
        screen.blit(fondo, (0, 0))

        for plataforma in plataformas:
            screen.blit(plataforma.image, plataforma.rect)

        screen.blit(personaje.image, personaje.rect)
        screen.blit(enemigo.image, enemigo.rect)
        screen.blit(ara.image, ara.rect)
        screen.blit(mos.image, mos.rect)
        screen.blit(d.image, d.rect)

        pygame.display.flip()

        temporizador.tick(60)

    pygame.quit()

def main2():
    # variables
    pygame.init()

    pygame.mixer.music.load("tema2.ogg")
    pygame.mixer.music.play(1)

    jugando = True

    screen = pygame.display.set_mode((1300, 400))
    pygame.display.set_caption("RÁPIDO Y ESTUDIOSO")

    fondo2 = pygame.image.load("es2.png").convert()

    hasperdido = pygame.image.load("Hasperdido.png").convert_alpha()

    nar = Nar()
    ene = Ene()
    d = D()
    personaje = Personaje()
    plataforma0 = Plataforma(205, 283, 222, 8, (
    224, 153, 115))  # Ejemplo de plataforma, ajusta las coordenadas y el tamaño según tus necesidades
    plataforma02 = Plataforma(790, 273, 273, 9, (224, 153, 115))
    plataforma03 = Plataforma(536, 182, 240, 10, (205, 205, 205))
    plataforma04 = Plataforma(410, 188, 150, 4, (205, 205, 205))
    plataformas = [plataforma0, plataforma02, plataforma03, plataforma04]
    temporizador = pygame.time.Clock()
    tiempo_fin_juego = None
    posicion_transicion = 1260  # Establece la posición en el eje x para la transición

    while jugando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jugando = False

        personaje.update()
        ene.update(personaje.invulnerable)  # Actualiza la posición del enemigo
        nar.update(personaje.invulnerable)
        d.update(personaje.invulnerable)

        # Colisiones con Enemigo
        if pygame.sprite.collide_rect(ene, personaje):
            personaje.make_invulnerable(120)
            personaje.rect.x = 0
            personaje.rect.y = 300

        # Colisiones con Ara
        if pygame.sprite.collide_rect(nar, personaje):
            personaje.make_invulnerable(120)  # 60 frames = 1 segundo
            personaje.rect.x = 0
            personaje.rect.y = 300

        # Colisiones con d
        if pygame.sprite.collide_rect(d, personaje):
            personaje.make_invulnerable(120)  # 60 frames = 1 segundo
            personaje.rect.x = 0
            personaje.rect.y = 300

        # Colisiones con la plataforma
        for plataforma in plataformas:
            if pygame.sprite.collide_rect(personaje, plataforma):
                personaje.rect.y = plataforma.rect.y - personaje.rect.height
                personaje.player_y_change = 0
                personaje.jump_count = 2
                personaje.jumping = False

        if personaje.rect.x > posicion_transicion:
            break  # Sale del bucle para cambiar de nivel

        # actualizacion grafica
        screen.blit(fondo2, (0, 0))

        for plataforma in plataformas:
            screen.blit(plataforma.image, plataforma.rect)

        screen.blit(personaje.image, personaje.rect)
        screen.blit(nar.image, nar.rect)
        screen.blit(ene.image, ene.rect)
        screen.blit(d.image, d.rect)

        pygame.display.flip()

        temporizador.tick(60)

    pygame.quit()


# pygame.display.flip
# pygame.quit()

def main3():
    pygame.init()

    pygame.mixer.music.load("tema3.ogg")
    pygame.mixer.music.play(1)

    class Personaje(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = personaje = pygame.image.load("p.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.move_ip(0, 300)
            self.muerto = 0
            self.jumping = False
            self.jump_count = 2
            self.gravity = 1
            self.player_y_change = 0
            self.invulnerable = False
            self.invulnerable_timer = 0

        def update(self):
            teclas = pygame.key.get_pressed()
            # Verifica si el personaje está en modo invulnerable y actualiza el temporizador
            if self.invulnerable:
                self.invulnerable_timer -= 1
                if self.invulnerable_timer <= 0:
                    self.invulnerable = False

            # Si el personaje no está en modo invulnerable, permite el movimiento
            if not self.invulnerable:
                if teclas[pygame.K_a]:
                    self.image = personaje = pygame.image.load("piz.png").convert_alpha()
                    if self.rect.x > 0:
                        self.rect.x -= 2.5
                elif teclas[pygame.K_d]:
                    self.image = personaje = pygame.image.load("pd.png").convert_alpha()
                    if self.rect.x < 1260:
                        self.rect.x += 2.5

            # Verifica si ninguna tecla de movimiento está presionada
            if not any([teclas[pygame.K_a], teclas[pygame.K_d], teclas[pygame.K_SPACE]]):
                self.image = personaje = pygame.image.load("p.png").convert_alpha()

            if not self.invulnerable:
                # Verifica si la tecla de espacio está presionada y no está actualmente saltando
                if teclas[pygame.K_SPACE] and not self.jumping:
                    self.player_y_change = -10  # Velocidad vertical inicial del salto
                    self.jumping = True

            # Aplicar gravedad y actualizar posición vertical del salto
            if self.jumping:
                self.player_y_change += self.gravity
                self.rect.y += self.player_y_change

                # Si ha alcanzado una altura máxima de salto, comienza a descender
                if self.jump_count <= 0:
                    self.jumping = False
                self.jump_count -= 1
            else:
                # Si no está saltando, aplica gravedad normal
                self.player_y_change += self.gravity
                self.rect.y += self.player_y_change

                # Evitar que el jugador caiga fuera de la pantalla
                if self.rect.y > 300:
                    self.rect.y = 300
                    self.player_y_change = 0
                if self.rect.y < 0:
                    self.rect.y = 0
                    self.player_y_change = 0

        def make_invulnerable(self, duration):
            # Activa el modo invulnerable y establece el temporizador
            self.invulnerable = True
            self.invulnerable_timer = duration

        def check_collision_with_projectiles(self, proyectiles):
            # Verifica colisiones con los proyectiles
            if pygame.sprite.spritecollide(self, proyectiles, True):
                self.make_invulnerable(120)  # Tiempo de invulnerabilidad
                self.rect.x = 0
                self.rect.y = 300

    class Bib(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = bib = pygame.image.load("bib.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.move_ip(1200, 300)
            self.speed = 8  # Ajusta la velocidad del enemigo
            self.jump_timer = 0
            self.projectile_timer = 0

        def update(self, personaje_invulnerable):
            # Si el personaje está invulnerable, no se mueve
            if not personaje_invulnerable:
                # Mueve al enemigo de izquierda a derecha
                self.rect.x += self.speed
                # Si el enemigo alcanza los bordes de la pantalla, invierte la dirección
                if self.rect.x <= 1000 or self.rect.x >= 1290 - self.rect.width:
                    self.speed = -self.speed

                # Actualiza la posición en el eje y
                self.rect.y += random.choice([-15, 0, 15])  # Cambia la posición en el eje y de manera aleatoria
                self.rect.y = max(0, min(400 - self.rect.height, self.rect.y))  # Evita que salga de la pantalla en el eje y

                # Actualiza el temporizador de salto
                if self.jump_timer > 0:
                    self.jump_timer -= 1

                # Actualiza el temporizador de generación de proyectiles
                if self.projectile_timer > 0:
                    self.projectile_timer -= 1

                # Verifica si puede saltar y lanza proyectiles hacia la izquierda
                if self.jump_timer == 0 and random.randint(1, 100) <= 10:  # Probabilidad de salto del 5%
                    self.jump()
                    self.jump_timer = 30  # Espera 60 frames antes de poder saltar nuevamente
                elif self.projectile_timer == 0 and random.randint(1,100) <= 10:  # Probabilidad de lanzar proyectil del 10%
                    self.launch_projectile()
                    self.projectile_timer = 30  # Espera 60 frames antes de poder lanzar otro proyectil

        def jump(self):
            # Salto con altura máxima de 6
            self.rect.y -= min(8, self.rect.y)

        def launch_projectile(self):
            # Crea un proyectil y lo lanza hacia la izquierda
            projectile = Proyectil(self.rect.x, self.rect.centery)
            proyectiles.add(projectile)

    class Proyectil(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.image.load("proyectil.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed = 14  # Ajusta la velocidad del proyectil

        def update(self):
            # Mueve el proyectil hacia la izquierda
            self.rect.x -= self.speed

    class Lib(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = lib = pygame.image.load("lib.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.move_ip(random.randint(0, 1300 - self.rect.width), random.randint(0, 400 - self.rect.height))
            self.speed_x = random.choice([-15, 15])  # Ajusta la velocidad del enemigo en el eje x
            self.speed_y = random.choice([-15, 15])  # Ajusta la velocidad del enemigo en el eje y

        def update(self, personaje_invulnerable):
            # Si el personaje está invulnerable, no se mueve
            if not personaje_invulnerable:
                # Mueve al enemigo de izquierda a derecha
                self.rect.x += self.speed_x
                self.rect.y += self.speed_y
                # Si el enemigo alcanza los bordes de la pantalla, invierte la dirección
                if self.rect.x <= 50 or self.rect.x >= 1300 - self.rect.width:
                    self.speed_x = -self.speed_x
                if self.rect.y <= 0 or self.rect.y >= 400 - self.rect.height:
                    self.speed_y = -self.speed_y

    class D(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = d = pygame.image.load("d.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.move_ip(0, -35)

    jugando = True
    # variables

    screen = pygame.display.set_mode((1300, 400))
    pygame.display.set_caption("RÁPIDO Y ESTUDIOSO")

    fondo = pygame.image.load("es3.png").convert()

    hasperdido = pygame.image.load("Hasperdido.png").convert_alpha()

    d = D()
    bib = Bib()
    lib = Lib()
    personaje = Personaje()
    proyectiles = pygame.sprite.Group()
    plataforma = Plataforma(1170, 234, 109, 6, (
    224, 120, 17, 255))  # Ejemplo de plataforma, ajusta las coordenadas y el tamaño según tus necesidades
    plataforma2 = Plataforma(830, 290, 310, 8, (109, 13, 76, 255))
    plataforma3 = Plataforma(563, 293, 181, 8, (109, 13, 76, 255))
    plataformas = [plataforma, plataforma2, plataforma3]
    temporizador = pygame.time.Clock()
    tiempo_fin_juego = None
    posicion_transicion = 1260  # Establece la posición en el eje x para la transición

    while jugando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jugando = False

        personaje.update()
        lib.update(personaje.invulnerable)  # Actualiza la posición del enemigo
        bib.update(personaje.invulnerable)
        d.update(personaje.update)

        # Colisiones con Lib
        if pygame.sprite.collide_rect(lib, personaje):
            personaje.make_invulnerable(120)
            personaje.rect.x = 0
            personaje.rect.y = 300
        if pygame.sprite.collide_rect(personaje, lib):
            lib.rect.x = 250
            lib.rect.y = 112

        # Colisiones con Bib
        if pygame.sprite.collide_rect(bib, personaje):
            personaje.make_invulnerable(120)  # 60 frames = 1 segundo
            personaje.rect.x = 0
            personaje.rect.y = 300

        # Colisiones con d
        if pygame.sprite.collide_rect(d, personaje):
            personaje.make_invulnerable(120)  # 60 frames = 1 segundo
            personaje.rect.x = 0
            personaje.rect.y = 300

        # Colisiones con Proyectiles
        personaje.check_collision_with_projectiles(proyectiles)

        # Colisiones con la plataforma
        for plataforma in plataformas:
            if pygame.sprite.collide_rect(personaje, plataforma):
                personaje.rect.y = plataforma.rect.y - personaje.rect.height
                personaje.player_y_change = 0
                personaje.jump_count = 2
                personaje.jumping = False

        if personaje.rect.x > posicion_transicion:
            break  # Sale del bucle para cambiar de nivel

        # actualizacion grafica
        screen.blit(fondo, (0, 0))

        for plataforma in plataformas:
            screen.blit(plataforma.image, plataforma.rect)

        screen.blit(personaje.image, personaje.rect)
        screen.blit(lib.image, lib.rect)
        screen.blit(bib.image, bib.rect)
        screen.blit(d.image, d.rect)

        proyectiles.update()
        proyectiles.draw(screen)

        pygame.display.flip()

        temporizador.tick(60)

    pygame.quit()

if __name__ == '__main__':
    # Después de ejecutar main3, mostrar la imagen "hasganado.png" durante 7 segundos
    screen = pygame.display.set_mode((400, 400))
    comienzo = pygame.image.load("comienzo.png").convert_alpha()
    screen.blit(comienzo, (0, 0))
    pygame.display.set_caption("RÁPIDO Y ESTUDIOSO")
    pygame.init()
    pygame.mixer.music.load("ini.ogg")
    pygame.mixer.music.play(1)
    pygame.display.flip()

    # Pausar la ejecución durante 5 segundos
    pygame.time.delay(5000)
    main0()
    main()  # Ejecutar el primer juego
    # Una vez que el primer juego ha terminado, ejecutar el segundo juego
    main2()
    main3()
    # Después de ejecutar main3, mostrar la imagen "hasganado.png" durante 7 segundos
    screen = pygame.display.set_mode((400, 400))
    has_ganado_image = pygame.image.load("Hasganado.png").convert_alpha()
    screen.blit(has_ganado_image, (0, 0))
    pygame.display.set_caption("RÁPIDO Y ESTUDIOSO")
    pygame.init()
    pygame.mixer.music.load("fin.ogg")
    pygame.mixer.music.play(1)
    pygame.display.flip()

    # Pausar la ejecución durante 5 segundos
    pygame.time.delay(5000)

    pygame.quit()