# gptrepo

This repository includes a simple validation module.

## Usage

```
from validator import validate_inputs, calculate, ValidationError

RULES = {
    "a": (0, 10),
    "b": (1, 5),
}

values = {"a": 3, "b": 2}
valid, errors = validate_inputs(values, RULES)
if valid:
    result = calculate(values, RULES)
    print(result)
else:
    print(errors)
```

Run tests with:

```
pytest
```


