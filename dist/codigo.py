import hashlib

def simular_sha256(texto):
    resultado = hashlib.sha256(texto.encode())
    return resultado.hexdigest()

def minar_bloque(datos_transaccion, dificultad):
    """
    Intenta encontrar un hash que comience con 'n' ceros (dificultad).
    """
    nonce = 0
    objetivo = "0" * dificultad
    
    print(f"--- Iniciando minería con dificultad: {dificultad} ---")
    
    while True:
        contenido = f"{datos_transaccion}{nonce}"
        hash_intentado = simular_sha256(contenido)
        
        if nonce < 6:
            print(f"Nonce: {nonce} -> Hash: {hash_intentado}")
        elif nonce == 6:
            print("...")
        if hash_intentado.startswith(objetivo):
            print(f"\n¡BLOQUE MINADO!")
            print(f"Nonce final: {nonce}")
            print(f"Hash válido: {hash_intentado}")
            return hash_intentado
        
        nonce += 1

# --- PRUEBA DEL SIMULADOR ---
mensaje = "Bitcoin: De Alex Reyes TI BIS: 5to año 2026"

# 1. Ver un hash simple
print(f"Hash inicial de '{mensaje}':\n{simular_sha256(mensaje)}\n")

# 2. Simular el proceso de minería (buscar 4 ceros al principio)
minar_bloque(mensaje, dificultad=4)