def main():
    print("Seleccione una opcion:\n1) Digitar los parámetros del suelo\n2) Leer un archivo\n")
    k = eval(input())
    if(k == 1):
        pasa_T4= float(input("Digite el porcentaje que pasa por el tamiz No.4: "))
        pasa_T200 = float(input("Digite el porcentaje que pasa por el tamiz No.200: "))
        lim_liquido = float(input("Digite el limite líquido: "))
        indice_plastico = float(input("Digite el indice plástico: "))
        cu = float(input("Digite el coeficiente de uniformidad Cu: "))
        cc = float(input("Digite el coeficiente de curvatura Cc: "))
        R = calsificacion(pasa_T4, pasa_T200, lim_liquido, indice_plastico, cu, cc)
        print(R)
    elif(k == 2):
        Arch = input("Introduzca el nombre del archivo. Ej: Suelos.txt")
        Suelos = open(Arch, "r")
        Resultados = open("Resultados.txt", "w+")
        f1 = Suelos.readlines()
        for x in f1:
            x = x.split(" ")
            Resultados.write(calsificacion(float(x[0]), float(x[1]), float(x[2]), float(x[3]), float(x[4]), float(x[5])) + "\n")
        Resultados.close()
        Suelos.close()


def calsificacion(pasa_T4, pasa_T200, lim_liquido, indice_plastico, cu, cc):
    TipoSuelo = ""
    if pasa_T200 > 50:
        TipoSuelo += "Es un suelo fino: "
        if lim_liquido > 50 and indice_plastico > 0.7*(lim_liquido-20):
            TipoSuelo += "limo de alta plasticidad."
        if lim_liquido < 50 and indice_plastico > 0.7*(lim_liquido - 20):
            TipoSuelo += "limo de baja plasticidad."
        if lim_liquido > 50 and indice_plastico < 0.7*(lim_liquido - 20):
            TipoSuelo += "arcilla de alta plasticidad."
        if lim_liquido < 50 and indice_plastico < 0.7*(lim_liquido - 20):
            TipoSuelo += "arcilla de baja plasticidad."
    if pasa_T200 <= 50:                                          #suelo grueso
        if pasa_T4 > 50:                                       #Arena
            TipoSuelo += "Se trata de un suelo grueso: arena, "
            if pasa_T200 < 5:                                 #usar granulometria
                if (cu > 6) and ( 1 <= cc <= 3) :
                    TipoSuelo +=  "esta bien gradada."
                else:
                    TipoSuelo += "esta pobremente gradada."
            if pasa_T200 > 5 and pasa_T200 < 12: # gradnulometria y atterberg
                if (cu > 6) and (1 <= cc <= 3):
                    TipoSuelo += " esta bien gradada."
                else:
                    TipoSuelo += " esta pobremente gradada."

                if 0.73*(lim_liquido-20) < indice_plastico:
                    TipoSuelo += "Tipo de arena: arcilla."
                else:
                    TipoSuelo += "Tipo de arena: limo."

            if  pasa_T200 > 12:                   #atterberg
                if 0.73*(lim_liquido-20) < indice_plastico:
                    TipoSuelo += " es una arena arcillosa"
                else:
                    TipoSuelo += " es una arena limosa"

        if pasa_T4 < 50:                                          #grava
            TipoSuelo += "Se trata de un suelo grueso: grava,"

            if pasa_T200 < 5:                                 #usar granulometria
                if (cu > 4) and ( 1 > cc <= 3):
                    TipoSuelo += " esta bien gradada."
                else:
                    TipoSuelo += " esta pobremente gradada."

            if pasa_T200 > 5 and pasa_T200 < 12:               # granulometria y atterberg
                if (cu > 4) and (1 > cc <= 3):
                    TipoSuelo += " esta bien gradada."
                else:
                    TipoSuelo += " esta pobremente gradada."

                if 0.73 * (lim_liquido-20) < indice_plastico:
                    TipoSuelo += "Tipo de grava: arcilla."
                else:
                    TipoSuelo += "Tipo de grava: limo."

            if  pasa_T200 > 12:                   #atterberg
                if 0.73 * (lim_liquido-20) < indice_plastico:
                    TipoSuelo += " es una grava arcillosa"
                else:
                    TipoSuelo += " es una grava limosa"
    return TipoSuelo
main()