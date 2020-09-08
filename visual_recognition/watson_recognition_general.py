import json
import os
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# Código para acesso à API: key + URL
mykey = {
    "key": "",
    "url": ""
}

if os.path.exists('mykey.json'):
    with open('mykey.json') as json_file:
        mykey = json.load(json_file)


authenticator = IAMAuthenticator(mykey["key"])

visual_recognition = VisualRecognitionV3(version='2018-03-19',
                                         authenticator=authenticator)

visual_recognition.set_service_url(mykey["url"])

#desabilita SSL, caso sua rede ou laboratório exijam isso
#visual_recognition.disable_SSL_verification()

classifier_ids_possiveis = ['default', 'food', 'explicit']
classifier_id = classifier_ids_possiveis[0]

# Atenção ao caminho relativo, pode ser necessário trocar ".." por "."
with open('../datasets/imagens/food/bacalhoada.jpg', 'rb') as one_image_file:
    classes1 = visual_recognition.classify(images_file=one_image_file,
                                           threshold=0.6,
                                           classifier_ids=classifier_id).get_result()
print(f"Conteúdo JSON resultante do classificador '{classifier_id}':")
print(json.dumps(classes1, indent=2))

def minha_funcao_imagens(arquivo: str, classificador: str) -> dict:
    # Coloque aqui o código da função.

    # Coloque aqui o retorno correto da função.
    variavel_retorno = {}
    return variavel_retorno


