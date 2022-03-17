from datetime import datetime, timedelta


MENU={
    'item1': 10,
    'item2': 20,
    'item3': 30,
    'item4': 50,
    'item5': 10
}

KITCHEN_STOVES = {
    'stove1': 'item1',
    'stove2': 'item2',
    'stove3': None,
    'stove4':None
}


FOODS_PREPARING = {}

def get_preparation_time(items):
    cookingTimings = []
    waiting_time = 0
    for i in items:
        if i in KITCHEN_STOVES.values():
            cookingTimings.append(MENU[i])
            cooking_end_time = datetime.now() + timedelta(minutes = MENU[i])
            FOODS_PREPARING[i] = cooking_end_time
        else:
            # check if any value in KITCHEN_STOVES is None
            if None in KITCHEN_STOVES.values():
                key = list(KITCHEN_STOVES.keys())[list(KITCHEN_STOVES.values()).index(None)]
                # assign item to available stove
                KITCHEN_STOVES[key] = i
                cookingTimings.append(MENU[i])
                cooking_end_time = datetime.now() + timedelta(minutes = MENU[i])
                FOODS_PREPARING[i] = cooking_end_time
                
            else:
                # check for minimum_time in which stove will be available .i.e (cooking_end_time - current time)
                
                # waiting_time += minimum_time
                # 
                pass


    print(FOODS_PREPARING)
    print(f'============Your order will be prepared in {max(cookingTimings) + waiting_time} minutes===========')


get_preparation_time(['item1','item2', 'item3', 'item5'])



# class KitchenStove:
    
#     def __init__(self, assigned=False, available_in=None, next=None):
#         self.assigned = assigned
#         self.available_in = available_in
#         self.next = next
    
#     def get_total_available_spaces():
#         pass
    
#     def get_active_spaces():
#         pass
    
#     def no_of_active_spaces():
#         pass

#     def get_next_available_spaces():
#         pass
# # ========================================================

# class Menu:
    
#     def __init__(self, name: None, cookingTime: None):
#         self.name = name
#         self.cookingTime = cookingTime
        
# # =======================================================


# class Order:
#     def __init__(self):
#         self.item = None
        
#     def no_of_items(self):
#         pass
        
    
#     def get_preparation_time(self):
#         if self.no_of_items <= KitchenStove.no_of_active_spaces():
#             # check item with max time
#             # assign space: true
#             # return food preparation time
#             pass
#         else:
#             # assign avalalble space to items
#             # mt = get assigned item max time
#             # assign next available spaces to remaining items
#             # wt = get waiting time
#             # mtr = get max food preparation time from remaining items
#             # if mt >= wt + mtr:
#                 # Preparation time = mt
#             # else:
#                 # wt + mtr will be preparation time
#                 pass
