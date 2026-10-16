import os
import sys

info_count, warning_count, error_count=0,0,0                                                                
errors={}

if len(sys.argv)<2:
    print("Usage: python3 log_analyzer.py <log_directory>")
    sys.exit(1)

log_directory=sys.argv[1]

if not os.path.isdir(log_directory):
    print("Directory does not exist:", log_directory)
    sys.exit(1)

for root, directories, files in os.walk(log_directory):
    
    for file in files:
        if file.endswith(".log"):
            path=os.path.join(root, file)

            with open(path, "r") as log_file:

                for line in log_file:
                    
                    parts=line.split()
                    message=" ".join(parts[3:])
                    
                    if "INFO" in line:
                        info_count+=1
    
                    elif "WARNING" in line:
                        warning_count+=1
                        
                    elif "ERROR" in line:
                        
                        if message  not in errors:
                           errors[message]=1
                           
                        else:
                            errors[message]+=1
                            
                        error_count+=1
    

print(f"INFO: {info_count}\nWARNING: {warning_count}\nERROR: {error_count}")
print("=====ERROR SUMMARY=====")

highest_count=0

for key, value in errors.items():
    print(f"{key}: {value}")
    if value>highest_count:
        highest_count=value

print("=====Most Frequent Errors=====")

if len(errors)==0:
    print("There are no errors")          

else:
    for key, value in errors.items():
        if value==highest_count:
            print(key,":",value,"\n")

