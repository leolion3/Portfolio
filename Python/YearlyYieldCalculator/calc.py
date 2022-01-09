import sys


# Used for graph
values = []
use_graph = False


def get_value(years_left, yearly_yield, val, annual_investment):
	global values, use_graph
	if years_left == 0:
		return val
	else:
		current_value = annual_investment + val + val * yearly_yield
		if use_graph:
			values.append(round(current_value, 2))
		return get_value(years_left-1, yearly_yield, current_value, annual_investment)


if len(sys.argv) < 4:
	print('Usage: python calc.py <initial $> <Years> <Annual yield as floating point number> [Annual invested money]')
	exit(-1)


val = float(sys.argv[1])
years = int(sys.argv[2])
annual_yield = float(sys.argv[3])
invested_per_year = 0
if len(sys.argv) > 5:
	if sys.argv[5] == 'True':
		import matplotlib.pyplot as plt
		use_graph = True
		values.append(val)
		get_value(years, annual_yield, val, invested_per_year)
		# Set graph colors
		plt.rcParams['axes.facecolor']='black'
		plt.rcParams['savefig.facecolor']='black'
		plt.rcParams['axes.edgecolor']='white'
		fig=plt.figure(facecolor='black')
		ax = fig.add_subplot(111)
		plt.xlabel('Time')
		plt.ylabel('$')
		plt.xticks(range(0, years + 1))
		# Plot available balance
		ax.plot(range(0, years + 1), values, color='green', linestyle='--', marker='o')
		for i,j in zip(range(0, years + 1), values):
			if i % 2 == 0:
				ax.annotate(f'{str(round(j))} $', xy=(i,j), weight="bold", fontsize=10, color='lime', horizontalalignment='left', verticalalignment='top')
			else:
				ax.annotate(f'{str(round(j))} $', xy=(i,j), weight="bold", fontsize=10, color='lime', horizontalalignment='right', verticalalignment='bottom')
		ax.spines['bottom'].set_color('white')
		ax.spines['right'].set_color('white')
		ax.xaxis.label.set_color('white')
		ax.yaxis.label.set_color('white')
		ax.tick_params(axis='x', colors='white')
		ax.tick_params(axis='y', colors='white')
		ax.set_title(f'Growth: {round(float(values[-1]) / float(val)) * 100}% | {values[-1]}$\nAnnual yield {round(annual_yield * 100,2)}%', color='lime')
		plt.show()
elif len(sys.argv) > 4:
	invested_per_year = float(sys.argv[4])
	print(f'Yield using {round(annual_yield * 100, 2)}% annual yield and {val}$ starting money and an investment of {invested_per_year}$ annually over {years} years is: {round(get_value(years, annual_yield, val, invested_per_year), 2)}$')
else:
	print(f'Yield using {round(annual_yield * 100, 2)}% annual yield and {val}$ starting money over {years} years is: {round(get_value(years, annual_yield, val, 0), 2)}$')