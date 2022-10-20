# Investment Yield Calculator

Calculates the amount of money one gets for a given annual yield percentage, a certain amount of starting cash and a given timespan. Can also be given an annual investment value so the accumulative wealth is calculated over time.

## Requirements

By default, the script does not require any libraries. If you do wish do visualize the annual yield over time, then matplotlib is required.

```bash
pip install matplotlib
```

## Usage

Usage (variable in quare braces is optional):
```bash
python calc.py <initial $> <Years> <Annual yield as floating point number> [Annual invested money] [graphical - default False]
```

Example given 25k$ starting cash, 25 years timespan, 15% annual yield and 25k$ invested yearly:
```
#> python ./calc.py 25000 25 0.15 25000
Yield using 15.0% annual yield and 25000.0$ starting money and an investment of 25000.0$ annually over 25 years is: 6142799.25$
```

## Optional: Graph visualisation

To toggle graph visualisation, add the 5th commandline argument:
```
#> python ./calc.py 25000 25 0.15 25000 True
```

### Output

![Demonstration](https://raw.githubusercontent.com/leolion3/Portfolio/master/Python/YearlyYieldCalculator/yield_demo.png)
