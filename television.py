class Television:
    # Class Constants
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """ This used to set the default instance variables."""
        self.__mute: bool = False
        self.__volume = Television.MIN_VOLUME
        self.__status: bool = False
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """This used to turn the tv on and off by changing the value of the status variable"""
        self.__status = not self.__status

    def mute(self) -> None:
        """Mute or unmute the TV when it's on by changing the value of the muted variable."""
        if self.__status:
            self.__mute = not self.__mute

    def channel_down(self) -> None:
        """Decrease the TV channel value when the TV is on."""
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def channel_up(self) -> None:
        """Increase the TV channel value when the TV is on."""
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def volume_up(self) -> None:
        """Increase the TV volume when the TV is on."""
        if self.__status:
            self.__mute = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decrease the TV volume when the TV is on. If the TV is muted, unmute it."""
        if self.__status:
            self.__mute = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Send the values of the TV object in the format Power = [status], Channel = [channel], Volume = [volume].
        :return the status, channel value, and volume value """
        if self.__mute:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
