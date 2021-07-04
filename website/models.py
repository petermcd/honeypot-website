from django.db import models


class Setting(models.Model):
    name = models.CharField(max_length=30, unique=True)
    value = models.CharField(max_length=255)

    def __str__(self) -> str:
        """
        To string method

        :return: The name of the setting
        """
        return self.name

    def __repr__(self) -> str:
        """
        Representation of the object

        :return: Str showing the setup of the object
        """
        return f'name={self.name}, value={self.value}'
