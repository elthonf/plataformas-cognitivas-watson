import requests
import json

classificadores_possiveis = ['default', 'food', 'explicit']
classifier_id = classificadores_possiveis[0]

url = "http://localhost:8080/minha_funcao_imagens?classificador=" + classifier_id

with open('../datasets/imagens/food/bacalhoada.jpg', 'rb') as one_image_file:
    file_content = one_image_file.read()

payload = file_content
headers = {
  'Content-Type': 'image/jpeg'
}

response = requests.request("GET", url, headers=headers, data=payload)

response_json = response.json()
print(json.dumps(response_json, indent=2))