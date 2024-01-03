ingreso_mensual= 60
gasto_mensual = 8000

#if anidados y elif

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en déficit")
    elif ingreso_mensual -gasto_mensual > 3000:
        print("estas bien, seguí así")
    else:
        print("La verdad que estas gastando mucho, controlá tus adicciones")
elif ingreso_mensual >1000:
    print("estas bien en latinoamérica")
elif ingreso_mensual >500:
    print("estas bien en argentina")
elif ingreso_mensual >200:
    print ("estas bien en venezuela")
else:
    print("Tenes que buscar otro trabajo")