from pathlib import Path

def encode(ip):
    op = []
    for chr in ip.upper():
        if chr.isspace():
            op.append("00")
        elif chr.isalpha():
            op.append(f"{ord(chr)-64:02d}")
        elif chr.isdigit():
            op.append(f"{ord(chr)-21:02d}")
    return "".join(op)

def decode(ip):
    op = []
    for i in range(0, len(ip), 2):
        pair = ip[i:i+2]
        if pair == "00":
            op.append(" ")
        elif int(pair)<=26:
            op.append(chr(int(pair) + 64))
        else:
            op.append(chr(int(pair) + 21))
    return "".join(op)

def get_from_file(file_name):
    path = Path(file_name)
    if not path.exists():
        return None
    return path.read_text().strip()


print("Hellowwww")

while True:
    choice = int(input("What do you want to perform ?\n1. Encode\n2. Decode\n3. Exit\n"))
    
    match choice:
        case 1:

            ip_mode = int(input("How do you want to input ?\n1. Through CLI\n2. From File\n"))
            match ip_mode:

                case 1:
                    string = input("IP anything you want to encode: ")
                    op = encode(string)
                    print(f"Encoded OP: {op}")

                case 2:
                    file_name = input("Enter the file name where ur IP exists: ")
                    file_content = get_from_file(file_name)
                    if file_content is None:
                        print("The entered file doesn't exist in CWD.")
                    elif not file_content:
                        print("The file is empty.")
                    else:
                        op = encode(file_content)
                        print(f"Encoded IP: {op}")

        case 2:

            ip_mode = int(input("How do you want to input ?\n1. Through CLI\n2. From File\n"))
            match ip_mode:

                case 1:
                    string = input("IP anything you want to decode: ")
                    op = decode(string)
                    print(f"Decoded OP: {op}")

                case 2:
                    file_name = input("Enter the file name where the ip exists: ")
                    file_content = get_from_file(file_name)
                    if file_content is None:
                        print("The entered file doesn't exist in CWD.")
                    elif not file_content:
                        print("The file is empty.")
                    else:
                        op = decode(file_content)
                        print(f"Decoded IP: {op}")

        case 3:
            print("Babaaiiii")
            break

        case _:
            print("Please choose a valid option\n")