import os
import time
import datetime
time.sleep(2)
os.system('cls')

print('''
    CALCULA TU ÍNDICE DE MASA CORPORAL (IMC)
    El índice de masa corporal (IMC) es una razón matemática que asocia la masa y la talla de una persona.
    Fue ideado por el estadístico belga Adolphe Quetelet.
    (*) El IMC es un criterio ampliamente aceptado pero no es exacto.
    ''')

def guardar_consulta():
    registro = open('consultas.txt', 'a')
    registro.write(str(datetime.datetime.now().replace(microsecond=0)) + ' | Cálculo de IMC de ' + nombre + ': ' + str(calculo) + ' (' + valor + ')\n')
    registro.close()
while True:
    nombre = input('¿Cómo te llamás?: ')
    try:
        peso = int(input('¿Cuánto pesás? (en kilogramos): '))
    except ValueError:
        print('(Sólo se permite el ingreso de números, intentá nuevamente)')
        continue
    try:
        altura = int(input ('¿Cuánto medís? (en centímetros): '))
    except ValueError:
        print('(Sólo se permite el ingreso de números, intentá nuevamente)')
        continue
    
    calculo = round((peso / (altura/100)**2), 2)
    print('\nTu IMC es: ' + str(calculo))                         #Paso la variable float a string
    
    if calculo < 16.00:
        valor = 'El valor es considerado como delgadez severa.'
    elif calculo < 16.99:
        valor = 'El valor es considerado como delgadez moderada.'
    elif calculo < 18.49:
        valor = 'El valor es considerado como delgadez leve.'
    elif calculo < 24.99:
        valor = 'El valor es considerado como normal.'
    elif calculo < 29.99:
        valor = 'El valor es considerado como sobrepeso.'
    elif calculo < 34.99:
        valor = 'El valor es considerado como obesidad leve.'
    elif calculo < 39.99:
        valor = 'El valor es considerado como obesidad media.'
    elif calculo >= 40.00:
        valor = 'El valor es considerado como obesidad mórbida.'
    print(valor)
    guardar_consulta()
    continuar = input('\n¿Querés hacer otra consulta? (sí / no): ')
    if continuar == ('s'):
        continue
    elif continuar == ('si'):
        continue
    elif continuar == ('sí'):
        continue
    else:
        print('\nGracias por utilizar el programa.')
        break