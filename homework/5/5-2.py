# 某公司規定氣溫高於 28 度可開冷氣; 氣溫低於 15 度可開暖氣。
# 請寫一程式，由鍵盤輸入氣溫 t，然後顯示現在溫度及狀態(狀態為: 開冷氣、開暖氣、不開機，3種)。
# 例如: 輸入 30，顯示 "現在溫度為 30 度，開冷氣。"

def temperature_detect(x):
    if t < 15:
        return f'現在溫度為 {t} 度，開暖氣。'
    elif 28 < t:
        return f'現在溫度為 {t} 度，開冷氣。'
    else:
        return f'現在溫度為 {t} 度，不開機。'

t = int(input('輸入氣溫: '))

print(temperature_detect(t))