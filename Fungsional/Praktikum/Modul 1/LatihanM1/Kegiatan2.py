# pisahkan antara nilai int, float, dan string dengan ketentuan :
random_list = [105, 3.1, "Hello", 737, "Phyton", 2.7, "World", 412, 5.5, "AI"]
# - Data float disimpan dalam bentuk tuple
# - Data string disimpan ke dalam list
# - Dan data int disimpan dalam dictionary dengan memisahkan angka satuan, puluhan, dan ratusan

int_dict = {}
float_tuple = ()
string_list = []

for item in random_list:
    if isinstance(item, int):
        # Memisahkan angka satuan, puluhan, dan ratusan
        satuan = item % 10
        puluhan = (item // 10) % 10
        ratusan = item // 100
        
        # Menyimpan dalam dictionary
        int_dict[item] = (ratusan, puluhan, satuan)
    elif isinstance(item, float):
        # Menyimpan dalam tuple
        float_tuple += (item,)
    elif isinstance(item, str):
        # Menyimpan dalam list
        string_list.append(item)

print("Integer Dictionary:", int_dict)
print("Float Tuple:", float_tuple)
print("String List:", string_list)