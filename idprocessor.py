import re

class idprocessor: 

    # Checks if a string has numbers
    def hasnumbers(self, input):
        return bool(re.search(r'\d', input))

    # Checking for names
    # Checking for all UPPER CASE words and obtaining name by process of elimination
    def namevalidator(self, input):
        # Ensuring that it is not PAN Number
        if not self.hasnumbers(input):
            return input
        return False

    # Checking output for PANNumber, returns the number if found
    def pannumbervalidator(self, input):
        regexmatch = re.search(r'[A-Z]{5}[0-9]{4}[A-Z]', input)
        if regexmatch is not None:
            return regexmatch.group()
        else:
            return "PAN not found!"

    # Checking output for Date of Birth, returns the number if found
    def datevalidator(self, input):
        regexmatch = re.search(r'\d{2}[-/]\d{2}[-/]\d{4}', input)
        if regexmatch is not None:
            return regexmatch.group()
        else: 
            return "Date of birth not found!"

    def postprocess(self, input):
        name = self.namevalidator(input)
        pannumber = self.pannumbervalidator(input)
        dateofbirth = self.datevalidator(input)
        
        output = "Your name is: " + name + "\n\n"
        output += "Your PAN Number is: " + pannumber + "\n\n"
        output += "Your date of birth is: " + dateofbirth
        return output