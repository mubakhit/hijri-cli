"""
hijri - print and convert dates in the Umm al-Qura Hijri calendar
from the command line.

Copyright (c) 2026 Muhammad Bakhit <muhammadbakhit@outlook.com>

This tool is inspired by, and built on, the "hijra" project by Ojuba Linux
(https://github.com/ojuba-org/hijra), written by Muayyad Saleh Alsadi.
Sadly, that project is no longer being developed. This tool is my attempt
to keep its work useful: it reuses its conversion engine (hijra.py), adds
official Umm al-Qura calendar support, and offers it as a simple command
that works like the "date" command.

    Released under the terms of the Waqf Public License.
    This program is free software; you can redistribute it and/or modify
    it under the terms of the latest version of the Waqf Public License
    as published by Ojuba.org.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

    A copy of the license is included in this repository (Waqf-LICENSE-en.txt).

Umm al-Qura table data (hijra_uq.py) is taken from the "hijridate" project
by Mohammed Alshehri, under the MIT License (see LICENSE-hijridate.txt).
"""

import datetime
import hijra
import argparse

HIJRI_MONTHS = ["Muharram", "Safar", "Rabi' I", "Rabi' II", "Jumada I", "Jumada II", "Rajab", "Sha'ban", "Ramadan", "Shawwal", "Dhul Qadah", "Dhul Hijjah"]

def format_hijri (year,month,day,weekday):
    """This function formats the Hijri date into a string representation, including the weekday, day, month name, and year."""
    hijri_month = HIJRI_MONTHS[month - 1]
    return f"{weekday} {day} {hijri_month} {year}"


def parse_hijri (parts):
    parts = [int(num) for num in parts.split("-")]
    h_year, h_month, h_day = parts
    if not (1 <= h_month <= 12 and 1 <= h_day <= 30):
            raise ValueError("month or day out of range")
    if h_year < 1343 or h_year > 1500:
            print("Warning: The date is less than 1343 or greater than 1500, which is outside the range of the Umm al-Qura calendar. This date may not be accurate!.")
    return h_year, h_month, h_day

def main():
    parser = argparse.ArgumentParser(prog="hijri",description="Print or convert dates in the Umm al-Qura Hijri calendar.")
    parser.add_argument("-d", "--date", help="Gregorian date to convert to Hijri, as YYYY-MM-DD")
    parser.add_argument("-g", "--to-gregorian", help="Hijri date to convert to gregorian, as YYYY-MM-DD")
    args = parser.parse_args()

    """From Hijri to Gregorian, and Exit"""
    if args.to_gregorian != None:
        try:
            h_year,h_month,h_day = parse_hijri(args.to_gregorian)
            g_year,g_month,g_day = hijra.hijri_to_gregorian(h_year,h_month,h_day)
            g_date = datetime.date(g_year,g_month,g_day)
        except ValueError:
            parser.error("Invalid Hijri date. Use YYYY-MM-DD.")
        print(g_date.strftime("%A %d %B %Y")) # Example: Monday 05 August 2024
        return

    """From Gregorian to Hijri"""
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


