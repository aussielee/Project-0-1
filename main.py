# CarFinder Program

import os

def clear_screen():
    # Clear the terminal screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    
    # Initialize list of allowed vehicles
    AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']
    
    # Main program loop
    while True:
        
        # Display menu options
        print("********************************")
        print("AutoCountry Vehicle Finder v0.3")
        print("********************************")
        print("Please Enter the following number below from the following menu:")
        print(" ")
        print("1. PRINT all Authorized Vehicles")
        print("2. SEARCH for Authorized Vehicle")
        print("3. ADD an Authorized Vehicle")
        print("4. Exit")
        print("********************************")
        
        # Input validation loop
        choice = None
        while choice not in ['1', '2', '3', '4']:
            choice = input("Enter your choice (1-4): ")
            if choice not in ['1', '2', '3', '4']:
                print("Please enter a valid option (1-4).")
        
        # Option 1: Display all authorized vehicles
        if choice == '1':
            print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
            for vehicle in AllowedVehiclesList:
                print(vehicle)
        
        # Option 2: Search for a specific authorized vehicle
        elif choice == '2':
            search_query = input("Please Enter the full Vehicle name: ")
            if search_query in AllowedVehiclesList:
                print(f"\033[1m{search_query} is an authorized vehicle.\033[0m")
            else:
                print(f"{search_query} is not an authorized vehicle, please check the spelling and try again.")
        
        # Option 3: Add a new vehicle to the authorized list
        elif choice == '3':
            new_vehicle = input("Please enter the name of the vehicle to add: ")
            if new_vehicle:
                AllowedVehiclesList.append(new_vehicle)
                print(f"\033[1mYou have added \"{new_vehicle}\" as an authorized vehicle\033[0m")
            else:
                print("Vehicle name cannot be empty.")
        
        # Option 4: Exit the program
        elif choice == '4':
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break

        # Add a space between previous result and menu refresh
        print("\n")  # This line adds an empty line for visual separation

# Program entry point
if __name__ == "__main__":
    main()
