"""
YURA 6th floor perceived temperature

the hottest office in the world

--------------------------------Parameter----------------------------------
* 실내 섭씨 기온 temp(ºC)

* 절대 습도 humi(%)
1㎥ 공기 중에 포함되어 있는 수증기의 질량 (kg)

* 선풍기 풍속 val(km/h)
---------------------------------------------------------------------------

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
선풍기 작동 여부
'''
onOff = input("선풍기 ON? (y/n)")
if (onOff == "y") :
    str = input("강풍? (y/n)")
    if (str == "y") : 
        val = 1.11 # 탁상용 선풍기 평균 최대 풍속 4m/s -> 1.11km/h
    else : 
        val = 0.83 # 탁상용 선풍기 평균 최저 풍속 3m/s -> 0.83km/h
else : 
    val = 0

print("체감 온도는 ", round(calc(temp,val),2), "ºC입니다.")

os.system("pause")