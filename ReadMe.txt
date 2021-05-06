0. This is an attempt to create a Vaccine notification system for Windows systems. None of the creds that the user enters, leave the user's local machine, and hence respect's user's privacy. I am trying to better manage the user credentials on the local system.

1. Run the SETUP.bat "As an Administrator" and provide the required information.

2. Email ID and password is required as, the id you provide will email itself, so as to generate email notifications. None of the information you enter will leave your system. Check the main.py file for verifying the same. THE PASSWORD IS AN APPLICATION PASSWORD THAT YOU NEED TO GENERATE FROM GOOGLE APPPASSWORD FROM https://myaccount.google.com/apppasswords AFTER ENABLING 2-FACTOR AUTHENTICATION IN https://myaccount.google.com/security.

3. System will restart to make sure that the Notifier is seamlessly running in background. Make sure that you save all unsaved work.

4. To stop receiving notification, run the STOPNOTIF.py "As an Administrator", and when asked for an input, enter yes. System will restart to make sure that the Notifier has stopped in background.

5. Please protect user_details.txt, as it contains your gmail app password, I apologize for the careless handling of the user credentials...
