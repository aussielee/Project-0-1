# CarFinder Program

import os
import msvcrt

def clear_screen():
    """Clear the terminal screen based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    """Prints the main menu."""
    print("********************************")
    print("AutoCountry Vehicle Finder v0.4")
    print("********************************")
    print("Please enter the number from the menu below:")
    print()
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD an Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
    print("********************************")

def get_user_choice():
    """Gets and validates the user's menu choice without pressing Enter."""
    while True:
        if msvcrt.kbhit():
            choice = msvcrt.getch().decode('utf-8')
            if choice in ['1', '2', '3', '4', '5']:
                return choice
            else:
                print("Invalid option, please press a valid key (1-5).")

def display_vehicles(vehicles):
    """Displays all authorized vehicles."""
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    for vehicle in vehicles:
        print(vehicle)

def search_vehicle(vehicles):
    """Searches for a specific vehicle in the list."""
    search_query = input("Please enter the full vehicle name: ").strip()
    if search_query in vehicles:
        print(f'"{search_query}" is an authorized vehicle.')
    else:
        print(f'"{search_query}" is not an authorized vehicle. Please check the spelling and try again.')

def load_vehicles_from_file(filename):
    """Load vehicles from a file into a list."""
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def save_vehicles_to_file(filename, vehicles):
    """Save the list of vehicles to a file."""
    with open(filename, 'w') as file:
        for vehicle in vehicles:
            file.write(f"{vehicle}\n")

def add_vehicle(vehicles, filename):
    """Adds a new vehicle to the list and updates the file."""
    new_vehicle = input("Enter the name of the vehicle to add: ").strip()
    if new_vehicle:
        vehicles.append(new_vehicle)
        save_vehicles_to_file(filename, vehicles)
        print(f'You have added "{new_vehicle}" as an authorized vehicle.')
    else:
        print("Vehicle name cannot be empty.")

def delete_vehicle(vehicles, filename):
    """Deletes a vehicle from the list after confirmation and updates the file."""
    vehicle_to_remove = input("Enter the full vehicle name to REMOVE: ").strip()
    if vehicle_to_remove in vehicles:
        confirm = input(f"Are you sure you want to remove '{vehicle_to_remove}'? (yes/no): ").lower()
        if confirm == 'yes':
            vehicles.remove(vehicle_to_remove)
            save_vehicles_to_file(filename, vehicles)
            print(f'{vehicle_to_remove} has been removed from the authorized vehicles.')    
        else:
            print("Removal canceled.")
    else:
        print(f'"{vehicle_to_remove}" is not in the list of authorized vehicles. Please check the spelling and try again.')

def main():
    filename = 'allowed_vehicles.txt'
    
    # Check if the file exists, if not, create it with the initial list of vehicles
    if not os.path.exists(filename):
        AllowedVehiclesList = [
            'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck',
            'Toyota Tundra', 'Rivian R1T', 'Ram 1500'
        ]
        save_vehicles_to_file(filename, AllowedVehiclesList)
    
    allowed_vehicles = load_vehicles_from_file(filename)
    
    while True:
        print_menu()
        choice = get_user_choice()
        
        if choice == '1':
            display_vehicles(allowed_vehicles)
        elif choice == '2':
            search_vehicle(allowed_vehicles)
        elif choice == '3':
            add_vehicle(allowed_vehicles, filename)
        elif choice == '4':
            delete_vehicle(allowed_vehicles, filename)
        elif choice == '5':
            print("Thank you for using the AutoCountry Vehicle Finder. Goodbye!")
            break

        print("\n")  # Visual separation for next menu display

if __name__ == "__main__":
    main()
