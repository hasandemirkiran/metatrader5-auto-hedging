import numpy as np
from MT5 import *
import warnings
warnings.filterwarnings("ignore")


def random():
    values = [True, False]
    buy = np.random.choice(values)
    sell = not buy

    return buy, sell


symbols_list = {
    # "Nasdaq 100": ["NAS100", 0.1],
    # "Russel 2000": ["US2000", 0.1],
    # "Gold USD": ["XAUUSD", 0.01],
    "GBP USD": ["GBPUSD", 0.10],
    # "S&P 500": ["US500", 0.1],
    # "Us dollar vs Canadian dollar": ["USDCAD", 0.01],
    "Euro vs USdollar": ["EURUSD", 0.10]
    }


current_account_info = mt5.account_info()
print("------------------------------------------------------------------")
print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print()
print()
print(current_account_info)
print()
print()
print(f"Balance: {current_account_info.balance} USD,\t"
      f"Equity: {current_account_info.equity} USD, \t"
      f"Profit: {current_account_info.profit} USD")
print("------------------------------------------------------------------")


start = datetime.now().strftime("%H:%M:%S")  # "23:59:59"

while True:

    # Launch the algorithm
    # Verfication for launch
    if datetime.now().weekday() not in (5, 6):
        is_time = datetime.now().strftime("%H:%M:%S") == start
    else:
        is_time = False

    if is_time:
        # Close all trades
        if mt5.positions_total() > 0:
            MT5.close_all_night()

        for asset in symbols_list.keys():
            # Initialize the inputs
            symbol = symbols_list[asset][0]
            lot = symbols_list[asset][1]

            buy, sell = random()

            # Run the algorithm
            MT5.run(symbol, buy, sell, lot)
