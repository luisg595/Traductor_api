# -*- coding: utf-8 -*-
import httplib
import urllib
import json

def requestTranslation(source, target, text):
	parametros = urllib.urlencode({'sl': source, 'tl': target, 'q': text})
	cabeceras = {"Charset":"UTF-8","User-Agent":"AndroidTranslate/5.3.0.RC02.130475354-53000263 5.1 phone TRANSLATE_OPM5_TEST_1"}
	abrir_conexion = httplib.HTTPSConnection("translate.google.com")
	abrir_conexion.request("POST", "/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&hl=es-ES&ie=UTF-8&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e", parametros, cabeceras)
	respuesta = abrir_conexion.getresponse()
	if respuesta.status == 200:
		respuesta = json.loads(respuesta.read())
		for x in respuesta['sentences']:
			return x['trans']
	else:
		return "Ocurrió un error"

text = raw_input("Ingrese un texto para traducir: ")
respuesta = requestTranslation("es", "en", text)
print respuesta