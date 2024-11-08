# CarFinder Program

def main():
    
    # Initialize list of allowed vehicles
    AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']
    
    # Main program loop
    while True:
        # Display menu options
        print("********************************")
        print("AutoCountry Vehicle Finder v0.2")
        print("********************************")
        print("Please Enter the following number below from the following menu:")
        print(" ")
        print("1. PRINT all Authorized Vehicles")
        print("2. SEARCH for Authorized Vehicle")
        print("3. Exit")
        print("********************************")
        choice = input("Enter your choice (1-3): ")
        
        # Handle user selection
        if choice == '1':
            # Display all authorized vehicles
            print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
            for vehicle in AllowedVehiclesList:
                print(vehicle)
        elif choice == '2':
            # Search for a specific vehicle
            search_query = input("Please Enter the full Vehicle name: ")
            if search_query in AllowedVehiclesList:
                print(f"\033[1m{search_query} is an authorized vehicle.\033[0m")
            else:
                print(f"\033[1m{search_query} is not an authorized vehicle, if you received this in error please check the spelling and try again.\033[0m")
        elif choice == '3':
            # Exit program
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            input("Press any key to exit...")
            break
        else:
            # Handle invalid input
            print("Invalid choice, please try again.")

# Program entry point
if __name__ == "__main__":
    main()
