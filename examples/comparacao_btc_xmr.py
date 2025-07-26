from src.centralization_model import centralization_index

btc = {
    "sigma_H": 0.12e18,
    "H_avg_dev": 318e12,
    "eta": 1 / 11e-12,
    "eta_ideal": 1 / 11e-12,
    "H_dev_max": 318e12,
    "H_net": 970.74e18
}

xmr = {
    "sigma_H": 0.5e9,
    "H_avg_dev": 12.8e3,
    "eta": 12.8e3 / 150,
    "eta_ideal": 1 / 11e-12,
    "H_dev_max": 12.8e3,
    "H_net": 5.83e9
}

C_btc = centralization_index(**btc, alpha=1.5, beta=1.0, gamma=2.0)
C_xmr = centralization_index(**xmr, alpha=1.5, beta=1.0, gamma=2.0)

print("C_BTC =", C_btc)
print("C_XMR =", C_xmr)
print("Razao (XMR / BTC) =", C_xmr / C_btc)