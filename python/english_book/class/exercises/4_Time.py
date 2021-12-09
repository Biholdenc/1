class Time:
    def __init__(self, time_in_second):
        self.time_in_second = time_in_second
        self.minute = 0
        self.second = 0

    def convert_to_minutes(self):
        self.minute = self.time_in_second // 60
        self.second = self.time_in_second % 60
        if self.second == 0:
            self.second = '00'
        return '{}:{}'.format(self.minute, self.second)

    def convert_to_hours(self):
        hours = self.time_in_second // 3600
        if self.minute > 60:
            self.minute = self.minute % 60
        return '{}:{}:{}'.format(hours, self.minute, self.second)

x = Time(3830)
print(x.convert_to_minutes())
print(x.convert_to_hours())