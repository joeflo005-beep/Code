event_name = "Big Mouth Pizza"
cost = 65
service_charge = cost * .2
group_size = 5
grand_total = cost + service_charge
total_per_person = grand_total / group_size

print("Welcome to PayUp!")
print()
print(f"Here's the breakdown for {event_name}:")
print()
print(f"Cost: ${cost}")
print(f"Service Charge: ${service_charge}")
print(f"Group Size: {group_size}")
print(f"Grand Total: ${grand_total}")
print()
print(f"Each person must PayUp: ${total_per_person}")