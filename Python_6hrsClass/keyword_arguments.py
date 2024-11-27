def hello(greeting, title, first_name, last_name):
    print(f"{greeting}, {title} {first_name} {last_name}")

#hello("Hello", "Mr.", "John", "Doe")
hello(greeting = "Hello", title = "Mr.", first_name = "TU", last_name = "TU") 
#PS:不可以改順序(hello(title = "Hello", greeting = "Mr.", first_name = "TU", last_name = "TU"))
#好處可以少輸入錯誤的風險


def get_phone(country_code, area_code, first, last):
    return f"+{country_code}-{area_code}-{first}-{last}"

print(str(get_phone(country_code = "886", area_code = "09", first = "605", last = "93551")))