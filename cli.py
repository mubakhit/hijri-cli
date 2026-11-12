import datetime
import hijra
import argparse

HIJRI_MONTHS = ["Muharram", "Safar", "Rabi' I", "Rabi' II", "Jumada I", "Jumada II", "Rajab", "Sha'ban", "Ramadan", "Shawwal", "Dhul Qadah", "Dhul Hijjah"]

def format_hijri (year,month,day,weekday):
    hijri_month = HIJRI_MONTHS[month - 1]
    return f"{weekday} {day} {hijri_month} {year}"


def main():
    parser = argparse.ArgumentParser(prog="hijri",description="Print or convert dates in the Umm al-Qura Hijri calendar.")
    parser.add_argument("-d", "--date", help="Gregorian date to convert, as YYYY-MM-DD")
    args = parser.parse_args()

    if args.date == None:
        target = datetime.datetime.now() # Example: 2026-11-13 01:49:45
        time_text = target.strftime("%X") # Time Now in HH:mm:ss
    else:
        try:
            target = datetime.date.fromisoformat(args.date)
            time_text = ""
        except ValueError:
            parser.error("Invalid date format. Please use YYYY-MM-DD.")

    weekday = target.strftime("%A") # Example Friday
    h_year,h_month,h_day = hijra.gregorian_to_hijri(target.year,target.month,target.day)
    text = format_hijri(h_year,h_month,h_day,weekday)

    if time_text:
        print(text, time_text)
    else:
        print(text)


if __name__ == "__main__":
    main()


