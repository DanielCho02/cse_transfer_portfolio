class DatabaseServerManager:
    """
    Class making practice: Managing customer data and order handling.
    Combines Customer Database and Order Server functionalities to provide seamless operations.
    Allows customer registration, order management, and database queries.
    """

    def __init__(self):
        """
        Initializes the OrderDatabaseManager with separate modules for customer database and order server.
        Attributes:
        - __customer_db: A private dictionary to store customer data (customer ID -> customer name).
        - __order_server: A private list to manage orders (order number, order items).
        """
        self.__customer_db = {}
        self.__order_server = []

    def registerCustomer(self, customer_id, customer_name):
        """
        Registers a new customer in the database.

        Parameters:
        - customer_id (str): Unique identifier for the customer.
        - customer_name (str): Name of the customer.

        Returns:
        - dict: {customer_id: customer_name} if successfully added.
        - int: -1 if the customer ID already exists.
        """
        if customer_id in self.__customer_db:
            return -1
        self.__customer_db[customer_id] = customer_name
        return {customer_id: customer_name}

    def getCustomerByID(self, customer_id):
        """
        Retrieves customer name by their ID.

        Parameters:
        - customer_id (str): Unique identifier for the customer.

        Returns:
        - dict: {customer_id: customer_name} if the customer exists.
        - int: -1 if the customer ID is not found.
        """
        if customer_id not in self.__customer_db:
            return -1
        return {customer_id: self.__customer_db[customer_id]}

    def makeOrder(self, order_num, order_list):
        """
        Places a new order in the server queue.

        Parameters:
        - order_num (str): Unique order identifier.
        - order_list (list): List of items in the order.

        Returns:
        - list: [order_num, order_list] if the order is successfully added.
        - int: -1 if the order number already exists.
        """
        for order in self.__order_server:
            if order[0] == order_num:
                return -1
        new_order = [order_num, order_list]
        self.__order_server.append(new_order)
        return new_order

    def cancelOrder(self, order_num):
        """
        Cancels an existing order by its number.

        Parameters:
        - order_num (str): Unique order identifier.

        Returns:
        - list: [order_num, order_items] if the order is successfully removed.
        - int: -1 if the order is not found.
        """
        for order in self.__order_server:
            if order[0] == order_num:
                self.__order_server.remove(order)
                return order
        return -1

    def getOrderCount(self):
        """
        Retrieves the total number of active orders.

        Returns:
        - int: The count of active orders.
        """
        return len(self.__order_server)

    def serveNextOrder(self):
        """
        Serves the next order in the queue.

        Returns:
        - list: [order_num, order_items] for the served order.
        - int: -1 if there are no orders to serve.
        """
        if not self.__order_server:
            return -1
        return self.__order_server.pop(0)

    def getCustomerOrders(self):
        """
        Retrieves all orders currently in the queue.

        Returns:
        - list: List of all active orders in the queue.
        """
        return self.__order_server

    def getCustomerList(self):
        """
        Retrieves the list of all customers.

        Returns:
        - dict: All customers in the format {customer_id: customer_name}.
        """
        return self.__customer_db

    def getWaitingTime(self, order_num, prod_time):
        """
        Calculates the waiting time for a given order number.

        Parameters:
        - order_num (str): Unique order identifier.
        - prod_time (int): Production time per item.

        Returns:
        - int: The total waiting time for the order.
        - int: -1 if the order is not found.
        """
        waiting_time = 0
        for order in self.__order_server:
            if order[0] == order_num:
                return waiting_time + len(order[1]) * prod_time
            waiting_time += len(order[1]) * prod_time
        return -1

    def getDuplicateCustomerNames(self):
        """
        Finds and retrieves all customers with duplicate names.

        Returns:
        - dict: Dictionary of {customer_id: customer_name} for customers with duplicate names.
        """
        name_count = {}
        for name in self.__customer_db.values():
            name_count[name] = name_count.get(name, 0) + 1

        duplicates = {cid: cname for cid, cname in self.__customer_db.items() if name_count[cname] > 1}
        return duplicates

    def addServiceToOrder(self, order_num, service):
        """
        Adds a service to an existing order.

        Parameters:
        - order_num (str): Unique order identifier.
        - service (str): Service to add to the order.

        Returns:
        - list: [order_num, updated_order_items] if the order is found.
        - int: -1 if the order is not found.
        """
        for order in self.__order_server:
            if order[0] == order_num:
                order[1].append(service)
                return order
        return -1

    def updateCustomerName(self, customer_id, new_name):
        """
        Updates the name of an existing customer.

        Parameters:
        - customer_id (str): Unique identifier for the customer.
        - new_name (str): New name to update for the customer.

        Returns:
        - dict: {customer_id: new_name} if the update is successful.
        - int: -1 if the customer ID is not found.
        """
        if customer_id not in self.__customer_db:
            return -1
        self.__customer_db[customer_id] = new_name
        return {customer_id: new_name}

    def getOrderDetails(self, order_num):
        """
        Retrieves the details of a specific order by its number.

        Parameters:
        - order_num (str): Unique order identifier.

        Returns:
        - list: [order_num, order_items] if the order exists.
        - int: -1 if the order is not found.
        """
        for order in self.__order_server:
            if order[0] == order_num:
                return order
        return -1

    def removeCustomer(self, customer_id):
        """
        Removes a customer from the database.

        Parameters:
        - customer_id (str): Unique identifier for the customer.

        Returns:
        - dict: {customer_id: customer_name} if the removal is successful.
        - int: -1 if the customer ID is not found.
        """
        if customer_id not in self.__customer_db:
            return -1
        removed_customer = {customer_id: self.__customer_db.pop(customer_id)}
        return removed_customer

    def calculateTotalItems(self):
        """
        Calculates the total number of items across all active orders.

        Returns:
        - int: The total count of items in all orders.
        """
        total_items = 0
        for order in self.__order_server:
            total_items += len(order[1])
        return total_items

    def getOrderSummary(self):
        """
        Generates a summary of all orders including the number of items in each order.

        Returns:
        - list: List of dictionaries containing order details and item counts.
        Example: [{'order_num': 'O1', 'item_count': 3}, ...]
        """
        summary = []
        for order in self.__order_server:
            summary.append({'order_num': order[0], 'item_count': len(order[1])})
        return summary
