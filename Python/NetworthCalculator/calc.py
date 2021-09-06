#!/usr/bin/env python3
import matplotlib.pyplot as plt
import sys
import ast
import json
import math


def usage():
	print('Usage: calc.py starting_cash months config.json')
	exit()


if len(sys.argv) < 4:
	usage()


json_data = None
with open(sys.argv[3], 'r',encoding="utf-8") as f:
	json_data = json.loads(f.read())

income = json_data.get("income")
income_change_time = json_data.get("income_change_time")
changed_income = json_data.get("changed_income")
additional_starting_cash = json_data.get("additional_starting_cash")
expenses = json_data.get("expenses")
limited_expenses = json_data.get("limited_expenses")
food = json_data.get("food")


try:
	current_cash = float(sys.argv[1]) + sum(additional_starting_cash)
	months = int(sys.argv[2])
except:
	usage()


# Data sets
plotted_available = []
plotted_expenses = []
plotted_income = []
plotted_months = range(1, months + 1)


# Compute values
for a in range(1, months + 1):
	current_payments = []
	for key, value in expenses.items():
		if a % int(key) == 0:
			current_payments.append(sum(value))
	for key, value in limited_expenses.items():
		if a <= int(key):
			current_payments.append(sum(value)) 
	# Too many sum calls, but idc :P
	if a > income_change_time:
		current_cash = current_cash + sum(changed_income) - sum(current_payments) - sum(food)
		plotted_available.append(current_cash)
		plotted_income.append(sum(changed_income))
		plotted_expenses.append(sum(current_payments) + sum(food))
	else:
		current_cash = current_cash + sum(income) - sum(current_payments) - sum(food)
		plotted_available.append(current_cash)
		plotted_income.append(sum(income))
		plotted_expenses.append(sum(current_payments) + sum(food))
		

# Compute growth
monetary_change  = round(plotted_available[-1] - plotted_available[0], 2)
growth = (plotted_available[-1] - plotted_available[0]) / plotted_available[0]
if growth > 0:
	growth+=1
growth = round(growth * 100, 2)

# Set graph colors
plt.rcParams['axes.facecolor']='black'
plt.rcParams['savefig.facecolor']='black'
plt.rcParams['axes.edgecolor']='white'
fig=plt.figure(facecolor='black')
ax = fig.add_subplot(111)
plt.xlabel('Time')
plt.ylabel('$')
plt.xticks(plotted_months)


# Plot available balance
ax.plot(plotted_months, plotted_available, color='green', linestyle='--', marker='o')
for i,j in zip(plotted_months, plotted_available):
    ax.annotate(f'{str(round(j))} $', xy=(i,j), weight="bold", fontsize=12, color='lime', horizontalalignment='left', verticalalignment='bottom')


# Plot expenses
ax.plot(plotted_months, plotted_expenses, color='darkred', linestyle='--', marker='o')
for i,j in zip(plotted_months, plotted_expenses):
	ax.annotate(f'{str(round(j))} $', xy=(i,j), weight="bold", fontsize=12, color='red', horizontalalignment='right', verticalalignment='top')


# Plot income 
ax.plot(plotted_months, plotted_income, color='blue', marker='o')
for i,j in zip(plotted_months, plotted_income):
	ax.annotate(f'{str(round(j))} $', xy=(i,j), weight="bold", fontsize=12, color='blue', horizontalalignment='right', verticalalignment='bottom')


# MORE GRAPH COLOOOOORS :D
ax.spines['bottom'].set_color('white')
ax.spines['right'].set_color('white')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
if growth > 0:
	ax.set_title(f'Growth: +{growth}% | +{monetary_change}$', color='lime')
else:
	ax.set_title(f'Growth: {growth}% | {monetary_change}$', color='red')
plt.legend(['Available Balance', 'Expenses', 'Income'], labelcolor=['lime', 'red', 'blue'])
plt.show()