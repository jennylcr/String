# this program reads 10 product codes from a text file (A3 Codes.txt attached)
# and determines if each conforms to the rules

# define global variables
codes = []  # product codes list
invalid_codes = []  # invalid codes list
valid_codes = []  # valid codes list
invalid_restricted = []  # invalid restricted codes list


# this function reads product codes from the text file
def getCodes():
    try:
        # open the file
        file = open('A3 Codes.txt', 'r')
    except FileNotFoundError:
        # if the file does not exist, print the error
        print("File not found! \n")
    else:
        # for each lin in the file
        for line in file:
            # remove whitespace and add to the list
            codes.append(line.strip())
        # close the file
        file.close()


# this function validates codes
def validateCodes():
    try:
        # for each code in the list
        for code in codes:
            # split the product code by '-'
            current_code = code.split('-')
            # if the code is less than 10 characters, add to the invalid code list
            if len(current_code[0]) < 10:
                invalid_codes.append(code)
            # if position 4 through 7 of the code is not digit, add to the invalid code list
            elif not (current_code[0][3:7]).isdigit():
                invalid_codes.append(code)
            # if the character in the 10th position is not a capital letter or alphabetic letter, add to the invalid code list
            elif not current_code[0][9].isalpha() or not current_code[0][9].isupper():
                invalid_codes.append(code)
            # if all requirements meet, add to the valid code list
            else:
                valid_codes.append(code)
    # if the index does not exist, print the error
    except IndexError:
        print("IndexError in validateCodes function.")


# this function finds invalid restricted code
def validateRestrictedCodes():
    try:
        # for each code in the valid code list
        for code in valid_codes:
            # split the product code by '-'
            current_code = code.split('-')
            # if the security level is R and country code is 2000 or higher, add to the invalid restricted codes list
            if current_code[0][9] == 'R' and int(current_code[0][3:7]) >= 2000:
                invalid_restricted.append(code)
    # if the index does not exist, print the error
    except IndexError:
        print("IndexError in validateRestrictedCodes function.")


# the main function
def main():
    # get product codes
    getCodes()
    # validate codes
    validateCodes()
    # find invalid restricted codes
    validateRestrictedCodes()

    # display valid codes if any
    if len(valid_codes) > 0:
        # print valid codes header
        print("Valid Code(s) are: ")
        # print all valid codes, seperated by the newline character
        print(*valid_codes, sep="\n")

    # display invalid codes if any
    if len(invalid_codes) > 0:
        # print invalid code header
        print("\nInvalid Code(s) are: ")
        # print all invalid codes, seperated by the newline character
        print(*invalid_codes, sep="\n")

    # display invalid restricted codes if any
    if len(invalid_restricted) > 0:
        # print invalid restricted codes header
        print("\nInvalid Restricted Code(s) are: ")
        # print all invalid restricted codes, seperated by the newline character
        print(*invalid_restricted, sep="\n")


# call the main function
main()
