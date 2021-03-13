# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 15:53:02 2021

Calculate the distance between two points on a sphere with haversine equation.

@author: Javier Cebrián 
"""

import numpy as np


####################################################################
class pointOnSphere:
    """
    A class used to create a point with two coordinates.

    ...

    Attributes
    ----------
    latitude : float
        latitude in decimal form.
    longitude : float
        longitude in decimal form.
    """
    
    def __init__(self,latitude,longitude):
        self.latitude=latitude
        self.longitude=longitude
            
####################################################################

def distance(pointOne,pointTwo,sphereRadio):
    """
    Method with haversine equation calculate distance between two points on a 
    spherical surface.
    
    Parameters
    ----------
    pointOne : pointOnSphere object 
        Coordinates of the first point
    pointTwo : pointOnSphere object 
        Coordinates of the second point
    sphereRadio : float
        Radio of the sphere with points on surface.
    
    Returns
    -------
    distance : float
        Distance
    """
    lat1=pointOne.latitude*np.pi/180
    long1=pointOne.longitude*np.pi/180
    
    lat2=pointTwo.latitude*np.pi/180
    long2=pointTwo.longitude*np.pi/180
    
    distance=2*sphereRadio*np.arcsin(np.sqrt((np.sin((lat2-lat1)/2))**2+np.cos(lat1)*np.cos(lat2)*(np.sin((long2-long1)/2))**2))
        
    return distance
####################################################################


# i.e.: Distance between Madrid <-> Barcelona
try:
    point1=pointOnSphere(40.4165,-3.70256)
    point2=pointOnSphere(41.38879,2.15899)
except NameError as e:
    print('Data must be numerical')

dist=distance(point1,point2,6371)
print('Distance is:' +str(round(dist, 2))+'Km')

