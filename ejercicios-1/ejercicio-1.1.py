otros_cursos_min = 2.5
otros_cursos_max= 7
otros_cursos_promedio= 4
dalto_curso=1.5

#duración de crudos
crudo_promedio=5
crudo_dalto=3.5

#diferencias de duración
diferencia_con_min= 100- dalto_curso /otros_cursos_min *100
diferencia_con_max=100 - dalto_curso *1000 //otros_cursos_max /10
diferencia_con_promedio= 100 -dalto_curso/otros_cursos_promedio*100


#Calculando porcentaje de espacios vacíos que se remueven
tiempo_vacio_promedio= 100 - otros_cursos_promedio*1000 //crudo_promedio /10
tiempo_vacio_dalto= 100- dalto_curso *1000 //crudo_dalto /10

#mostrando diferencias de duración
print("----------------")
print(f'''El curso de dalto dura: 
 - Un {diferencia_con_max}% menos que el mas rápido.
 - Un{int(diferencia_con_min)}% menos que el mas lento.
 - Un{diferencia_con_promedio}% menos que el promedio''')
print("----------------")
#mostrando porcentaje de tiempo vacío removido
print(f'Un curso promedio elimina un {int(tiempo_vacio_promedio)}% de tiempo vacío')
print(f'Un curso de Dalto eliminó el {tiempo_vacio_dalto}% de tiempo vacío')
print("----------------")
print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_promedio *100 //dalto_curso /10} horas de otros cursos')
print(f'Ver 10 horas de otros cursos equivale a ver {dalto_curso *100 // otros_cursos_promedio/10} horas de este curso')
print("----------------")