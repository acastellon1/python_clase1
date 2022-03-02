

from ast import If


def Calcularsueldo(sueldo, diastrabajados):
    sueldoapagar = (sueldo/30)*diastrabajados
    return sueldoapagar

def main():
    SALARIOMIN = 1000000
    SUBALIMENT = 120000
    SUBTRANSP = 80000
    BONO = 50000
    nombre = input("Digite su nombre ==>  ")
    sueldo = int(input("Digite su sueldo ==>  "))
    diastrabajados = int(input("Digite los dias laborados ==>  "))
    sueldoapagar = Calcularsueldo(sueldo, diastrabajados)

    if sueldo < (SALARIOMIN * 2):
        sueldoapagar = sueldoapagar + SUBALIMENT + SUBTRANSP
    else:
        sueldoapagar = sueldoapagar + BONO    

    print(f"Su nombre es: {nombre} y su sueldo correspondiente es: {sueldoapagar: .0f}")



if __name__ == "__main__":
    main()
