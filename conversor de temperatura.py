while True:
    print("🌡️ conversor de temperatura 🌡️")
    print("Digite 'sair' para encerrar")

    entradaC = input("Digite a temperatura °C e converta para °F: ")
    if entradaC.lower() == "sair":
        print("Encerrado")
        break

    entradaF = input("Digite a temperatura °F e converta para °C: ")
    if entradaF.lower() == "sair":
        print("Encerrado")
        break

    try:
        temperaturaC = float(entradaC)
        temperaturaF = float(entradaF)
    except ValueError:
        print("Letras não são válidas, digite apenas números!")
        continue

    conversorC = (temperaturaC * 9/5) + 32
    conversorF = (temperaturaF - 32) * 5/9
    print(f"{temperaturaC}°C = {conversorC:.2f}°F")
    print(f"{temperaturaF}°F = {conversorF:.2f}°C")
