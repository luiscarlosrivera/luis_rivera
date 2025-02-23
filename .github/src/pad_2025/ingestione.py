import json



class Ingestiones():
    def __init__(self):
        self.ruta_static="F:/Ingenieria/Analitica de datos/repositorios/luis_rivera/.github/src/pad_2025/static/"
        
    def leer_json(self):
        # r read w write

        ruta_json = "{}json/datos_persona.json".format(self.ruta_static)
        datos=""
        with open(ruta_json,"r",encoding="utf-8") as f:
            datos = json.load(f)
        return datos    
    
    def leer_txt(self):
        # r read w write

        ruta_json = "{}txt/info.txt".format(self.ruta_static)
        datos=""
        with open(ruta_json,"r",encoding="utf-8") as f:
            datos = f.read()
        return datos 

    

inges = Ingestiones() 
datos_json = inges.leer_json()
print(datos_json)

    