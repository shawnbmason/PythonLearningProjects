weight = 4.8
cost_ground = ''
drone= ''
cost_ground_premium = 125.00

#Ground Shipping

if weight <= 2 :
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
 cost_ground = weight * 3.0 + 20
elif weight <= 10:
  cost_ground = weight * 4.0 + 20
else:
  cost_ground = weight * 4.75 + 20

print("Ground Shipping $", cost_ground)
print("Ground Shipping Premium $", cost_ground_premium)

#Drone

if weight <= 2 :
  drone = weight * 4.5
elif weight <= 6:
 drone = weight * 9.0
elif weight <= 10:
  drone = weight * 12.0 
else:
  drone = weight * 14.25

print("Drone Shipping $", drone)