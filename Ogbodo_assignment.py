# Defining the parent class Event
class Event: 
# initializing with various attributes
    def __init__(self, event_name, event_date, event_time, event_location):
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.event_location = event_location
        # empty guest and vendor list to contain more than 1
        self.guests = []
        self.vendors = []

# using the string method to name the event, date, time and location
    def __str__(self):
        return f"Event: {self.event_name}\nDate: {self.event_date}\nTime: {self.event_time}\nLocation: {self.event_location}"

# add_guest method to display an added guest
    def add_guest(self, guest):
        # add a guest to the list
        self.guests.append(guest)
        print(f"{guest.name} has been added to the guest list.")

# vendor method to manage the vendors
    def add_vendor(self, vendor):
        # adding vendors to the list of vendors
        self.vendors.append(vendor)
        print(f"{vendor.name} has been added as a vendor.")

# sending invitation methods
    def send_invitations(self):
        print(f"{self.event_name} has received a Invitation!.")

# displaying the rsvp for the Event
    def track_rsvp(self):
        print(f"Tracking RSVP for {self.event_name}.")

# using inheritance for other classes from Event
class Guest(Event):
    def __init__(self, event_name, date, time, location, name, email):
        super().__init__(event_name, date, time, location)
        self.name = name
        self.email = email
        self.rsvp_status = "Pending"
        self.attendance = False

    def __str__(self):
        return f"Guest: {self.name}\nEmail: {self.email}\nRSVP: {self.rsvp_status}"

    def rsvp(self, status):
        self.rsvp_status = status
        print(f"{self.name} RSVP is {self.rsvp_status}.")

    def check_in(self):
        self.attendance = True
        print(f"{self.name} has checked in for {self.event_name}.")        


class Vendor(Event):
    def __init__(self, event_name, date, time, location, name, service, contact):
        super().__init__(event_name, date, time, location)
        self.name = name
        self.service = service
        self.contact = contact

    def __str__(self):
        return f"Vendor: {self.name}\nService: {self.service}\nContact: {self.contact}"

    def send_invoice(self):
        print(f"{self.name} has sent an invoice for {self.event_name}.")

    def receive_payment(self):
        print(f"{self.name} has received payment for {self.event_name}.")


class Vendor(Event):
    def __init__(self, event_name, date, time, location, name, service, contact):
        super().__init__(event_name, date, time, location)
        self.name = name
        self.service = service
        self.contact = contact
# variuos methods in the vendor class
    def __str__(self):
        return f"Vendor: {self.name}\nService: {self.service}\nContact: {self.contact}"

    def send_invoice(self):
        print(f"{self.name} has sent an invoice for {self.event_name}.")

    def receive_payment(self):
        print(f"{self.name} has received payment for {self.event_name}.")


class Invitation(Event):
    def __init__(self, event_name, date, time, location, guest):
        super().__init__(event_name, date, time, location)
        self.guest = guest
        self.invitation_status = "Not Sent"
# variuos methods in the invitation class
    def __str__(self):
        return f"Guest: {self.guest.name}\nInvitation Status: {self.invitation_status}"

    def send_invitation(self):
        self.invitation_status = "Sent"
        print(f"Invitation sent to {self.guest.name} for {self.event_name}.")

    def update_status(self, status):
        self.invitation_status = status
        print(f"Invitation status updated to {self.invitation_status}.")


# Creating and event object fro the event class
event1 = Event("20th anniversary Celebration", "31 October 2026", "5:00 pm", "Tokyo")

# Creating guest object from the Guest class
guest1 = Guest(event1.event_name, event1.event_date, event1.event_time, event1.event_location, "Sammy", "sammilenium@gmail.com")
guest2 = Guest(event1.event_name, event1.event_date, event1.event_time, event1.event_location, "Edynas", "ededdeddy@gmail.com")
guest3 = Guest(event1.event_name, event1.event_date, event1.event_time, event1.event_location, "Williams", "wilhklyham@gmail.com")

# Creating a vendor objct and using class Vendor
vendor1 = Vendor(event1.event_name, event1.event_date, event1.event_time, event1.event_location, "Lux service", "Event Rental", "+1-(859)-(384)")

# Add Guests and Vendor
event1.add_guest(guest1)
event1.add_guest(guest2)
event1.add_guest(guest3)
print()
event1.add_vendor(vendor1)
print()
# Send Invitations
event1.send_invitations()

# sending invitations to the guests
invitation1 = Invitation(event1.event_name, event1.event_date, event1.event_time, event1.event_location, guest1)

invitation3 = Invitation(event1.event_name, event1.event_date, event1.event_time, event1.event_location, guest3)

invitation1.send_invitation()
invitation1.update_status("Accepted")
print()
invitation3.send_invitation()
invitation3.update_status("Accepted")
print("=======================")
guest1.rsvp("Accepted")
guest2.rsvp("Declined")
guest3.rsvp("Accepted")
print("=======================")

event1.track_rsvp()
guest1.check_in()
guest3.check_in()
print("===========================================================")
vendor1.send_invoice()
vendor1.receive_payment()
print("===========================================================")
print(f"\n{event1}\n")
print(f"{guest1}\n")
print(f"{guest3}\n")
print(f"{vendor1}")
print("=======================")
print(invitation1)     
print(invitation3)                                
