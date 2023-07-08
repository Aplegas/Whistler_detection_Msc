import numpy as np


def geocentric_R1(theta, theta_h, R_E=6370e3):
    """
    Calculation the geoocetric radius of the dipole model
    theta: float (latitude on the field line)
    theta_h: float (Invariant latitude of the field line)
    R_E: float (planet radius, default Earth)
    return: float """
    return R_E * ((np.cos(theta) ** 2) / (np.cos(theta_h) ** 2))


def R_h(h, R_E=6370e3):
    """
    Calculate radius at the reference height
    h: float (reference height)
    R_E: float (planet radius, default Earth)
    return: float"""
    return h + R_E


def geocentric_R2(theta, L_value, R_E=6370e3):
    """
    Calculation the geoocetric radius of the dipole model
    theta: float (latitude on the field line)
    theta_h: float (Invariant latitude of the field line)
    R_E: float (planet radius, default Earth)
    returen: float """
    return L_value * R_E * np.cos(theta) ** 2


def theta_h(h, L_value, R_E=6370e3):
    """Calculating latitude at 
    the reference height h.
    h: float (height)
    L_value: float 
    R_E: float (planet radius, default Earth)
    return: float"""
    return np.arccos(np.sqrt((R_E + h) / (R_E * L_value)))


def ds_dtheta(L_value, theta, R_E=6370e3):
    """calculate ds of the arclength.
    theta: float (latitude)
    L_value: float (L_value)
    R_E: float (planet radius, default Earth)
    return float"""
    return R_E * L_value * np.cos(theta) * (1 + 3 * np.sin(theta) ** 2) ** 0.5


def arclenlength(theta, theta_h, R_h):
    """Calculate the arclength of the dipole field line.
    theta: float (latitude on the field line)
    theta_h: float (Invariant latitude of the field line)
    R_h    : float (geocentric radius at the reference height
    Return: float"""
    t0 = 0.5 * R_h / (np.sqrt(3) * np.cos(theta_h) ** 2)
    t2 = np.log(np.sqrt(3) * np.sin(theta) + np.sqrt(3 * np.sin(theta) ** 2 + 1))
    t3 = np.sqrt(3) * np.sin(theta) * np.sqrt(1 + 3 * np.sin(theta) ** 2)
    return t0 * (t2 + t3)


def integ_arclenlenth(theta, L_value, R_E=6370e3):
    """Arclength in integral form.
    theta: float (latitude on the field line)
    L_value: float (L_value)
    R_E: float (planet radius, default Earth)
    return: float"""
    return L_value * R_E * np.cos(theta) * np.sqrt(1 + 3 * (np.sin(theta)) ** 2)


if __name__ == "__main__":
    print()
