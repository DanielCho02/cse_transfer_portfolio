class RemoteControl:
    """
    Class making practice: Implements basic functionalities of a remote control.
    Allows channel management, navigation, blocking/unblocking, and saving/loading channel data.
    """
    def __init__(self):
        """
        Initializes the RemoteControl class with an empty list for enabled channels.
        Attributes:
        - __enabledChannelList: A private list storing [channel number (int), channel name (str)].
        - __current_channel: A private attribute pointing to the currently active channel.
        """
        self.__enabledChannelList = []
        self.__current_channel = None

    def powerOnRemoteControl(self, channel_list):
        """
        Activates the remote control with a given list of channels.

        Parameters:
        - channel_list (list): A list of lists, where each inner list contains [channel number (int), channel name (str)].

        Returns:
        - int: The number of channels added to the enabled list.
        """
        for channel in channel_list:
            self.__enabledChannelList.append(channel)
        self.__current_channel = self.__enabledChannelList[0] if self.__enabledChannelList else None
        return len(self.__enabledChannelList)

    def gotoChannel(self, channel_num):
        """
        Switches to a channel with the specified channel number.

        Parameters:
        - channel_num (int): The number of the channel to switch to.

        Returns:
        - str: The name of the channel switched to, or the current channel name if not found.
        """
        if not self.__enabledChannelList:
            return "No channels available"

        for channel in self.__enabledChannelList:
            if channel[0] == channel_num:
                self.__current_channel = channel
                return channel[1]
        return self.__current_channel[1]

    def nextChannel(self):
        """
        Moves to the next channel in the list.

        Returns:
        - str: The name of the channel switched to.
        """
        if not self.__enabledChannelList:
            return "No channels available"

        current_channel_index = self.__enabledChannelList.index(self.__current_channel)
        next_channel_index = (current_channel_index + 1) % len(self.__enabledChannelList)
        self.__current_channel = self.__enabledChannelList[next_channel_index]
        return self.__current_channel[1]

    def previousChannel(self):
        """
        Moves to the previous channel in the list.

        Returns:
        - str: The name of the channel switched to.
        """
        if not self.__enabledChannelList:
            return "No channels available"

        current_channel_index = self.__enabledChannelList.index(self.__current_channel)
        prev_channel_index = (current_channel_index - 1) % len(self.__enabledChannelList)
        self.__current_channel = self.__enabledChannelList[prev_channel_index]
        return self.__current_channel[1]

    def blockChannel(self):
        """
        Blocks the current channel, removing it from the enabled list.

        Returns:
        - str: The name of the newly selected current channel, or a message if no channels remain.
        """
        if not self.__enabledChannelList:
            return "No channels to block"

        blocked_channel = self.__current_channel
        self.__enabledChannelList.remove(blocked_channel)
        self.__current_channel = self.__enabledChannelList[0] if self.__enabledChannelList else None
        return self.__current_channel if self.__current_channel else "No channels available"

    def unblockChannel(self, blocked_channel_num):
        """
        Re-enables a previously blocked channel.

        Parameters:
        - blocked_channel_num (int): The number of the blocked channel to be re-added.

        Returns:
        - int: 1 if successfully unblocked, -1 if the channel is already enabled.
        """
        if not any(blocked_channel_num == channel[0] for channel in self.__enabledChannelList):
            insert_index = 0
            for i, channel in enumerate(self.__enabledChannelList):
                if channel[0] > blocked_channel_num:
                    insert_index = i
                    break
            self.__enabledChannelList.insert(insert_index, [blocked_channel_num, ""])
            self.__current_channel = self.__enabledChannelList[0]
            return 1
        else:
            return -1

    def powerOffRemoteControl(self):
        """
        Saves the list of enabled channels to a CSV file.

        File format:
        - Each line contains a channel number and name separated by a comma.

        Returns:
        - str: A message indicating success or if there are no channels to save.
        """
        if not self.__enabledChannelList:
            return "No channels to save"

        with open('output.csv', 'w') as file:
            for channel in self.__enabledChannelList:
                file.write(f'{channel[0]},{channel[1].strip()}\n')

    def favorChannel(self):
        """
        Marks the current channel as a favorite by incrementing its favor count.

        Returns:
        - int: 1 if successful, or a message if no channels are available.
        """
        if not self.__enabledChannelList:
            return "No channels available"

        if len(self.__current_channel) == 3:
            self.__current_channel[2] += 1
        else:
            self.__current_channel.append(1)
            return 1

    def aiNextChannel(self):
        """
        Uses AI logic to switch to the next channel based on favor count.

        Returns:
        - int: The number of the selected channel, or a message if no channels are available.
        """
        if not self.__enabledChannelList:
            return "No channels available"

        current_channel_favor = self.__current_channel[2] if len(self.__current_channel) == 3 else 0

        next_channel_num = -1
        min_channel_num = float('inf')
        for channel in self.__enabledChannelList:
            if len(channel) == 3 and channel[2] == current_channel_favor - 1:
                if channel[0] < min_channel_num:
                    min_channel_num = channel[0]
                    next_channel_num = channel[0]

        if next_channel_num == -1:
            max_favor = 0
            for channel in self.__enabledChannelList:
                if len(channel) == 3 and channel[2] > max_favor:
                    max_favor = channel[2]
            for channel in self.__enabledChannelList:
                if len(channel) == 3 and channel[2] == max_favor:
                    next_channel_num = channel[0]
                    break

        for channel in self.__enabledChannelList:
            if channel[0] == next_channel_num:
                self.__current_channel = channel
                break

        return next_channel_num

    def aiPreviousChannel(self):
        """
        Uses AI logic to switch to the previous channel based on favor count.

        Returns:
        - int: The number of the selected channel, or a message if no channels are available.
        """
        if not self.__enabledChannelList:
            return "No channels available"

        current_channel_favor = self.__current_channel[2] if len(self.__current_channel) == 3 else 0

        prev_channel_num = -1
        min_channel_num = float('inf')
        for channel in self.__enabledChannelList:
            if len(channel) == 3 and channel[2] == current_channel_favor + 1:
                if channel[0] < min_channel_num:
                    min_channel_num = channel[0]
                    prev_channel_num = channel[0]

        if prev_channel_num == -1:
            min_favor = float('inf')
            for channel in self.__enabledChannelList:
                if len(channel) == 3 and channel[2] < min_favor:
                    min_favor = channel[2]
            for channel in self.__enabledChannelList:
                if len(channel) == 3 and channel[2] == min_favor:
                    prev_channel_num = channel[0]
                    break

        for channel in self.__enabledChannelList:
            if channel[0] == prev_channel_num:
                self.__current_channel = channel
                break

        return prev_channel_num

    def getChannelList(self):
        """
        Retrieves the list of enabled channels.

        Returns:
        - list: The enabled channels, or a message if no channels are available.
        """
        if not self.__enabledChannelList:
            return "No channels available"
        return self.__enabledChannelList

    def getCurrentChannel(self):
        """
        Retrieves information about the current channel.

        Returns:
        - list: The current channel information, or a message if no channel is selected.
        """
        if not self.__current_channel:
            return "No current channel selected"
        return self.__current_channel
