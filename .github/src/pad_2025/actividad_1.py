import json



class Ingestiones():
    def __init__(self):
        self.ruta_static="src/pad_2025/static/"
        
    def leer_json(self):
        

        ruta_json = "{}json/datos_persona.json".format(self.ruta_static)
        datos=""
        with open(ruta_json,"r",encoding="utf-8") as f:
            datos = json.load(f)
        return datos    
    
    def leer_txt(self):
       

        ruta_json = "{}txt/info.txt".format(self.ruta_static)
        datos=""
        with open(ruta_json,"r",encoding="utf-8") as f:
            datos = f.read()
        return datos 

    def leer_varios_txt(self,nombre=""):
       

        ruta_txt = "{}txt/{}".format(self.ruta_static,nombre)
        datos=""
        with open(ruta_txt,"r",encoding="utf-8") as f:
            datos = f.read()
        return datos   

inges = Ingestiones() 
datos_json = inges.leer_json()
print(datos_json)

print("********************************************************")
datos_txt = inges.leer_txt()
print(datos_txt)

print ("*******************************************************")

nombre_archivo = "info copy.txt"
datos_txt_dos = inges.leer_varios_txt(nombre_archivo)
print(datos_txt_dos)