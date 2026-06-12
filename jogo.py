import random
import os
import time


## cria o mapa padrao

mapa_inicial=[[],[],[],[],[],[],[],[],[],[]]
for i in range(10):
        for j in range(10):
                mapa_inicial[i].append('🟦')   ## 🌊 💣

mapa_baixo=[[],[],[],[],[],[],[],[],[],[]]
for i in range(10):
        for j in range(10):
                mapa_baixo[i].append(0)  

## copia o mapa padrao em outras variaveis para ser usado em casos diversos

mapa_jogador=[linha[:] for linha in mapa_inicial]        ## copia_lista = [lista_original[:]]  -- muito util pois assim voce consegue criar uma copia de uma lista desejada

mapa_feedback_robo=[linha[:] for linha in mapa_inicial]

mapa_feedback_jogador=[linha[:] for linha in mapa_inicial]

mapa_barcos_robo=[linha[:] for linha in mapa_inicial] ## mapa que contem todos os barcos do robo

mapa_baixo_robo=[linha[:] for linha in mapa_baixo]

mapa_baixo_jogador=[linha[:] for linha in mapa_baixo]

## funcoes uteis e autoexplicativas

barcos_robo_restantes=5
barcos_jogador_restantes=5



def modificar_mapa(coordenadaX,coordenadaY,caracter,mapa):
        mapa[coordenadaX][coordenadaY]=caracter

        return mapa


def mostrar_mapa_V2(mapa):
        for h in range(1,11):
                print(h, end="  ")
        print(" ")
        
        for i in range(10):
                for j in range(10):
                        print(mapa[i][j], end=" ")
                print(f'{i+1}')                
        
def usuario_escolhe_coordenada():
        while True:
                try:
                        X=int(input("digite a coordenada X escolhida: "))
                        if 0<X<11:
                                break
                        else:
                                print("valor invalido, tente novamente")       
                except ValueError:
                        print("valor invalido, tente novamente")
        while True:
                try: 
                        Y=int(input("digite a coordenada Y escolhida: "))
                        if 0<Y<11:
                                break
                        else:
                                print("valor invalido, tente novamente")
                except ValueError:
                        print("valor invalido, tente novamente")
        return X-1, Y-1

def robo_escolhe():
        X=random.randint(0,10)
        return X

def limpar_tela():
        os.system('clear')

def escolher_direcao_barco():
        while True:
                direcao=input(" (H) orizontal ou (V) ertical ")
                if direcao=="V" or  direcao=="H":
                        return direcao
                else: 
                        print("Direcao invalida, tente novamente")


def colocar_barcos_grandes(direcao,barco,Y,X,mapa):
        global mapa_baixo_jogador
        global mapa_jogador
        mapa_backup=[linha[:] for linha in mapa]
        while True:
                mapa_backup=[linha[:] for linha in mapa]
                try:
                        if direcao=="H":
                                verificacao=0
                                while verificacao==0:
                                        print(f'navio atual: {'[🚢]'+'🚢'*(barco)} Da esquerda para direita (horizontal) ou de cima para baixo (vertical) ')
                                        print("")
                                        verificacao=1
                                        for i in range(barco):
                                                if mapa[Y][X+i] == '🚢':
               
                                                        limpar_tela()
                                                        mostrar_mapa_V2(mapa)
                                                        print("da escolhida ja contem algum barco.")
                                                        Xbarco, Ybarco = usuario_escolhe_coordenada()
                                                        Y, X = Ybarco, Xbarco
                                                        direcao = escolher_direcao_barco()
                                                        verificacao=0
                                                        break
           
                                for i in range(barco):
                                        
                                        modificar_mapa(Y,X+i,'🚢',mapa)
                                        modificar_mapa(Y,X+i,barco,mapa_baixo_jogador)
                                

                                
                                return mapa
                        else:                                                        
                                verificacao=1 ## caso seja identificado algum barco ja existente nas coordenadas especificadas, ele fica perguntando denovo ate dar certo
                                while verificacao==1:
                                        verificacao=0
                                        for i in range(barco):
                                                if mapa[Y+i][X] == '🚢':

                                                        limpar_tela()
                                                        mostrar_mapa_V2(mapa)
                                                        print("Coordenada escolhida ja contem algum barco.")
                                                        Xbarco, Ybarco = usuario_escolhe_coordenada()
                                                        Y, X = Ybarco, Xbarco
                                                        direcao = escolher_direcao_barco()
                                                        verificacao=1
                                                        break
                                for i in range(barco):
                                        modificar_mapa(Y+i,X,'🚢',mapa)
                                        modificar_mapa(Y+i,X,barco,mapa_baixo_jogador)


                                return mapa
                except IndexError:
                        limpar_tela()
                        mostrar_mapa_V2(mapa_jogador)
                        print("valor fora do mapa, tente novamente")
                        mapa_jogador = [linha[:] for linha in mapa_backup]
                        Xbarco, Ybarco = usuario_escolhe_coordenada()
                        Y, X = Ybarco, Xbarco
                        direcao = escolher_direcao_barco()

def colocar_os_barcos_do_jogador():
        print("Posicione seus NAVIOS!")
        print("")
        
        for i in range(1,6,1):

                
                Xbarco, Ybarco = usuario_escolhe_coordenada()
                sentido_barco=escolher_direcao_barco()
                limpar_tela()
                colocar_barcos_grandes(sentido_barco,i,Ybarco,Xbarco,mapa_jogador)
                mostrar_mapa_V2(mapa_jogador)
        return mapa_jogador

def animacao_ataque_jogador(Y,X,mapa,direcao,inicio):    ## direcao = [ -1 vai de baixo para cima /-/ +1 vai de cima para baixo ]             ## inicio = [ 9 comeca de baixo /-/ 1 comeca de cima ]
        mapa_copia=[linha[:] for linha in mapa] 
        for i in range(inicio,X-1,direcao):
                limpar_tela()
                mapa_copia=[linha[:] for linha in mapa]
                modificar_mapa(i,Y,'💣',mapa_copia)
                mostrar_mapa_V2(mapa_copia)
                print("")
                mostrar_mapa_V2(mapa_feedback_jogador)
                time.sleep(0.1)
                limpar_tela()
        mostrar_mapa_V2(mapa_copia)
        print("")
        mostrar_mapa_V2(mapa_feedback_jogador)
        time.sleep(0.5)
def colocar_barcos_grandes_robo_horizontal(Ycoordenada,Xcoordenada):
       
        
        for i in range(1,4):
        
                pontos=0
                while True:
                        
                        contador=0
                        while contador<i:
                                contador+=1
                                try:
        
                                        if mapa_baixo_robo[Ycoordenada][Xcoordenada+contador-1]==0:
        
                                                pontos+=1
        
                                        else:
                                                contador=0
                                                pontos=0
                                                Ycoordenada=robo_escolhe()
                                                Xcoordenada=robo_escolhe()
                        
                                except IndexError:
        
                                                contador=0
                                                pontos=0
                                                Ycoordenada=robo_escolhe()
                                                Xcoordenada=robo_escolhe()              
        
                        if pontos==i:
                                break
                for h in range(i):
        
                        modificar_mapa(Ycoordenada,Xcoordenada+h,i,mapa_baixo_robo)


        
        return mapa_baixo_robo       

def colocar_barcos_grandes_robo_vertical(Ycoordenada,Xcoordenada):
       
        
        for i in range(4,6):
        
                pontos=0
                while True:
                        
                        contador=0
                        while contador<i:
                                contador+=1
                                try:
        
                                        if mapa_baixo_robo[Ycoordenada+contador-1][Xcoordenada]==0:
        
                                                pontos+=1
        
                                        else:
                                                contador=0
                                                pontos=0
                                                Ycoordenada=robo_escolhe()
                                                Xcoordenada=robo_escolhe()
                        
                                except IndexError:
        
                                                contador=0
                                                pontos=0
                                                Ycoordenada=robo_escolhe()
                                                Xcoordenada=robo_escolhe()              
        
                        if pontos==i:
                                break
                for h in range(i):
        
                        modificar_mapa(Ycoordenada+h,Xcoordenada,i,mapa_baixo_robo)

        
        return mapa_baixo_robo        
                
                        
def emoji_acerto_erro(Xusuario,Yusuario,mapa):
        if mapa[Yusuario][Xusuario]== 0:
                return '🌊'
        else:
                return '💥'

def retornar_quantidade_barcos_restantes_mapa(barco_buscado,mapa):
        
        qtd_barco_buscado=0

        for i in range(10):
                for j in range(10):
                        if mapa[i][j]==barco_buscado:
                                qtd_barco_buscado+=1
        
        return qtd_barco_buscado

def detectar_retornar_valor(Ycoordenada,Xcoordenada,mapa):
        
        
        return mapa[Ycoordenada][Xcoordenada]

def multiplicar_por_10_paraa_achar_depois_facil(Xcoordenada,Ycoordenada,mapa):
        
        
        mapa[Ycoordenada][Xcoordenada] *= 10

        return mapa
def encontrar_multiplicado_por_10_e_trocar_por_fogo(valor_a_ser_procurado,mapa_a_procurar,mapa_a_mexer):



        for i in range(10):
                for j in range(10):
                        if mapa_a_procurar[i][j]==valor_a_ser_procurado*10:
                                mapa_a_mexer[i][j]='🔥'


def main ():
        print("")
        print("Bem vindo ao jogo Batalha Naval.")
  
        print("")
        print("")      
        
        
        print("🌊 = voce acertou o oceano")
        print("")
        print("💥 = voce acertou alguma enbarcacao")
        print("")
        print("🔥 = voce destruiu a enbarcacao por completo")
        print("")

        
        input("Aperte Enter, se voce entendeu: ")
        limpar_tela()

        
        global barcos_robo_restantes
        global barcos_jogador_restantes
        
        mostrar_mapa_V2(mapa_jogador)
        colocar_os_barcos_do_jogador()
        limpar_tela()
        
        colocar_barcos_grandes_robo_horizontal(robo_escolhe(),robo_escolhe())
        colocar_barcos_grandes_robo_vertical(robo_escolhe(),robo_escolhe())
        
        while barcos_robo_restantes > 0 and barcos_jogador_restantes > 0:
                limpar_tela()
                mostrar_mapa_V2(mapa_feedback_robo)
                print("")
                mostrar_mapa_V2(mapa_feedback_jogador)

                

                ## usuario ataca
                
                Xusuario,Yusuario = usuario_escolhe_coordenada()
                
                animacao_ataque_jogador(Xusuario,Yusuario,mapa_feedback_robo,-1,9)
                
                valor_original = mapa_baixo_robo[Yusuario][Xusuario]
                
                modificar_mapa(Yusuario,Xusuario,emoji_acerto_erro(Xusuario,Yusuario,mapa_baixo_robo),mapa_feedback_robo)
                
                multiplicar_por_10_paraa_achar_depois_facil(Xusuario,Yusuario,mapa_baixo_robo)
                
                if valor_original != 0 and retornar_quantidade_barcos_restantes_mapa(valor_original, mapa_baixo_robo) == 0:
                        barcos_robo_restantes -= 1
                        encontrar_multiplicado_por_10_e_trocar_por_fogo(valor_original, mapa_baixo_robo, mapa_feedback_robo)
                
                if barcos_robo_restantes == 0:
                        break
                
                ## robo ataca

                X_robo = robo_escolhe() - 1
                Y_robo = robo_escolhe() - 1
                
                print("")
                print("Robo Ataca!")
                print("")
                time.sleep(2)
                for i in range(0, Y_robo + 1):
                        limpar_tela()
                        mapa_temp = [linha[:] for linha in mapa_feedback_jogador]
                        modificar_mapa(i, X_robo, '💣', mapa_temp)
                        mostrar_mapa_V2(mapa_feedback_robo)
                        print("")
                        mostrar_mapa_V2(mapa_temp)
                        
                        
                        time.sleep(0.1)
                
                valor_original_jogador = mapa_baixo_jogador[Y_robo][X_robo]
                
                modificar_mapa(Y_robo, X_robo, emoji_acerto_erro(X_robo, Y_robo, mapa_baixo_jogador), mapa_feedback_jogador)
                multiplicar_por_10_paraa_achar_depois_facil(X_robo, Y_robo, mapa_baixo_jogador)
                
                if valor_original_jogador != 0 and retornar_quantidade_barcos_restantes_mapa(valor_original_jogador, mapa_baixo_jogador) == 0:
                        barcos_jogador_restantes -= 1
                        encontrar_multiplicado_por_10_e_trocar_por_fogo(valor_original_jogador, mapa_baixo_jogador, mapa_feedback_jogador)
        if barcos_robo_restantes==0 and barcos_jogador_restantes>0:
                limpar_tela()
                print("jogador venceu, parabens")
                time.sleep(3)
        else:
                limpar_tela()
                print("robo venceu, mas nao desista")
                time.sleep(3)
        print("Trabalho feito por John Batista e Mateus Costa para a disciplina de Raciocinio Algoritimico")




main()


