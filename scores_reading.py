import csv
import logging
import os

# define variable for files and folders
folder_name = "logs"
filename="logs/app.log"

# We need to confirm if the logs folder already exist else we create
os.makedirs(folder_name, exist_ok=True)

# setup logging configurations
logging.basicConfig(
    filename=filename,              # Log file name
    level=logging.DEBUG,             # Log all levels DEBUG and above
    format="%(asctime)s - %(levelname)s - %(message)s" # Format for logging
)

# define the function
def average_score(file_path):
    # define our variables with defaults values to initialize them
    total_score = 0
    number_of_student = 0
    
    # gracefully handle the operation to avoid fatal crashes
    try:
        # take file handling into context "with"
        with open(file_path, "r") as file:
            # read the processed file from the context and pass into the csv reader (parser) and variable
            processedFile = csv.reader(file)

            # run a  loop to iterate all the rows in the csv
            for row in processedFile:
                # attempt to remove the first row which is the column names
                if(row[0] == "Name" ):
                    continue # helps to skip the first row
                # print(row)
                
                # increment actions to increase score per row and the student count per iteration
                total_score += float(row[1])
                number_of_student += 1
                
        # gracefully handle our average calculation
        try:
            # raise an error when there are no student records in the file
            if(total_score == 0):
                raise ValueError("No student record found") #raising the error
            
            # the actual average calculation
            average_score = total_score/number_of_student
            # log the results in a format
            logging.info(f"The total scores is {total_score} and the number of students is {number_of_student}.\n The average score is {average_score}")
            return average_score #return the result to the calling point.
        
        # capture, log and return our zero error in case we have it
        except ZeroDivisionError:
            logging.error("File not found")
            return None
        
        # capture, log and return our custom raised value error
        except ValueError as error:
            logging.error(error)
            return error
        
    # capture, log and return the file not found error if the file is missing
    except FileNotFoundError as error:
        logging.error(error)
        return None

# call the function in a print
print(average_score("scores.csv"))