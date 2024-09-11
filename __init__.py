from flask import Flask, jsonify, request
from chatbot import respuesta as rp
from faq import intro

app = Flask(__name__)
@app.route("/webhook/", methods=["GET", "POST"])
def webhook_whatsapp():
    if request.method == "GET":
        #SI EL TOKEN ES IGUAL AL QUE RECIBIMOS
        if request.args.get('hub.verify_token') == "xd":
            print('xd')
            #ESCRIBIMOS EN EL NAVEGADOR EL VALOR DEL RETO RECIBIDO DESDE FACEBOOK
            return request.args.get('hub.challenge')
        else:
            #SI NO SON IGUALES RETORNAMOS UN MENSAJE DE ERROR
          return "Error de autentificacion."
    
    data = request.get_json()
    try:
        mensaje = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
        telefonoCliente = data['entry'][0]['changes'][0]['value']['messages'][0]['from']
        if mensaje:
            print(mensaje)
            respuesta = rp(str(mensaje))
            enviar(telefonoCliente, str(respuesta))
    except: pass

    return jsonify({"status": "success"}), 200



def enviar(telefonoRecibe,respuesta):
  from heyoo import WhatsApp
  token='EAAnSvk9VZAJoBO9EyZAlUmj2Gk9ZAn4fmoBXd05MUgu5ekOe58ATeIbsubntG1gKTHhZChrUVly0imRatBWkoWwoHFSZC69852qfoZAytEMxT9RPQG5WlxzpD5ATSl9zAKD0GMFXZCTHrCI8dOzQrEbrAZASWadlH8ajFQsnrCNqyZCnuX7loLpDIsPXQFeYbOusD0vaGOlW2XFsPMWZBN'
  idNumeroTeléfono='395928573602774'
  mensajeWa=WhatsApp(token,idNumeroTeléfono)
  #telefonoRecibe=telefonoRecibe.replace("521","52")

  mensajeWa.send_message(respuesta,telefonoRecibe)





#INICIAMSO FLASK
if __name__ == "__main__":
  app.run(debug=True)