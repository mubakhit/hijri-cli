# hijri-cli

A  command that prints and converts dates in the Umm al-Qura Hijri
calendar, the official calendar of Saudi Arabia. It works like the `date`
command, with no locale setup needed.

```
$ hijri
Friday 3 Jumada II 1448 15:11:13
```

## Install

The recommended way to install `hijri-cli` is with
[pipx](https://pipx.pypa.io/). pipx installs command-line tools in their own
isolated environment and makes the command available everywhere.

```
pipx install hijri-cli
```

> **Note:** Plain `pip install hijri-cli` fails on most modern Linux
> distributions (Ubuntu 23.04+, Debian 12+, Fedora and others) with an
> `externally-managed-environment` error. This is a protection built into the
> system Python, not a problem with this package. Use pipx instead. Do not use
> `--break-system-packages`.

### Step 1: install pipx

**Ubuntu / Debian**

```
sudo apt install pipx
pipx ensurepath
```

**Fedora**

```
sudo dnf install pipx
pipx ensurepath
```

**Arch Linux**

```
sudo pacman -S python-pipx
pipx ensurepath
```

**Windows** (PowerShell)

```
python -m pip install --user pipx
python -m pipx ensurepath
```

Close and reopen your terminal after `ensurepath`, so the new `PATH` takes
effect.

### Step 2: install hijri-cli

```
pipx install hijri-cli
```

### Upgrade or remove

```
pipx upgrade hijri-cli
pipx uninstall hijri-cli
```

### Alternative: pip inside a virtual environment

If you prefer pip, install inside a virtual environment. The `hijri` command
is then available only while that environment is active.

Linux:

```
python3 -m venv .venv
source .venv/bin/activate
pip install hijri-cli
```

Windows (PowerShell):

```
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install hijri-cli
```

Requires Python 3.8 or newer.

## Usage

Print today's Hijri date and the current time:

```
$ hijri
Friday 3 Jumada II 1448 15:11:13
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

Show all options:

```
$ hijri --help
usage: hijri [-h] [-d DATE] [-g TO_GREGORIAN]
```

| Option | Long form | Value | What it does |
|---|---|---|---|
| (none) | | | Print today's Hijri date and time |
| `-d` | `--date` | Gregorian date, `YYYY-MM-DD` | Convert to Hijri |
| `-g` | `--to-gregorian` | Hijri date, `YYYY-MM-DD` | Convert to Gregorian |
| `-h` | `--help` | | Show help |

## Accuracy

> **Note:** Dates from 1343 AH to 1500 AH (1924 to 2077 CE) follow the
> official Umm al-Qura table. Dates outside this range are calculated
> arithmetically and may differ from the official calendar by a day. The tool
> prints a warning when you convert a Hijri date outside the table range.

## Credits

This tool is inspired by, and built on, the
[hijra](https://github.com/ojuba-org/hijra) project by Ojuba Linux, written
by Muayyad Saleh Alsadi. Sadly, that project is no longer being developed.
This tool reuses its conversion engine (`hijra.py`), adds Umm al-Qura
support, and offers it as a simple command.

The Umm al-Qura table data comes from the
[hijridate](https://github.com/dralshehri/hijridate) project by
Mohammed Alshehri.

## Contributing

Bug reports and suggestions are welcome on the
[issues page](https://github.com/mubakhit/hijri-cli/issues).

## License

Released under the Waqf Public License. See `LICENSE.txt` (English) and
`LICENSE-ar.txt` (Arabic).

The Umm al-Qura table data is under the MIT License. See
`hijridate-LICENSE.txt`.
