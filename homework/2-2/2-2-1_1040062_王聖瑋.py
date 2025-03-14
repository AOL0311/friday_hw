def calc(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    return f'{days}天{hours}時{minutes}分{seconds}秒'

seconds = int(input('輸入秒數(s): '))
print(calc(seconds))