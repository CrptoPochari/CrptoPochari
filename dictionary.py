foods = {'ramen':"拉麵", "pasta":"義大利麵"}
foods = {
    'ramen':"拉麵", 
    "pasta":"義大利麵"
}

# Add key should with = value
foods['tea'] = "茶"

print(foods["ramen"])


drinks1 = {
    "name": "麥香奶茶",
    "price": 10
}
drinks2 = {
    "name": "奶茶",
    "price": 30
}
drinks_menu = [drinks1, drinks2]
drinks_menu[0]['name'] # "麥香奶茶"
drinks_menu[1]['price'] # "30"