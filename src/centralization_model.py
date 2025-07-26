def centralization_index(sigma_H, H_avg_dev, eta, eta_ideal, H_dev_max, H_net,
                          alpha=1.5, beta=1.0, gamma=2.0):
    term1 = (sigma_H / H_avg_dev) ** alpha
    term2 = (eta_ideal / eta) ** beta
    term3 = (H_dev_max / H_net) ** gamma
    return term1 * term2 * term3