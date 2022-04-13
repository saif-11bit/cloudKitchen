# Cloud Kitchen prep time
from datetime import datetime, timedelta


class CloudKitchen:

    def __init__(self):
        self.stoves = {
            '1': {
                'item': None,
                'available': True
            },
            '2': {
                'item': None,
                'available': True
            },
            '3': {
                'item': None,
                'available': True
            },
        }
        self.menu_items = {
            '1': {
                'name': 'Biryani',
                'prep_time': 40
            },
            '2': {
                'name': 'Pizza',
                'prep_time': 30
            },
            '3': {
                'name': 'Burger',
                'prep_time': 15
            },
            '4': {
                'name': 'Momos',
                'prep_time': 10
            }
        }
        self.order_completed = {}
        self.order_on_stove = {}
        # {
        #     '<order:id>':{
        #         'item1':'item:expected_time',
        #         'item2':'item:expected_time',
        #     },
        #     '<order:id>':{
        #         'item1':'item:expected_time',
        #     },
        # }
        self.order_queue = {}
        # {
        #     '<order:id>':{
        #         'item1':'item:prep_time',
        #         'item2':'item:prep_time',
        #     },
        #     '<order:id>':{
        #         'item1':'item:prep_time',
        #         'item2':'item:prep_time',
        #         'item3':'item:prep_time',
        #     },
        # }
        self.original_order = {}

    def check_availablity(self):
        """Will check the stove availablity"""
        avail_stove = []
        booked_stove = []
        for stove_id in self.stoves.keys():
            if self.stoves[stove_id]["available"]:
                print(f"Stove {stove_id} is available")
                avail_stove.append(stove_id)
            else:
                print(f"Stove {stove_id} is booked")
                booked_stove.append(stove_id)
        return avail_stove, booked_stove

    def new_orders(self, order):
        """Receive new orders from orders"""
        avail_stove, booked_stove = self.check_availablity()
        for order_id, order_items in order.items():
            # Copy the same in self.original_order
            self.original_order[order_id] = order_items
            # Insert in self.order_queue
            self.order_queue[order_id] = {}
            for item in order_items:
                self.order_queue[order_id][f"{item}"] = self.menu_items[
                    f"{item}"]['prep_time']

        print('Before update_order_stove order_queue', self.order_queue)
        for stove_id in avail_stove:
            if len(self.order_queue) < 1:
                break
            self.update_order_stove(stove_id)
            print('order_on_stove', self.order_on_stove)

        print('After update_order_stove order_queue', self.order_queue)

    def update_order_stove(self, stove_id):
        """Will update the order_queue, order_on_stove and stove  
    availability dict."""

        # Update the stove with the first item in order_queue
        first_order_in_queue = tuple(self.order_queue.values())[0]
        first_item_in_order_queue = tuple(first_order_in_queue)[0]
        self.stoves[stove_id]['item'] = first_item_in_order_queue

        # Updating stove availability
        self.stoves[stove_id]['available'] = False

        # Append in order_on_stove
        first_order_id = tuple(self.order_queue.keys())[0]
        # Check if the dictionary exist with order_id exist
        if self.order_on_stove.get(f'{first_order_id}') is None:
            self.order_on_stove[f'{first_order_id}'] = {}

        prep_end_time = datetime.now() + timedelta(
            minutes=self.menu_items[f'{first_item_in_order_queue}']
            ['prep_time'])
        self.order_on_stove[f'{first_order_id}'][
            f'{first_item_in_order_queue}'] = prep_end_time

        # Remove from order_queue
        self.order_queue[f'{first_order_id}'].pop(first_item_in_order_queue)

        # Check if the order_queue with the first_order_id has no data. Then delete it
        if len(self.order_queue.get(f'{first_order_id}')) < 1:
            del self.order_queue[f'{first_order_id}']

    def get_waiting_time(self, item_id):
        pass

    def cooking_update(self):
        #
        pass


if __name__ == "__main__":
    a = CloudKitchen()
    # Order will be a dict containg order_id as a key and order items as a value that will be a  list
    first_order = {'1': [4, 2]}
    a.new_orders(first_order)
    second_order = {'2': [3, 4]}
    a.new_orders(second_order)
