import read_from_file_and_net as rfn

my_url = "https://markfoley.info/pa1/gettysburg.txt"

url_data = rfn.get_file_from_net(my_url)

print(f"{url_data}")

my_file = ".cache/utf-8.txt"

my_file_data = rfn.read_any_file(my_file)

print(f"{my_file_data}")