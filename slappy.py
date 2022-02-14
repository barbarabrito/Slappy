from bs4 import BeautifulSoup
import requests


def p_scraper():
              
    try:
        url = input("URL: ")
        print("\n")
        result = requests.get(url)
        soup = BeautifulSoup(result.content, 'html.parser')
        
        texto = soup.find('div',class_)
        
        try:
            for tx in texto.find_all('p'):
                print(tx.get_text()) 
                print("\n")        
        except:
            print("nenhum resultado encontrado")

    except:
         print("\nurl não é válida")

    
v = "s"

while v == "s":
    
    print("------------------")
    print("1 - Estadão \n2 - Folha de SP\n3 - El País\n4 - O Globo\n5 - Uol ")
    print("------------------")    
    n = input("selecione o número correspondente ao jornal:\n")
    
    if n == '1':
        class_ = 'n--noticia__content'
    elif n == '2':
        class_ = 'c-news__body'
    elif n == '3':
        class_ = 'a_c clearfix'
    elif n == '4':
        class_ = 'article__content-container'
    elif n == '5':
        class_ = 'text'
    else:
        print("Resposta inválida, programa finalizado")
        break
    
    p_scraper()

    print("\n")
            
    v = input("Ler outra noticia? (Digite 's' para sim, 'n' para nao) s/n: ")
    
else:
    
    print("Programa finalizado")


