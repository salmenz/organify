#!/usr/bin/env python3

import numpy as np
import random
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

"""la base est une succession de tableau qui sont
les agendas de chaque utilisateurs"""

def clusturing(x):
    """cette fonction réalise le partage
    en 5 clusters des utilisaterus
    la base x est un tableay de taille P x N x  M
    ou P est le nombre de personnes, N le nombre de jours
    et M le nombres de plages horaires"""
    P, N, M = np.shape(x)
    X = np.zeros((P, N * M))
    for i in range(P):
        X[i, :] = np.ndarray.flatten(x[i, :, :])
    km = KMeans(
        n_clusters=5, init='random',
        n_init=10, max_iter=300, 
        tol=1e-04, random_state=0
    )
    y_km = km.fit_predict(X)
    return y_km

def proposition(z, x):
    """l'individu nouvellement arrivé doit être mis
    dans un cluster afin de lui faire des proposition
    son emploi est le tableau z de taille N x M. x reste
    la base départ"""
    M, N = np.shape(z)
    zz = np.reshape(z, (1, M, N))
    xz = np.concatenate((x, zz), axis=0)
    y_km = clusturing(xz)
    cluter_z = y_km[-1]
    X_z = xz[y_km == cluter_z, : ,:]
    l, l1, l2 = np.shape(X_z)
    return X_z[random.randint(0, l-1), :, :]
    

x = np.random.rand(10, 9, 8)
z = np.random.rand(9, 8)

print(proposition(z, x))
