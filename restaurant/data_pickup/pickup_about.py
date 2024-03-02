from ._pickup_base import PickupBase

class PickupAbout(PickupBase):
    def __init__(self, file_name: str):
        super().__init__(file_name)
        print(self)

    def __str__(self):
        return f"load file: {self.file_name}\naddress: {hex(id(self))}"

    def get_caption(self):
        return self.get_dict()['caption']

pickup_about = PickupAbout("data_about.json")