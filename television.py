class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__temp = Television.MIN_VOLUME

    def mute(self):          # changes volume from 0 to the previous amount
        if self.__status:
            if not self.__muted:
                self.__muted = not self.__muted
                self.__temp = self.__volume
                self.__volume = Television.MIN_VOLUME
            elif self.__muted:
                self.__muted = not self.__muted
                self.__volume = self.__temp
        return None

    def channel_up(self):         # changes channel up
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
        return None

    def power(self):             # turns the tv on and off
        self.__status = not self.__status
        if not self.__status:
            self.__muted = not self.__muted
        return None

    def channel_down(self):            # changes channel down
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
        return None

    def volume_up(self):                    # changes volume up
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
        return None

    def volume_down(self):            # changes volume down
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
        return None

    def __str__(self):         # output
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
