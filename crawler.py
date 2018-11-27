import requests
from lxml import html

r = requests.get('http://www.anatel.gov.br/institucional/noticias-destaque/2065-telefonia-fixa-tem-queda-de-1-224-404-linhas-em-12-meses')

tree = html.fromstring(r.content)

print tree.xpath('//*[@id="content-section"]/div/div[1]/h1/a/text()')[0].strip()
print tree.xpath('//*[@id="content-section"]/div/div[1]/p[4]/text()')[0].strip()
