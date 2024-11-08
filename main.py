# CarFinder Program

def main():
    # Display program header
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    
    # Initialize list of allowed vehicles
    AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']
    
    # Main program loop
    while True:
        # Display menu options
        print("Please Enter the following number below from the following menu:")
        print("1. PRINT all Authorized Vehicles")
        print("2. Exit")
        choice = input("Enter your choice (1-2): ")
        
        # Handle user selection
        if choice == '1':
            # Display all authorized vehicles
            print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
            for vehicle in AllowedVehiclesList:
                print(vehicle)
        elif choice == '2':
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
