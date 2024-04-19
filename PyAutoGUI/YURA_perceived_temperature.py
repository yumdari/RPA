"""
유라 6층 체감 온도

체감온도 = 13.12 + 0.6215*(기온) - 11.37*(풍속^0.16) + 0.3965*(풍속^0.16)*(기온)
"""
import math
import os

def calc(temp, val):
    perc_temp = 13.12 + 0.6215*float(temp) - 11.37*math.pow(float(val),0.16) + 0.3965*math.pow(float(val),0.16)*float(temp)
    return perc_temp

'''
사무실 기온 입력
'''
temp = input("사무실 기온 입력(ºC) : ")

'''
선풍기 풍속 입력
'''
val = input("선풍기 풍속 입력(km/h) : ")

print("체감 온도는 ", round(calc(temp,val),2), "ºC입니다.")

os.system("pause")