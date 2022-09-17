# valores por colores
alieg_rojo = 10
alieg_verde = 5
alieg_azul = 2

#ingreso de datos
r = int(input("Ingrese la cantidad de alienigenas derrumbados rojos: "))
v = int(input("Ingrese la cantidad de alienigenas derrumbados verdes: "))
a = int(input("Ingrese la cantidad de alienigenas derrumbados azules: "))

#puntos por colores
total_puntos_rojo = (r * alieg_rojo)
total_puntos_verde = (v * alieg_verde)
total_puntos_azul = (a * alieg_azul)

#suma de puntos sin porcentaje
total_puntos = total_puntos_rojo + total_puntos_verde + total_puntos_azul

#porcentaje de puntos aplicando al total de puntos
bonus_rojo = int(total_puntos * 0.1)
bonus_verde = int(total_puntos * 0.05)
bonus_azul = int(total_puntos * 0.02)

#porcentaje de puntos aplicando al total de puntos por color
bonus_total_puntos_rojo = int((r * alieg_rojo)*0.1)
bonus_total_puntos_verde = int((v * alieg_verde)*0.05)
bonus_total_puntos_azul = int((a * alieg_azul)*0.02)

if (r > 10) and (v > 5) and (a > 2):
    total_ptos = total_puntos + bonus_rojo + bonus_verde + bonus_azul
    #total_ptos = total_puntos + bonus_total_puntos_rojo + bonus_total_puntos_verde + bonus_total_puntos_azul
    print("La cantidad de puntos obtenidos en el juego es de : ", total_ptos)
    
elif (v <=5) and (a > 2):
        total_ptos = total_puntos + bonus_azul
        #total_ptos = total_puntos + bonus_total_puntos_rojo + bonus_total_puntos_azul
        print("La cantidad de puntos obtenidos en el juego es de : ", total_ptos)
        
elif (a <= 2):
            total_ptos = total_puntos
            print("La cantidad de puntos obtenidos en el juego es de : ", total_ptos)
    
else:
    if(r <= 10) and (v > 5) and ( a > 2):
        total_ptos = total_puntos + bonus_verde + bonus_azul
        #total_ptos = total_puntos + bonus_total_puntos_verde + bonus_total_puntos_azul
        print("La cantidad de puntos obtenidos en el juego es de : ", total_puntos)
    
    elif(v <= 5) and (a > 2):
        total_ptos = total_puntos + bonus_azul
        #total_ptos = total_puntos + bonus_total_puntos_azul
        print("La cantidad de puntos obtenidos en el juego es de : ", total_ptos)
    
    else:
        total_ptos = total_puntos 
        print("La cantidad de puntos obtenidos en el juego es de : ", total_bonus)
        
        
        
        
    
