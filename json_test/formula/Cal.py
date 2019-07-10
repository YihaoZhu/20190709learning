from Input import data
import math

def Cal(data):
    house_115_lower_bound = math.ceil(data.Area_match_floor[115] * 0.9)
    house_115_upper_bound = math.ceil(data.Area_match_floor[115] * 1.1)
    house_140_lower_bound = math.ceil(data.Area_match_floor[140] * 0.9)
    house_140_upper_bound = math.ceil(data.Area_match_floor[140] * 1.1)
    house_180_lower_bound = math.ceil(data.Area_match_floor[180] * 0.9)
    house_180_upper_bound = math.ceil(data.Area_match_floor[180] * 1.1)
    Ground_truth_Area = data.landArea
    Initial_Area = 90000
    Actual_Area = 0
    for i in range(house_115_lower_bound,house_115_upper_bound):
        Area_115 = i * data.each_floor_num[115] * data.building_num[115] * 115
        for j in range(house_140_lower_bound,house_140_upper_bound):
            Area_140 = j * data.each_floor_num[140] * data.building_num[140] * 140
            for k in range(house_180_lower_bound,house_180_upper_bound):
                Area_180 = k * data.each_floor_num[180] * data.building_num[180] * 180
                Actual_Area = Area_115 + Area_140 + Area_180
                if abs(Ground_truth_Area - Actual_Area) < Initial_Area:
                    Initial_Area = abs(Actual_Area - Ground_truth_Area)
                    Actual_i = i
                    Actual_j = j
                    Actual_k = k
    print(Actual_i)
    print(Actual_j)
    print(Actual_k)

Cal(data)