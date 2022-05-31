# docker build -t desafio_la_caja .
# docker images
# docker run desafio_la_caja
# docker run  -it desafio_la_caja /bin/bash


#Module A: debe realizar el join de los datasets
# de entrada donde la salida debe ser los pagos sumarizados para cada uno de los clientes.

from numpy import empty
import pandas as pd
import config as cfg
import soporte


# abro el archivo de clientes
df_customers, exito = soporte.abrir_archivo(cfg.dataset_customers)
 
if not exito:
    quit()


# abro el archivo de pagos    
df_payments, exito = soporte.abrir_archivo(cfg.dataset_payments)
 
if not exito:
    quit() 

# uno los 2 datasets 
df_sum = df_customers.join(df_payments.set_index('id_customer'), on='id_customer')

# sumarizo por pagos
df_sum = df_sum.groupby(by=["id_customer", "date", "job","marital","education"]).sum("payment")
 
# doy aviso y grabo 
print(f"Primer Paso Ejecutado, Se crea el archivo {cfg.dataset_customers_sum}")
df_sum.to_csv(cfg.dataset_customers_sum, sep=";")

# ejecuto el segundo paso del pipe
exec(open(cfg.step2).read())
 
 

 
 


 




 
 