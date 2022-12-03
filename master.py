import json
file_name = "./data/poi.json"

def options_menu():
    print("\nPoints Of Interest(POIs)")
    print("\nSelect Option:")
    print("\n(1) View POIs")
    print("\n(2) POI Search")
    print("\n(3) Add POI")
    print("\n(4) Delete POI")
    print("\n(5) POI Enquiry")
    print("\n(6) Exit")
    
def view_poi():
    with open(file_name, "r") as poi_file:
        data = json.load(poi_file)
        index = 0
        
        for entry in data:
            poi_name = entry["poi_name"]
            
            print(f"\nIndex Number {index}")
            print(f"Name of POI: {poi_name}")
            print("\n")
            index = index + 1

def poi_search():
    with open(file_name, "r") as poi_file:
        data = json.load(poi_file)
        
        user_search = input("Enter POI name to search: ")
        for entry in data:        
            poi_name = entry["poi_name"]
            poi_type = entry["poi_type"]
            poi_description = entry["poi_description"]
            
            if user_search in entry.values():
                print(f"\nSearch result:")
                print(f"\n{poi_name}, {poi_type}")
                print(f"\n{poi_description}")
            else:
                print(f"\nPOI Not Found")
            break
                                   
def add_poi():
    new_poi = {}
    with open(file_name, "r") as poi_file:
        new_data = json.load(poi_file)
        
    new_poi["name"] = input("Name of poi: ")
    new_poi["type"] = input("Type of poi: ")
    new_poi["description"] = input("POI Description: ")
    new_data.append(new_poi)
    with open(file_name, "w") as poi_file:
        json.dump(new_data, poi_file, indent=4)
        
def delete_poi():
    view_poi()
    new_data = []
    
    with open(file_name, "r") as poi_file:
        data = json.load(poi_file)
        data_length = len(data) - 1
        
    print("Select POI index Number to delete")
    
    del_option = input(f"Choose a number between 0 and {data_length}: ")
    index = 0
    for entry in data:
        if index == int(del_option):
            index = index + 1
        else:
            new_data.append(entry)
            index = index + 1
    with open(file_name, "w") as poi_file:
        json.dump(new_data, poi_file, indent=4)
        
def poi_enquiry():
    view_poi()
    with open(file_name, "r") as poi_file:
        data = json.load(poi_file)
        
        location_name = input("\nName of POI to make enquiry: ")
        for entry in data:
            if location_name in entry.values():
                print(f"\nState Your Enquiry:")
                
                print(f"\n(1) What type of beverages does your offer")
                print(f"\n(2) Does your restaurant offer vegan or gluten-free food?")
                print(f"\n(3) What are your open/close? time")
                print(f"\n(4) Does Pub/Bar offer non-alcoholic drinks?")
            
                request = input("\nEnter request number: ")
                if request == "1":
                    print("\nEnquiry Recieved")
                    return (f"What type of beverages does your offer")
                elif request == "2":
                    print("\nEnquiry Recieved")
                    return (f"Does your restaurant offer vegan or gluten-free food?")
                elif request == "3":
                    print("\nEnquiry Recieved")
                    return (f"What are your open/close? time")
                elif request == "4":
                    print("\nEnquiry Recieved")
                    return (f"Does Pub/Bar offer non-alcoholic drinks?")
                else:
                    print("\nUnknown Request")
        
while True:
    options_menu()
    option = input("\nEnter Number: ")
    if option == "1":
        view_poi()
    elif option == "2":
        poi_search()
    elif option == "3":
        add_poi()
    elif option == "4":
        delete_poi()
    elif option == "5":
        poi_enquiry()
    elif option == "6":
        break
    else:
        print("Unknown option, You did not enter a number")