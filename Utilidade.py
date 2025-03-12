def validar_numero(numero):
    try:
        return float(numero)
    except ValueError:
        raise ValueError("Entrada inválida. Insira um novo número.")