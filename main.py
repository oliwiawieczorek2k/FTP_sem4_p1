#from samolot import Samolot
#from kamera import Kamera
import math
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
#import tkinter as tk
#from tkinter import *

class Samolot:

    def __init__(self, name, predkosc_min, predkosc_max, pulap, czas_lotu):
        self.name = name
        self.predkosc_min = predkosc_min
        self.predkosc_max = predkosc_max
        self.pulap = pulap
        self.czas_lotu = czas_lotu


class Kamera:

    def __init__(self, name, wymiar_matrycy1, wymiar_matrycy2, wymiar_piksela, kanaly_spektralne, ogniskowa, cykl_pracy, waga):
        self.name = name
        self.wymiar_matrycy1 = wymiar_matrycy1
        self.wymiar_matrycy2 = wymiar_matrycy2
        self.wymiar_piksela = wymiar_piksela
        self.kanaly_spektralne = kanaly_spektralne
        self.ogniskowa = ogniskowa
        self.cykl_pracy = cykl_pracy
        self.waga = waga


samolot1 = Samolot("Cessna 402", 132, 428, 8200, 5)
samolot2 = Samolot("Cessna T206H NAV III", 100, 280, 4785, 5)
samolot3 = Samolot("Vulcan Air P68 Observer 2", 135, 275, 6100, 6)
samolot4 = Samolot("Tencam MMA", 120, 267, 4572, 6)

kamera1 = Kamera("Z/I DMC IIe 230", 15552, 14144, 5.6, ["R", "G", "B", "NIR"], 92, 1.8, 63)
kamera2 = Kamera("Leica DMC III", 25728, 14592, 3.9, ["R", "G", "B", "NIR"], 92, 1.9, 63)
kamera3 = Kamera("UltraCam Falcon M2 70", 17310, 11310, 6.0, ["R", "G", "B", "NIR"], 70, 1.35, 61)
kamera4 = Kamera("UltraCam Eagle M2 80", 23010, 14790, 4.6, ["R", "G", "B", "NIR"], 80, 1.65, 61)


def getW(GSD, kamera):
    return GSD * (kamera.ogniskowa * pow(10, -3) / (kamera.wymiar_piksela * pow(10, -6)))


def getLx(GSD, kamera):
    if kamera.wymiar_matrycy1 < kamera.wymiar_matrycy2:
        return GSD * kamera.wymiar_matrycy1
    else:
        return GSD * kamera.wymiar_matrycy2


def getLy(GSD, kamera):
    if kamera.wymiar_matrycy1 > kamera.wymiar_matrycy2:
        return GSD * kamera.wymiar_matrycy1
    else:
        return GSD * kamera.wymiar_matrycy2


def getBx(Lx, p):
    return Lx * (100 - p) / 100


def getBy(Ly, q):
    return Ly * (100 - q) / 100


def getNy(By, Dy):
    return math.ceil(Dy / By)


def getNx(Bx, Dx):
    return math.ceil(Dx / Bx + 4)


def getBy2(Ny, Dy):
    return Dy / Ny


def getBx2(Nx, Dx):
    return Dx / (Nx - 4)


def getp2(Lx, Bx):
    return 100 - 100 * Bx / Lx


def getq2(Ly, By):
    return 100 - 100 * By / Ly


def getdt(Bx, samolot):
    return (Bx / (samolot.predkosc_max * 1000/3600)), (Bx / (samolot.predkosc_min * 1000/3600)) #min/max ????

def getN(Nx, Ny):
    return Nx * Ny


def getTime(dt, N, Ny, kamera):
    return N*dt[0] + (Ny-1)*140


def plot(Nx, Ny, Lx, Ly):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    for i in range(Nx):
        for j in range(Ny):
            rectangle = matplotlib.patches.Rectangle((1000 + i * Lx, 1000 + j * Ly), Lx, Ly, fc='none', ec='red', lw=0.3)
            circle = matplotlib.patches.Circle((1000 + Lx / 2 + i * Lx, 1000 + Ly / 2 + j * Ly), 50, color='red')
            ax.add_patch(rectangle)
            ax.add_patch(circle)

    plt.xlim([0, Nx * Lx + 2000])
    plt.ylim([0, Ny * Ly + 2000])
    plt.show()

if __name__ == '__main__':

    #dane
    Dx = 19090
    Dy = 17219
    kamera = kamera1
    samolot = samolot4
    GSD = 0.25
    p = 60
    q = 30

    #obliczenia
    W = getW(GSD, kamera)
    print("W = ", W)
    Lx = getLx(GSD, kamera)
    Ly = getLy(GSD, kamera)
    print("Lx = ", Lx)
    print("Ly = ", Ly)
    Bx = getBx(Lx, p)
    By = getBy(Ly, q)
    print("Bx = ", Bx)
    print("By = ", By)
    Nx = getNx(Bx, Dx)
    Ny = getNy(By, Dy)
    print("Nx = ", Nx)
    print("Ny = ", Ny)
    Bx = getBx2(Nx, Dx)
    By = getBy2(Ny, Dy)
    print("Bx = ", Bx)
    print("By = ", By)
    p = getp2(Lx, Bx)
    q = getq2(Ly, By)
    print("p = ", p)
    print("q = ", q)
    dt = getdt(Bx, samolot)
    print("dt = ", dt)
    N = getN(Nx, Ny)
    print("N = ", N)
    Time = getTime(dt, N, Ny, kamera)
    print("Time = ", Time)

    #czesc graficzna
    plot(Nx, Ny, Lx, Ly)