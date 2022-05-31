import pandas as pd
import soporte
import config as cfg
from datetime import date, timedelta
import calendar


print(f"Segund Paso Ejecutado, Se Lee y aplica reglas al archivo {cfg.dataset_customers_sum}")

df_sum, exito = soporte.abrir_archivo(cfg.dataset_customers_sum)

if not exito:
    quit() 


try: 

    perido_actual = date(int(cfg.fecha_periodo[:4]), int(cfg.fecha_periodo[5:7]), int(cfg.fecha_periodo[8:10]))

    periodo_anterior = perido_actual + timedelta(-31)
    
    diault = calendar.monthrange(periodo_anterior.year,periodo_anterior.month)
    periodo_anterior = date( periodo_anterior.year , periodo_anterior.month ,  diault[1] )

#    print(perido_actual, periodo_anterior)

# esta es la regla 1
    regla1 =  (( df_sum.job == "management" ) | ( df_sum.job == "admin." ) ) & (df_sum.date == str(periodo_anterior) )  &  (df_sum.payment >= 10000)    
    df_regla1 = df_sum[regla1][["id_customer", "payment"]].assign(Descuento=30) 
#   print(df_regla1)

# esta es la regla 2
    regla2 =  (( df_sum.job == "blue-collar" ) | ( df_sum.job == "technician" ) | ( df_sum.job == "entrepreneur" ) ) 
    regla2 = regla2 & ( df_sum.date == str(periodo_anterior) )
    regla2 = regla2 & ((df_sum.payment >= 5000) & (df_sum.payment < 10000))
    df_regla2 = df_sum[regla2][["id_customer", "payment"]].assign(Descuento=20) 
#    print(df_regla2)

# concateno las 2 reglas
    df_lista_general = pd.concat([df_regla1, df_regla2])

# guardo el archivo final   
    df_lista_general.to_csv(cfg.dataset_clientes_resultado, sep=";") 

    print(f"Archivo resultado del Pipeline {cfg.dataset_clientes_resultado}")    
    
except Exception as e:
    print("Ocurrio el siguiente error -->", e) 
 

 



 