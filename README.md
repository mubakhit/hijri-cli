# hijri-cli

A simple command that prints and converts dates in the Umm al-Qura Hijri
calendar, the official calendar of Saudi Arabia. It works like the `date`
command, with no locale setup needed.

## Install

```
pip install hijri-cli
```

## Usage

Print today's Hijri date:

```
$ hijri
Friday 3 Jumada II 1448 14:34:5
```

Convert a Gregorian date to Hijri:

```
$ hijri -d 2024-08-05
Monday 1 Safar 1446
```

Convert a Hijri date to Gregorian:

```
$ hijri -g 1446-02-01
Monday 05 August 2024
```

Show help:

```
$ hijri --help
```

## Accuracy

Dates from 1343 AH to 1500 AH (1924 to 2077 CE) follow the official
Umm al-Qura table. Dates outside this range are calculated arithmetically
and may differ from the official calendar by a day.

## Credits

This tool is inspired by, and built on, the
[hijra](https://github.com/ojuba-org/hijra) project by Ojuba Linux, written
by Muayyad Saleh Alsadi. Sadly, that project is no longer being developed.
This tool reuses its conversion engine (`hijra.py`) and adds Umm al-Qura
support.

The Umm al-Qura table data comes from the
[hijridate](https://github.com/dralshehri/hijridate) project by
Mohammed Alshehri.

## License

Released under the Waqf Public License. See `LICENSE.txt`.

The Umm al-Qura table data is under the MIT License.
See `hijridate-LICENSE.txt`.