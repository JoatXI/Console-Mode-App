def delete_poi(file_name, line_number):
    with open(file_name) as file:
        lines = file.readlines()
        
    if line_number <= len(lines):
        del lines[line_number -1]
        
        with open(file_name, "w") as file:
            for line in lines:
                file.write(line)
        
    else:
        print("line", line_number, "not in")
        
    print(lines)
        
delete_poi("poi.csv", 3)