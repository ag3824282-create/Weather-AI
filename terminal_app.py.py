from utils.menu import show_main_menu
from services.weather_service import search_weather
from utils.menu import print_separator

def main():
    try:
        while True:
            show_main_menu()
            choice = input("Enter your choice (1 or 2): ")
            if choice == "1":
                input_city = input("Enter the city name: ")
                try:
                    weather_info = search_weather(input_city)
                    print_separator()
                except (ValueError, ConnectionError) as exc:
                    print(f"❌ {exc}")
                    input("\nPress Enter to continue...")
                    continue

                if weather_info:
                    print(f"☁ Weather in {weather_info['city']}:")
                    print(f"🌡 Temperature: {weather_info['temperature']}°C")
                    print(f"  Description: {weather_info['description']}")
                    print(f"💧 Humidity: {weather_info['humidity']}%")
                    print(f"🌬 Wind Speed: {weather_info['wind_speed']} m/s")
                    
            elif choice == "2":
                print("Thank you for using Weather AI. Goodbye!")
                break
            else:
                print("This feature is under development.")

    except KeyboardInterrupt:
        print("\nExiting the application. Goodbye!")

if __name__ == "__main__":
    main()
