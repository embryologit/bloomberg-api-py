# bloomberg-api-py
Exploits publically accessible APIs from bloomberg.com for simple financial data.

## get started
on linux. cd into module directory.

```
pip install -r requirements.txt
```

open main.py and change variable "query" to company you like. Spaces are permitted. Indexes, funds, currencies may also work.

```
python3 main.py
```

## notes to current state of repo
development has been halted because bloomberg.com is pretty good at blocking this script. Potential solutions are being tested. As of now those utilize request header customization and selenium chromedriver browser-automation.
