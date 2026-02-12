# Must complete decode

from pathlib import Path

def encode(word):
    result = []
    for letter in word.upper():
        if letter == " ":
            result.append("00")
        elif letter.isalpha():
            result.append(f"{ord(letter)-64:02d}")
        elif letter.isdigit():
            result.append(f"{ord(letter)-21:02d}")
    return "".join(result)

def decode(word):
    result = []
    for i in range(0, len(word), 2):
        pair = word[i:i+2]
        if pair == "00":
            result.append(" ")
        elif int(pair)<=26:
            result.append(chr(int(pair) + 64))
        else:
            result.append(chr(int(pair) + 21))
    return "".join(result)

def get_from_file(file_name):
    path = Path(file_name)
    if not path.exists():
        return None
    return path.read_text().strip()

while True:
    choice = int(input("What do you want to perform ?\n1. Convert Alphabet String\n2. Convert Coded String\n3. Exit\n"))
    
    match choice:
        case 1:

            ip_mode = int(input("How do you want to input ?\n1. Through CLI\n2. From File\n"))
            match ip_mode:

                case 1:
                    string = input("Enter any word: ")
                    op = encode(string)
                    print(f"Encoded Word: {op}")

                case 2:
                    file_name = input("Enter the file name where the ip exists: ")
                    file_content = get_from_file(file_name)
                    if file_content is None:
                        print("The entered file doesn't exist in CWD.")
                    elif not file_content:
                        print("The file is empty.")
                    else:
                        op = encode(file_content)
                        print(f"Encoded Word: {op}")

        case 2:

            ip_mode = int(input("How do you want to input ?\n1. Through CLI\n2. From File\n"))
            match ip_mode:

                case 1:
                    string = input("Enter any word: ")
                    op = decode(string)
                    print(f"Encoded Word: {op}")

                case 2:
                    file_name = input("Enter the file name where the ip exists: ")
                    file_content = get_from_file(file_name)
                    if file_content is None:
                        print("The entered file doesn't exist in CWD.")
                    elif not file_content:
                        print("The file is empty.")
                    else:
                        op = decode(file_content)
                        print(f"Decoded Word: {op}")

        case 3:
            print("Babaaiiii")
            break

        case _:
            print("Please choose a valid option\n")