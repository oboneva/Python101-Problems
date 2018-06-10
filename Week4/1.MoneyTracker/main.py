from parse_money_tracker_data import ParseData
from aggregated_money_tracker import AggregatedMoneyTracker
from money_tracker import MoneyTracker
from money_tracker_menu import MoneyTrackerMenu
import sys

def main():
    user_name = sys.argv[1].lower()
    user_filename = "money_tracker_{}.txt".format(user_name)
    parsed_data = ParseData(user_filename)
    aggregated_object = AggregatedMoneyTracker(parsed_data)
    money_tracker = MoneyTracker(aggregated_object)
    menu = MoneyTrackerMenu(user_name, money_tracker)

if __name__ == '__main__':
    main()
