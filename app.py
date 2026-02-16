from flask import Flask, render_template

app = Flask(__name__)

MENU = [
    {
        "id": "happy-hour",
        "label": "HAPPY HOUR",
        "hours": "Tuesday - Friday 2:30 - 6:00pm",
        "accent": "#9a5a43",
        "columns": [
            {
                "title": "LIBATIONS",
                "items": [
                    {"name": "ALL WINE (6 OZ.)", "desc": "$2 off house wine", "price": "8"},
                    {"name": "DRAFT BEERS", "desc": "rotating local taps", "price": "8"},
                    {"name": "SPECIALTY COCKTAILS", "desc": "seasonal margarita + paloma", "price": "12"},
                    {"name": "BARREL AGED COCKTAILS", "desc": "old fashioned, aged in-house", "price": "12"},
                ],
            },
            {
                "title": "SWEETS!",
                "items": [
                    {"name": "BREAD PUDDING", "desc": "brioche, vanilla custard, caramel-bourbon sauce", "price": "9"},
                    {"name": "CHOCOLATE LAVA CAKE", "desc": "molten center, vanilla bean ice cream", "price": "11"},
                    {"name": "PEACH COBBLER PARFAIT", "desc": "warm peach compote, pecan crunch, salted caramel", "price": "10"},
                ],
            },
        ],
    },
    {
        "id": "lunch",
        "label": "LUNCH",
        "hours": "Daily 11:00am - 3:00pm",
        "accent": "#2f6f5e",
        "columns": [
            {
                "title": "TACOS",
                "items": [
                    {"name": "TACO AL VAPOR", "desc": "steamed tortilla, salsa roja, onion + cilantro", "price": "3"},
                    {"name": "BARBACOA TACO", "desc": "slow-cooked beef, lime, cilantro", "price": "4"},
                    {"name": "CARNITAS TACO", "desc": "crispy pork, pico de gallo", "price": "4"},
                ],
            },
            {
                "title": "PLATES",
                "items": [
                    {"name": "TACO PLATE (3)", "desc": "choice of protein, rice + beans", "price": "14"},
                    {"name": "BURRITO", "desc": "protein, rice, beans, salsa, crema (optional)", "price": "13"},
                    {"name": "QUESADILLA", "desc": "melty cheese, pico, salsa verde", "price": "11"},
                ],
            },
        ],
    },
    {
        "id": "brunch",
        "label": "BRUNCH",
        "hours": "Sat - Sun 9:00am - 2:00pm",
        "accent": "#7a4aa8",
        "columns": [
            {
                "title": "BRUNCH FAVORITES",
                "items": [
                    {"name": "CHILAQUILES", "desc": "chips, salsa roja, crema, queso, eggs", "price": "15"},
                    {"name": "HUEVOS RANCHEROS", "desc": "fried eggs, ranchero salsa, beans, tortillas", "price": "14"},
                    {"name": "BREAKFAST TACOS (3)", "desc": "eggs, potato, cheese, salsa verde", "price": "13"},
                ],
            },
            {
                "title": "SIDES",
                "items": [
                    {"name": "FRUIT CUP", "desc": "seasonal fruit, tajín + lime", "price": "6"},
                    {"name": "PAPAS", "desc": "crispy breakfast potatoes", "price": "5"},
                    {"name": "PAN DULCE", "desc": "rotating sweet bread", "price": "4"},
                ],
            },
        ],
    },
    {
        "id": "dinner",
        "label": "DINNER",
        "hours": "Daily 5:00pm - 9:30pm",
        "accent": "#0e5aa7",
        "columns": [
            {
                "title": "SPECIALS",
                "items": [
                    {"name": "BIRRIA TACOS (3)", "desc": "crispy birria, consomé for dipping", "price": "17"},
                    {"name": "CARNE ASADA PLATE", "desc": "grilled steak, rice, beans, tortillas", "price": "20"},
                    {"name": "AL PASTOR TACOS (3)", "desc": "marinated pork, pineapple, onion + cilantro", "price": "16"},
                ],
            },
            {
                "title": "APPETIZERS",
                "items": [
                    {"name": "GUAC + CHIPS", "desc": "fresh avocado, pico, lime", "price": "10"},
                    {"name": "ELOTE", "desc": "street corn, crema, cotija, chile", "price": "8"},
                    {"name": "NACHOS", "desc": "beans, cheese, salsa, jalapeños", "price": "12"},
                ],
            },
        ],
    },
    {
        "id": "desserts",
        "label": "DESSERTS",
        "hours": "All day",
        "accent": "#b23a48",
        "columns": [
            {
                "title": "SWEETS!",
                "items": [
                    {"name": "CHURROS", "desc": "cinnamon sugar, chocolate dip", "price": "7"},
                    {"name": "FLAN", "desc": "classic caramel custard", "price": "8"},
                    {"name": "TRES LECHES", "desc": "milk cake, whipped cream", "price": "9"},
                ],
            },
            {
                "title": "EXTRAS",
                "items": [
                    {"name": "ICE CREAM", "desc": "vanilla or chocolate", "price": "6"},
                    {"name": "CAFÉ DE OLLA", "desc": "cinnamon coffee", "price": "5"},
                    {"name": "HOT CHOCOLATE", "desc": "mexican-style, lightly spiced", "price": "5"},
                ],
            },
        ],
    },
    {
        "id": "drinks",
        "label": "DRINKS",
        "hours": "All day",
        "accent": "#c57f17",
        "columns": [
            {
                "title": "REFRESHERS",
                "items": [
                    {"name": "HORCHATA", "desc": "rice milk, cinnamon, vanilla", "price": "5"},
                    {"name": "JAMAICA", "desc": "hibiscus iced tea", "price": "5"},
                    {"name": "TAMARINDO", "desc": "tamarind agua fresca", "price": "5"},
                ],
            },
            {
                "title": "CLASSICS",
                "items": [
                    {"name": "MEXICAN SODA", "desc": "Jarritos (assorted)", "price": "4"},
                    {"name": "SPARKLING WATER", "desc": "lime or plain", "price": "3"},
                    {"name": "ICED TEA", "desc": "unsweetened", "price": "3"},
                ],
            },
        ],
    },
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html', sections=MENU)

if __name__ == '__main__':
    app.run(debug=True)
