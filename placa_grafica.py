import os
import platform
import time
from templates import FIM


LARGURA = 80
ALTURA = 20

apagar_tela = lambda: os.system('cls') if platform.system() == 'Windows' else lambda: os.system('clear')


def desenhar_e_esperar(delta_t, fase, passo, tempo, msg):
    time.sleep(passo)
    apagar_tela()
    pontos_cartesianos = fase.calcular_pontos(tempo)
    print('%s Tempo: %.2f' % (msg, tempo))
    print(desenhar(*pontos_cartesianos))
    tempo += delta_t
    return tempo


def _animar(delta_t, fase, passo, tempo, msg):
    while not fase.acabou(tempo):
        tempo = desenhar_e_esperar(delta_t, fase, passo, tempo, msg)
    return tempo


def rebobina(delta_t, fase, passo, tempo, msg):
    while tempo > 0:
        tempo = desenhar_e_esperar(-delta_t, fase, passo, tempo, msg)
    return tempo


def animar(fase, passo=0.1, delta_t=0.1):
    tempo = 0
    tempo_final = _animar(delta_t, fase, passo, tempo, 'Play!')
    if input('Deseja ver o Replay? (s para sim): ').lower() == 's':
        velocidade_rebobina = 10
        rebobina(delta_t, fase, passo / velocidade_rebobina, tempo_final,
                 'Rebobinando %s vezes mais rápido!' % velocidade_rebobina)
        velocidade_replay = 3
        _animar(delta_t, fase, passo / velocidade_replay, tempo, 'Replay %s vezes mais rápido!' % velocidade_replay)
    apagar_tela()
    print(fase.status(tempo_final))
    print(FIM)


def normalizar_coordenadas(x, y):
    return x, ALTURA - y - 1


def esta_dentro_da_tela(x, y):
    return 0 < x < (LARGURA - 1) and 0 < y < (ALTURA - 1)


def escolher_caracter_limitrofe(x, y):
    if x == 0 or x == LARGURA - 1:
        return '|'
    if y == 0:
        return '-'
    return 'T'


def escolher_caracter(x, y, *pontos_cartesianos):
    for ponto in pontos_cartesianos:
        x_normalizdo, y_normalizado = normalizar_coordenadas(ponto.x, ponto.y)
        if x == x_normalizdo and y == y_normalizado:
            return ponto.caracter
    return ' '


def desenhar(*pontos_cartesianos):
    frame = ''
    for y in range(ALTURA):
        for x in range(LARGURA):
            if esta_dentro_da_tela(x, y):
                frame += escolher_caracter(x, y, *pontos_cartesianos)
            else:
                frame += escolher_caracter_limitrofe(x, y)
        frame += os.linesep
    return frame


def main():
    global Ponto, Fase

    class Ponto():
        def __init__(self, caracter):
            self.caracter = caracter
            self(0)

        def __call__(self, tempo):
            self.y = round(ALTURA * tempo / 5) if tempo < 5 else round(ALTURA * (10 - tempo) / 5)
            self.x = round(LARGURA * tempo / 10)
            return self

    class Fase():
        def __init__(self):
            self.p = Ponto('>')

        def calcular_pontos(self, tempo):
            return [self.p(tempo)]

        def acabou(self, tempo):
            return tempo > 10

        def status(self):
            return 'Você ganhou'

    animar(Fase())


if __name__ == '__main__':
    main()

