# -*- coding: utf-8 -*-

#####
# VosNoms (Matricule) .~= À MODIFIER =~.
###

import numpy as np
import random
from sklearn import linear_model


class Regression:
    def __init__(self, lamb, m=1):
        self.lamb = lamb
        self.w = None
        self.M = m

    def fonction_base_polynomiale(self, x):
        """
        Fonction de base qui projette la donnee x vers un espace polynomial tel que mentionne au chapitre 3.
        Si x est un scalaire, alors phi_x sera un vecteur à self.M dimensions : (x^1,x^2,...,x^self.M)
        Si x est un vecteur de N scalaires, alors phi_x sera un tableau 2D de taille NxM

        NOTE : En mettant phi_x = x, on a une fonction de base lineaire qui fonctionne pour une regression lineaire
        """
        # AJOUTER CODE ICI
        if np.isscalar(x):
            phi_x=x**np.arange(0,self.M+1)
        else:
            N = len(x)
            phi_x = np.zeros((N, self.M + 1))
            for i in range(N):
                phi_x[i] = x[i]**np.arange(0,self.M+1)
        return phi_x

    def recherche_hyperparametre(self, X, t):
        """
        Trouver la meilleure valeur pour l'hyper-parametre self.M (pour un lambda fixe donné en entrée).

        Option 1
        Validation croisée de type "k-fold" avec k=10. La méthode array_split de numpy peut être utlisée 
        pour diviser les données en "k" parties. Si le nombre de données en entrée N est plus petit que "k", 
        k devient égal à N. Il est important de mélanger les données ("shuffle") avant de les sous-diviser
        en "k" parties.

        Option 2
        Sous-échantillonage aléatoire avec ratio 80:20 pour Dtrain et Dvalid, avec un nombre de répétition k=10.

        Note: 

        Le resultat est mis dans la variable self.M

        X: vecteur de donnees
        t: vecteur de cibles
        """
        # AJOUTER CODE ICI
        #definissons une variable qui va contenir l'erreur minimale
        errMin = 0
        mErrMin = 0 
       # qui representera le M dont l erreur est minimale
       # nous allons faire une boucle Pour chaque m entre le Mmin et le Mmax
        for mTemp in range(Regression.min_, Regression.max_ +1):

           ErrSum = 0 
           self.M = mTemp
           #on entraine le modèle k fois avec une répartition des données différentes
           for k in range(1, 11):
               
               self.w = None

               X_train, X_test, y_train, y_test = train_test_split(X, t, test_size=Regression.DTEST)
               # On entraine le modèle sur les données (DTRAIN)
               self.entrainement(X_train, y_train)
               # On fait une prédiction sur les données restantes
               prediction = np.array([self.prediction(x) for x in X_test])
               # nous allons calculer l'erreur
               Erreur = np.array([self.Erreur(t_n, p_n)
                                  for t_n, p_n in zip(y_test, prediction)])
               ErrSum += Erreur.mean() #declaration d'une variable pour stocker la moyenne

           # Si c'est la première boucle on met à jour l'erreur min et le M correspondant
           if mTemp == Regression.min_:
               mErrMin = Regression.min
               errMin = ErrSum
           # Sinon si la nouvelle erreur est plus basse que l'erreur minimale on garde le nouveau m
           elif ErrSum < errMin:
               errMin = ErrSum
               self.M =mTemp
        self.M = mErrMin
           

    def entrainement(self, X, t, using_sklearn=False):
        """
        Entraîne la regression lineaire sur l'ensemble d'entraînement forme des
        entrees ``X`` (un tableau 2D Numpy, ou la n-ieme rangee correspond à l'entree
        x_n) et des cibles ``t`` (un tableau 1D Numpy ou le
        n-ieme element correspond à la cible t_n). L'entraînement doit
        utiliser le poids de regularisation specifie par ``self.lamb``.

        Cette methode doit assigner le champs ``self.w`` au vecteur
        (tableau Numpy 1D) de taille D+1, tel que specifie à la section 3.1.4
        du livre de Bishop.
        
        Lorsque using_sklearn=True, vous devez utiliser la classe "Ridge" de 
        la librairie sklearn (voir http://scikit-learn.org/stable/modules/linear_model.html)
        
        Lorsque using_sklearn=Fasle, vous devez implementer l'equation 3.28 du
        livre de Bishop. Il est suggere que le calcul de ``self.w`` n'utilise
        pas d'inversion de matrice, mais utilise plutôt une procedure
        de resolution de systeme d'equations lineaires (voir np.linalg.solve).

        Aussi, la variable membre self.M sert à projeter les variables X vers un espace polynomiale de degre M
        (voir fonction self.fonction_base_polynomiale())

        NOTE IMPORTANTE : lorsque self.M <= 0, il faut trouver la bonne valeur de self.M

        """
        #AJOUTER CODE ICI
        if self.M <= 0:
            self.recherche_hyperparametre(X, t)

        phi_x = self.fonction_base_polynomiale(X)
        self.w = [0, 1]

    def prediction(self, x):
        """
        Retourne la prediction de la regression lineaire
        pour une entree, representee par un tableau 1D Numpy ``x``.

        Cette methode suppose que la methode ``entrainement()``
        a prealablement ete appelee. Elle doit utiliser le champs ``self.w``
        afin de calculer la prediction y(x,w) (equation 3.1 et 3.3).
        """
        # AJOUTER CODE ICI
        return 0.5

    @staticmethod
    def erreur(t, prediction):
        """
        Retourne l'erreur de la difference au carre entre
        la cible ``t`` et la prediction ``prediction``.
        """
        # AJOUTER CODE ICI
        return 0.0
