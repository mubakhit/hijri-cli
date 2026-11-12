import datetime
import hijra

hijri_months_list = ["Muharram", "Safar", "Rabi' I", "Rabi' II", "Jumada I", "Jumada II", "Rajab", "Sha'ban", "Ramadan", "Shawwal", "Dhul Qadah", "Dhul Hijjah"]

def format_hijri (year_,month_,day_,weekday_):
    hijri_month = hijri_months_list[month_ - 1]
    return f"{weekday_} {day_} {hijri_month} {year_}"


def main():
    today = datetime.datetime.now()
    day_string_format = today.strftime("%A") #Day as Friday
    # timeNow = today.strftime("%X") #Time Now in HH:mm:ss
    day = today.day
    month = today.month
    year = today.year
    year_in_hijri,month_in_hijri,day_in_hijri = hijra.gregorian_to_hijri(year,month,day)
    x = format_hijri(year_in_hijri,month_in_hijri,day_in_hijri,day_string_format)
    print(x)


if __name__ == "__main__":
    main()


