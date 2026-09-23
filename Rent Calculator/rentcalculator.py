# ============================================
# Rent Calculator - Split shared expenses evenly
# among all flatmates/roommates
# ============================================

# --- Collect input from the user ---

# Monthly rent for the hostel/flat
rent = int(input("Enter your hostel/flat rent="))

# Total money spent on food/snacks for the group
food = int(input("Enter the amount of food ordered="))

# Total electricity units consumed this month
electricity_spend = int(input("Enter the total of electricity spend="))

# Cost charged per electricity unit (e.g. ₹/unit)
charge_per_unit = int(input("Enter the charge per unit="))

# Number of people sharing the flat/room
persons = int(input("Enter the number of persons living in room/flat="))

# --- Calculations ---

# Convert electricity units into actual rupee cost
total_bill = electricity_spend * charge_per_unit

# Add up all shared expenses (rent + food + electricity)
# then split equally among all persons.
# Note: uses integer division (//), so any remainder (paise/cents)
# is dropped rather than rounded.
output = (food + rent + total_bill) // persons

# --- Output ---

# Show how much each person owes
print("Each person will pay=", output)