# CarFinder Program

import os

def clear_screen():
    """Clear the terminal screen based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    """Prints the main menu."""
    print("********************************")
    print("AutoCountry Vehicle Finder v0.4")
    print("********************************")
    print("Please enter the number from the menu below:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD an Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
    print("********************************")

def get_user_choice():
    """Gets and validates the user's menu choice."""
    choice = input("Enter your choice (1-5): ")
    while choice not in ['1', '2', '3', '4', '5']:
        print("Invalid option, please enter a valid option (1-5).")
        choice = input("Enter your choice (1-5): ")
    return choice

def display_vehicles(vehicles):
    """Displays all authorized vehicles."""
    print("\nAuthorized vehicles:")
    for vehicle in vehicles:
        print(vehicle)

def search_vehicle(vehicles):
    """Searches for a specific vehicle in the list."""
    search_query = input("Please enter the full vehicle name: ").strip()
    if search_query in vehicles:
        print(f'"{search_query}" is an authorized vehicle.')
    else:
        print(f'"{search_query}" is not an authorized vehicle. Please check the spelling and try again.')

def add_vehicle(vehicles):
    """Adds a new vehicle to the list."""
    new_vehicle = input("Enter the name of the vehicle to add: ").strip()
    if new_vehicle:
        vehicles.append(new_vehicle)
        print(f'You have added "{new_vehicle}" as an authorized vehicle.')
    else:
        print("Vehicle name cannot be empty.")

def delete_vehicle(vehicles):
    """Deletes a vehicle from the list after confirmation."""
    vehicle_to_remove = input("Enter the full vehicle name to REMOVE: ").strip()
    if vehicle_to_remove in vehicles:
        confirm = input(f"Are you sure you want to remove '{vehicle_to_remove}'? (yes/no): ").lower()
        if confirm == 'yes':
            vehicles.remove(vehicle_to_remove)
            print(f'{vehicle_to_remove} has been removed from the authorized vehicles.')
        else:
            print("Removal canceled.")
    else:
        print(f'"{vehicle_to_remove}" is not in the list of authorized vehicles. Please check the spelling and try again.')

def main():
    allowed_vehicles = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan', 'Rivian R1T', 'Ram 1500']
    
    while True:
        print_menu()
        choice = get_user_choice()
        
        if choice == '1':
            display_vehicles(allowed_vehicles)
        elif choice == '2':
            search_vehicle(allowed_vehicles)
        elif choice == '3':
            add_vehicle(allowed_vehicles)
        elif choice == '4':
            delete_vehicle(allowed_vehicles)
        elif choice == '5':
            print("Thank you for using the AutoCountry Vehicle Finder. Goodbye!")
            break

        print("\n")  # Visual separation for next menu display

if __name__ == "__main__":
    main()
