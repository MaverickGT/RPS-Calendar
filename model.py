class Create_Event:
    def __init__(self, name,start_date, end_date, type, color, description, picture, start_time, end_time, all_day):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.type = type
        self.color = color
        self.description = description
        self.picture = picture
        self.start_time = start_time
        self.end_time = end_time
        self.all_day = all_day
class Event:
    def __init__(self, id, name, start_date, end_date, type, color, description, picture, start_time, end_time, all_day):
        self.id = id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.type = type
        self.color=color
        self.description = description
        self.picture = picture
        self.start_time = start_time
        self.end_time = end_time
        self.all_day = all_day
    
    def __str__(self) -> str:
        return f"Event {self.id}: {self.start_date} - {self.end_date} ({self.type}\n{self.picture}\n{self.description})"