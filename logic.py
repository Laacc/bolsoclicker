class GerenciarJogo:
    def __init__(self):
        self.pontos_totais = 0.0
        self.valor_clique = 1.0
        self.pontos_passivos = 0.0
        self.upgrades = {
            "clique01":{
                "custo":30.0,
                "mult":1.30,
                "tipo":"ativo"
            },
            "passivo01":{
                "custo":100.0,
                "mult":1.50,
                "tipo":"passivo"
            },
            "augment_c_01":{
                "custo":1500.0,
                "mult":3.0,
                "tipo":"augment_c"
            }
        }
    

    def add_pontos(self):
        self.pontos_totais += self.valor_clique

    def computar_pontos_passivos(self):
        self.pontos_totais += self.pontos_passivos

    def comprar_upgrade(self, id_upgrade):
        preço = self.upgrades[id_upgrade]["custo"]
        if self.pontos_totais >= preço:
            self.pontos_totais -= preço
            if self.upgrades[id_upgrade]["tipo"] == "ativo":
                self.valor_clique += 1
            elif self.upgrades[id_upgrade]["tipo"] == "passivo":
                self.pontos_passivos += 0.5
            elif self.upgrades[id_upgrade]["tipo"] == "augment_c":
                self.valor_clique *= 2
            self.upgrades[id_upgrade]["custo"] *= self.upgrades[id_upgrade]["mult"]
            return True
        return False
        

   