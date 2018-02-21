# -*- coding: utf-8 -*-

"""Main module."""

'''
Created on 20 Feb 2018

@author: Emmet Tracey
'''

import platform

#syteminfo program
def get_platform_info():
	return platform.platform()

if __name__ == '__main__':
	get_platform_info()
