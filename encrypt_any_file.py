from read_from_file_and_net import get_file_from_net as get_url

SEPARATOR_LINE = f"\n{'=' * 80}\n"


def encrypt(data, shift_key):
    encrypted_data = ""

    for char in data:
        encrypted_data += chr(ord(char) + shift_key)

    return encrypted_data


def write_encrypted_file(encrypted_file):
    with open(".cache/temp_encrypted", "w") as fh:
        fh.write(encrypted_file)


def main():
    try:
        url = input("Enter URL: ")
        encryption_key = int(input("Enter Shift Key -> Must be integer: "))

        data = get_url(url)
        encrypted_file = encrypt(data, encryption_key)
        decrypted_file = encrypt(encrypted_file, encryption_key * -1)
        write_encrypted_file(encrypted_file)

        print(f"\nSOURCE{SEPARATOR_LINE}{data}{SEPARATOR_LINE}\nENCRYPTED SOURCE{SEPARATOR_LINE}{encrypted_file}"
              f"{SEPARATOR_LINE}\nDECRYPTED SOURCE{SEPARATOR_LINE}{decrypted_file}{SEPARATOR_LINE}")

    except Exception as e:
        print(f"{e}")
        quit(1)


if __name__ == "__main__":
    main()
