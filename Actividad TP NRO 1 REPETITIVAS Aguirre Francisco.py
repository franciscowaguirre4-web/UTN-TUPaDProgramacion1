#EJERCICIO 1
#Ejercicio 1— “Caja del Kiosco” 
#Objetivo: Simular una compra con validaciones y cálculo de total. 
#Requisitos 
#1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while). 
#2. Pedir cantidad de productos a comprar (número entero positivo, validar con 
#.isdigit() en while). 
#3. Por cada producto (usar for): 
#o Pedir precio (entero, validar .isdigit()). 
#o Pedir si tiene descuento S/N (validar con while, aceptar s o n en 
#cualquier mayuscula/minuscula). 
#o Si tiene descuento: aplicar 10% al precio de ese producto. 
#4. Al final mostrar: 
#o Total sin descuentos 
#o Total con descuentos 
#o Ahorro total 
#o Promedio por producto (usar float y formatear con :.2f, ejem:

nombre = input("Cliente: ").strip()

while nombre == "" or not nombre .isalpha ():
    print ("Error: ingresa un nombre no vacio y solo con letras")
    nombre = input("Cliente: ").strip()

cantidad_str = input ("Ingresa la cantidad de productos: ").strip()

while not cantidad_str .isdigit() or int(cantidad_str) == 0:
    print ("Error: ingresa un numero entero positivo mayor a cero")
    cantidad_str = input ("Ingresa la cantidad de productos: ").strip()

cantidad_int = int (cantidad_str)
total_sin_descuento = 0
total_con_descuento = 0.0 

for i in range (1, cantidad_int + 1): 
    precio_str = input (f"Producto {i} - Precio: ").strip()

    while not precio_str .isdigit() or int (precio_str) == 0: 
        print ("Error, el precio debe ser un entero positivo")
        precio_str = input (f"Producto{i}-Precio: ").strip()       
        
    precio_int= int(precio_str)

    desc = input ("Descuento (S/N): ").strip().lower()

    while desc != "s" and desc != "n":
        print ("Error: Ingrese S para si o N para no")
        desc = input ("Descuento (S/N): ").strip().lower()

    total_sin_descuento += precio_int 

    if desc == "s": 
         precio_final = precio_int * 0.9 
    else: 
         precio_final = precio_int 

    total_con_descuento += precio_final 

ahorro = total_sin_descuento - total_con_descuento 
promedio = total_con_descuento / cantidad_int

print()
print (f"Total sin descuento: ${total_sin_descuento}")
print (f"Total con descuento: ${total_con_descuento:.2f}")
print (f"Ahorro total: ${ahorro:.2f}")
print (f"Promedio: $ {promedio:.2f}")

#Ejercicio 2 — “Acceso al Campus y Menú Seguro”
#Objetivo: Login con intentos + menú de acciones con validación estricta.
#Requisitos
#1. Definir credenciales fijas en el código:
#o usuario correcto: "alumno"
#o clave correcta: "python123"
#2. Permitir máximo 3 intentos para ingresar usuario y clave.
#3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar.
#4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir:
#1. Ver estado de inscripción (mostrar “Inscripto”)
#2. Cambiar clave (pedir nueva clave y confirmación; deben
#coincidir)
#3. Mostrar mensaje motivacional (1 frase)
#4. Salir
#5. Validación del menú:
#o Debe ser número (.isdigit())
#o Debe estar entre 1 y 4

# 1. Credenciales fijas
usuario_db = "alumno"
clave_db = "python123"

intentos = 0
acceso = False

# 2 y 3. Sistema de Login
while intentos < 3:
    intentos += 1
    print(f"\nIntento {intentos}/3 - Usuario: {usuario_db if intentos > 1 else '?'}")
    user_in = input("Usuario: ")
    pass_in = input("Clave: ")

    if user_in == usuario_db and pass_in == clave_db:
        print("Acceso concedido.")
        acceso = True
        break
    else:
        print("Error: credenciales inválidas.")

if not acceso:
    print("\nCuenta bloqueada")
else:
    # 4. Menú repetitivo
    while True:
        print("\n1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
        opcion = input("Opción: ")

        # 5. Validación del menú
        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
            continue
        
        opcion = int(opcion)
        if not (1 <= opcion <= 4):
            print("Error: opción fuera de rango.")
            continue

        if opcion == 1:
            print("Inscripto")
        
        elif opcion == 2:
            # Cambio de clave con validación de longitud
            nueva = input("Nueva clave: ")
            if len(nueva) < 6:
                print("Error: mínimo 6 caracteres.")
            else:
                confirma = input("Confirme nueva clave: ")
                if nueva == confirma:
                    clave_db = nueva
                    print("Clave actualizada.")
                else:
                    print("Error: las claves no coinciden.")
        
        elif opcion == 3:
            print("No te detengas hasta que te sientas orgulloso.")
            
        elif opcion == 4:
            print("Saliendo...")
            break

#✅ Ejercicio 3 (Alta) — “Agenda de Turnos con
#Nombres (sin listas)”
#Contexto
#Hay 2 días de atención: Lunes y Martes.
#Cada día tiene cupos fijos:
#• Lunes: 4 turnos
#• Martes: 3 turnos
#Reglas
#1. Pedir nombre del operador (solo letras).
#2. Menú repetitivo hasta salir:
#1. Reservar turno
#2. Cancelar turno (por nombre)
#3. Ver agenda del día
#4. Ver resumen general
#5. Cerrar sistema
#3. Reservar:
#o Elegir día (1=Lunes, 2=Martes).
#o Pedir nombre del paciente (solo letras).
#o Verificar que no esté repetido en ese día (comparando con las variables
#ya cargadas).
#o Guardar en el primer espacio libre (ej. lunes1, lunes2…).
#4. Cancelar:
#o Elegir día.
#o Pedir nombre del paciente (solo letras).
#o Si existe, cancelar y dejar el espacio vacío ("").
#5. Ver agenda del día:
#o Mostrar los turnos del día en orden (Turno 1..N), indicando “(libre)” si
#está vacío.
#6. Resumen general:
#o Turnos ocupados y disponibles por día.
#o Día con más turnos (o empate).



# Inicialización de variables (Sin listas)
lunes1 = ""; lunes2 = ""; lunes3 = ""; lunes4 = ""
martes1 = ""; martes2 = ""; martes3 = ""

# 1. Pedir nombre del operador
operador = ""
while True:
    operador = input("Nombre del operador: ")
    if operador.isalpha():
        break
    print("Error: Solo letras.")

# 2. Menú repetitivo
while True:
    print(f"\n--- SISTEMA DE TURNOS | Operador: {operador} ---")
    print("1. Reservar turno\n2. Cancelar turno\n3. Ver agenda del día\n4. Ver resumen general\n5. Cerrar sistema")
    opc = input("Seleccione opción: ")

    if not opc.isdigit():
        print("Error: Ingrese un número.")
        continue
    
    opc = int(opc)

    # 3. Reservar
    if opc == 1:
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        if dia == "1":
            paciente = input("Nombre paciente: ")
            if not paciente.isalpha():
                print("Error: Solo letras.")
            elif paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Error: Paciente ya tiene turno este día.")
            elif lunes1 == "": lunes1 = paciente; print("Turno 1 asignado.")
            elif lunes2 == "": lunes2 = paciente; print("Turno 2 asignado.")
            elif lunes3 == "": lunes3 = paciente; print("Turno 3 asignado.")
            elif lunes4 == "": lunes4 = paciente; print("Turno 4 asignado.")
            else: print("Sin cupos para el Lunes.")
        elif dia == "2":
            paciente = input("Nombre paciente: ")
            if not paciente.isalpha():
                print("Error: Solo letras.")
            elif paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Error: Paciente ya tiene turno este día.")
            elif martes1 == "": martes1 = paciente; print("Turno 1 asignado.")
            elif martes2 == "": martes2 = paciente; print("Turno 2 asignado.")
            elif martes3 == "": martes3 = paciente; print("Turno 3 asignado.")
            else: print("Sin cupos para el Martes.")

    # 4. Cancelar
    elif opc == 2:
        dia = input("Día para cancelar (1=Lunes, 2=Martes): ")
        paciente = input("Nombre paciente a cancelar: ")
        if dia == "1":
            if lunes1 == paciente: lunes1 = ""; print("Cancelado.")
            elif lunes2 == paciente: lunes2 = ""; print("Cancelado.")
            elif lunes3 == paciente: lunes3 = ""; print("Cancelado.")
            elif lunes4 == paciente: lunes4 = ""; print("Cancelado.")
            else: print("Paciente no encontrado.")
        elif dia == "2":
            if martes1 == paciente: martes1 = ""; print("Cancelado.")
            elif martes2 == paciente: martes2 = ""; print("Cancelado.")
            elif martes3 == paciente: martes3 = ""; print("Cancelado.")
            else: print("Paciente no encontrado.")

    # 5. Ver agenda
    elif opc == 3:
        dia = input("Ver agenda (1=Lunes, 2=Martes): ")
        if dia == "1":
            print(f"1: {lunes1 if lunes1!='' else '(libre)'}")
            print(f"2: {lunes2 if lunes2!='' else '(libre)'}")
            print(f"3: {lunes3 if lunes3!='' else '(libre)'}")
            print(f"4: {lunes4 if lunes4!='' else '(libre)'}")
        elif dia == "2":
            print(f"1: {martes1 if martes1!='' else '(libre)'}")
            print(f"2: {martes2 if martes2!='' else '(libre)'}")
            print(f"3: {martes3 if martes3!='' else '(libre)'}")

    # 6. Resumen General
    elif opc == 4:
        ocu_l = 0; ocu_m = 0
        if lunes1 != "": ocu_l += 1
        if lunes2 != "": ocu_l += 1
        if lunes3 != "": ocu_l += 1
        if lunes4 != "": ocu_l += 1
        if martes1 != "": ocu_m += 1
        if martes2 != "": ocu_m += 1
        if martes3 != "": ocu_m += 1
        
        print(f"Lunes: {ocu_l} ocupados, {4-ocu_l} libres.")
        print(f"Martes: {ocu_m} ocupados, {3-ocu_m} libres.")
        
        if ocu_l > ocu_m: print("Día con más turnos: Lunes")
        elif ocu_m > ocu_l: print("Día con más turnos: Martes")
        else: print("Empate en ocupación.")

    elif opc == 5:
        print("Cerrando sistema..."); break

#Ejercicio 4 — “Escape Room: La Bóveda”
#Historia
#Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo
#limitados.
#Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.
#Variables iniciales (NO se piden por teclado)
#• energia = 100
#• tiempo = 12
#• cerraduras_abiertas = 0
#• alarma = False
#• codigo_parcial = ""
#Validaciones obligatorias
#• No usar try/except.
# Pedir nombre del agente y validar con .isalpha() en un while.
#• Validar opciones del menú y cualquier número pedido con .isdigit() en un
#while.
#• El juego debe funcionar con estructuras secuenciales, condicionales y
#repetitivas (puede usar funciones propias del lenguaje como .lower(), len(),
#formateo, etc.).
#Regla anti-spam (muy importante)
#Para evitar que el jugador gane eligiendo “Forzar cerradura” 3 veces seguidas al
#iniciar:
#✅ Si el jugador elige Forzar cerradura (opción 1) 3 veces seguidas, entonces:
#• se cobra el costo normal (-20 energía, -2 tiempo),
#• NO abre cerradura, y
#• se activa la alarma automáticamente (alarma = True) porque “la cerradura se
#trabó”.
#Si el jugador elige opción 2 o 3, se corta la racha de “forzar seguidas”.
#Menú de acciones (se repite mientras el juego siga)
#El juego continúa mientras:
#• energia > 0, tiempo > 0, cerraduras_abiertas < 3
#• y no esté bloqueado por alarma.
#En cada turno mostrar el estado y el siguiente menú:
#1. Forzar cerradura (costo: -20 energía, -2 tiempo)
#o Si la energía está por debajo de 40, hay “riesgo de alarma”:
#▪ pedir un número 1-3 (validado). Si elige 3 → alarma=True.
#o Si no hay alarma, abre 1 cerradura.
#o Regla anti-spam: si es la 3ra vez seguida forzando, se activa alarma y
#no abre.
#2. Hackear panel (costo: -10 energía, -3 tiempo)
#o Debe usar un for de 4 pasos mostrando progreso.
#o En cada paso sumar una letra al codigo_parcial (por ejemplo “A”).
#o Si len(codigo_parcial) >= 8, se abre automáticamente 1 cerradura si
#todavía faltan3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10
#energía extra)
#Regla de bloqueo por alarma
#• Si alarma == True y tiempo <= 3 y todavía no se abrió la bóveda, el sistema
#se bloquea y se pierde.
#Condiciones de fin
#• Si cerraduras_abiertas == 3 → VICTORIA
#• Si energia <= 0 o tiempo <= 0 → DERROTA
#• Si se bloquea por alarma → DERROTA (bloqueo)


# Variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzado_seguido = 0 # Contador para regla anti-spam

# 1. Validar nombre del agente
nombre = ""
while True:
    nombre = input("Nombre del agente (solo letras): ")
    if nombre.isalpha():
        break
    print("Error: El nombre debe contener solo letras.")

print(f"\nBienvenido, Agente {nombre}. La misión comienza.")

# Bucle principal del juego
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    # Regla de bloqueo por alarma
    if alarma and tiempo <= 3:
        print("\n--- ¡SISTEMA BLOQUEADO POR ALARMA! DERROTA ---")
        break

    print(f"\nESTADO: Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3 | Alarma: {'ON' if alarma else 'OFF'}")
    print("1. Forzar cerradura (-20 E, -2 T)")
    print("2. Hackear panel (-10 E, -3 T)")
    print("3. Descansar (+15 E, -1 T)")
    
    opc = input("Acción: ")
    if not opc.isdigit():
        print("Error: Ingrese un número válido.")
        continue
    
    opc = int(opc)

    # ACCIÓN 1: FORZAR
    if opc == 1:
        forzado_seguido += 1
        energia -= 20
        tiempo -= 2
        
        # Regla anti-spam
        if forzado_seguido == 3:
            alarma = True
            print("¡La cerradura se trabó por forzar repetidamente! ALARMA ACTIVADA.")
        else:
            # Riesgo de alarma por baja energía
            if energia < 40:
                print("¡Riesgo de alarma! La cerradura está dura.")
                while True:
                    num = input("Elija un número de seguridad (1-3): ")
                    if num.isdigit() and 1 <= int(num) <= 3:
                        if int(num) == 3:
                            alarma = True
                            print("¡Activaste los sensores! ALARMA ON.")
                        break
                    print("Error: Elija 1, 2 o 3.")
            
            if not alarma:
                cerraduras_abiertas += 1
                print("¡Cerradura abierta con fuerza!")

    # ACCIÓN 2: HACKEAR
    elif opc == 2:
        forzado_seguido = 0 # Rompe racha
        energia -= 10
        tiempo -= 3
        print("Iniciando bypass...")
        for i in range(1, 5):
            print(f"Progreso: {i*25}%...")
            codigo_parcial += "A"
        
        if len(codigo_parcial) >= 8:
            cerraduras_abiertas += 1
            codigo_parcial = "" # Reinicia código tras abrir
            print("¡Código descifrado! Una cerradura se liberó.")

    # ACCIÓN 3: DESCANSAR
    elif opc == 3:
        forzado_seguido = 0 # Rompe racha
        recuperacion = 15
        if alarma:
            recuperacion -= 10
            print("El ruido de la alarma no te deja descansar bien.")
        
        energia += recuperacion
        if energia > 100: energia = 100
        tiempo -= 1
        print(f"Energía recuperada. Actual: {energia}")

    else:
        print("Opción fuera de rango.")

# CONDICIONES DE FIN
if cerraduras_abiertas >= 3:
    print(f"\n¡VICTORIA! El Agente {nombre} ha abierto la bóveda.")
elif energia <= 0:
    print("\nDERROTA: Te has quedado sin energía.")
elif tiempo <= 0:
    print("\nDERROTA: Se acabó el tiempo.")

#Ejercicio 5 — “Escape Room:"La Arena del
#Gladiador"
#1. Descripción del Escenario
#Vas a desarrollar un simulador de batalla por turnos en Python. El programa enfrentará a un
#usuario (Gladiador) contra un oponente controlado por la computadora (Enemigo). El
#objetivo es reducir los puntos de vida del oponente a cero antes de que él lo haga contigo.
#Este ejercicio evalúa el uso de variables (int, float, string, boolean), estructuras de
#control (if/elif/else), ciclos (while y for) y validación de datos estricta.
#2. Requerimientos Técnicos
#A. Tipos de Datos
#Debes utilizar obligatoriamente los siguientes tipos de datos para las variables del juego:
#• • String: Para el nombre del jugador.
#• • Int: Para los Puntos de Vida (HP) y cantidad de pociones.
#• • Float: Para el cálculo del daño (ej: un golpe crítico multiplica el ataque por 1.5).
#• • Boolean: Para controlar si el juego sigue activo o quién tiene el turno.
#B. Reglas de Validación (¡Importante!)
#• • No está permitido usar bloques try / except.
#• • Para validar texto, debes usar el método .isalpha() dentro de un ciclo while.
#• • Para validar números, debes usar el método .isdigit() dentro de un ciclo
#while.
#3. Flujo del Programa
#Paso 1: Configuración del Personaje
#El programa inicia pidiendo el nombre del Gladiador.
#• • Validación: El nombre solo puede contener letras. Si el usuario ingresa números,
#símbolos o lo deja vacío, el programa debe decir "Error: Solo se permiten letras" y volver a
#preguntar hasta que sea válido.
#Paso 2: Inicialización de Estadísticas 
#El programa debe definir las variables iniciales (sin preguntar al usuario):
#• • Vida del Gladiador: 100 (int)
#• • Vida del Enemigo: 100 (int)
#• • Pociones de Vida: 3 (int)
#• • Daño base "Ataque Pesado": 15 (int)
#• • Daño base del enemigo: 12 (int)
#• • Turno Gladiador : True (booleano)
#Paso 3: El Ciclo de Combate
#El juego entra en un ciclo que se repite mientras ambos combatientes tengan más de 0
#puntos de vida.
#Turno del Jugador:
#Muestra la vida actual de ambos y las pociones restantes. Luego, ofrece un menú con 3
#opciones:
#1. Ataque Pesado
#2. Ráfaga Veloz (Requiere uso de for)
#3. Curar
#• Validación del Menú: El programa debe pedir la opción al usuario. 1. Verificar que lo
#ingresado sea un número (.isdigit()).
#2. Verificar que el número sea 1, 2 o 3.
#o Si falla alguna validación, mostrar mensaje de error y volver a pedir.
#Lógica de las Acciones:
#Acción A: Ataque Pesado (Opción 1)
#• • Calcula el daño final. Si la vida del enemigo es menor a 20 puntos, el jugador
#realiza un "Golpe Crítico" multiplicando su daño base por 1.5 (resultado float).
#• • Resta el daño a la vida del enemigo.
#• • Muestra un mensaje: "¡Atacaste al enemigo por X puntos de daño!"
#Acción B: Ráfaga Veloz (Opción 2)
#• • Esta acción realiza una serie de golpes rápidos. Debes implementar un bucle for.
#• • El bucle debe repetirse 3 veces (usando range).
#• • Dentro del bucle, en cada repetición: 1. Resta 5 puntos de daño a la vida del enemigo.
#• 2. Muestra el mensaje: " > Golpe conectado por 5 de daño".

#Acción C: Curar (Opción 3) • • Si tienes pociones (> 0): Suma 30 puntos a tu vida y resta 1 poción.
#• • Si NO tienes pociones: Muestra "¡No quedan pociones!" y pierdes el turno (el
#enemigo ataca igual).
#Turno del Enemigo:
#Justo después de tu acción, el enemigo ataca automáticamente.
#• • Resta el daño base del enemigo (12) a tu vida.
#• • Muestra un mensaje: "¡El enemigo te atacó por 12 puntos de daño!"
#Paso 4: Fin del Juego
#Cuando el ciclo termine (porque la vida de alguno llegó a 0 o menos), debes evaluar:
#• • Si vida_jugador > 0: Mostrar "¡VICTORIA! [Nombre] ha ganado la batalla."
#• • Si vida_jugador <= 0: Mostrar "DERROTA. Has caído en combate."        


# Paso 1: Configuración del Personaje
nombre_jugador = ""
while True:
    nombre_jugador = input("Ingrese el nombre del Gladiador: ")
    if nombre_jugador.isalpha():
        break
    print("Error: Solo se permiten letras")

# Paso 2: Inicialización de Estadísticas
vida_gladiador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado_base = 15
ataque_enemigo_base = 12
juego_activo = True  # Boolean para controlar el flujo si fuera necesario

# Paso 3: El Ciclo de Combate
while vida_gladiador > 0 and vida_enemigo > 0:
    print(f"\n" + "="*30)
    print(f"ESTADO: {nombre_jugador} (HP: {vida_gladiador}) | Enemigo (HP: {vida_enemigo})")
    print(f"Pociones restantes: {pociones}")
    print("="*30)
    
    # Menú del Jugador con Validación Estricta
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")
    
    opcion = ""
    while True:
        opcion = input("Elija su acción (1-3): ")
        if opcion.isdigit():
            if 1 <= int(opcion) <= 3:
                break
            else:
                print("Error: El número debe estar entre 1 y 3.")
        else:
            print("Error: Ingrese un número válido.")
    
    opcion = int(opcion)

    # Lógica de las Acciones del Jugador
    if opcion == 1:
        # Ataque Pesado con Golpe Crítico (Float)
        daño_final = float(ataque_pesado_base)
        if vida_enemigo < 20:
            daño_final = ataque_pesado_base * 1.5
            print("¡GOLPE CRÍTICO!")
        
        vida_enemigo -= int(daño_final)
        print(f"¡Atacaste al enemigo por {daño_final} puntos de daño!")

    elif opcion == 2:
        # Ráfaga Veloz con bucle for
        print("¡Iniciando Ráfaga Veloz!")
        for i in range(3):
            vida_enemigo -= 5
            print(" > Golpe conectado por 5 de daño")

    elif opcion == 3:
        # Curar
        if pociones > 0:
            vida_gladiador += 30
            if vida_gladiador > 100: # Opcional: limitar a vida máxima original
                vida_gladiador = 100
            pociones -= 1
            print(f"¡Te has curado! Vida actual: {vida_gladiador}")
        else:
            print("¡No quedan pociones! Has perdido la oportunidad.")

    # Verificar si el enemigo murió antes de que contraataque
    if vida_enemigo <= 0:
        break

    # Turno del Enemigo (Automático)
    print("\n--- Turno del Enemigo ---")
    vida_gladiador -= ataque_enemigo_base
    print(f"¡El enemigo te atacó por {ataque_enemigo_base} puntos de daño!")

# Paso 4: Fin del Juego
print("\n" + "#"*30)
if vida_gladiador > 0:
    print(f"¡VICTORIA! {nombre_jugador} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
print("#"*30)


