"""
YURA 6th floor perceived temperature

the hottest office in the world

---------------------------------Formula-----------------------------------

https://data.kma.go.kr/climate/windChill/selectWindChillChart.do

※ 2022.6.2. 기준 여름철 체감온도 산출식 변경(2022.6.2.이전 3.5)

- 체감온도 = -0.2442 + 0.55399Tw + 0.45535Ta – 0.0022Tw2 + 0.00278TwTa + 3.0(기존 3.5)

* Tw = TaATAN[0.151977(RH+8.313659)1/2] + ATAN(Ta+RH) - ATAN(RH-1.67633) + 0.00391838RH3/2ATAN(0.023101RH) - 4.686035

** Ta : 기온(°C), Tw : 습구온도(Stull의 추정식 이용), RH : 상대습도(%)
---------------------------------------------------------------------------

"""
import math
import os

def calculate_tw(Ta, RH):
    #Ta = float(Ta)
    #RH = float(RH)
    Tw = Ta + 0.151977 * ((RH + 8.313659) ** 0.5) + math.atan(Ta + RH) - math.atan(RH - 1.67633) + 0.00391838 * RH ** 1.5 * math.atan(0.023101 * RH) - 4.686035
    return Tw

def calculate_expression(Tw, Ta):
    #Ta = float(Ta)
    expression_value = -0.2442 + 0.55399 * Tw + 0.45535 * Ta - 0.0022 * Tw ** 2 + 0.00278 * Tw * Ta + 3.0
    return expression_value

'''
사무실 기온 입력
'''
temp = float(input("사무실 기온 입력(ºC) : "))

'''
사무실 습도 입력
'''
humi = float(input("사무실 습도 입력(%) : "))

Tw = calculate_tw(temp, humi)

perv_temp = calculate_expression(Tw, temp)

print("유라 6층 사무실 체감 온도는 ", round(perv_temp,2), "ºC입니다. 살려주세요")

os.system("pause")