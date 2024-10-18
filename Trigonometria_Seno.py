import math

def calculadora_seno():
  """Uma função simples para calcular o seno de um ângulo."""

  while True:
    angulo = float(input("Digite o ângulo em graus: "))

    # Convertendo para radianos
    angulo_radianos = math.radians(angulo)

    # Calculando o seno
    resultado = math.sin(angulo_radianos)

    print(f"O seno de {angulo} graus é: {resultado:.4f}")

    # Perguntando se deseja continuar
    continuar = input("Deseja calcular outro seno? (sim/não): ")
    if continuar.lower() != 'sim':
      break

if __name__ == "__main__":
  calculadora_seno()