# ![Krispy](https://i.ibb.co/2tp76YQ/icon.png) Krispy Bot

A Package to Automate Krispy Kreme Survey using Selenium.

## Installation:

```sh
pip install -e ./krispy-bot
```

## Usage:

#### Example 0:

```python
krispy.bot(url, receipt, answers).finish_survey()
```

#### Example 1:

```python
import json
import krispy

with open("survey.json", "r", encoding="utf-8") as file:
    survey = (s := json.load(file))['url'], s['receipt'], s['answers']


krispy.bot(*survey).finish_survey()
```
