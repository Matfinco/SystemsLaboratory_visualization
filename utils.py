import numpy as np


def pendulum_dynamics(t, state, g, l, b=0):
    """
    Calcola le derivate di stato per un pendolo smorzato.

    Parametri:
    - t: tempo (non usato direttamente, ma richiesto per compatibilità con integratori)
    - state: lista o array con [theta, omega], dove:
        - theta: angolo (in radianti)
        - omega: velocità angolare
    - g: accelerazione gravitazionale
    - l: lunghezza del pendolo
    - b: coefficiente di smorzamento (attrito viscoso)

    Ritorna:
    - [dtheta/dt, domega/dt]: derivate temporali dell'angolo e della velocità angolare
    """
    theta, omega = state
    dtheta_dt = omega
    domega_dt = -(g / l) * np.sin(theta) - b * omega
    return [dtheta_dt, domega_dt]


def linearized_pendulum_dynamics(t, state, g, l, b=0):
    """
    Calcola le derivate di stato per un pendolo smorzato linearizzato.

    Linearizzazione: sin(theta) ≈ theta (valida per |theta| << 1 rad)

    Parametri:
    - t: tempo
    - state: [theta, omega]
    - g: accelerazione gravitazionale
    - l: lunghezza del pendolo
    - b: coefficiente di smorzamento

    Ritorna:
    - [dtheta/dt, domega/dt]
    """
    theta, omega = state
    dtheta_dt = omega
    domega_dt = -(g / l) * theta - b * omega
    return [dtheta_dt, domega_dt]
