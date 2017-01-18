# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 10:26:42 2017

@author: jdc14

The Olso model is one of the simplest models displaying self-organised criticality.
"""

import random

class Site(object):
    """
    The sites of the lattice.
    """
    p = 0.6    
    
    def __init__(self, local_slope, threshhold_slope):
        self._local_slope = local_slope
        self._threshhold_slope = threshhold_slope

    @property    
    def z(self):
        return self._local_slope

    @z.setter
    def z(self, val):
        self._local_slope = val

    @z.deleter
    def z(self):
        del(self._local_slope)
    
    @property
    def z_th(self):    
        return self._threshhold_slope

    @z_th.setter
    def z_th(self, val):
        self._threshhold_slope = val

    @z_th.deleter
    def z_th(self):
        del(self._threshhold_slope)
    
    def relax(self, other):
        """
        When a grain exceeds the threshhold slope. 
        It drops to the next lattice site.
        
        Inputs:
            self - Site object.
            other - Site object.  
            
        Returns:
            self - Site object.
            other - Site object.
            
        """
        self.z = self.z - 2
        other.z = other.z + 1
        
        rand = random.random()
        if rand <= self.p:
            self.z_th = 1
        elif 0.0 <= rand <= 1.0:
            self.z_th = 2
        else:
            raise ValueError('random.random generated an unexpected number {}'.format(rand))
    
    
class First_site(Site):
    """
    Has an additional 'drive' method.
    """
    
    def drive(self, local_slope):
        """
        Adds a grain to the left-most site.
        """
        self.z = self.z + 1

class Last_site(Site):
    def relax(self, other):
        self.z = self.z - 1
        other.z = other.z + 1
        
        rand = random.random()
        if rand <= self.p:
            self.z_th = 1
        elif 0.0 <= rand <= 1.0:
            self.z_th = 2
        else:
            raise ValueError('random.random generated an unexpected number {}'.format(rand))
