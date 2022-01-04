import Pegar_Links as pl
from flask import Flask, request, redirect, url_for,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
#token = ''
#DEFINE A ROTA E O MÉTODO
@app.route("/verificacao", methods=['POST']) 
#CRIA A FUNÇÃO
def Post_repository():

    #TRATATIVAS DE ERRO
    try:
        #print("requisicao recebida")
        codigo = request.json #{"CODIGO":2222}#
        #print("json extraido")
        link=[]
        #print("1 pegando codigo")
        link  = pl.Pegar_Codigo(codigo['CODIGO'])
        #print("2 pegando imagens")
        lista =[]
        lista = pl.Pegar_Imagens(link)
        #print(lista)
        #RETORNA A RESPOSTA AO USUÁRIO
        #print("resposta")
        
        return jsonify({'lista':lista})
     
        #return '<img src="https://drive.google.com/uc?export=view&id=19v4rukD8TcJMqNlVtwOOiVel5Ekb5Gt5">'#Pega a imagem e apresenta completamente

    except Exception as e:
        #print(e)
        return 'Devido a algum problema não foi possível realizar a operação'

#teste = Post_repository()
