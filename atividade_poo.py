class Pessoa:
    def __init__(self, nome, idade, peso, altura, sexo, estado = 'vivo', estado_civil = 'solteiro', conjuge = None):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.__sexo = sexo
        self.__estado = estado
        self.__estado_civil = estado_civil
        self.__conjuge =  conjuge

    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        if self.__estado != 'morto':
            return self.__idade
        else:
            return f"\n{self.__nome} está morto."
    @property
    def estado(self):
        return self.__estado
    @property
    def estado_civil(self):
        return self.__estado_civil
    @property
    def conjuge(self):
        return self.__conjuge

    @idade.setter
    def idade(self, valor):
        print('\nSem permissão!')

    def __str__(self):
        if self.__conjuge == None:
            return f'\n| Nome: {self.__nome:1} | Idade: {self.__idade:2} anos | Peso: {self.__peso}kg |\n| Altura: {self.__altura} | Sexo: {self.__sexo:8} | Estado civil: {self.__estado_civil} |'
        else:
            return f'\n| Nome: {self.__nome:1} | Idade: {self.__idade:2} anos | Peso: {self.__peso}kg |\n| Altura: {self.__altura} | Sexo: {self.__sexo:8} | Estado civil: {self.__estado_civil} | Conjuge: {self.__conjuge.nome} |'

    def morrer(self):
        self.__estado = 'morto'
        if self.__conjuge != None:
            self.__conjuge.tornarseviuvo()
        print(f'\n{self.__nome} morreu.')

    def tornarseviuvo(self):
        if self.conjuge.estado == 'morto':
            self.__estado_civil = 'viuvo'

    def envelhecer(self):
        if self.__estado != 'morto':
            if self.__idade < 21:
                self.__altura += 5
            self.__idade += 1
            print(f'\n{self.__nome} está com {self.__idade} e {self.__altura} cm de altura.')
        else:
            print(f'\nNão pode envelhecer. {self.__nome} está morto!')

    def engordar(self, peso = 1):
        if self.__estado != 'morto':
            self.__peso += peso
            print(f'\n{self.__nome} engordou {peso}kg.')
        else:
            print(f'\nNão pode engordar. {self.__nome} está morto!')

    def emagrecer(self, peso):
        if self.__estado != 'morto':
            self.__peso -= peso
            print(f'\nEmagreceu {peso}kg.')
        else:
            print(f'\nNão pode emagrecer. {self.__nome} está morto!')

    def crescer(self, altura):
        if self.__estado != 'morto':
            if self.__idade < 21:
                self.__altura += altura
                print(f'\nCresceu {altura} centímetros.')
            else:
                print(f'\nNão pode crescer. {self.__nome} tem mais de 21 anos de idade!')
        else:
            print(f'\nNão pode envelhecer. {self.__nome} está morto!')

    def casar(self, conjuge_p):
        if self.__estado != 'morto':
            if self.__idade >= 18:
                if self.__estado_civil != 'casado(a)':
                    if conjuge_p.estado != 'morto':
                        if conjuge_p.idade >= 18:
                            if self.estado_civil != 'casado(a)':
                                self.__estado_civil = 'casado(a)'
                                self.__conjuge = conjuge_p
                                conjuge_p.casar_externo(self)
                            else:
                                print(f'\nCasamento não permitido. {conjuge_p.nome} já está casado!')
                        else:
                            print(f'\nCasamento não permitido. {conjuge_p.nome} é de menor!')
                    else:
                        print(f'\nCasamento não permitido. {conjuge_p.nome} está morto!')
                else:
                    print(f'\nCasamento não permitido. {self.__nome} já está casado!')
            else:
                print(f'\nCasamento não permitido. {self.__nome} é de menor!')
        else:
            print(f'\nCasamento não permitido. {self.__nome} está morto!')

    def casar_externo(self, conjuge_p):
        self.__estado_civil = 'casado(a)'
        self.__conjuge = conjuge_p
           

maria = Pessoa('Maria', 5, 20, 100, 'F')
joao = Pessoa('João', 12, 40, 140, 'M')
pedro = Pessoa('Pedro', 22, 5, 170, 'M')
bia = Pessoa('Bia', 18, 55, 160, 'F')
julia = Pessoa('Julia', 30, 65, 170, 'F')
carlos = Pessoa('Carlos', 2, 11, 80, 'M')
jonas = Pessoa('Jonas', 4, 70, 180, 'M')

maria.idade = 10
maria.envelhecer()
pedro.crescer(2)
bia.casar(carlos)
pedro.casar(maria)
pedro.casar(julia)
pedro.casar(bia)
maria.morrer()
maria.engordar()
bia.casar(jonas)
bia.morrer
pedro.morrer()
jonas.casar(julia)
pedro.casar(bia)
print(pedro.idade)
joao.idade = 50