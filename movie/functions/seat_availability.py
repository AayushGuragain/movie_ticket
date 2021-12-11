from movie.models import Ticket, Booking
import datetime

def check_availability(ticket, start_time, end_time):
    available_list = []
    '''
    Returns true if all of available_list is true
    Otherwise returns false
    '''
    booking_list = Booking.objects.filter(ticket=ticket)
    for i in booking_list:
        if i.show_starts > end_time or i.show_ends < start_time:
            '''
            if the preexisting sho starts after user's show ends
            i.show_starts >(after) end_time (user end time) == True
            or
            i.show_ends <(before) start_timme (user start time) == True
            4th of December > 1st of December
            4th of December < 6th of December
            Future is higher value always
            '''
            available_list.append(True)
        else:
            available_list.append(False)

    return all(available_list)
