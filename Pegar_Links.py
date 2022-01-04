import pandas as pd
import pdb
#Aqui eu estou pegando apenas o código e o link (Onde aponta para os diferentes setores)
def Pegar_Codigo(codigo):
    #pdb.set_trace()
    url='https://docs.google.com/spreadsheets/d/1VyQpRnCMwZXDa0BUovyYy5ycNFKbAJQ0/edit?usp=sharing'#COLOQUE AQUI APENAS O LINK DA PLANILHA COM OS CÓDIGOS
    #url2='https://drive.google.com/uc?id=' + url.split('/')[-2]
    url_id = url.split('/')[-2]
    url4 = f'https://docs.google.com/spreadsheets/d/{url_id}/export?format=csv'
    df = pd.read_csv(url4)
    #print(df.head()) 
    link ='error'
   
    indice = 0
    for item in df['CODIGO']:
        #pdb.set_trace()
        if str(codigo) == str(item):
            link= df['LINK'][indice]
                
        indice +=1
        #print(link)  
    return link

#Aqui eu vou pegar os links das imagens, imagens diretas, ID e etc. de cada setor FALTA CONSERTAR!!!!
def Pegar_Imagens(link):
    #pdb.set_trace()
  
    #url2='https://drive.google.com/uc?id=' + url.split('/')[-2]
    url_id = link.split('/')[-2]
    url4 = f'https://docs.google.com/spreadsheets/d/{url_id}/export?format=csv'
    df = pd.read_csv(url4)
    #print(df) 
    linke =[]
    
    indice = 0
   
    for item in df['NOME']:
        
        img_direta= f"https://drive.google.com/uc?id={df['ID_IMAGEM'][indice]}"
        #img_direta= f"https://docs.google.com/spreadsheets/d/{df['ID_IMAGEM'][indice]}/export?format=csv"
        linke.append({"NOME":df['NOME'][indice], "LINK_IMAGEM":df['LINK_IMAGEM'][indice], "ID_IMAGEM":img_direta, "VALOR": df['VALOR'][indice],"MARCA": df['MARCA'][indice]})                
        indice +=1
        #print(link)  
    
    return linke


            