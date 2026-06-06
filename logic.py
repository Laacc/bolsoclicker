import sqlite3

class GerenciarJogo:
    def __init__(self):
        self.pontos_totais = 0.0
        self.valor_clique = 1.0
        self.pontos_passivos = 0.0
        self.upgrades = {
            "ativo01":{
                "custo":15.0,
                "mult":1.15,
                "tipo":"ativo"
            },
            "passivo01":{
                "custo":100.0,
                "mult":1.15,
                "tipo":"passivo"
            },
            "augment_c_01":{
                "custo":1500.0,
                "mult":1.50,
                "tipo":"augment_c"
            },
            "augment_p_01":{
                "custo":2000.0,
                "mult":1.50,
                "tipo":"augment_p"
            }
        }
        self.inicializar_banco()
        self.carregar_jogo()

    def inicializar_banco(self):
        conexao = sqlite3.connect("savegame.db")
        cursor = conexao.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS status_jogador(pontos_totais REAL, valor_clique REAL, pontos_passivos REAL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS upgrades(id_upgrade TEXT PRIMARY KEY, custo REAL)")
        conexao.commit()
        conexao.close()

    def salvar_jogo(self):
        conexao = sqlite3.connect("savegame.db")
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM status_jogador")
        cursor.execute("DELETE FROM upgrades")
        cursor.execute("INSERT INTO status_jogador(pontos_totais, valor_clique, pontos_passivos) VALUES(?, ?, ?)",(self.pontos_totais, self.valor_clique, self.pontos_passivos))
        for id_upgrade, info in self.upgrades.items():
            cursor.execute("INSERT INTO upgrades(id_upgrade, custo) VALUES(?, ?)",(id_upgrade, info["custo"]))
        conexao.commit()
        conexao.close()

    def carregar_jogo(self):
        conexao = sqlite3.connect("savegame.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT pontos_totais, valor_clique, pontos_passivos FROM status_jogador")
        resultado_jogador = cursor.fetchone()
        if resultado_jogador:
            self.pontos_totais = resultado_jogador[0]
            self.valor_clique = resultado_jogador[1]
            self.pontos_passivos = resultado_jogador[2]
        cursor.execute("SELECT id_upgrade, custo FROM upgrades")
        linhas_upgrades = cursor.fetchall()
        for id_up, custo_salvo in linhas_upgrades:
            if id_up in self.upgrades:
                self.upgrades[id_up]["custo"] = custo_salvo
        conexao.close()
    
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
                self.valor_clique *= 1.5
            elif self.upgrades[id_upgrade]["tipo"] == "augment_p":
                self.pontos_passivos * 1.5
            self.upgrades[id_upgrade]["custo"] *= self.upgrades[id_upgrade]["mult"]
            return True
        return False
    
    
        

   