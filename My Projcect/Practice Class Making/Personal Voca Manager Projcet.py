class PersonalVocaManager:
    """
    Class making practice: Simple personal vocabulary trainer which stores words and their frequencies.
    """
    __object_counter = 0  # Class-level attribute to track the number of objects created

    def __init__(self, object_id):
        """
        Initializes a PersonalVocaManager object with a unique identifier.

        Parameters:
        - object_id (str): The identifier for the object.

        Attributes:
        - __id (str): Stores the object's unique identifier.
        - __dict (dict): A dictionary to store word frequencies.
        """
        self.__id = object_id
        self.__dict = {}
        PersonalVocaManager.__object_counter += 1  # Increment the object count

    def get_id(self):
        """
        Retrieves the object's identifier.

        Returns:
        - str: The object's unique identifier.
        """
        return self.__id

    def set_id(self, object_id):
        """
        Sets the object's identifier.

        Parameters:
        - object_id (int, float, or str): The new identifier for the object.

        If the identifier is an int or float, it is set to "XXXX". Otherwise, it
        is set to the provided value.
        """
        if isinstance(object_id, (int, float)):
            self.__id = "XXXX"
        else:
            self.__id = object_id

    def get_number_of_objects(self):
        """
        Retrieves the total number of PersonalVocaManager objects created.

        Returns:
        - int: The total number of PersonalVocaManager objects.
        """
        return PersonalVocaManager.__object_counter

    def store_wordlist_as_dictionary(self, word_list):
        """
        Converts a list of words into a dictionary with word frequencies.

        Parameters:
        - word_list (list): A list of words to store in the dictionary.

        Returns:
        - dict: A dictionary with word frequencies.
        """
        word_list.sort()
        for word in word_list:
            self.__dict[word] = self.__dict.get(word, 0) + 1
        return self.__dict

    def get_word_count(self, keyword):
        """
        Retrieves the count of a specific word in the dictionary.

        Parameters:
        - keyword (str): The word to look up.

        Returns:
        - tuple: The word and its count, or False if the word is not in the dictionary.
        """
        return (keyword, self.__dict[keyword]) if keyword in self.__dict else False

    def get_word_list(self):
        """
        Returns a sorted list of all words in the dictionary.

        Returns:
        - list: A sorted list of words, or False if the dictionary is empty.
        """
        return sorted(self.__dict.keys()) if self.__dict else False

class EnhancedPersonalVocaManager(PersonalVocaManager):
    """
    Class making practice: Enhanced personal vocabulary trainer with advanced functionalities like merging and comparison.
    """

    def __init__(self, object_id="****"):
        """
        Initializes an EnhancedPersonalVocaManager object.

        Parameters:
        - object_id (str, optional): The identifier for the object. Defaults to "****".

        Inherits:
        - PersonalVocaManager.__init__ to handle object initialization.
        """
        super().__init__(object_id)

    def __str__(self):
        """
        Returns a string representation of the object.

        If the dictionary is empty, returns "<>". Otherwise, returns a string
        containing the dictionary's keys in sorted order, enclosed in "<>".

        Returns:
        - str: The string representation of the object.
        """
        if len(self._PersonalVocaManager__dict) == 0:
            return "<>"
        else:
            return "<" + ",".join(sorted(self._PersonalVocaManager__dict.keys())) + ">"

    def __gt__(self, target):
        """
        Compares the size of the dictionary with another EnhancedPersonalVocaManager object.

        Parameters:
        - target (EnhancedPersonalVocaManager): The object to compare against.

        Returns:
        - bool: True if this object's dictionary has more keys, False otherwise.
        """
        return len(self._PersonalVocaManager__dict) > len(target._PersonalVocaManager__dict)

    def __add__(self, target):
        """
        Merges the dictionaries of two EnhancedPersonalVocaManager objects.

        Parameters:
        - target (EnhancedPersonalVocaManager): The object to merge with.

        Returns:
        - EnhancedPersonalVocaManager: A new object with the merged dictionary.
        """
        result_dict = self._PersonalVocaManager__dict.copy()
        for item in target._PersonalVocaManager__dict:
            result_dict[item] = result_dict.get(item, 0) + target._PersonalVocaManager__dict[item]

        result_object = EnhancedPersonalVocaManager("0000")
        result_object._PersonalVocaManager__dict = result_dict
        return result_object
