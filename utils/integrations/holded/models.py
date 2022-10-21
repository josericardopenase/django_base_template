from genericpath import exists
from django.db import models
import requests

from config.settings.base import HOLDED_API_KEY


class HoldedEmployee(models.Model):
    holded_id = models.CharField(max_length=2500, null=True, blank=True)
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "key": HOLDED_API_KEY,
    }

    @property
    def has_holded_profile(self):
        return self.holded_id != None and self.holded_id != ""

    def create_holded_profile(self):
        url = "https://api.holded.com/api/team/v1/employees"

        payload = {
            "name": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
            "sendInvite": True,
        }

        response = requests.post(url, json=payload, headers=self.headers)

        if response.json()["status"] == 1:
            self.holded_id = response.json()["id"]
        else:
            raise Exception("Error no se ha podido crear el emplaedo de holded")

    def delete_holded_profile(self):
        url = "https://api.holded.com/api/team/v1/employees/" + self.holded_id

        response = requests.delete(url, headers=self.headers)

    class Meta:
        abstract = True
