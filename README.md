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
development has been halted because bloomberg.com is pretty good at blocking this script. Potential solutions are being tested. As of now those utilize request header customization and selenium chromedriver browser-automation. Request header customaization seems to work fine for now.

## strategy/further steps
- registry that saves response data from query search. This registry will be searched before an API-search is done to determine ticker for search query so that API-requests for already known search queries are avoided. Maybe this registry can be a relational database to seed more powerful local registry-searches (search-API returns multiple finds, each of which should be findable by multiple search queries)
- request header customizations is in need of fresh cookies. Develop script, that can bake fresh cookies (and other perishable headers) and feeds them to the script by updating REQUEST_HEADERS constant. This script shall only be called when current cookie or other perishable&needed element expire.
- cli functionality. typing query after "python3 bloomberg-api.py" will turn on script to search for query.
- Actual output of this script should not just be the json-reponse in stdout but also a write to a database (for now csv)
