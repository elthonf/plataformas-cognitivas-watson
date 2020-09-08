import json
import os
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from flask import Flask, request, jsonify, Response
app = Flask(__name__)



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

@app.route("/minha_funcao_imagens", methods=['GET', 'POST', 'PUT'])
def minha_funcao_imagens(request=request) -> dict:
    classifier_id = request.args.get("classifier_id", 'default')
    one_image_file = request.data

    from typing import BinaryIO

    # Coloque aqui o código da função.


    # Coloque aqui o retorno correto da função.
    variavel_retorno = {} #????
    return jsonify(variavel_retorno) #retorno padrão em formato JSON


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)


# Coloque aqui o RM do(s) aluno(s): XXXXXXXXX

