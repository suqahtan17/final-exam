
products=[
    ["1-Eid Mubarak: ",350.75,"SAR"],
    ["2-Men Gift Box: ",450.75,"SAR"],
    ["3-Anniversary/Love Gift Box: ",550.75,"SAR"],
    ["4-Winter Gift Box: ",300.75,"SAR"],
    ["5-Chocolate Gift Box: ",150.75,"SAR"],
    ["6-Newborn Gift Box: ",330.75,"SAR"]
]
for i in products:
    for x in i:
        print(x , end=" ")
    print()
message=int(input("Choose the product number: "))
index=message -1
if 0 <= index < len(products):
    price = products[index][1]
    total_price = price + (price * 0.15)
    print("Price including VAT 15% is:", total_price, "SAR")
else:
    print("Error: Product number out of range! Please choose from 1 to", len(products))