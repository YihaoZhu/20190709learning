from Input import apartment_Input
import numpy as np
a = apartment_Input.apartmentRadio
Match_building = {}
for i in range(len(a)):
    Match_building_key = a[i]["area"]
    Match_building_value = a[i]["areaRate"]
    Match_building[Match_building_key] = Match_building_value

print(Match_building)
print(Match_building[115])