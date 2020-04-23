def time2int(time):
    '''a string time format transmit to a int(miniutes)'''
    hour, min = time.split(':')
    return int(hour) * 60 + int(min)


def get_start_time(schedules, duration):
    # flatten and sort
    merged_schedules = [
        meeting for schedule in schedules for meeting in schedule]
    merged_schedules.sort(key=lambda meeting: meeting[0])
    open_start = '09:00'
    open_stop = '09:00'

    for meeting in merged_schedules:
        if meeting[0] > open_stop:
            open_stop = meeting[0]
        if time2int(open_stop) - time2int(open_start) >= duration:
            return open_start
        if meeting[1] > open_start:
            open_start = meeting[1]
    open_stop = '19:00'
    if time2int(open_stop) - time2int(open_start) >= duration:
        return open_start
    return None
