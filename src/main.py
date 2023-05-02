from src.actions import CustomActions
from src.constants.constants_names import URLNYTIMES
from src.exceptions import CustomException
from constants import constants_names
import configparser
import os
import logging

# Creating folder for logs ig does not exists
if not os.path.exists("output"):
    os.makedirs("output")
logging.basicConfig(filename='output/trace-robot.log', level=logging.ERROR)
# Taking initial configuration from config file
config = configparser.ConfigParser()
config.read('config.ini')
# Reading parameters from the file
search_phrase = config.get('search', 'SEARCH_PHRASE')
news_categories = config.get('search', 'CATEGORY').split(',')
news_categories = [category.upper() for category in news_categories]

# checking search phrase is not empty
if not search_phrase:
    search_phrase = " "
# Getting number of months to filter by data
num_months = config.get('search', 'NUMBER_OF_MONTHS')

#Intiliazing the robot
def main():
    # Create an instance of my custom actions class
    custom_actions = CustomActions(URLNYTIMES)
    # Execute the function to open the web site
    # open_website = custom_actions.open_website(constants_names.URLNYTIMES)

    custom_actions.apply_datetime(num_months)

    if custom_actions.open_website(constants_names.URLNYTIMES):
        if custom_actions.maximaze_nav():
            if custom_actions.accept_cookies():
                if custom_actions.click_search_bar():
                    if custom_actions.write_search_term(search_phrase):
                        custom_actions.apply_datetime(num_months)
                        custom_actions.apply_categories(news_categories)
                        articles = custom_actions.extract_articles(search_phrase)
                        custom_actions.write_to_excel(articles)
                        print(articles)




if __name__ == "__main__":
    main()
