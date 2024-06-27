import datetime


class Solution:

    def day_of_the_week(self, year: int, month: int, day: int) -> str:
        input_date = datetime.date(year, month, day)
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
        return weekdays[input_date.weekday()]


print(Solution.day_of_the_week(None, 1998, 1, 30))
