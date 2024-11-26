#promedio duracion
duracion_min_otros= 2.5
duracion_max_otros= 7
duracion_promedio_otros=4
duracion_propia= 1.5

#duracion horas sin editar
promedio_otros= 5
propia = 3.5

#DURACION CON RESPECTO A OTROS Y PROMEDIOS %
dif_con_min= 100-(duracion_propia / duracion_min_otros * 100)
dif_con_max= 100-(duracion_propia *1000 // duracion_max_otros / 10)
dif_con_prom= 100-(duracion_propia / duracion_promedio_otros * 100)

#Promedio de edicion
edicion_promedio_otros= 100-(duracion_promedio_otros *1000 // promedio_otros  / 10)
edicion_promedio_propia= 100-(duracion_propia  *1000 // propia / 10)


#SHOWS resultados
print(f'Duracion propia es {dif_con_min}% menos que la mas rapida del mercado')
print(f'Duracion propia es {dif_con_max}% menos que la mas lenta del mercado')
print(f'Duracion propia es {dif_con_prom}% menos que el promedio del mercado')

print(f'En promedio otros editan {edicion_promedio_otros}% de tiempo')
print(f'En promedio se edita {edicion_promedio_propia}% de tiempo')

print(f'Ver 10 horas aqui serian ver {duracion_promedio_otros * 100 // duracion_propia / 10} horas de otro')