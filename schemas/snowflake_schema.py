class DimCity:
    def __init__(self, city_id, city, state, country):
        self.city_id = city_id
        self.city = city
        self.state = state
        self.country = country

class DimLocation:
    def __init__(self, location_id, street, city_id):
        self.location_id = location_id
        self.street = street
        self.city_id = city_id

class DimProduct:
    def __init__(self, product_id, name, cost_price, selling_price):
        self.product_id = product_id
        self.name = name
        self.cost_price = cost_price
        self.selling_price = selling_price

class FactSales:
    def __init__(self, location_id, product_id, units_sold, rupees_sold):
        self.location_id = location_id
        self.product_id = product_id
        self.units_sold = units_sold
        self.rupees_sold = rupees_sold

def main():
    print('----------DimCity Table----------\n')
    cities = []
    entries = int(input('Number of Entries: '))
    for i in range(entries):
        print('\nCity '+str(i+1)+':')
        while True:
            id = input("\tID: ")
            loop = False
            for city in cities:
                if city.city_id == id:
                    print("\tID already exists!")
                    loop = True
                    break
            if not loop:
                break
        city = input("\tCity: ")
        state = input("\tState: ")
        country = input("\tCountry: ")
        cities.append(DimCity(id, city, state, country))

    print('\n----------DimLocation Table----------\n')
    locations = []
    entries = int(input('Number of Entries: '))
    for i in range(entries):
        print('\nLocation '+str(i+1)+':')
        while True:
            id = input("\tID: ")
            loop = False
            for location in locations:
                if location.location_id == id:
                    print("\tID already exists!")
                    loop = True
                    break
            if not loop:
                break
        street = input("\tStreet: ")
        city_id = input("\tCity ID: ")
        locations.append(DimLocation(id, street, city_id))

    print('\n----------DimProduct Table----------\n')
    products = []
    entries = int(input('Number of Entries: '))
    for i in range(entries):
        print('\nProduct '+str(i+1)+':')
        while True:
            id = input("\tID: ")
            loop = False
            for product in products:
                if product.product_id == id:
                    print("\tID already exists!")
                    loop = True
                    break
            if not loop:
                break
        name = input("\tName: ")
        cost_price = input("\tCost Price: ")
        selling_price = input("\tSelling Price: ")
        products.append(DimProduct(id, name, cost_price, selling_price))

    print('\n----------FactSales Table----------\n')
    sales = []
    entries = int(input('Number of Entries: '))
    for i in range(entries):
        print('\nSale '+str(i+1)+':')
        while True:
            location_id = input("\tLocation ID: ")
            loop = True
            for location in locations:
                if location.location_id == location_id:
                    loop = False
                    break
            if not loop:
                break
            else:
                print("\tNo such DimLocation entry found!")
        while True:
            product_id = input("\tProduct ID: ")
            loop = True
            for product in products:
                if product.product_id == product_id:
                    loop = False
                    break
            if not loop:
                break
            else:
                print("\tNo such DimProduct entry found!")
        units_sold = input("\tUnits Sold: ")
        rupees_sold = input("\tRupees Sold: ")
        sales.append(FactSales(location_id, product_id, units_sold, rupees_sold))

    print("\n\nDimCity Entries:")
    for city in cities:
        print(city.city_id+"\t"+city.city+"\t\t\t"+city.state+"\t\t\t"+city.country)
    print("\n\nDimLocation Entries:")
    for location in locations:
        print(location.location_id+"\t"+location.street+"\t\t\t"+location.city_id)
    print("\nDimProduct Entries:")
    for product in products:
        print(product.product_id+"\t"+product.name+"\t\t\t"+product.cost_price+"\t"+product.selling_price)
    print("\nFactSales Entries:")
    for sale in sales:
        print(sale.location_id+"\t"+sale.product_id+"\t"+sale.units_sold+"\t"+sale.rupees_sold)

if __name__ == "__main__":
    main()