from Input import apartment_Input


class Match_Building:
    def __init__(self,Input):
        #初始化
        # 导入输入
        self.apartmentRadio = Input
        # 计容总建筑面积
        self.landArea = 0
        # 初始化户型匹配
        self.Match_building = {}
        # 初始化buildingArea数据结构
        self.buildingArea = {}
        #执行匹配
        # 户型匹配，结果返回self.Match_building
        self.Match()
        # 数据结构创建，结果返回self.buildingArea
        self.create()
        # 取计容总建筑面积
        self.pick_landArea()
        print(self.landArea)
        print(self.buildingArea)
        print(self.Match_building)
        print(self.Match_building[115])
    def Match(self):
        for i in range(len(self.apartmentRadio)):
            Match_building_key = self.apartmentRadio[i]["area"]
            Match_building_value = self.apartmentRadio[i]["areaRate"]
            self.Match_building[Match_building_key] = Match_building_value
    def create(self):
        dict3 = {}
        dict1 = {"name": "计容总建筑面积", "planValue": 1000}
        dict2 = {"name": "不计容总建筑面积", "planValue": 500}
        dict3["detail"] = [dict1,dict2]
        dict4 = {"sumplanValue": 5000}
        self.buildingArea = dict4
        self.buildingArea.update(dict3)

    def pick_landArea(self):
        for i in range(len(self.buildingArea["detail"])):
            if self.buildingArea["detail"][i]["name"] == "计容总建筑面积":
                self.landArea = self.buildingArea["detail"][i]["planValue"]
                break



Match_Building(apartment_Input.apartmentRadio)
