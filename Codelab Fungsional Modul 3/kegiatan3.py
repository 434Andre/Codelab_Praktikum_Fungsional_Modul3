import random

# Membuat daftar acak yang berisi nilai int, float, dan string
random_list = [1, 2.7, "Hello", 3, "World", 4.7, 5.5, "AI"]

# Memisahkan nilai float, int, dan string
float_values = list(filter(lambda x: isinstance(x, float), random_list))
int_values = list(filter(lambda x: isinstance(x, int), random_list))
string_values = list(filter(lambda x: isinstance(x, str), random_list))

print("Data Float:")
print(tuple(float_values))

print("Data Int:")
# Menggunakan map() untuk memproses nilai integer
def process_integer(value):
    units = value % 10
    tens = (value // 10) % 10
    hundreds = (value // 100) % 10
    return {'ratusan': hundreds, 'puluhan': tens, 'satuan': units}

int_data = list(map(process_integer, int_values))

for data in int_data:
    print(data)

print("Data String:")
print(string_values)
