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


class Logins(models.Model):
    id = models.AutoField(primary_key=True)
    host = models.TextField(unique=True)
    username = models.TextField(unique=True)
    password = models.TextField(unique=True)
    processed = models.IntegerField(default=0)
    when = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "logins"
