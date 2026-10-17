print("===== AUTOMATIC DRIP IRRIGATION SYSTEM =====")

soil = input("Enter soil condition (dry/wet): ")
rain = input("Is it raining? (yes/no): ")
temperature = float(input("Enter temperature in Celsius: "))
borewell = input("Is borewell water available? (yes/no): ")

print("\n===== SYSTEM ANALYSIS =====")

if rain == "yes":
    print("Rain detected.")
    print("Borewell pump is OFF.")
    print("Irrigation is not required.")

elif soil == "wet":
    print("Soil has enough moisture.")
    print("Borewell pump is OFF.")

elif soil == "dry":
    if borewell == "no":
        print("Borewell water is unavailable.")
        print("Borewell pump is OFF.")

    elif borewell == "yes":
        if temperature >= 35:
            print("High temperature detected.")
            print("Borewell pump is ON.")
            print("Drip irrigation duration: 15 minutes.")

        elif temperature >= 25:
            print("Moderate temperature detected.")
            print("Borewell pump is ON.")
            print("Drip irrigation duration: 10 minutes.")

        else:
            print("Low temperature detected.")
            print("Borewell pump is ON.")
            print("Drip irrigation duration: 5 minutes.")

    else:
        print("Invalid borewell input.")

else:
    print("Invalid soil condition.")

print("\n===== SYSTEM COMPLETED =====")
