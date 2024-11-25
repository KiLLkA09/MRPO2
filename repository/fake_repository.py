class FakeRepository:
    def __init__(self):
        self.data = []

    def add(self, obj):
        self.data.append(obj)

    def get_all(self):
        return self.data

    def find_by_id(self, obj_id, id_field='id'):
        for obj in self.data:
            if getattr(obj, id_field) == obj_id:
                return obj
        return None
