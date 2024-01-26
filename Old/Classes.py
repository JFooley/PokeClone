import random

class Movimento:
    def __init__(self, id, nome, elemento, tipo, poder, acuracia):
        self.id = id
        self.nome = nome
        self.elemento = elemento
        self.tipo = tipo
        self.poder = poder
        self.acuracia = acuracia

class Personagem:
    def __init__(self, nome, forca, magia, def_fisica, def_magica, velocidade, vida_atual, vida, elementos):
        self.nome = nome
        self._forca = self._ajustar_valor(forca)
        self._magia = self._ajustar_valor(magia)
        self._def_fisica = self._ajustar_valor(def_fisica)
        self._def_magica = self._ajustar_valor(def_magica)
        self._velocidade = self._ajustar_valor(velocidade)
        self.vida_atual = self._ajustar_valor(vida_atual)
        self._vida = self._ajustar_valor(vida)
        self.elementos = elementos

    def _ajustar_valor(self, valor):
        # Garante que o valor esteja dentro do intervalo de 0 a 100
        return max(0, min(valor, 100))

    @property
    def forca(self):
        return self._forca

    @forca.setter
    def forca(self, valor):
        self._forca = self._ajustar_valor(valor)

    @property
    def magia(self):
        return self._magia

    @magia.setter
    def magia(self, valor):
        self._magia = self._ajustar_valor(valor)

    @property
    def def_fisica(self):
        return self._def_fisica

    @def_fisica.setter
    def def_fisica(self, valor):
        self._def_fisica = self._ajustar_valor(valor)

    @property
    def def_magica(self):
        return self._def_magica

    @def_magica.setter
    def def_magica(self, valor):
        self._def_magica = self._ajustar_valor(valor)

    @property
    def velocidade(self):
        return self._velocidade

    @velocidade.setter
    def velocidade(self, valor):
        self._velocidade = self._ajustar_valor(valor)

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        self._vida = self._ajustar_valor(valor)

    @property
    def vida_atual(self):
        return self._vida_atual
    
    @vida_atual.setter
    def vida_atual(self, valor):
        self._vida_atual = self._ajustar_valor(valor)

    def calcular_dano(self, ataque, defensor):
        # Verifica se o ataque é do mesmo elemento do defensor
        bonus_elemento = 1.5 if ataque.elemento in defensor.elementos else 1.0

        if ataque.tipo == "fisico":
            dano_base = (self.forca * ataque.poder) / 100
            defensor_defesa = defensor.def_fisica
        else:
            dano_base = (self.magia * ataque.poder) / 100
            defensor_defesa = defensor.def_magica

        dano_total = dano_base * bonus_elemento

        # Calcula o dano final considerando a defesa do defensor
        porcentagem_reduzida = ((defensor_defesa / (100 + defensor_defesa)) * 150)
        dano_final = (dano_total * (100 - porcentagem_reduzida)) / 100
        
        for elemento in defensor.elementos:
            if superEffect[elemento] == ataque.elemento:
                dano_final *= 2
            elif nonSuperEffect[elemento] == ataque.elemento:
                dano_final *= 0.5


        return round(dano_final)

    def realizar_ataque(self, defensor, ataqueID):
        # Seleciona um movimento de ataque aleatório
        ataque = movimentos_ataque[ataqueID]
        chatlog = "\n" + self.nome + " está usando " + ataque.nome + "! \n"

        # Sorteia um valor de acurácia entre 0 e 100
        valor_acuracia_sorteado = random.randint(0, 100)

        if valor_acuracia_sorteado <= ataque.acuracia:
            # O ataque foi bem-sucedido, calcula o dano
            dano = self.calcular_dano(ataque, defensor)

            # Aplica o dano ao defensor
            defensor.vida_atual -= dano
            chatlog += defensor.nome + " recebeu " + str(dano) + " de dano. "

            efetividade = 1
            for elemento in defensor.elementos:
                if superEffect[elemento] == ataque.elemento:
                    efetividade *= 2
                elif nonSuperEffect[elemento] == ataque.elemento:
                    efetividade *= 0.5
            
            if efetividade < 1:
                chatlog += "É pouco efetivo..."
            elif efetividade > 1:
                chatlog += "É super efetivo!"

        else:
            chatlog += self.nome + " errou o ataque!"

        return chatlog
    
# Moves
movimentos_ataque = [
    Movimento(1, "Passar o turno"   , "nenhum"  , "fisico", 0   , 100),
    Movimento(2, "Jato d'Água"      , "agua"    , "magico", 90  , 100),
    Movimento(3, "Lapada dágua"     , "agua"    , "fisico", 50  , 100),
    Movimento(4, "Soco de Fogo"     , "fogo"    , "fisico", 50  , 100),
    Movimento(5, "Chama Ardente"    , "fogo"    , "magico", 50  , 100),
    Movimento(6, "Folha Cortante"   , "planta"  , "fisico", 50  , 100),
    Movimento(7, "Raio solar"       , "planta"  , "magico", 50  , 100),
]

# Dic de efetividade
superEffect = {"fogo" : "agua", "agua" : "planta", "planta" : "fogo"}
nonSuperEffect = {"agua" : "fogo", "planta" : "agua", "fogo" : "planta"}

# Criando personagens
personagem1 = Personagem("Guerreiro", 70, 30, 50, 50, 70, 60, 60, ["fogo"])
personagem2 = Personagem("Mago", 30, 70, 50, 50, 80, 40, 40, ["agua"])