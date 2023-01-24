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
    print("\n(6) Answer Enquiries")
    print("\n(7) Exit")
    
def view_poi():
    with open(file_name, "r") as poi_file:
        data = json.load(poi_file)
        index = 0
        
        for entry in data:
            poi_name = entry["poi_name"]
            
            print(f"\nIndex Number: {index}")
            print(f"POI Name: {poi_name}")
            print("\n")
            index = index + 1

def poi_search():
    with open(file_name, "r") as poi_file:
        data = json.load(poi_file)
        user_search = input("Enter POI name to search: ")
        index = 0

        for i in data:
            poi_name = i["poi_name"]
            poi_type = i["poi_type"]
            poi_description = i["poi_description"]
            
            if user_search == poi_name:
                print(f"{poi_name}, {poi_type}")
                print(f"\n{poi_description}")
                index = index + 1
                                   
def add_poi():
    new_poi = {}
    with open(file_name, "r") as poi_file:
        new_data = json.load(poi_file)
        
    new_poi["poi_name"] = input("Name of poi: ")
    new_poi["poi_type"] = input("Type of poi: ")
    new_poi["poi_description"] = input("POI Description: ")
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
        
        poi_name = input("\nName of POI to make enquiry: ")
        for entry in data:
            if poi_name in entry.values():
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
                    enquiry_data.append(poi_name)
                    enquiry_data.append(faq1)
                elif request == "2":
                    print("\nEnquiry Recieved")
                    enquiry_data.append(poi_name)
                    enquiry_data.append(faq2)
                elif request == "3":
                    print("\nEnquiry Recieved")
                    enquiry_data.append(poi_name)
                    enquiry_data.append(faq3)
                elif request == "4":
                    print("\nEnquiry Recieved")
                    enquiry_data.append(poi_name)
                    enquiry_data.append(faq4)
                else:
                    print("\nUnknown Request")

        with open(text_file, "a+") as enquiry_file:
            enquiry_file.seek(0)
            data = enquiry_file.read(100)
            
            if len(data) > 0:
                enquiry_file.write("\n")
            enquiry_file.writelines(str(enquiry_data))
            
def answer_enquiry():
    with open(text_file, "r") as enquiry_file:
        data = enquiry_file.readlines()
        i = 1
        
        for line in data:
            print(f"\nEnuiry Number: {i}")
            print(line)
            i = i + 1
        
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
        answer_enquiry()
    elif option == "7":
        break
    else:
        print("Unknown option, You did not enter a number")