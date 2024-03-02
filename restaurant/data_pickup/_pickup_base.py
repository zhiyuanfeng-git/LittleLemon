from .utility import get_file_full_path,load_json

class PickupBase:
    FIELD_README = 'readme'
    FIELD_LIST = 'list'
    FIELD_DICT = 'dict'

    def __init__(self, file_name: str):
        try:
            self.file_name = file_name
            self.data_dict = None
            file_path = get_file_full_path(file_name)
            with open(file_path) as file:
                self.data_dict = load_json(file)
        except Exception as e:
            print(f"Load File Error: {e}")
            raise

    def __get_by_key(self, key):
        return self.data_dict[key]
    
    def get_readme(self):
        return self.__get_by_key(PickupBase.FIELD_README)
    
    def get_list(self):
        return self.__get_by_key(PickupBase.FIELD_LIST)

    def get_dict(self):
        return self.__get_by_key(PickupBase.FIELD_DICT)