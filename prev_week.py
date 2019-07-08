import datetime


def previous_week():
    date_today = datetime.date.today()
    dow_today = date_today.weekday()
    if dow_today == 6:
        days_ago_saturday = 1
    else:
        days_ago_saturday = dow_today + 2
    delta_saturday = datetime.timedelta(days=days_ago_saturday)
    saturday = date_today - delta_saturday
    delta_prev_sunday = datetime.timedelta(days=6)
    prev_sunday = saturday - delta_prev_sunday
    return saturday, prev_sunday


def week_before_last():
    date_today = datetime.date.today()
    dow_today = date_today.weekday()
    if dow_today == 6:
        days_ago_saturday = 8
    else:
        days_ago_saturday = dow_today + 2 + 7
    delta_saturday = datetime.timedelta(days=days_ago_saturday)
    saturday = date_today - delta_saturday
    delta_prev_sunday = datetime.timedelta(days=6)
    prev_sunday = saturday - delta_prev_sunday
    return saturday, prev_sunday


if __name__ == '__main__':
    previous_week()
    week_before_last()
