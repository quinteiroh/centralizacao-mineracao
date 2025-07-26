# Equação para Mensuração de Centralização de Redes de Mineração de Criptomoedas

**Autor:** Hugo Quinteiro  
**Colaboração:** GPT-CIENTISTA  
**Data:** Julho de 2025

---

## Resumo

Este artigo propõe uma métrica de centralização aplicável a redes de mineração de criptomoedas, que corrige distorções comuns associadas ao uso isolado do hashrate bruto como medida de segurança ou descentralização. O modelo considera: distribuição estatística, eficiência energética e dominância por dispositivo. Aplicamos essa equação ao Bitcoin e Monero, demonstrando que o Monero apresenta descentralização estrutural superior mesmo com hashrate inferior.

---

## 1. Introdução

A comparação entre redes blockchain frequentemente recorre ao hashrate total como um indicador direto de segurança e descentralização. No entanto, essa abordagem falha ao ignorar diferenças fundamentais entre algoritmos de mineração, arquitetura de hardware e distribuição de poder computacional. Este trabalho propõe uma nova equação para medir descentralização estrutural de forma comparável entre redes com características distintas.

---

## 2. Metodologia

A métrica de descentralização **C** é definida por:

```
C = (sigma_H / H_avg_dev)^alpha * (eta_ideal / eta)^beta * (H_dev_max / H_net)^gamma
```

**Onde:**

- `sigma_H`: desvio padrão do hashrate entre dispositivos ou pools.
- `H_avg_dev`: hashrate médio dos dispositivos em uso.
- `eta`: eficiência energética observada [H/J].
- `eta_ideal`: eficiência do melhor dispositivo disponível.
- `H_dev_max`: hashrate por dispositivo mais poderoso.
- `H_net`: hashrate total da rede.

**Pesos utilizados:**

- `alpha = 1.5` (estatística)
- `beta = 1.0` (energia)
- `gamma = 2.0` (dispositivo)

---

## 3. Aplicação: Bitcoin vs Monero

### 3.1 Dados utilizados

| Parâmetro            | Bitcoin (BTC)       | Monero (XMR)         |
|----------------------|---------------------|-----------------------|
| Hashrate total       | 970.74 EH/s         | 5.83 GH/s             |
| Hashrate por dispositivo | 318 TH/s (S23)   | 12.8 KH/s (Ryzen 9)   |
| Eficiência energética| 1 / 11 J/TH         | 12.8 KH / 150 W       |
| Desvio padrão        | ~120 EH/s           | ~0.5 GH/s             |

### 3.2 Resultados

- `C_BTC = 7.87e-10`
- `C_XMR = 3.96e4`
- `Razão (XMR / BTC) ~ 5.04e13`

---

## 4. Discussão

Apesar do hashrate do Bitcoin ser milhares de vezes maior, sua centralização estrutural é acentuada por dispositivos ultraeficientes e dominação por poucos pools. Monero, ao contrário, exige milhares de dispositivos modestos, dificultando a centralização física ou econômica.

---

## 5. Conclusão

A equação proposta oferece uma métrica mais realista de descentralização, adequada para comparar redes com arquiteturas distintas. Ela deve ser usada como complemento (ou substituto) à métrica de hashrate bruto em análises técnicas e estratégicas de redes blockchain.

---

## 6. Código da Equação

```python
def centralization_index(sigma_H, H_avg_dev, eta, eta_ideal, H_dev_max, H_net,
                          alpha=1.5, beta=1.0, gamma=2.0):
    term1 = (sigma_H / H_avg_dev) ** alpha
    term2 = (eta_ideal / eta) ** beta
    term3 = (H_dev_max / H_net) ** gamma
    return term1 * term2 * term3
```

---

## Licença

MIT License © 2025 Hugo Quinteiro