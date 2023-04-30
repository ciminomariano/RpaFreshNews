from src.actions import CustomActions
from src.exceptions import CustomException
from constants import constants_names

def main():
    # Create an instance of my custom actions class
    custom_actions = CustomActions()
    # Execute the function to open the web site
    #open_website = custom_actions.open_website(constants_names.URLNYTIMES)
    if custom_actions.open_website(constants_names.URLNYTIMES):
        if custom_actions.maximaze_nav():
            if custom_actions.accept_cookies():
                if custom_actions.click_search_bar():
                    if custom_actions.write_search_term("nba"):
                        print("Search term sent")

if __name__ == "__main__":
    main()