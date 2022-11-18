bill=float(input("bill:"))
tip=int(input("tip ? 10, 12 or 15 :"))
people=int(input("people to split the bill :"))

tip_percent=tip/100

total_tip_amount= bill * tip_percent

total_bill= bill + total_tip_amount

bill_per_person= total_bill / people

final_amount=round(bill_per_person ,2)

print(final_amount)