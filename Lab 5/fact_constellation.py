class DimDate:
    def __init__(self, date_id, date):
        self.date_id = date_id
        self.date = date

class DimProduct:
    def __init__(self, product_id, name, cost_price, selling_price):
        self.product_id = product_id
        self.name = name
        self.cost_price = cost_price
        self.selling_price = selling_price

class DimArea:
    def __init__(self, area_id, street, city, state, country):
        self.area_id = area_id
        self.street = street
        self.city = city
        self.state = state
        self.country = country

class DimRetailer:
    def __init__(self, retailer_id, name, area_id):
        self.retailer_id = retailer_id
        self.name = name
        self.area_id = area_id

class DimSupplier:
    def __init__(self, supplier_id, name, area_id):
        self.supplier_id = supplier_id
        self.name = name
        self.area_id = area_id

class FactPurchases:
    def __init__(self, product_id, date_id, supplier_id, buyer_id, units_purchased):
        self.product_id = product_id
        self.date_id = date_id
        self.supplier_id = supplier_id
        self.buyer_id = buyer_id
        self.units_purchased = units_purchased

class FactSales:
    def __init__(self, product_id, date_id, retailer_id, units_sold):
        self.product_id = product_id
        self.date_id = date_id
        self.retailer_id = retailer_id
        self.units_sold = units_sold

def main():
    print('----------DimDate Table----------\n')
    dates = []
    entries = int(input('Number of Entries: '))
    for i in range(entries):
        print('\nDate '+str(i+1)+':')
        while True:
            id = input("\tID: ")
            loop = False
            for date in dates:
                if date.date_id == id:
                    print("\tID already exists!")
                    loop = True
                    break
            if not loop:
                break

        date = input("\tDate: ")
        dates.append(DimDate(id, date))

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

    print('\n----------DimArea Table----------\n')
    areas = []
    entries = int(input('Number of Entries: '))
    for i in range(entries):
        print('\nArea '+str(i+1)+':')
        while True:
            id = input("\tID: ")
            loop = False
            for area in areas:
                if area.area_id == id:
                    print("\tID already exists!")
                    loop = True
                    break
            if not loop:
                break
        street = input("\tStreet: ")
        city = input("\tCity: ")
        state = input("\tState: ")
        country = input("\tCountry: ")
        areas.append(DimArea(id, street, city, state, country))

    print('\n----------DimSupplier Table----------\n')
    suppliers = []
    entries = int(input('Number of Entries: '))
    for i in range(entries):
        print('\nSupplier '+str(i+1)+':')
        while True:
            id = input("\tID: ")
            loop = False
            for supplier in suppliers:
                if supplier.supplier_id == id:
                    print("\tID already exists!")
                    loop = True
                    break
            if not loop:
                break
        name = input("\tName: ")
        area_id = input("\tArea ID: ")
        suppliers.append(DimSupplier(id, name, area_id))

    print('\n----------DimRetailer Table----------\n')
    retailers = []
    entries = int(input('Number of Entries: '))
    for i in range(entries):
        print('\nRetailer '+str(i+1)+':')
        while True:
            id = input("\tID: ")
            loop = False
            for retailer in retailers:
                if retailer.retailer_id == id:
                    print("\tID already exists!")
                    loop = True
                    break
            if not loop:
                break
        name = input("\tName: ")
        area_id = input("\tArea ID: ")
        retailers.append(DimRetailer(id, name, area_id))

    print('\n----------FactPurchases Table----------\n')
    purchases = []
    entries = int(input('Number of Entries: '))
    for i in range(entries):
        print('\nSale '+str(i+1)+':')
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
        while True:
            date_id = input("\tDate ID: ")
            loop = True
            for date in dates:
                if date.date_id == date_id:
                    loop = False
                    break
            if not loop:
                break
            else:
                print("\tNo such DimDate entry found!")
        while True:
            supplier_id = input("\tSupplier ID: ")
            loop = True
            for supplier in suppliers:
                if supplier.supplier_id == supplier_id:
                    loop = False
                    break
            if not loop:
                break
            else:
                print("\tNo such DimSupplier entry found!")
        while True:
            buyer_id = input("\tBuyer ID: ")
            loop = True
            for buyer in retailers:
                if buyer.retailer_id == buyer_id:
                    loop = False
                    break
            if not loop:
                break
            else:
                print("\tNo such DimRetailer entry found!")
        units_purchased = input("\tUnits Purchased: ")
        purchases.append(FactPurchases(product_id, date_id, supplier_id, buyer_id, units_purchased))

    print('\n----------FactSales Table----------\n')
    sales = []
    entries = int(input('Number of Entries: '))
    for i in range(entries):
        print('\nSale '+str(i+1)+':')
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
        while True:
            date_id = input("\tDate ID: ")
            loop = True
            for date in dates:
                if date.date_id == date_id:
                    loop = False
                    break
            if not loop:
                break
            else:
                print("\tNo such DimDate entry found!")
        while True:
            retailer_id = input("\tRetailer ID: ")
            loop = True
            for retailer in retailers:
                if retailer.retailer_id == retailer_id:
                    loop = False
                    break
            if not loop:
                break
            else:
                print("\tNo such DimRetailer entry found!")
        units_sold = input("\tUnits Sold: ")
        sales.append(FactSales(product_id, date_id, retailer_id, units_sold))

    print("\n\nDimDate Entries:")
    for date in dates:
        print('{0:5} {1:10}'.format(date.date_id, date.date))
    print("\nDimProduct Entries:")
    for product in products:
        print('{0:5} {1:15} {2:10} {3:10}'.format(product.product_id, product.name, product.cost_price, product.selling_price))
    print("\nDimArea Entries:")
    for area in areas:
        print('{0:5} {1:15} {2:15} {3:15} {4:15}'.format(area.area_id, area.street, area.city, area.state, area.country))
    print("\nDimRetailer Entries:")
    for retailer in retailers:
        print('{0:5} {1:20} {2:5}'.format(retailer.retailer_id, retailer.name, retailer.area_id))
    print("\nDimSupplier Entries:")
    for supplier in suppliers:
        print('{0:5} {1:15} {2:5}'.format(supplier.supplier_id, supplier.name, supplier.area_id))
    print("\nFactPuchases Entries:")
    for purchase in purchases:
        print('{0:5} {1:5} {2:5} {3:5} {4:10}'.format(purchase.product_id, purchase.date_id, purchase.supplier_id, purchase.buyer_id, purchase.units_purchased))
    print("\nFactSales Entries:")
    for sale in sales:
        print('{0:5} {1:5} {2:5} {3:10}'.format(sale.product_id, sale.date_id, sale.retailer_id, sale.units_sold))

if __name__ == "__main__":
    main()