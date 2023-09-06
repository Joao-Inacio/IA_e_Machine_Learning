# Importação
from sys import argv

from pade.acl.aid import AID
from pade.core.agent import Agent
from pade.misc.utility import display_message, start_loop


class Agente(Agent):
    def __init__(self, aid):
        super(Agente, self).__init__(aid=aid)
        display_message(self.aid.localname, 'Olá')


if __name__ == '__main__':
    numero_agentes = 3
    c = 0
    agentes = list()
    for i in range(numero_agentes):
        porta = int(argv[1]) + c
        nome_agente = 'agente{}@localhost:{}'.format(porta, porta)
        agente = Agente(AID(name=nome_agente))
        agentes.append(agente)
        c += 1000
    start_loop(agentes)
