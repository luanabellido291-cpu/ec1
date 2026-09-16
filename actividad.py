print("REVISION FACIL DE CONTRATOS")
print("Bienvenido al sistema de revisión de contratos.")
print("Responde si o no a las siguientes preguntas para determinar si el contrato es válido.")


pregunta1 = input("1. ¿El contrato tiene los nombres completos de las personas o empresas que van a firmar?")
pregunta2 = input("2. ¿Las dos partes están de acuerdo con lo que dice el contrato?")
pregunta3 = input("3. ¿El contrato explica claramente para qué se está haciendo el acuerdo?")
pregunta4 = input("4. ¿El contrato indica qué debe hacer cada persona que participa?")
pregunta5 = input("5. ¿El contrato indica cuanto tiempo va a durar el acuerdo?")
pregunta6 = input("6. ¿El contrato explica cuando y como se realizaran los pagos?")
pregunta7 = input("7. ¿El contrato dice que pasa si una de las personas no cumple con lo acordado?")
pregunta8 = input("8. ¿Hay alguna parte del contrato que no entiende o que le parece confusa?")

if pregunta1 == "si" and pregunta2 == "si" and pregunta3 == "si" and pregunta4 == "si" and pregunta5 == "si" and pregunta6 == "si" and pregunta7 == "si" and pregunta8 == "no":
    print("Resultado: Bajo riesgo.")
elif pregunta1 == "si" and pregunta3 == "si" and pregunta4 == "si" and pregunta8 == "si":
    print("Resultado: Riesgo medio.")
else: 
    print("Resultado: Requiere mayor revisión.")