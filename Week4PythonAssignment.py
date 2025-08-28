import os

def process_file_with_error_handling():
    """
    The program asks the user for a file name, reads the contents, processes the text and writes the outcome to a novel file. It literally handles common file-realted errors

    """
    while True:
        #Prompting the user to enter the filename
        input_filename = input("Please enter the name of the input file with .txt extension: ")
        