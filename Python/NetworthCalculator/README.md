# Net Bank-Account Balance Calculator

This tool calculates over a given period of time how much money you will have in your bank account based on your income(s) and expenses.

## Prerequisites

Needed libraries:

```python
matplotlib
```

## Usage:

Open the file config.js and set the parameters. These are as follows:

- The array "income" lists a set of income streams
- The "income_change_time" should be set to an amount of months after which your income changes to a new amount. If it doesn't change, set it to Zero (0).
- The "changed_income" parameter works just like the income parameter, only it is only used after the "income_change_time" has passed.
- The "additional_starting_cash" is money that should be taken into account when starting the calculation, for instance money that people owe you, redeemable credit card points, coupons or similar stuff.
- The "expenses" are your expenses. These have the format {"every_x_months" : [payments_seperated_by_commas]}. An example is a monthly payment of 100$: {"1" : [ 100 ]} where 1 stands for paid 1x per month and 100 is the amount paid. Multiple payments would look like this: {"1" : [50, 100, 30]}.
- The "limited_expenses" are expenses that will stop being paid after a given amount of time, such as loans or similar. The format here is {"months_remaining" : [payments_seperated_by_commas]}. Example: a 50$/month payment plan that has 3 months remaining would be formatted as {"3" : [50]}. Multiple payments would have the format {"3" : [69, 420, 66]}
- The "food" is self explanatory. It lists your food expenses, seperated by commas, similar to the income parameter.

To execute the script, use the following syntax:

```bash
python3 calc.py current_bank_balance months_to_calculate config.json 
```

Where:
- "current_bank_balance" is how much you currently have in your account and
- "months_to_calculate" is how many months ahead you want to calculate (BE WARNED that with too many values the plot will be filled to the brim!)

## Example

The below example runs a computation over 12 months time with a current bank balance of 696$, an income of 2300$ (consisting of 2 different income streams), a changed income after 5 months (new income is 700$ down from 2300$), 50$ in additional starting cash (let's assume he got a gift from a friend or something), 700$ in monthly expenses, 50$ in quarterly expenses, 1500$ in semesterly expenses, 400$/month for food and a payment plan for 2 months for 150$/month.

### Config.json

```json
{
	"income" : [
			 2000,
			 300 
		],
	"income_change_time" : 5,
	"changed_income" : [
			700
		],
	"additional_starting_cash" : [
			50
		],
	"expenses" : {
			"1" : [
					500,
					150,
					50
				],
			"3" : [
					10,
					35,
					5
				],
			"6" : [
					1500
				]
		},
	"limited_expenses" : {
			"2" :  [
					50,
					100
				]
		},
	"food" : [
			400
		]
}
```

```bash
python3 calc.py 696 12 config.json 
```

### Output

![alt text](https://github.com/leolion3/Portfolio/blob/master/Python/NetworthCalculator/demo.png "Example")
