import json
file_name = "./data/poi.json"
text_file = "./data/enquiry.txt"

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
    poi_sorting("poi_name")
    with open(file_name, "r") as poi_file:
        data = json.load(poi_file)
        index = 0
        
        for entry in data:
            poi_name = entry["poi_name"]
            
            print(f"\nIndex Number: {index}")
            print(f"Name of POI: {poi_name}")
            print("\n")
            index = index + 1

def poi_search():
    with open(file_name, "r") as poi_file:
        data = json.load(poi_file)
        
        for entry in data:
            poi_name = entry["poi_name"]
            
            user_search = input("Enter POI name to search: ")
            if user_search in entry:
                print(f"\n{poi_name}")
            else:
                print("POI Not Found")
                
                                   
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
    enquiry_data = []
    
    with open(file_name, "r") as poi_file:
        data = json.load(poi_file)
        
        location_name = input("\nName of POI to make enquiry: ")
        for entry in data:
            if location_name in entry.values():
                print(f"\nState Your Enquiry:")
                
                faq1 = "(1) What types of beverages does you offer"
                faq2 = "(2) Does your restaurant offer vegan or gluten-free food?"
                faq3 = "(3) What are your open/close time?"
                faq4 = "(4) Does Pub/Bar offer non-alcoholic drinks?"
                
                print(f"\n{faq1}")
                print(f"\n{faq2}")
                print(f"\n{faq3}")
                print(f"\n{faq4}")
            
                request = input("\nEnter request number: ")
                if request == "1":
                    print("\nEnquiry Recieved")
                    return faq1
                elif request == "2":
                    print("\nEnquiry Recieved")
                    return faq2
                elif request == "3":
                    print("\nEnquiry Recieved")
                    return faq3
                elif request == "4":
                    print("\nEnquiry Recieved")
                    return faq4
                else:
                    print("\nUnknown Request")
                    enquiry_data.append(entry)
        with open(text_file, "w") as f:
            f.write(enquiry_data)
                    
                    
def poi_sorting(key):
    with open(file_name, "r") as poi_file:
        data = json.load(poi_file)
        
        for i in range(len(data) - 1, 0, -1):
            for j in range(i):
                if data[j][key] > data[j + 1][key]:
                    temp = data[j]
                    data[j] = data[j + 1]
                    data[j + 1] = temp
        return data
        
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