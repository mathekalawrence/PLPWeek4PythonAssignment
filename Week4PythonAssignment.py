import os

def process_file_with_error_handling():
    """
    The program asks the user for a file name, reads the contents, processes the text and writes the outcome to a novel file. It literally handles common file-realted errors

    """
    while True:
        #Prompting the user to enter the filename
        input_filename = input("Please enter the name of the input file with .txt extension: ")
        output_filename = "processed_" + os.path.basename(input_filename)

        #Exception handling
        try:
            #Read the input file contents
            with open(input_filename, 'r') as infile:
                original_text = infile.read()

            print(f"Confirmed!..Successfully read the file: {input.filename}")

            #Process the text
            modified_text = original_text.upper()

            #WRITE the modified content to a new file.
            with open(output_filename, 'w') as outfile:
                outfile.write(modified_text)

            print(f"The processed text was successfully written to: {output_filename}")
            print("Well done. Process complete!")

            #if successful, the loop has to be broken
            break

        except FileNotFoundError:
            #Handling the error if the file is non-existent
            print(f"Error got!: The document '{input_filename}' not found.")
            print("Please check the filename and try again now or later..")

        except IOError as e:
            #Handling other I/O errors..like permisssion errors
            print(f"Permission error (I/O) occurred: {e}")
            print("The program will restart. You may kindly try again.")

            