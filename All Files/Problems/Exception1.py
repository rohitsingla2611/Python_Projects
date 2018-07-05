class LessFoodException(Exception):
    def __init__(self, food_quainty):
        message = 'Food given was ' + str(food_quainty) + 'please increase food quantity'
        super.__init__(message)


class MoreFoodException(Exception):
    def __init__(self, food_quainty):
        message = 'Food given was ' + str(food_quainty) + 'Please decrease food quantity'
        super.__init__(message)
