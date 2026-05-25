from customtkinter import *
from CTkMessagebox import CTkMessagebox
from logic import GerenciarJogo

class JanelaPrincipal(CTk):
    def __init__(self):
        super().__init__()
        self.logica = GerenciarJogo()
        self.title("Bolsoclicker")
        self.geometry("500x500")
        self.resizable(False, False)
        self.label_pontos = CTkLabel(self, text=str(self.logica.pontos_totais))
        self.label_pontos.place(relx=0.5, rely=0.1, anchor="center")
        self.botao_click = CTkButton(self, command=self.clique_botao, text="+", width=32, height=32, corner_radius=128)
        self.botao_click.place(relx=0.5, rely=0.5, anchor="center")
        self.botao_upgrade_1_temp = CTkButton(self, command=self.atualizar_preco_upgrade_1, text=f"{self.logica.upgrades["clique01"]["custo"]:.0f}")
        self.botao_upgrade_1_temp.place(relx=0.5, rely=0.8, anchor="center")
        self.botao_upgrade_p1_temp = CTkButton(self, command=self.atualizar_preco_upgrade_p1, text=f"{self.logica.upgrades["passivo01"]["custo"]:.0f}")
        self.botao_upgrade_p1_temp.place(relx=0.5, rely=0.9, anchor="center")
        self.loop_pontos_passivos()
        

    def clique_botao(self):
        self.logica.add_pontos()
        self.atualizar_pontos_tela()

    def atualizar_pontos_tela(self):
        self.label_pontos.configure(text=f"{self.logica.pontos_totais:.0f}")

    def atualizar_preco_upgrade_1(self):
        self.logica.comprar_upgrade("clique01")
        self.botao_upgrade_1_temp.configure(text=f"{self.logica.upgrades["clique01"]["custo"]:.0f}")
        self.atualizar_pontos_tela()

    def atualizar_preco_upgrade_p1(self):
        self.logica.comprar_upgrade("passivo01")
        self.botao_upgrade_p1_temp.configure(text=f"{self.logica.upgrades["passivo01"]["custo"]:.0f}")
        self.atualizar_pontos_tela()

    def loop_pontos_passivos(self):
        self.logica.computar_pontos_passivos()
        self.atualizar_pontos_tela()
        self.after(1000, self.loop_pontos_passivos)
        