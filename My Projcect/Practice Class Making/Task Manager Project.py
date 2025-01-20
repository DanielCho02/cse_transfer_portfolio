class TaskManager:
    """ 
    Class making practice: Simple task manager which creates, sorts, stores, and retrieves tasks.
    Creating and registering tasks, searching, managing deadlines and priorities, input/output of data files.
    """
    def __init__(self):
        """
        Initializes the TaskManager class with an empty list to store tasks.
        Attributes:
        - __tasks: A private list to store task records.
        Each task is represented as a dictionary with the following keys:
        - 'student_id': A string representing the student's ID (10 digits).
        - 'deadline': A string representing the task deadline in YYYYMMDD format.
        - 'task_id': A string representing the task identifier (4 alphanumeric characters).
        - 'priority': An integer representing the task priority (1, 2, or 3).
        """
        self.__tasks = []  # Private list to store task records

    def createTask(self, student_id, deadline, task_id, priority):
        """
        Creates a task record and validates the input data.

        Parameters:
        - student_id (str): The student's ID (must be 10 characters).
        - deadline (str): The task deadline in YYYYMMDD format.
        - task_id (str): The task identifier (4 alphanumeric characters).
        - priority (int): The task priority (1, 2, or 3).

        Returns:
        - list: The task record if created successfully.
        - int: -1 if the input data types are invalid.
        - int: -2 if the input values are not in the correct format.
        """
        if not isinstance(student_id, str) or not isinstance(deadline, str) or not isinstance(task_id, str) or not isinstance(priority, int):
            return -1
        if len(student_id) != 10 or len(deadline) != 8 or len(task_id) != 4 or priority not in [1, 2, 3]:
            return -2

        task = {
            'student_id': student_id,
            'deadline': deadline,
            'task_id': task_id,
            'priority': priority
        }
        self.__tasks.append(task)
        return task

    def getTaskByID(self, task_id):
        """
        Retrieves a task by its identifier.

        Parameters:
        - task_id (str): The identifier of the task to retrieve.

        Returns:
        - list: The task record if found.
        - int: -1 if the task is not found.
        """
        for task in self.__tasks:
            if task['task_id'] == task_id:
                return task
        return -1

    def checkDeadline(self, task_id, today_date):
        """
        Checks if the deadline of a task is valid compared to today's date.

        Parameters:
        - task_id (str): The identifier of the task to check.
        - today_date (str): Today's date in YYYYMMDD format.

        Returns:
        - bool: True if the deadline is valid, False otherwise.
        - int: -1 if the task is not found.
        """
        task = self.getTaskByID(task_id)
        if task == -1:
            return -1
        return task['deadline'] >= today_date

    def deferDeadline(self, task_id, delay):
        """
        Defers the deadline of a task by a specified number of days.

        Parameters:
        - task_id (str): The identifier of the task to update.
        - delay (int): The number of days to extend the deadline (1-14 days).

        Returns:
        - list: The updated task record if successful.
        - int: -1 if the task is not found.
        - int: -2 if the delay exceeds 14 days.
        """
        if delay > 14:
            return -2

        task = self.getTaskByID(task_id)
        if task == -1:
            return -1

        year, month, day = int(task['deadline'][:4]), int(task['deadline'][4:6]), int(task['deadline'][6:8])
        day += delay

        if day > 31:
            day -= 31
            month += 1
            if month > 12:
                month = 1
                year += 1

        task['deadline'] = f"{year:04d}{month:02d}{day:02d}"
        return task

    def getEarliestTask(self):
        """
        Retrieves the task with the earliest deadline.

        Returns:
        - list: The task with the earliest deadline.
        - int: -1 if there are no tasks.
        """
        if not self.__tasks:
            return -1

        earliest_task = self.__tasks[0]
        for task in self.__tasks:
            if task['deadline'] < earliest_task['deadline'] or (
                task['deadline'] == earliest_task['deadline'] and task['priority'] < earliest_task['priority']):
                earliest_task = task
        return earliest_task

    def getTasksSorted(self, reverse=False):
        """
        Retrieves all tasks sorted by deadline and priority.

        Parameters:
        - reverse (bool): If True, sorts in descending order.

        Returns:
        - list: A list of sorted tasks.
        """
        sorted_tasks = []
        tasks_copy = self.__tasks[:]

        while tasks_copy:
            earliest = self.getEarliestTask()
            sorted_tasks.append(earliest)
            tasks_copy.remove(earliest)

        if reverse:
            sorted_tasks.reverse()

        return sorted_tasks

    def saveToFile(self, filename):
        """
        Saves all task records to a CSV file.

        Parameters:
        - filename (str): The name of the file to save the tasks.
        """
        with open(filename, 'w') as file:
            for task in self.__tasks:
                file.write(f"{task['student_id']},{task['deadline']},{task['task_id']},{task['priority']}\n")

    def loadFromFile(self, filename):
        """
        Loads task records from a CSV file.

        Parameters:
        - filename (str): The name of the file to load the tasks from.
        """
        self.__tasks = []
        with open(filename, 'r') as file:
            for line in file:
                student_id, deadline, task_id, priority = line.strip().split(',')
                self.createTask(student_id, deadline, task_id, int(priority))

    def checkPriority(self, task_id):
        """
        Checks if the priority of a task is valid.

        Parameters:
        - task_id (str): The identifier of the task to check.

        Returns:
        - bool: True if the priority is valid, False otherwise.
        - int: -1 if the task is not found.
        """
        task = self.getTaskByID(task_id)
        if task == -1:
            return -1
        return task['priority'] in [1, 2, 3]

    def getTaskByStudentID(self, student_id):
        """
        Retrieves all tasks associated with a specific student ID.

        Parameters:
        - student_id (str): The student ID to search for.

        Returns:
        - list: A list of tasks associated with the student ID.
        - int: -1 if no tasks are found.
        """
        tasks_by_student = [task for task in self.__tasks if task['student_id'] == student_id]
        return tasks_by_student if tasks_by_student else -1

    def deleteTask(self, task_id):
        """
        Deletes a task by its identifier.

        Parameters:
        - task_id (str): The identifier of the task to delete.

        Returns:
        - list: The deleted task record if successful.
        - int: -1 if the task is not found.
        """
        for task in self.__tasks:
            if task['task_id'] == task_id:
                self.__tasks.remove(task)
                return task
        return -1

    def updatePriority(self, task_id, new_priority):
        """
        Updates the priority of a task.

        Parameters:
        - task_id (str): The identifier of the task to update.
        - new_priority (int): The new priority value (1, 2, or 3).

        Returns:
        - list: The updated task record if successful.
        - int: -1 if the task is not found.
        - int: -2 if the new priority is invalid.
        """
        if new_priority not in [1, 2, 3]:
            return -2

        task = self.getTaskByID(task_id)
        if task == -1:
            return -1

        task['priority'] = new_priority
        return task

    def countTasks(self):
        """
        Counts the total number of tasks in the system.

        Returns:
        - int: The total number of tasks.
        """
        return len(self.__tasks)

    def getOverdueTasks(self, today_date):
        """
        Retrieves all tasks that are overdue compared to today's date.

        Parameters:
        - today_date (str): Today's date in YYYYMMDD format.

        Returns:
        - list: A list of overdue tasks.
        """
        return [task for task in self.__tasks if task['deadline'] < today_date]
