import requests

def proxy():
    url = "http://gimmeproxy.com/api/getProxy?protocol=http"
    r = requests.get(url).json()
    print r
#    return {r['protocol']:r['curl']}

url = 'https://www.ferendum.com/pt/votarpost3.php'
data = {"record3":"","record4":"","pregunta_ID":"173594","sec_digit":"23993","config_anonimo":"1","config_aut_req":"0","titulo":"Lula+ou+Bolsonaro?","votos_array[]":"892669","submit_votacion":"Enviar"}
headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}

proxies = proxy()
r = requests.post(url,proxies=proxies,data=data,headers=headers)

print r.status_code
if "Obrigado por participar desta enquente de Ferendum.com!" in r.content:
    print "Voto realizado com sucesso!"
