import pandas as pd
 

def abrir_archivo(name):

    exito = True

    try:
    
        name = pd.read_csv(name, sep = ";",   encoding="latin1")

    except:
        
     
        exito = False   
        print(f"El archivo {name} no se encuentra, revisar el archivo config.py")
     

    return name, exito
