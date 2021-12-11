'''
Here we create our database, specify if they are character, or integer, or some other field, or borrowed from where.
__str__ function is used to display what the models are about.

'''

from django.db import models
from django.conf import settings
#Create your models here.

class Ticket(models.Model):
    HALL_NUMBERS_TUPLE = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))
    SEAT_TYPE_TUPLE = (
        ('D', 'Diamond'),
        ('P', 'Platinum'),
        ('G', 'Gold'),
        ('S', 'Silver'),
        ('B', 'Bronze')
    )
    ROWS_TUPLE = (('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'))
    SEAT_NUMBERS_TUPLE = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('3', '3'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'))

    hall_no = models.CharField(max_length=1, choices=HALL_NUMBERS_TUPLE, default='1')
    type = models.CharField(max_length=1, choices=SEAT_TYPE_TUPLE, default='D')
    seat_row = models.CharField(max_length=1, choices=ROWS_TUPLE, default='A')
    seat_number = models.CharField(max_length=1, choices=SEAT_NUMBERS_TUPLE, default='1')


    def __str__(self):
        return f'H{self.hall_no}, T{self.type}, {self.seat_row}{self.seat_number}'

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    show_starts = models.DateTimeField()
    show_ends = models.DateTimeField()

    def __str__(self):
        return f'{self.user} booked {self.ticket} from {self.show_starts} to {self.show_ends}'
