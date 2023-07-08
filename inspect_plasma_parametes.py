#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 5 10:03:48 2023

@author: gt2023
"""
import numpy as np
from matplotlib import pyplot as plt
from model_parameters import  model_frequencies as mf
from model_parameters import dipole_model as dip
from model_parameters import dipole_codinates as r

# from IPython.core.debugger import set_trace
font = {"size": 9.5}
plt.rc("font", **font)
SMALL_SIZE = 8
plt.rc("legend", fontsize=SMALL_SIZE)


def B_intesnity_with_latitude(initial_theta=90, final_theta=0, subdivisions=34000):
    """This functions plots magnetic intensity with decreasing latitudes.
    initial_theta: float or int
    final_theta: float or int
    subdivisions: int
    """
    theta = np.linspace(initial_theta * (np.pi / 180), final_theta, subdivisions)
    L_value = 1 / np.cos(theta) ** 2
    fig, ax = plt.subplots()
    ax.plot(
        theta * (180 / np.pi), mf.B_SI(theta, L_value), color="green", label="IS units"
    )
    ax.set_xlabel(r"$\mathrm{ \theta}\ [\degree]$")
    ax.set_ylabel(r"$B\ [\mu T]$")
    ax.set_title(
        r"$Magnetic\ field\ intensity\ (B)\ vs\ decreasing\ latitude\ (\mathrm{\theta})$",
        fontsize=10,
    )
    plt.ticklabel_format(axis="y", style="sci", scilimits=(-6, -6))
    fig.savefig("magnetic_latitude.eps", format="eps", dpi=2000, bbox_inches="tight")
    plt.close()


def gyrofrequency_with_Lvalues(
    initiaL_value=1.5, finaL_value=6, theta=0, subdivisions=34000
):
    """This function plots gyrofrequency with increasing L_values.
    initiaL_value: float or int
    finaL_value: float or int
    theta      : float
    subdivisions: int
    """
    L_value = np.linspace(initiaL_value, finaL_value, subdivisions)
    fig, ax = plt.subplots()
    w_b_P = mf.w_b_P(theta, L_value)
    ax.semilogy(
        L_value, w_b_P, color="Green", lw=1,
    )
    ax.legend(loc=0)
    ax.set_xlabel("L")
    ax.set_ylabel(r"$\omega_{b}\ [rad/s]$")
    ax.set_title(
        r"$\mathrm{Gyrofrequency\ (\omega_{b})\ vs\ increasing\ L-values\ (L)}$",
        fontsize=10,
    )
    ax.annotate(
        r"$\theta\ =\ {}\degree$".format(theta), (max(L_value) - 0.8, max(w_b_P) - 0.5)
    )
    fig.savefig(
        "gyrofre_with_L_values.eps", format="eps", dpi=2000, bbox_inches="tight"
    )
    plt.close()


def gyrofrequecy_with_latitude(initiaL_value=1.5, finaL_value=6, delta_Lvalue=0.5,subdivisions=34000):
    """This function plots gyrofrequency with decreasing Latitude.
    initiaL_value: float or int
    finaL_value: float or int
    theta      : float
    delta_Lvalue: int
    subdivisions: int
    """
    fig, ax = plt.subplots()
    for l in np.arange(initiaL_value, finaL_value, delta_Lvalue):
        L_value = l
        theta_h = r.theta_h(1000e3, L_value, R_E=6370e3)
        theta = np.linspace(theta_h, 0,subdivisions)
        w_b_P = mf.w_b_P(theta, L_value)
        theta = theta * (180 / np.pi)
        theta_h_label = theta_h * (180 / np.pi)
        theta_h_label = round(theta_h_label, 2)
        ax.semilogy(
            theta,
            w_b_P,
            lw=1,
            label=r"$L={}\ {}\ \theta_{}={}\degree$".format(
                l, ",", "{r}", theta_h_label
            ),
        )
        ax.legend(loc=4)
        ax.set_xlabel(r"$\mathrm{\theta}\ [\degree]$")
        ax.set_ylabel(r"$\omega_{b}\ [rad/s]$")
        ax.set_title(
            r"$\mathrm{Gyrofrequency\ (\omega_{b})\ vs\ decreasing\ latitude\ (\theta)\ at\ constant\ L-value\ (L)}$",
            fontsize=10,
        )
        fig.savefig(
            "gyrofre_with_latitude.eps", format="eps", dpi=2000, bbox_inches="tight"
        )
        plt.close()


def plasmafrequency_with_Lvalues(
    initiaL_value=1.5, finaL_value=6, theta=0, subdivisions=34000, n_h=1000
):
    """This function plots plasmafrequency with decreasing L_value.
    initiaL_value: float or int (inital L_value)
    finaL_value: float or int (final L_value)
    theta      : float   (terminal latitude)
    delta_Lvalue: int   ( spacing between L_values)
    n_h         : float (reference electron density)
    subdivisions: int
    """
    L_value = np.linspace(initiaL_value, finaL_value, subdivisions)
    theta = 0
    theta_h = r.theta_h(1000e3, L_value, R_E=6370e3)
    electron_density = dip.electron_density_P(theta, L_value, theta_h, n_h=n_h)
    w_p = mf.w_p(electron_density)
    fig, ax = plt.subplots()
    ax.semilogy(L_value, w_p, color="blue", lw=1)
    ax.set_xlabel("L")
    ax.set_ylabel(r"$\omega_{p}\ [rad/s]$")
    ax.annotate(
        r"$\theta={}\degree$".format(theta), (max(L_value) - 0.5, max(w_p) - 0.5)
    )
    ax.annotate(
        r"$N_{}={}\ cm^{}$".format("{r}", n_h, "{-3}"),
        (max(L_value) - 1.1, max(w_p) - 15801),
    )
    ax.set_title(
        r"$\mathrm{Plasma-frequency\ (\omega_{p})\ vs\ increasing\ L-values\ (L)\ from\ L=1.5\ to\ L=6.5}$",
        fontsize=10,
    )
    fig.savefig(
        "plasmafre_with_L_values.eps", format="eps", dpi=2000, bbox_inches="tight"
    )
    plt.close()


def plasmafrequency_with_latitude(
    initiaL_value=1.5, finaL_value=6, delta_Lvalue=0.5, n_h=1000, subvisions=3000
):
    """This function plots plasmafrequecy with decreasing Latitude.
    initiaL_value: float or int (inital L_value)
    finaL_value: float or int (final L_value)
    theta      : float   (terminal latitude)
    delta_Lvalue: int   ( spacing between L_values)
    n_h         : float (reference electron density)
    """
    fig, ax = plt.subplots()
    for l in np.arange(initiaL_value, finaL_value, delta_Lvalue):
        L_value = l
        theta_h = r.theta_h(1000e3, L_value, R_E=6370e3)
        theta_h_label = theta_h * (180 / np.pi)
        theta_h_label = round(theta_h_label, 2)
        theta = np.linspace(theta_h, 0, subvisions)
        electron_density = dip.electron_density_P(theta, L_value, theta_h, n_h=n_h)
        w_p = mf.w_p(electron_density)
        theta = theta * (180 / np.pi)
        ax.semilogy(
            theta,
            w_p,
            lw=1,
            label=r"$L={}\ {}\ \theta_{}={}\degree$".format(
                l, ",", "{r}", theta_h_label
            ),
        )
        ax.legend(loc=2)
        ax.set_xlabel(r"$\theta\ [\degree]$")
        ax.set_ylabel(r"$\omega_{p}\ [rad/s]$")
        stringValues = ("{p}", "{r}", "{}".format(n_h), "{-3}")
        tl = r"$Plasma-frequency\ (\omega_{})\ vs\ decreasing\ latitude\ (\theta).\ N_{}={}\ cm^{}$".format(
            *stringValues
        )
        ax.set_title(tl, fontsize=10)
        fig.savefig(
            "plasmafre_with_latitude.eps", format="eps", dpi=2000, bbox_inches="tight"
        )
        plt.close()


def comparison_plasmafr_gyrofre_with_latitude(
    init_N_h=1000, final_N_h=10000, delta_N_h=1000, Lvalue_arr=np.arange(6) + 1.5
):
    """This function plots plasmafrequecy with decreasing Latitude.
    initiaL_value: float or int (inital L_value)
    finaL_value: float or int (final L_value)
    theta      : float   (terminal latitude)
    delta_Lvalue: int   ( spacing between L_values)
    init_N_h    : float (initial reference electron density)
    final_N_h   : float (final reference electron density)
    delta_N_h   : float (incremental reference electron density)
    Lvalue_arr  : np.ndarray  (L_value array)
    """
    for L_value in Lvalue_arr:
        for n_h in np.arange(init_N_h, final_N_h, delta_N_h):
            L_value = L_value
            theta_h = r.theta_h(1000e3, L_value, R_E=6370e3)
            theta = np.linspace(theta_h, 0, 34000)
            electron_density = dip.electron_density_P(theta, L_value, theta_h, n_h=n_h)
            w_p = mf.w_p(electron_density)
            w_b_P = mf.w_b_P(theta, L_value)
            theta_h_label = theta_h * (180 / np.pi)
            theta_h_label = round(theta_h_label, 2)
            fig, ax = plt.subplots()
            ax.semilogy(
                theta * (180 / np.pi),
                w_p,
                color="blue",
                lw=1,
                label=r"$Plasmafrequecy\ for\ L={}$".format(L_value),
            )
            ax.semilogy(
                theta * (180 / np.pi),
                w_b_P,
                color="Green",
                lw=1,
                label=r"$Gyrofrequecy\ for\ L={}$".format(L_value),
            )
            ax.legend(loc="upper left")
            # plt.grid(True, which="both")
            ax.set_xlabel(r"$\mathrm{\theta}\ [\degree]$")
            ax.set_ylabel(r"$\mathrm{\omega_{b}\ and\ \omega_{p}\ [rad/s]}$")
            ax.set_title(
                r"$Comparison\ of\ gyrofrequency\ (\omega_{})\ and\ Plasma-frequency\ (\omega_{})$"
                "\n"
                r"$with\ decreasing\ latitude\ (\theta).\ N_{}={}\ cm^{},\ \theta_{}={}\degree$".format(
                    "{b}", "{p}", "{r}", n_h, "{-3}", "{r}", theta_h_label
                ),
                loc="left",
            )
            fig.savefig(
                "L_{}_N_{}_w_p_and_w_b_with_latitude.eps".format(L_value, n_h),
                format="eps",
                dpi=2000,
                bbox_inches="tight",
            )  # fig.dpi
            plt.close()


if __name__ == "__main__":
    B_intesnity_with_latitude(initial_theta=90, final_theta=0)
    gyrofrequency_with_Lvalues(
        initiaL_value=1.5, finaL_value=6, theta=0, subdivisions=34000
    )
    gyrofrequecy_with_latitude(initiaL_value=1.5, finaL_value=6, delta_Lvalue=1.5)
    plasmafrequency_with_Lvalues(
        initiaL_value=1.5, finaL_value=6, theta=0, subdivisions=34000, n_h=1000
    )
    plasmafrequency_with_latitude(
        initiaL_value=1.5, finaL_value=6, delta_Lvalue=0.5, n_h=1000
    )
    comparison_plasmafr_gyrofre_with_latitude(
        init_N_h=1000, final_N_h=10000, delta_N_h=1000, Lvalue_arr=np.arange(6) + 1.5
    )
