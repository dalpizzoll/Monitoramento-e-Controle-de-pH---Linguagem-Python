##Controle de Dosagem em Tanques de Fluidos (Batelada)

Sistema em Python para monitoramento e controle de qualidade de pH em processos industriais por batelada, voltado para automação nas indústrias química, alimentícia e de saneamento.

---

## 📌 Visão Geral

O projeto simula a amostragem e a validação contínua do pH em múltiplos tanques de processamento utilizando redundância de sensores. A partir da média ponderada de leitura de cada tanque, o sistema determina se o lote está dentro dos parâmetros exigidos para liberação do escoamento ou se deve reter o produto e emitir alarmes operacionais.

---

## ⚙️ Funcionalidades

- **Amostragem Multissensor:** Simulação de múltiplos sensores por tanque para cálculo de média representativa.
- **Validação Inteligente de Lote:** Avaliação do pH médio contra os limites operacionais predefinidos.
- **Tomada de Decisão Automatizada:**
  - **Lote Conforme:** Abertura automática da válvula de escoamento.
  - **Lote Não Conforme:** Retenção do lote, diagnóstico de acidez/alcalinidade e acionamento de alarme químico.
- **Loop de Monitoramento em Tempo Real:** Execução contínua com intervalo configurável entre ciclos de leitura.

---

## 📐 Parâmetros do Sistema

| Parâmetro | Valor Padrão | Descrição |
| :--- | :--- | :--- |
| `linhas` | `4` | Quantidade de tanques na planta |
| `colunas` | `3` | Sensores de pH instalados por tanque |
| `faixa_min` | `6.5` | Limite inferior de pH permitido |
| `faixa_max` | `7.5` | Limite superior de pH permitido |
| `time.sleep` | `20s` | Intervalo de tempo entre varreduras |

---

## 🔄 Fluxo do Algoritmo

1. **`coletar_ph_tanques()`**: Gera matriz de leituras ($5.5 \le \text{pH} \le 8.5$) simulando a telemetria dos sensores.
2. **`validar_lotes()`**: Processa a média de pH por tanque e retorna o vetor de status (`1` para liberado, `0` para retido).
3. **`acionar_valvulas_escoamento()`**: Define a atuação física (abertura de válvula ou alarme químico).
4. **Exibição e Controle**: Apresenta no console o status detalhado do tanque e aguarda o ciclo seguinte.

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.x instalado (não requer instalação de pacotes externos).

### Execução
1. Clone o repositório ou faça o download do arquivo `.py`:
   ```bash
   git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
   cd nome-do-repositorio
