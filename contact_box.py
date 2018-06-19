from kivy.uix.widget import Widget
from kivy.uix.button import Button 
from kivy.uix.image import Image 
from kivy.uix.label import Label 

class ContactBox(Widget):               
    def __init__(self, contact_name, **kwargs):
        super(ContactBox, self).__init__(**kwargs) 
        self.contact_name = contact_name
    
        # Box button
        self.box_button = Button()
        self.box_button.size_hint = None, None
        self.box_button.width = 402
        self.box_button.height = 80

        # self.box_button.background_color = (255, 255, 255, 1)

        # Contact photo image
        self.contact_photo = Image()
        self.box_button.add_widget(self.contact_photo)
        self.contact_photo.source = ("interface/Home/contact.png")
        self.contact_photo.size_hint = (None, None)
        self.contact_photo.pos_hint = (None, None)
        self.contact_photo.size = (80, 80)
        self.contact_photo.pos = (0, 0)

        # Contact status img
        self.contact_img_status = Image()
        self.contact_img_status.source = ("interface/online.png")
        self.box_button.add_widget(self.contact_img_status)
        self.contact_img_status.size_hint = (None, None)
        self.contact_img_status.pos_hint = (None, None)
        self.contact_img_status.size = (80, 80)
        self.contact_img_status.pos = (330, self.contact_img_status.parent.y)
        
        # Contact name label
        self.lbl_name = Label()
        self.box_button.add_widget(self.lbl_name)
        self.lbl_name.text = self.contact_name
        self.lbl_name.size = (15, 120)
        self.lbl_name.pos = (90, self.contact_img_status.parent.y)

        self.add_widget(self.box_button) #

    def set_status(self, contact_status):
        if self.contact_status is True:
            self.contact_img_status.source = ("interface/online.png")
        elif self.contact_status is False:
            self.contact_img_status.source = ("interface/online.png")

# class Test(App):                        #
#     def build(self):                    #
#         return ContactBox("Joao")      
#         # return ContactBox("Joao")       #

# Test().run()                            #

