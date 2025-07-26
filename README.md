# 🧮 Equação de Centralização para Redes de Mineração de Criptomoedas

Este repositório implementa uma equação original para estimar a centralização estrutural de redes de mineração de criptomoedas, comparando algoritmos e arquiteturas de forma justa — independente do hashrate bruto.

## ✍️ Autor
**Hugo Quinteiro**  
Colaboração: GPT-CIENTISTA (OpenAI)

## 📌 Objetivo
Comparar redes como Bitcoin (SHA-256, ASIC) e Monero (RandomX, CPU) levando em conta:
- Distribuição estatística de hashrate
- Eficiência energética
- Capacidade de dominação por dispositivo individual

## 📐 Equação

C = (sigma_H / H_avg_dev)^alpha * (eta_ideal / eta)^beta * (H_dev_max / H_net)^gamma

## 📂 Estrutura

- `src/centralization_model.py`: função principal da equação.
- `examples/comparacao_btc_xmr.py`: cálculo aplicado com dados reais.
- `artigo/`: PDF técnico com metodologia e resultados.

## 🚀 Executar Exemplo

```bash
python examples/comparacao_btc_xmr.py
```

## 📝 Licença

MIT License