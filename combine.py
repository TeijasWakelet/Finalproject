"""
What this program does and why it was built:

The final project will aim to provide the user with guidance on the correct amount of medication that he/she has taken.
The program will ask the user for the amount of medication that he/she has taken and provide a detailed analysis of how
much medication they have missed or perhaps over dosed on. The program will showcase this information via a graphic on
a canvas, that is dynamic and adaptive to the input the user provides each time, i.e. on the amount of medication
that they have taken. Furthermore, the program will then seek to provide guidance on next steps for the user, depending
on the amount of medication that they have taken.

The above set of actions essentially is the core concept of an app that I had developed, which will aim to provide a
data driven line of communication between a psychiatrist/doctor and his/her patient. Often people suffering from
mental health illnesses often struggle with their daily functions, which sometimes adversely affects their intake of
the correct amount of medication and their power to recollect how much medication they have actually taken. This leads
to a very complicated situation, where the patient is then unable to provide proper feedback to the doctor, which
creates confusion in the treatment process and the patient's recovery cycle. This app and the mechanisms it is built
will aim to mitigate such an event from happening and its consequences, by allowing for the doctor to set up the
patients daily prescription on the app, which will then prompt the user to regularly input the exact amount of
medication that they have consumed in a day. This information will then be presented on a graphic and sent across to
the doctor on a daily basis (via the app). The doctor is then empowered by the information they receive, which will
enable them to make the right decisions going forward.

How this program works:

This program will make certain assumption before it begins to run. It will assume that the doctor has already set up
the patient on the app with the required amount of daily medication. This program has been built to be dynamic in it's
representation of the patient's input of the amount of medication they have consumed, via the use of visual graphics.
It has not been built to be adaptive to any changes made by the doctor to the amount of medication that the patient
needs to have on a daily basis, this change will have to be made manually for now. Perhaps through some mechanism it
can be built into the program in the future.

The user will be given two options:

Option 1: Reports generated for each Dose of the medication.

This option is for doctors who would like to administer a stronger level of visibility over their patient's consumption
habits. Particulary in instances of patients who are on very high doses of medication, this option provides a almost
"live" method of keeping track of overdoses and medications missed. Reports will be available when patient administers
the medication during all points of the day.

Option 2: Reports generated at the end of the day.

This option is great for the doctor to administer on a patient who doesn't require as much attention to detail on
their medication consumption. This method will showcase at the end of the day a report of all the medication that
the patient has had/not had and will update the app.

Future additions:

I will continue to work on this project going forward. The aim will be to create an IOS app that does all of the
above. I will also look into certain machine learning algorithms that could allow for the user to just take a picture
of all of the medication they are having from inside of the app. The app will then identify the medications and the
quantity of each of them and generate a report. I am not sure whether this can actually be done, but I am looking
forward to starting the process of figuring this out!


"""



from simpleimage import SimpleImage
import tkinter
import time
import random
from PIL import ImageTk
from PIL import Image


THYRONORM = 100.0

THYRONORM_NAME = "Thyronorm (100)"

BUPRON = 300.0

BUPRON_NAME = "Bupron (300)"

PROTHIADEN = 25.0

ATIVAN = 50.00

ATIVAN_NAME = "Ativan (50)"

ATIVAN_EVENING = 100.00

ATIVAN_EVENING_NAME = "Ativan (100)"

PREGACENT = 75.00

PREGACENT_NAME = "Pregacant (75)"

VITAMIN_D3 = 100.00

VITAMIN_D3_NAME = "Vitamin D3 (100)"

BETACAP_TR40 = 100.00

BETACAP_TR40_NAME = "Betacap TR40 (100)"

TIBOLONE = 100.00

TIBOLONE_NAME = "Tibolone (100)"

PROTHIADEN_NAME = "Prothiaden (25)"

CANVAS_WIDTH = 300

CANVAS_HEIGHT = 300

OVERDOSE = 2

CANVAS_HEIGHT_1 = 800

CANVAS_WIDTH_1 = 800



def main():

    # Checks if the user has had their medication based on the input that the user provides.
    ask_name = input("Hey there! What is your name?")
    # Asks the user for the doctor's contact number.
    enter_doctor_contact = input("Hey" + " " + str(ask_name) + " " + "What is your Doctor's contact number?")

    # Ask user what day it is.
    ask_day = input("Hey" + " " + str(ask_name) + " " + " what is the date today")

    # Ask user which report generation option they have been recommended by the doctor.

    ask_user = int(input("Hey" + " " + str(ask_name) + " " + " which type of report would you like to generate? Type "
                                                         "1 to generate report for each medicine or "
                                                             "type any other number for a different option"))

    report_generator = 0
    while report_generator != 1:

        if ask_user == 1:
            # Morning doseage = 9:00 - 11:00
            Morning_dose = 1
            while Morning_dose != OVERDOSE:
                print("Lets start recording the amount of medication you took in the morning.")
                # Morning dose of all medication
                Thyronorm = reminder_medication_1(ask_name, enter_doctor_contact, ask_day, THYRONORM, THYRONORM_NAME)
                Bupron = reminder_medication_1(ask_name, enter_doctor_contact, ask_day, BUPRON, BUPRON_NAME)
                Prothiaden = reminder_medication_1(ask_name, enter_doctor_contact, ask_day, PROTHIADEN, PROTHIADEN_NAME)
                VitaminD3 = reminder_medication_1(ask_name, enter_doctor_contact, ask_day, VITAMIN_D3, VITAMIN_D3_NAME)
                Morning_dose += 1

            # Afternoon doseage = 11:00 - 17:00
            Afternoon_dose = 1
            while Afternoon_dose != OVERDOSE:
                print("Lets start recording the amount of medication you took in the afternoon.")
                # Afternoon dose of all medication
                Ativan = reminder_medication_1(ask_name, enter_doctor_contact, ask_day, ATIVAN, ATIVAN_NAME)
                Betacap = reminder_medication_1(ask_name, enter_doctor_contact, ask_day, BETACAP_TR40, BETACAP_TR40_NAME)
                Afternoon_dose += 1

            #  night doseage = 21:00 - 23:59
            Night_dose = 1
            while Night_dose != OVERDOSE:
                # Night dose of all medication
                print("Lets start recording the amount of medication you took in the night.")
                Ativan_evening = reminder_medication_1(ask_name, enter_doctor_contact, ask_day,
                                                       ATIVAN_EVENING, ATIVAN_EVENING_NAME)
                Tibolone = reminder_medication_1(ask_name, enter_doctor_contact, ask_day, TIBOLONE, TIBOLONE_NAME)
                Night_dose += 1

            report_generator += 1
            break



        # Creation of a large canvas showcasing all the important information about patient's medication consumption.
        c1, c2, c3, c4, c5, c6, c7, c8 = make_canvas(300, 300, title=str(ask_name) + " " + "Medication")

        ask_user_1 = int(input("Hey" + " " + str(ask_name) + " " + " Type 2 for an end of the day report or any other "
                                                                   "number to end process"))

        if ask_user_1 == 2:

            # Morning doseage = 9:00 - 11:00
            Morning_dose = 1
            while Morning_dose != OVERDOSE:
                print("Lets start recording the amount of medication you took in the morning.")
                # Morning dose of all medication
                Thyronorm = reminder_medication(c1, ask_name, enter_doctor_contact, ask_day, THYRONORM, THYRONORM_NAME)
                Bupron = reminder_medication(c2, ask_name, enter_doctor_contact, ask_day,  BUPRON, BUPRON_NAME)
                Prothiaden = reminder_medication(c3, ask_name, enter_doctor_contact, ask_day,  PROTHIADEN, PROTHIADEN_NAME)
                VitaminD3 = reminder_medication(c4, ask_name, enter_doctor_contact, ask_day,  VITAMIN_D3, VITAMIN_D3_NAME)
                Morning_dose += 1

            # Afternoon doseage = 11:00 - 17:00
            Afternoon_dose = 1
            while Afternoon_dose != OVERDOSE:
                print("Lets start recording the amount of medication you took in the afternoon.")
                # Afternoon dose of all medication
                Ativan = reminder_medication(c5, ask_name, enter_doctor_contact, ask_day,  ATIVAN, ATIVAN_NAME)
                Betacap = reminder_medication(c6, ask_name, enter_doctor_contact, ask_day,  BETACAP_TR40, BETACAP_TR40_NAME)
                Afternoon_dose += 1

            #  night doseage = 21:00 - 23:59
            Night_dose = 1
            while Night_dose != OVERDOSE:
                # Night dose of all medication
                print("Lets start recording the amount of medication you took in the night.")
                Ativan_evening = reminder_medication(c7, ask_name, enter_doctor_contact, ask_day,
                                                     ATIVAN_EVENING, ATIVAN_EVENING_NAME)
                Tibolone = reminder_medication(c8, ask_name, enter_doctor_contact, ask_day, TIBOLONE, TIBOLONE_NAME)
                c8.mainloop()
                Night_dose += 1
        report_generator += 1
        break






def reminder_medication(canvas, find_name, doctor_contact, date, value_of_medication, name_of_medication):


    # Start of function that asks user for their input on how much medication they have had, returning back a canvas.
    # Makes sure that the user is guided back to enter right amount of medication if wrong input added.
    medication_take = 0
    while medication_take != 1:
        #Find out the amount of medication user has had.
        ask_dosage = int(input("Hey" + " " + str(find_name) + " " + "how many mg of" + " " + str(name_of_medication) +
                               " " + "did you have?"))
        # Checks if the user has had too little or too much of the medication.
        if ask_dosage <= value_of_medication or ask_dosage >= value_of_medication:
            missed_dose = float(value_of_medication - ask_dosage)
            missed_dose_percentage = (missed_dose / value_of_medication) * 100

            # If the percentage of the medication missed is o %.
            if missed_dose_percentage == 0:
                print("Well done, you have had the required dosage")

                # Showcases the % of the medication missed on the canvas.
                canvas.create_arc(93.75, 93.75, 187.5, 187.5, start=0, extent=359, fill="Green")
                canvas.create_oval(93.75, 93.75, 187.5, 187.5)
                canvas.create_line(140.62, 93.75, 140.62, 187.5)
                canvas.create_line(93.75, 140.62, 187.5, 140.62)
                # Borders for each canvas
                canvas.create_line(10, 10, 10, 290, fill="Red")
                canvas.create_line(10, 10, 290, 10, fill="Red")
                canvas.create_line(290, 10, 290, 290, fill="Red")
                canvas.create_line(10, 290, 290, 290, fill="Red")
                # Enters the name of the medication
                canvas.create_text(22, 30, anchor='w', font='Courier 14', text='Medication:' + " "
                                                                                + str(name_of_medication))
                # Enters the date
                canvas.create_text(22, 60, anchor='w', font='Courier 14', text='Date:' + " " + str(date))
                # Outlines how much of medication has been missed on the canvas.
                canvas.create_text(22, 240, anchor='w', font='Courier 14', text='Missed dosage:' + str(missed_dose)
                                                                                + 'mg!')
                canvas.create_text(22, 270, anchor='w', font='Courier 14',
                                   text='Well done!! :)', fill = "Green")

                medication_take += 1
                return
            # If the percentage of the medication missed is between 0 and 12.5 %.
            elif (missed_dose_percentage <= 12.5) and (missed_dose_percentage > 0):
                print("You have to add another" + str(missed_dose) + "mg to your dose of Thyronorm")

                # Showcases the % of the medication missed on the canvas.
                canvas.create_arc(93.75, 93.75, 187.5, 187.5, start=0, extent=45, fill="Red")
                canvas.create_oval(93.75, 93.75, 187.5, 187.5)
                canvas.create_line(140.62, 93.75, 140.62, 187.5)
                canvas.create_line(93.75, 140.62, 187.5, 140.62)
                # Borders for each canvas
                canvas.create_line(10, 10, 10, 290, fill="Red")
                canvas.create_line(10, 10, 290, 10, fill="Red")
                canvas.create_line(290, 10, 290, 290, fill="Red")
                canvas.create_line(10, 290, 290, 290, fill="Red")
                # Enters the name of the medication
                canvas.create_text(22, 30, anchor='w', font='Courier 14', text='Medication:' + " "
                                                                                + str(name_of_medication))
                # Enters the date
                canvas.create_text(22, 60, anchor='w', font='Courier 14', text='Date:' + " " + str(date))
                # Outlines how much of medication has been missed on the canvas.
                canvas.create_text(22, 240, anchor='w', font='Courier 14', text='Missed dosage:' + str(missed_dose)
                                                                                + 'mg!')
                # Outlines next steps for the patient depending on how much medication has been missed.
                canvas.create_text(22, 270, anchor='w', font='Courier 14',
                                   text='Please add' + " " + str(missed_dose) + " " + 'to next dose', fill = "Purple")

                medication_take += 1
                return
            # If the percentage of the medication missed is between 12.5 and 25 %.
            elif (missed_dose_percentage <= 25) and (missed_dose_percentage >= 12.5):
                print("You have to add another" + str(missed_dose) + "mg to your dose of Thyronorm")

                # Showcases the % of the medication missed on the canvas.
                canvas.create_arc(93.75, 93.75, 187.5, 187.5, start=0, extent=90, fill="Red")
                canvas.create_oval(93.75, 93.75, 187.5, 187.5)
                canvas.create_line(140.62, 93.75, 140.62, 187.5)
                canvas.create_line(93.75, 140.62, 187.5, 140.62)
                # Borders for each canvas
                canvas.create_line(10, 10, 10, 290, fill="Red")
                canvas.create_line(10, 10, 290, 10, fill="Red")
                canvas.create_line(290, 10, 290, 290, fill="Red")
                canvas.create_line(10, 290, 290, 290, fill="Red")
                # Enters the name of the medication
                canvas.create_text(22, 30, anchor='w', font='Courier 14', text='Medication:' + " "
                                                                                + str(name_of_medication))
                # Enters the date
                canvas.create_text(22, 60, anchor='w', font='Courier 14', text='Date:' + " " + str(date))
                # Outlines how much of medication has been missed on the canvas.
                canvas.create_text(22, 240, anchor='w', font='Courier 14', text='Missed dosage:' + str(missed_dose)
                                                                                + 'mg!')
                # Outlines next steps for the patient depending on how much medication has been missed.
                canvas.create_text(22, 270, anchor='w', font='Courier 14',
                                   text='Please add' + " " + str(missed_dose) + " " + 'to next dose', fill = "Purple")

                medication_take += 1
                return missed_dose_percentage
            # If the percentage of the medication missed is between 25 and 37.5 %.
            elif (missed_dose_percentage <= 37.5) and (missed_dose_percentage >= 25):
                print("You have to add another" + str(missed_dose) + "mg to your dose of Thyronorm")

                # Showcases the % of the medication missed on the canvas.
                canvas.create_arc(93.75, 93.75, 187.5, 187.5, start=0, extent=135, fill="Red")
                canvas.create_oval(93.75, 93.75, 187.5, 187.5)
                canvas.create_line(140.62, 93.75, 140.62, 187.5)
                canvas.create_line(93.75, 140.62, 187.5, 140.62)
                # Borders for each canvas
                canvas.create_line(10, 10, 10, 290, fill="Red")
                canvas.create_line(10, 10, 290, 10, fill="Red")
                canvas.create_line(290, 10, 290, 290, fill="Red")
                canvas.create_line(10, 290, 290, 290, fill="Red")
                # Enters the name of the medication
                canvas.create_text(22, 30, anchor='w', font='Courier 14', text='Medication:' + " "
                                                                                + str(name_of_medication))
                # Enters the date
                canvas.create_text(22, 60, anchor='w', font='Courier 14', text='Date:' + " " + str(date))
                # Outlines how much of medication has been missed on the canvas.
                canvas.create_text(22, 240, anchor='w', font='Courier 14', text='Missed dosage:' + str(missed_dose)
                                                                                + 'mg!')
                # Outlines next steps for the patient depending on how much medication has been missed.
                canvas.create_text(22, 270, anchor='w', font='Courier 14',
                                   text='Please add' + " " + str(missed_dose) + " " + 'to next dose', fill = "Purple")

                medication_take += 1
                return
            # If the percentage of the medication missed is between 37.5 and 50%.
            elif (missed_dose_percentage <= 50) and (missed_dose_percentage >= 37.5):
                print("You have to add another" + str(missed_dose) + "mg to your dose of Thyronorm")

                # Showcases the % of the medication missed on the canvas.
                canvas.create_arc(93.75, 93.75, 187.5, 187.5, start=0, extent=180, fill="Red")
                canvas.create_oval(93.75, 93.75, 187.5, 187.5)
                canvas.create_line(140.62, 93.75, 140.62, 187.5)
                canvas.create_line(93.75, 140.62, 187.5, 140.62)
                # Borders for each canvas
                canvas.create_line(10, 10, 10, 290, fill="Red")
                canvas.create_line(10, 10, 290, 10, fill="Red")
                canvas.create_line(290, 10, 290, 290, fill="Red")
                canvas.create_line(10, 290, 290, 290, fill="Red")
                # Enters the name of the medication
                canvas.create_text(22, 30, anchor='w', font='Courier 14', text='Medication:' + " "
                                                                                + str(name_of_medication))
                # Enters the date
                canvas.create_text(22, 60, anchor='w', font='Courier 14', text='Date:' + " " + str(date))
                # Outlines how much of medication has been missed on the canvas.
                canvas.create_text(22, 240, anchor='w', font='Courier 14', text='Missed dosage:' + str(missed_dose)
                                                                                + 'mg!')
                # Outlines next steps for the patient depending on how much medication has been missed.
                canvas.create_text(22, 270, anchor='w', font='Courier 14',
                                   text='Please add' + " " + str(missed_dose) + " " + 'to next dose', fill = "Purple")

                medication_take += 1
                return
            # If the percentage of the medication missed is 50 and 62.5 %.
            elif (missed_dose_percentage <= 62.5) and (missed_dose_percentage >= 50):
                print("You have to add another" + str(missed_dose) + "mg to your dose of Thyronorm")

                # Showcases the % of the medication missed on the canvas.
                canvas.create_arc(93.75, 93.75, 187.5, 187.5, start=0, extent=225, fill="Red")
                canvas.create_oval(93.75, 93.75, 187.5, 187.5)
                canvas.create_line(140.62, 93.75, 140.62, 187.5)
                canvas.create_line(93.75, 140.62, 187.5, 140.62)
                # Borders for each canvas
                canvas.create_line(10, 10, 10, 290, fill="Red")
                canvas.create_line(10, 10, 290, 10, fill="Red")
                canvas.create_line(290, 10, 290, 290, fill="Red")
                canvas.create_line(10, 290, 290, 290, fill="Red")
                # Enters the name of the medication
                canvas.create_text(22, 30, anchor='w', font='Courier 14', text='Medication:' + " "
                                                                                + str(name_of_medication))
                # Enters the date
                canvas.create_text(22, 60, anchor='w', font='Courier 14', text='Date:' + " " + str(date))
                # Outlines how much of medication has been missed on the canvas.
                canvas.create_text(22, 240, anchor='w', font='Courier 14', text='Missed dosage:' + str(missed_dose)
                                                                                + 'mg!')
                # Outlines next steps for the patient depending on how much medication has been missed.
                canvas.create_text(22, 270, anchor='w', font='Courier 14',
                                   text='Please call' + " " + str(doctor_contact) + " " + 'ASAP', fill = "Orange")

                medication_take += 1
                return
            # If the percentage of the medication missed is 62.5 and 75 %.
            elif (missed_dose_percentage <= 75) and (missed_dose_percentage >= 62.5):
                print("You have to add another" + str(missed_dose) + "mg to your dose of Thyronorm")

                # Showcases the % of the medication missed on the canvas.
                canvas.create_arc(93.75, 93.75, 187.5, 187.5, start=0, extent=270, fill="Red")
                canvas.create_oval(93.75, 93.75, 187.5, 187.5)
                canvas.create_line(140.62, 93.75, 140.62, 187.5)
                canvas.create_line(93.75, 140.62, 187.5, 140.62)
                # Borders for each canvas
                canvas.create_line(10, 10, 10, 290, fill="Red")
                canvas.create_line(10, 10, 290, 10, fill="Red")
                canvas.create_line(290, 10, 290, 290, fill="Red")
                canvas.create_line(10, 290, 290, 290, fill="Red")
                # Enters the name of the medication
                canvas.create_text(22, 30, anchor='w', font='Courier 14', text='Medication:' + " "
                                                                                + str(name_of_medication))
                # Enters the date
                canvas.create_text(22, 60, anchor='w', font='Courier 14', text='Date:' + " " + str(date))
                # Outlines how much of medication has been missed on the canvas.
                canvas.create_text(22, 240, anchor='w', font='Courier 14', text='Missed dosage:' + str(missed_dose)
                                                                                + 'mg!')
                # Outlines next steps for the patient depending on how much medication has been missed.
                canvas.create_text(22, 270, anchor='w', font='Courier 14',
                                   text='Please call' + " " + str(doctor_contact) + " " + 'ASAP', fill = "Orange")

                medication_take += 1
                return

            # If the percentage of the medication missed is 75 and 87.5 %.
            elif (missed_dose_percentage <= 87.5) and (missed_dose_percentage > 75):
                print("You have to add another" + str(missed_dose) + "mg to your dose of Thyronorm")

                # Showcases the % of the medication missed on the canvas.
                canvas.create_arc(93.75, 93.75, 187.5, 187.5, start=0, extent=315, fill="Red")
                canvas.create_oval(93.75, 93.75, 187.5, 187.5)
                canvas.create_line(140.62, 93.75, 140.62, 187.5)
                canvas.create_line(93.75, 140.62, 187.5, 140.62)
                # Borders for each canvas
                canvas.create_line(10, 10, 10, 290, fill="Red")
                canvas.create_line(10, 10, 290, 10, fill="Red")
                canvas.create_line(290, 10, 290, 290, fill="Red")
                canvas.create_line(10, 290, 290, 290, fill="Red")
                # Enters the name of the medication
                canvas.create_text(22, 30, anchor='w', font='Courier 14', text='Medication:' + " "
                                                                                + str(name_of_medication))
                # Enters the date
                canvas.create_text(22, 60, anchor='w', font='Courier 14', text='Date:' + " " + str(date))
                # Outlines how much of medication has been missed on the canvas.
                canvas.create_text(22, 240, anchor='w', font='Courier 14', text='Missed dosage:' + str(missed_dose)
                                                                                + 'mg!')
                # Outlines next steps for the patient depending on how much medication has been missed.
                canvas.create_text(22, 270, anchor='w', font='Courier 14',
                                   text='Please call' + " " + str(doctor_contact) + " " + 'ASAP', fill = "Orange")

                medication_take += 1
                return
            # If the percentage of the medication missed is 87.5 and 100 %.
            elif (missed_dose_percentage <= 100) and (missed_dose_percentage > 87.5):
                # Showcases the % of the medication missed on the canvas.
                print("You have to add another" + str(missed_dose) + "mg to your dose of Thyronorm")

                canvas.create_arc(93.75, 93.75, 187.5, 187.5, start=0, extent=359, fill="Red")
                canvas.create_oval(93.75, 93.75, 187.5, 187.5)
                canvas.create_line(140.62, 93.75, 140.62, 187.5)
                canvas.create_line(93.75, 140.62, 187.5, 140.62)
                # Borders for each canvas
                canvas.create_line(10, 10, 10, 290, fill="Red")
                canvas.create_line(10, 10, 290, 10, fill="Red")
                canvas.create_line(290, 10, 290, 290, fill="Red")
                canvas.create_line(10, 290, 290, 290, fill="Red")
                # Enters the name of the medication
                canvas.create_text(22, 30, anchor='w', font='Courier 14', text='Medication:' + " "
                                                                                + str(name_of_medication))
                # Enters the date
                canvas.create_text(22, 60, anchor='w', font='Courier 14', text='Date:' + " " + str(date))
                # Outlines how much of medication has been missed on the canvas.
                canvas.create_text(22, 240, anchor='w', font='Courier 14', text='Missed dosage:' + str(missed_dose)
                                                                                + 'mg!')
                # Outlines next steps for the patient depending on how much medication has been missed.
                canvas.create_text(22, 270, anchor='w', font='Courier 14',
                                   text='Please call' + " " + str(doctor_contact) + " " + 'ASAP', fill = "Orange")

                medication_take += 1
                return
            # If the percentage of the medication is overdosed above o %.
            elif missed_dose_percentage < 0:
                print("ALERT: You have overdosed your medication, please seek further help")

                # Showcases the % of the medication overdosed on the canvas.
                canvas.create_arc(93.75, 93.75, 187.5, 187.5, start=0, extent=359, fill="Black")
                canvas.create_oval(93.75, 93.75, 187.5, 187.5)
                canvas.create_line(140.62, 93.75, 140.62, 187.5)
                canvas.create_line(93.75, 140.62, 187.5, 140.62)
                # Borders for each canvas
                canvas.create_line(10, 10, 10, 290, fill="Red")
                canvas.create_line(10, 10, 290, 10, fill="Red")
                canvas.create_line(290, 10, 290, 290, fill="Red")
                canvas.create_line(10, 290, 290, 290, fill="Red")
                # Enters the name of the medication
                canvas.create_text(22, 30, anchor='w', font='Courier 14', text='Medication:' + " "
                                                                                + str(name_of_medication))
                # Enters the date
                canvas.create_text(22, 60, anchor='w', font='Courier 14', text='Date:' + " " + str(date))
                # Outlines how much of medication has been overdosed on the canvas.
                canvas.create_text(22, 220, anchor='w', font='Courier 14', text='Alert!!')
                canvas.create_text(22, 240, anchor='w', font='Courier 14', text='Remove from next dose:' + " " +
                                                                                str(missed_dose) + " " + 'mg!')
                # Outlines next steps for the patient depending on how much medication has been missed.
                canvas.create_text(22, 270, anchor='w', font='Courier 14', text='Warning: Overdose!!', fill = "Red")

                medication_take += 1
                return
            # Invalid entry by the user.
            else:
                medication_take += 0



def reminder_medication_1(find_name, doctor_contact, date, value_of_medication, name_of_medication):


    # Start of function that asks user for their input on how much medication they have had, returning back a canvas.
    # Makes sure that the user is guided back to enter right amount of medication if wrong input added.
    medication_take = 0
    while medication_take != 1:
        #Find out the amount of medication user has had.
        ask_dosage = int(input("Hey" + " " + str(find_name) + " " + "how many mg of" + " " + str(name_of_medication) +
                               " " + "did you have?"))
        # Checks if the user has had too little or too much of the medication.
        if ask_dosage <= value_of_medication or ask_dosage >= value_of_medication:
            missed_dose = float(value_of_medication - ask_dosage)
            missed_dose_percentage = (missed_dose / value_of_medication) * 100

            # If the percentage of the medication missed is o %.
            if missed_dose_percentage == 0:
                print("Well done, you have had the required dosage")
                canvas = make_canvas1(CANVAS_WIDTH_1, CANVAS_HEIGHT_1, str(name_of_medication))
                # Showcases the % of the medication missed on the canvas.
                canvas.create_arc(250, 250, 500, 500, start=0, extent=360, fill="Red")
                canvas.create_oval(250, 250, 500, 500)
                canvas.create_line(375, 250, 375, 500)
                canvas.create_line(250, 375, 500, 375)
                # Borders for each canvas
                canvas.create_line(10, 10, 10, 790, fill="Red")
                canvas.create_line(10, 10, 790, 10, fill="Red")
                canvas.create_line(790, 10, 790, 790, fill="Red")
                canvas.create_line(10, 790, 790, 790, fill="Red")
                # Enters the name of the medication
                canvas.create_text(22, 50, anchor='w', font='Courier 42', text='Medication:' + " "
                                                                                + str(name_of_medication))
                # Enters the date
                canvas.create_text(22, 150, anchor='w', font='Courier 42', text='Date:' + " " + str(date))
                # Outlines how much of medication has been missed on the canvas.
                canvas.create_text(22, 600, anchor='w', font='Courier 42', text='Missed dosage:' + str(missed_dose)
                                                                                + 'mg!')
                canvas.create_text(22, 700, anchor='w', font='Courier 33',
                                   text='Well done!! :)', fill = "Green")
                canvas.mainloop()
                medication_take += 1
                return
            # If the percentage of the medication missed is between 0 and 12.5 %.
            elif (missed_dose_percentage <= 12.5) and (missed_dose_percentage > 0):
                print("You have to add another" + str(missed_dose) + "mg to your dose of Thyronorm")
                canvas = make_canvas1(CANVAS_WIDTH_1, CANVAS_HEIGHT_1, str(name_of_medication))
                # Showcases the % of the medication missed on the canvas.
                canvas.create_arc(250, 250, 500, 500, start=0, extent=45, fill="Red")
                canvas.create_oval(250, 250, 500, 500)
                canvas.create_line(375, 250, 375, 500)
                canvas.create_line(250, 375, 500, 375)
                # Borders for each canvas
                canvas.create_line(10, 10, 10, 790, fill="Red")
                canvas.create_line(10, 10, 790, 10, fill="Red")
                canvas.create_line(790, 10, 790, 790, fill="Red")
                canvas.create_line(10, 790, 790, 790, fill="Red")
                # Enters the name of the medication
                canvas.create_text(22, 50, anchor='w', font='Courier 42', text='Medication:' + " "
                                                                                + str(name_of_medication))
                # Enters the date
                canvas.create_text(22, 150, anchor='w', font='Courier 42', text='Date:' + " " + str(date))
                # Outlines how much of medication has been missed on the canvas.
                canvas.create_text(22, 600, anchor='w', font='Courier 42', text='Missed dosage:' + str(missed_dose)
                                                                                + 'mg!')
                # Outlines next steps for the patient depending on how much medication has been missed.
                canvas.create_text(22, 700, anchor='w', font='Courier 33',
                                   text='Please add' + " " + str(missed_dose) + " " + 'to next dose', fill = "Purple")
                canvas.mainloop()
                medication_take += 1
                return
            # If the percentage of the medication missed is between 12.5 and 25 %.
            elif (missed_dose_percentage <= 25) and (missed_dose_percentage >= 12.5):
                print("You have to add another" + str(missed_dose) + "mg to your dose of Thyronorm")
                canvas = make_canvas1(CANVAS_WIDTH_1, CANVAS_HEIGHT_1, str(name_of_medication))
                # Showcases the % of the medication missed on the canvas.
                canvas.create_arc(250, 250, 500, 500, start=0, extent=90, fill="Red")
                canvas.create_oval(250, 250, 500, 500)
                canvas.create_line(375, 250, 375, 500)
                canvas.create_line(250, 375, 500, 375)
                # Borders for each canvas
                canvas.create_line(10, 10, 10, 790, fill="Red")
                canvas.create_line(10, 10, 790, 10, fill="Red")
                canvas.create_line(790, 10, 790, 790, fill="Red")
                canvas.create_line(10, 790, 790, 790, fill="Red")
                # Enters the name of the medication
                canvas.create_text(22, 50, anchor='w', font='Courier 42', text='Medication:' + " "
                                                                                + str(name_of_medication))
                # Enters the date
                canvas.create_text(22, 150, anchor='w', font='Courier 42', text='Date:' + " " + str(date))
                # Outlines how much of medication has been missed on the canvas.
                canvas.create_text(22, 600, anchor='w', font='Courier 42', text='Missed dosage:' + str(missed_dose)
                                                                                + 'mg!')
                # Outlines next steps for the patient depending on how much medication has been missed.
                canvas.create_text(22, 700, anchor='w', font='Courier 33',
                                   text='Please add' + " " + str(missed_dose) + " " + 'to next dose', fill = "Purple")
                canvas.mainloop()
                medication_take += 1
                return
            # If the percentage of the medication missed is between 25 and 37.5 %.
            elif (missed_dose_percentage <= 37.5) and (missed_dose_percentage >= 25):
                print("You have to add another" + str(missed_dose) + "mg to your dose of Thyronorm")
                canvas = make_canvas1(CANVAS_WIDTH_1, CANVAS_HEIGHT_1, str(name_of_medication))
                # Showcases the % of the medication missed on the canvas.
                canvas.create_arc(250, 250, 500, 500, start=0, extent=135, fill="Red")
                canvas.create_oval(250, 250, 500, 500)
                canvas.create_line(375, 250, 375, 500)
                canvas.create_line(250, 375, 500, 375)
                # Borders for each canvas
                canvas.create_line(10, 10, 10, 790, fill="Red")
                canvas.create_line(10, 10, 790, 10, fill="Red")
                canvas.create_line(790, 10, 790, 790, fill="Red")
                canvas.create_line(10, 790, 790, 790, fill="Red")
                # Enters the name of the medication
                canvas.create_text(22, 50, anchor='w', font='Courier 42', text='Medication:' + " "
                                                                                + str(name_of_medication))
                # Enters the date
                canvas.create_text(22, 150, anchor='w', font='Courier 42', text='Date:' + " " + str(date))
                # Outlines how much of medication has been missed on the canvas.
                canvas.create_text(22, 600, anchor='w', font='Courier 42', text='Missed dosage:' + str(missed_dose)
                                                                                + 'mg!')
                # Outlines next steps for the patient depending on how much medication has been missed.
                canvas.create_text(22, 700, anchor='w', font='Courier 33',
                                   text='Please add' + " " + str(missed_dose) + " " + 'to next dose', fill = "Purple")
                canvas.mainloop()
                medication_take += 1
                return
            # If the percentage of the medication missed is between 37.5 and 50%.
            elif (missed_dose_percentage <= 50) and (missed_dose_percentage >= 37.5):
                print("You have to add another" + str(missed_dose) + "mg to your dose of Thyronorm")
                canvas = make_canvas1(CANVAS_WIDTH_1, CANVAS_HEIGHT_1, str(name_of_medication))
                # Showcases the % of the medication missed on the canvas.
                canvas.create_arc(250, 250, 500, 500, start=0, extent=180, fill="Red")
                canvas.create_oval(250, 250, 500, 500)
                canvas.create_line(375, 250, 375, 500)
                canvas.create_line(250, 375, 500, 375)
                # Borders for each canvas
                canvas.create_line(10, 10, 10, 790, fill="Red")
                canvas.create_line(10, 10, 790, 10, fill="Red")
                canvas.create_line(790, 10, 790, 790, fill="Red")
                canvas.create_line(10, 790, 790, 790, fill="Red")
                # Enters the name of the medication
                canvas.create_text(22, 50, anchor='w', font='Courier 42', text='Medication:' + " "
                                                                                + str(name_of_medication))
                # Enters the date
                canvas.create_text(22, 150, anchor='w', font='Courier 42', text='Date:' + " " + str(date))
                # Outlines how much of medication has been missed on the canvas.
                canvas.create_text(22, 600, anchor='w', font='Courier 42', text='Missed dosage:' + str(missed_dose)
                                                                                + 'mg!')
                # Outlines next steps for the patient depending on how much medication has been missed.
                canvas.create_text(22, 700, anchor='w', font='Courier 33',
                                   text='Please add' + " " + str(missed_dose) + " " + 'to next dose', fill = "Purple")
                canvas.mainloop()
                medication_take += 1
                return
            # If the percentage of the medication missed is 50 and 62.5 %.
            elif (missed_dose_percentage <= 62.5) and (missed_dose_percentage >= 50):
                print("You have to add another" + str(missed_dose) + "mg to your dose of Thyronorm")
                canvas = make_canvas1(CANVAS_WIDTH_1, CANVAS_HEIGHT_1, str(name_of_medication))
                # Showcases the % of the medication missed on the canvas.
                canvas.create_arc(250, 250, 500, 500, start=0, extent=225, fill="Red")
                canvas.create_oval(250, 250, 500, 500)
                canvas.create_line(375, 250, 375, 500)
                canvas.create_line(250, 375, 500, 375)
                # Borders for each canvas
                canvas.create_line(10, 10, 10, 790, fill="Red")
                canvas.create_line(10, 10, 790, 10, fill="Red")
                canvas.create_line(790, 10, 790, 790, fill="Red")
                canvas.create_line(10, 790, 790, 790, fill="Red")
                # Enters the name of the medication
                canvas.create_text(22, 150, anchor='w', font='Courier 42', text='Medication:' + " "
                                                                                + str(name_of_medication))
                # Enters the date
                canvas.create_text(22, 50, anchor='w', font='Courier 42', text='Date:' + " " + str(date))
                # Outlines how much of medication has been missed on the canvas.
                canvas.create_text(22, 600, anchor='w', font='Courier 42', text='Missed dosage:' + str(missed_dose)
                                                                                + 'mg!')
                # Outlines next steps for the patient depending on how much medication has been missed.
                canvas.create_text(22, 700, anchor='w', font='Courier 33',
                                   text='Please call' + " " + str(doctor_contact) + " " + 'immediately', fill = "Red")
                canvas.mainloop()
                medication_take += 1
                return
            # If the percentage of the medication missed is 62.5 and 75 %.
            elif (missed_dose_percentage <= 75) and (missed_dose_percentage >= 62.5):
                print("You have to add another" + str(missed_dose) + "mg to your dose of Thyronorm")
                canvas = make_canvas1(CANVAS_WIDTH_1, CANVAS_HEIGHT_1, str(name_of_medication))
                # Showcases the % of the medication missed on the canvas.
                canvas.create_arc(250, 250, 500, 500, start=0, extent=270, fill="Red")
                canvas.create_oval(250, 250, 500, 500)
                canvas.create_line(375, 250, 375, 500)
                canvas.create_line(250, 375, 500, 375)
                # Borders for each canvas
                canvas.create_line(10, 10, 10, 790, fill="Red")
                canvas.create_line(10, 10, 790, 10, fill="Red")
                canvas.create_line(790, 10, 790, 790, fill="Red")
                canvas.create_line(10, 790, 790, 790, fill="Red")
                # Enters the name of the medication
                canvas.create_text(22, 50, anchor='w', font='Courier 42', text='Medication:' + " "
                                                                                + str(name_of_medication))
                # Enters the date
                canvas.create_text(22, 150, anchor='w', font='Courier 42', text='Date:' + " " + str(date))
                # Outlines how much of medication has been missed on the canvas.
                canvas.create_text(22, 600, anchor='w', font='Courier 42', text='Missed dosage:' + str(missed_dose)
                                                                                + 'mg!')
                # Outlines next steps for the patient depending on how much medication has been missed.
                canvas.create_text(22, 700, anchor='w', font='Courier 33',
                                   text='Please call' + " " + str(doctor_contact) + " " + 'immediately', fill = "Red")
                canvas.mainloop()
                medication_take += 1
                return

            # If the percentage of the medication missed is 75 and 87.5 %.
            elif (missed_dose_percentage <= 87.5) and (missed_dose_percentage > 75):
                print("You have to add another" + str(missed_dose) + "mg to your dose of Thyronorm")
                canvas = make_canvas1(CANVAS_WIDTH_1, CANVAS_HEIGHT_1, str(name_of_medication))
                # Showcases the % of the medication missed on the canvas.
                canvas.create_arc(250, 250, 500, 500, start=0, extent=315, fill="Red")
                canvas.create_oval(250, 250, 500, 500)
                canvas.create_line(375, 250, 375, 500)
                canvas.create_line(250, 375, 500, 375)
                # Borders for each canvas
                canvas.create_line(10, 10, 10, 790, fill="Red")
                canvas.create_line(10, 10, 790, 10, fill="Red")
                canvas.create_line(790, 10, 790, 790, fill="Red")
                canvas.create_line(10, 790, 790, 790, fill="Red")
                # Enters the name of the medication
                canvas.create_text(22, 50, anchor='w', font='Courier 42', text='Medication:' + " "
                                                                                + str(name_of_medication))
                # Enters the date
                canvas.create_text(22, 150, anchor='w', font='Courier 42', text='Date:' + " " + str(date))
                # Outlines how much of medication has been missed on the canvas.
                canvas.create_text(22, 600, anchor='w', font='Courier 42', text='Missed dosage:' + str(missed_dose)
                                                                                + 'mg!')
                # Outlines next steps for the patient depending on how much medication has been missed.
                canvas.create_text(22, 700, anchor='w', font='Courier 33',
                                   text='Please call' + " " + str(doctor_contact) + " " + 'immediately', fill = "Red")
                canvas.mainloop()
                medication_take += 1
                return
            # If the percentage of the medication missed is 87.5 and 100 %.
            elif (missed_dose_percentage <= 100) and (missed_dose_percentage > 87.5):
                # Showcases the % of the medication missed on the canvas.
                print("You have to add another" + str(missed_dose) + "mg to your dose of Thyronorm")
                canvas = make_canvas1(CANVAS_WIDTH_1, CANVAS_HEIGHT_1, str(name_of_medication))
                canvas.create_arc(250, 250, 500, 500, start=0, extent=359, fill="Red")
                canvas.create_oval(250, 250, 500, 500)
                canvas.create_line(375, 250, 375, 500)
                canvas.create_line(250, 375, 500, 375)
                # Borders for each canvas
                canvas.create_line(10, 10, 10, 790, fill="Red")
                canvas.create_line(10, 10, 790, 10, fill="Red")
                canvas.create_line(790, 10, 790, 790, fill="Red")
                canvas.create_line(10, 790, 790, 790, fill="Red")
                # Enters the name of the medication
                canvas.create_text(22, 50, anchor='w', font='Courier 42', text='Medication:' + " "
                                                                                + str(name_of_medication))
                # Enters the date
                canvas.create_text(22, 150, anchor='w', font='Courier 42', text='Date:' + " " + str(date))
                # Outlines how much of medication has been missed on the canvas.
                canvas.create_text(22, 600, anchor='w', font='Courier 42', text='Missed dosage:' + str(missed_dose)
                                                                                + 'mg!')
                # Outlines next steps for the patient depending on how much medication has been missed.
                canvas.create_text(22, 700, anchor='w', font='Courier 33',
                                   text='Please call' + " " + str(doctor_contact) + " " + 'immediately', fill = "Red")
                canvas.mainloop()
                medication_take += 1
                return
            # If the percentage of the medication is overdosed above o %.
            elif missed_dose_percentage < 0:
                print("ALERT: You have overdosed your medication, please seek further help")
                canvas = make_canvas1(CANVAS_WIDTH_1, CANVAS_HEIGHT_1, str(name_of_medication))
                # Showcases the % of the medication overdosed on the canvas.
                canvas.create_arc(250, 250, 500, 500, start=0, extent=359, fill="Black")
                canvas.create_oval(250, 250, 500, 500)
                canvas.create_line(375, 250, 375, 500)
                canvas.create_line(250, 375, 500, 375)
                # Borders for each canvas
                canvas.create_line(10, 10, 10, 790, fill="Red")
                canvas.create_line(10, 10, 790, 10, fill="Red")
                canvas.create_line(790, 10, 790, 790, fill="Red")
                canvas.create_line(10, 790, 790, 790, fill="Red")
                # Enters the name of the medication
                canvas.create_text(22, 50, anchor='w', font='Courier 42', text='Medication:' + " "
                                                                                + str(name_of_medication))
                # Enters the date
                canvas.create_text(22, 150, anchor='w', font='Courier 42', text='Date:' + " " + str(date))
                # Outlines how much of medication has been overdosed on the canvas.
                canvas.create_text(22, 600, anchor='w', font='Courier 30', text='Alert!! Remove from next dose:' + " " +
                                                                                str(missed_dose) + " " + 'mg!',
                                   fill = "Red")
                # Outlines next steps for the patient depending on how much medication has been missed.
                canvas.create_text(22, 700, anchor='w', font='Courier 42', text='Warning: Overdose!!', fill = "Red")
                canvas.mainloop()
                medication_take += 1
                return
            # Invalid entry by the user.
            else:
                medication_take += 0






def turn_image_red(filename):
    Image = SimpleImage(filename)

    # Change colour of the image to red
    for pixel in Image:
        pixel.red = pixel.red
        pixel.green = pixel.green // 2
        pixel.blue = pixel.blue // 2

    return Image

######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height, title=None):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    objects = {}
    top = tkinter.Tk()
    top.minsize(width=width * 4, height=height * 2)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width=width, height=height, background = "white")
    canvas2 = tkinter.Canvas(top, width=width, height=height, background="white")
    canvas3 = tkinter.Canvas(top, width=width, height=height, background="white")
    canvas4 = tkinter.Canvas(top, width=width, height=height, background="white")
    canvas5 = tkinter.Canvas(top, width=width, height=height, background="white")
    canvas6 = tkinter.Canvas(top, width=width, height=height, background="white")
    canvas7 = tkinter.Canvas(top, width=width, height=height, background="white")
    canvas8 = tkinter.Canvas(top, width=width, height=height, background="white")
    canvas.place(x=0, y=0)
    canvas2.place(x=width, y=0)
    canvas3.place(x=width * 2, y=0)
    canvas4.place(x=width * 3, y=0)
    canvas5.place(x=0, y=height)
    canvas6.place(x=width, y=height)
    canvas7.place(x=width * 2, y=height)
    canvas8.place(x=width * 3, y=height)

    return canvas, canvas2, canvas3, canvas4, canvas5, canvas6, canvas7, canvas8

def make_canvas1(width, height, title=None):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    objects = {}
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # add this so (0, 0) works correctly
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    return canvas




if __name__ == '__main__':
    main()
