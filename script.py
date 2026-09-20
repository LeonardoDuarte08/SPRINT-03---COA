from machine import Pin
from time import sleep

led_verde = Pin(5, Pin.OUT)
led_amarelo = Pin(4, Pin.OUT)
led_vermelho = Pin(3, Pin.OUT)

# SITUACAO 1

geracao = 4000
consumo = 1500
disponivel = geracao - consumo

led_verde.off()
led_amarelo.off()
led_vermelho.off()

print("SITUACAO 1")
print("GERACAO:", geracao, "W")
print("CONSUMO:", consumo, "W")
print("DISPONIVEL:", disponivel, "W")

if disponivel >= 1000:
    led_verde.on()
    print("STATUS: RECARGA AUTORIZADA")

print("Decimal:", disponivel)
print("Binario:", bin(disponivel))
print("Hexadecimal:", hex(disponivel))

sleep(5)

# SITUACAO 2

geracao = 1800
consumo = 1500
disponivel = geracao - consumo

led_verde.off()
led_amarelo.off()
led_vermelho.off()

print()
print("SITUACAO 2")
print("GERACAO:", geracao, "W")
print("CONSUMO:", consumo, "W")
print("DISPONIVEL:", disponivel, "W")

if disponivel > 0 and disponivel < 1000:
    led_amarelo.on()
    print("STATUS: RECARGA REDUZIDA")

sleep(5)

# SITUACAO 3

geracao = 1000
consumo = 1800
disponivel = geracao - consumo

led_verde.off()
led_amarelo.off()
led_vermelho.off()

print()
print("SITUACAO 3")
print("GERACAO:", geracao, "W")
print("CONSUMO:", consumo, "W")
print("DISPONIVEL:", disponivel, "W")

if disponivel <= 0:
    led_vermelho.on()
    print("STATUS: RECARGA BLOQUEADA")
