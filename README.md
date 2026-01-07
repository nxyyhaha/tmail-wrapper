# tmail-api (Python wrapper)

Python port of the `TMail-API` wrapper. Provides a tiny `TMail` client
that mirrors the original Node package API.

Quick example

```py
from tmail-py import TMail

client = TMail('https://default.tmail.thehp.in/api', 'API_KEY')
print(client.domains())
print(client.create())
print(client.messages('email@domain.com'))
```

CLI

```
python -m tmail_api.cli https://default.tmail.thehp.in/api API_KEY domains
```
