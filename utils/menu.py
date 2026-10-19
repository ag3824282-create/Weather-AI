menu_items = [
    "Search weather",
    "Exit"
]
def print_separator():
    print("=" * 50)

def show_main_menu():
    try:
        print_separator()
        print(("Weather AI").center(50))
        print_separator()
        print("Welcome to Weather AI! Please select an option:")
        for index, item in enumerate(menu_items, start=1):
            print(f"{index}. {item}")
    except Exception:
        print_separator()
        print("Sorry, I cannot display the menu at this time. Please try again later.")