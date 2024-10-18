# Trigotech 
## Descrição do projeto 

O objetivo era criar uma ferramenta simples que permitisse aos usuários inserir um ângulo em graus e obter o valor do seno correspondente.

## Funcionalidades

O seno é a razão entre o cateto oposto e a um ângulo e a hipotenusa em um circulo trigonométrico. 
Com isso quando o usuário enserir o ângulo que, queira calcular e com isso ela deve da o resultado correto em radiado.

## Tecnologias utilizadas 

A linguagem que usamos foi o pyhton;

Usamos o Vs code;

github. 

## Membros da Equipe 

* Anah Melissa;
* Mariana Eduarda;
* Pedro Vieira;
* Sara Ferreira;
* Ylena Maria;

## Dificuldades 

A nossa maior dificuldade é que tentamos passar a linguagem de Python para Javascript, Nós até conseguimos.
Mas quando fomos testar, acabava que o resultado não aparecia para o usuário.

## Algoritimo

```
import math

def calculadora_seno():
 """Uma função simples para calcular o seno de um angulo."""

while True: 
angulo = float(input("Digite o ângulo em graus: "))

# Convertendo para radianos
 angulo_radianos = math.radians (angulo)

#Calculando o seno 
resultado = math.sin(angulo_radianos)

print(f"o seno de {angulo} graus é: (resultado: .4f}")

#Perguntando se deseja continuar 
continuar input("Deseja calcular outro seno? (sim/não): ") 
if continuar. lower() != 'sim':

break

If __name__== "__main__":
calculadora_ seno()
