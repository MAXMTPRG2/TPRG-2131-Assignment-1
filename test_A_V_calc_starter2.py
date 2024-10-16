#Max Molnar 100746162
#TPRG 2131 Assignment 1 October 15th, 2024

#This program is strictly my own work. Any material
#beyond course learning materials that is taken from
#the web or other sources is properly cited, giving
#full credit to the oringinal author(s).

# This script is a pytest file that tests the functions of the main assignment file A_V_calc_starter2.py

from A_V_calc_starter2 import Rec_area, Rec_volume, sphere_volume, circle_area, triangle_area  

def test_Rec_area():                          # All tests in this function should pass
    '''Test Rec_area function'''
    assert Rec_area(5, 10) == 50                
    assert Rec_area(5, 6) == 30
    assert Rec_area(8, 8) == 64
    assert Rec_area(20, 60) == 1200
    assert Rec_area(6, 3) == 18

def test_Rec_volume():                        # All tests in this function should pass
    '''Test Rec_volume function'''
    assert Rec_volume(5, 10, 25) == 1250
    assert Rec_volume(3, 6, 8) == 144
    assert Rec_volume(2, 4, 3) == 24
    assert Rec_volume(7, 14, 3) == 294
    assert Rec_volume(13, 9, 2) == 234

def test_sphere_volume():                     # All tests in this function should pass
    '''Test sphere_volume function'''
    assert sphere_volume(5) == 523.6
    assert sphere_volume(14) == 11494.04
    assert sphere_volume(8) == 2144.66
    assert sphere_volume(2) == 33.51
    assert sphere_volume(11) == 5575.28

def test_circle_area():                       # All tests in this function should pass
    '''Test circle_area function'''
    assert circle_area(20) == 1256.64
    assert circle_area(3) == 28.27
    assert circle_area(45) == 6361.73
    assert circle_area(7) == 153.94
    assert circle_area(65) == 13273.23

def test_triangle_area():                    # All tests in this function should pass
    '''Test triangle_area function'''
    assert triangle_area(10, 5) == 25
    assert triangle_area(41, 6) == 123
    assert triangle_area(3, 16) == 24
    assert triangle_area(74, 25) == 925
    assert triangle_area(62, 4) == 124