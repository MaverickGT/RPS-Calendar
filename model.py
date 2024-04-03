class Create_Event:
    def __init__(self, name,start_date, end_date, type, description, picture):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.type = type
        self.description = description
        self.picture = picture
class Event:
    def __init__(self, id, name, start_date, end_date, type, description, picture):
        self.id = id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.type = type
        self.description = description
        self.picture = picture
    
    def __str__(self) -> str:
        return f"Event {self.id}: {self.start_date} - {self.end_date} ({self.type}\n{self.picture}\n{self.description})"