# SPRINT 03---COMPUTER-ORGANIZATION-AND-ARCHITECTURE

## Integrantes

- Leonardo Gabriel Sá Duarte — RM 569029
- Timoteo de Andrade Romano — RM 569711
- Bruno Albuquerque Aguiar — RM 569035
- João Pedro Conturbia — RM 569788
- Eduardo Oliveira  — RM 570374
- Enzo De Nadai - RM 569985

---

## Sobre o projeto

O objetivo da atividade foi desenvolver um protótipo de um sistema inteligente de controle de sessão de recarga utilizando o Raspberry Pi Pico e MicroPython.

A simulação foi desenvolvida no Wokwi e utiliza valores simulados de geração e consumo de energia para determinar se uma sessão de recarga deverá ser autorizada, reduzida ou bloqueada.

O projeto foi inspirado no conceito de gerenciamento inteligente de energia utilizado em soluções como a GoodWe Smart Energy Controller.

---

## Funcionamento

O sistema utiliza dois valores principais:

- Geração de energia;
- Consumo da residência.

A partir desses valores, é calculada a energia disponível:

```text
Energia Disponível = Geração - Consumo
```

Com base no resultado:

- **LED Verde (GP5):** Recarga Autorizada
- **LED Amarelo (GP3):** Recarga Reduzida
- **LED Vermelho (GP4):** Recarga Bloqueada

## Cenários testados

| Geração | Consumo | Disponível | Resultado |
|---:|---:|---:|---|
| 4000 W | 1500 W | 2500 W | Recarga Autorizada |
| 1800 W | 1500 W | 300 W | Recarga Reduzida |
| 1000 W | 1800 W | -800 W | Recarga Bloqueada |

## Representação de dados

Para o valor de **2500 W**:

- Decimal: `2500`
- Binário: `100111000100`
- Hexadecimal: `9C4`

## Conceitos aplicados

O projeto demonstra os conceitos de:

- Entrada de dados;
- Processamento;
- Memória;
- Saída;
- Sistemas numéricos;
- Integração entre hardware e software.

## Tecnologias

- Raspberry Pi Pico
- MicroPython
- Wokwi
