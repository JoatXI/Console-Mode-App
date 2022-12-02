import json
file_name = "./data/poi.json"

def options_menu():
    print(" ")
    print("Points Of Interest(POIs)")
    print(" ")
    print("Select Option:")
    print(" ")
    print("(1) View POIs")
    print(" ")
    print("(2) POI Search")
    print(" ")
    print("(3) Add POI")
    print(" ")
    print("(4) Delete POI")
    print(" ")
    print("(5) POI Enquiry")
    print(" ")
    print("(6) Exit")
    print(" ")
    
def view_poi():
    with open(file_name, "r") as poi_file:
        data = json.load(poi_file)
        index = 0
        
        for entry in data:
            poi_name = entry["poi_name"]
            
            print(" ")
            print(f"Index Number {index}")
            print(f"Name of POI: {poi_name}")
            print("\n")
            index = index + 1

def poi_search():
    with open(file_name, "r") as poi_file:
        data = json.load(poi_file)
        
    start = 0
    end = len(data) - 1
    user_search = input("Enter POI name to search: ")
    
    while start <= end:
        middle = (start + end)// 2
        midpoint = data[middle]
        if midpoint > user_search:
            end = middle - 1
        elif midpoint < user_search:
            start = middle + 1
        else:
            return midpoint
        
        data.sort()
                            
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
    
    del_option = input(f"Select a number between 0 and {data_length}: ")
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
    with open(file_name, "r") as poi_file:
        data = json.load(poi_file)
        
        for entry in data:
            entry["poi_name"] = input("Which POI do you want to make an enquiry: ")
            print(f"\nState your enquiry")
            
            user_enquiry = input("Enter enquiry: ")
            request = ["vegan", "beverage", "close", "alcohol", "gluten"]
            
            for entry in request:
                poi_name = entry["poi_name"]
                poi_type = entry["poi_type"]
                poi_description = entry["poi_description"]
                if user_enquiry in request:
                    print(poi_name)
                    print(poi_type)
                    print(poi_description)
                else:
                    print("Sorry we do not offer this request")
                break
        
        
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