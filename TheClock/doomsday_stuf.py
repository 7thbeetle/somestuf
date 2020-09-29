__author__ = "Kuzey Rodoplu"

import time
import locale


locale.setlocale(locale.LC_ALL, 'english')
epoch = time.localtime()
print("\n" * 500)


## Sayaçlar başlıyor

## -------------------------------------------------------------------------
year = epoch.tm_year
month = epoch.tm_mon

if year % 4 == 0:  ## yılın gün sayısı
    dayofyear = 366
else:
    dayofyear = 365

if month in {1, 3, 5, 7, 8, 10, 12}:  ## ayın gün sayısı
    moday = 31
elif month in {4, 6, 9, 11}:
    moday = 30
elif month == 2 and dayofyear % 4 == 0:
    moday = 29
elif month == 2 and dayofyear % 4 != 0:
    moday = 28


## Dakikaya kalan saniye bölümü
secondGone = epoch.tm_sec
print("⬛" * (secondGone * 100 // 60), "⬜" * (100 - (secondGone * 100 // 60)), "\n{} seconds left to next minute\n".format(60 - secondGone), sep="")


## Saate kalan dakika bölümü
minuteGone = epoch.tm_min
print("⬛" * (minuteGone * 100 // 60), "⬜" * (100 - (minuteGone * 100 // 60)), "\n{} minutes left to next hour\n".format(60 - minuteGone), sep="")


## Güne kalan saat bölümü
hourGone = epoch.tm_hour
print("⬛" * (hourGone * 100 // 24), "⬜" * (100 - (hourGone * 100 // 24)), "\n{} hours left to next day\n".format(24 - hourGone), sep="")


## Aya kalan gün bölümü
dayzGone = epoch.tm_mday
print("⬛" * (dayzGone * 100 // moday), "⬜" * (100 - (dayzGone * 100 // moday)), "\n{} days left to next month\n".format(moday - dayzGone), sep="")


## Yıla kalan gün bölümü
yearday = epoch.tm_yday
print("⬛" * (yearday * 100 // dayofyear), "⬜" * (100 - (yearday * 100 // dayofyear)), "\n{} days left to next year\n".format(dayofyear - yearday), sep="")


## Next Valentine's Day bölümü
if yearday <= 45:
    roadToVal = 45 - yearday
elif yearday > 45:
    roadToVal = (dayofyear - yearday) + 45
print("⬛" * (100 - (roadToVal * 100 // dayofyear)), "⬜" * (roadToVal * 100 // dayofyear), "\n{} days left to next Valentine's Day\n".format(roadToVal), sep="")


## Next Haloween bölümü
if dayofyear == 365:
    if 304 >= yearday:
        roadToHaloween = 304 - yearday
    else:
        roadToHaloween = (365 - yearday) + 304
else:
    if 305 >= yearday:
        roadToHaloween = 305 - yearday
    else:
        roadToHaloween = (366 - yearday) + 305
print("⬛" * (100 - (roadToHaloween * 100 // dayofyear)), "⬜" * (roadToHaloween * 100 // dayofyear), "\n{} days left to next Haloween\n".format(roadToHaloween), sep="")


## Next Christmas bölümü 359/360
if dayofyear == 365:
    if 359 >= yearday:
        roadToChrist = 359 - yearday
    else:
        roadToChrist = (365 - yearday) + 359
else:
    if 360 >= yearday:
        roadToChrist = 360 - yearday
    else:
        roadToChrist = (366 - yearday) + 360
print("⬛" * (100 - (roadToChrist * 100 // dayofyear)), "⬜" * (roadToChrist * 100 // dayofyear), "\n{} days left to next Christmas\n".format(roadToChrist), sep="")


## Next Decade bölümü
print("⬛" * ((year % 10) * 10), "⬜" * ((10 - (year % 10)) * 10), "\n{} years left to next decade\n".format(10 - (year % 10)), sep="")


## Next Century bölümü
print("⬛" * (year % 100), "⬜" * (100 - (year % 100)), "\n{} years left to next century\n".format(100 - (year % 100)), sep="")


## Next Millennium bölümü
print("⬛" * ((year % 1000) // 10), "⬜" * ((1000 - (year % 1000)) // 10), "\n{} years left to next decade\n".format(1000 - (year % 1000)), sep="")


## End of the reality we know bölümü
print("⬛" * 99, "⬜", """\nA few years left to end of the reality we know...
What will you do about that?
Be kind to people and nature, live your life and don't let anyone ruin it.
Do that.""", sep="")
