def consultation_charges(amount):
    return amount


def laboratory_charges(amount):
    return amount


def medicine_charges(amount):
    return amount


def room_charges(days, daily_rate):
    return days * daily_rate


def final_bill(consultation, laboratory, medicine, room, category="regular"):
    total = consultation + laboratory + medicine + room
    discounts = {"regular": 0, "senior": 10, "insurance": 20}
    discount = discounts.get(category, 0)
    return total - total * discount / 100



consultation = consultation_charges(500)
laboratory = laboratory_charges(1200)
medicine = medicine_charges(800)
room = room_charges(3, 1500)
print(final_bill(consultation, laboratory, medicine, room, "senior"))
