# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 16:01:07 2017

@author: Karencita
"""

class pila(object):
    def __init__(self):
        self.a=[]
    def meter(self, e):
        self.a.append(e)
    def obtener(self):
        return self.a.pop()
    @property
    def longitud(self):
        return len(self.a)
    def __str__(self):
        return str(self.a)

class fila(pila):
    def obtener(self):
        return self.a.pop(0)
    
        
class grafica:
    def __init__(self):
        self.vertices=set()
        self.aristas= dict()
        self.vecinos=dict()
    
    def agrega(self,v):
        self.vertices.add(v)
        if not v in self.vecinos:
            self.vecinos[v]=set()
    def conecta(self, u,v, peso=1):
        self.agrega(v)
        self.agrega(u)
        self.aristas[(v,u)]=self.aristas[(u,v)]=peso
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)
    def __str__(self):
        return "Aristas= " +str(self.aristas)+"\nVertices"+str(self.vertices)
        
def BFS(grafo, vertice):
    vistos = []
    por_ver = fila()
    por_ver.meter(vertice)
    while por_ver.longitud >0:
        vertice = por_ver.obtener()
        if vertice not in vistos:
            vistos.append(vertice)
            for vecino in grafo.vecinos[vertice]:
                por_ver.meter(vecino)
    return vistos
            
def DFS(grafo, vertice):
    vistos = []
    por_ver = pila()
    por_ver.meter(vertice)
    while por_ver.longitud >0:
        vertice = por_ver.obtener()
        if vertice not in vistos:
            vistos.append(vertice)
            for vecino in grafo.vecinos[vertice]:
                por_ver.meter(vecino)
    return vistos        
    
    
    