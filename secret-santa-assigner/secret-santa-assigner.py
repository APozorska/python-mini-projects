"""
Secret Santa - Classic Class Implementation with Couples and Singles (Anonymized)

This script assigns each participant a Secret Santa recipient while excluding:
- themselves,
- their partner (if applicable),
- and ensuring unique assignments.

Participants are divided into couples and singles. Email notification functionality is included but disabled by default.

Before use, replace participant names and emails with real data!
"""

import random
import smtplib

class SecretSanta:
    # Example group of participants: couples and singles
    list_couples = [('ParticipantA1', 'ParticipantA2'),
                    ('ParticipantB1', 'ParticipantB2'),
                    ('ParticipantC1', 'ParticipantC2')]
    list_singles = ['Single1', 'Single2']

    # Build a dictionary of partners from the couples list
    dict_partners = {}
    for person1, person2 in list_couples:
        dict_partners[person1] = person2
        dict_partners[person2] = person1

    # Example, generic emails corresponding to participants (replace with your own)
    mails = {
        'ParticipantA1': 'participanta1@example.com',
        'ParticipantA2': 'participanta2@example.com',
        'ParticipantB1': 'participantb1@example.com',
        'ParticipantB2': 'participantb2@example.com',
        'ParticipantC1': 'participantc1@example.com',
        'ParticipantC2': 'participantc2@example.com',
        'Single1': 'single1@example.com',
        'Single2': 'single2@example.com'
    }

    def __init__(self):
        # List of all participants: singles + people from couples
        self.list_people = [person for person in self.list_singles] + [person for couple in self.list_couples for person in couple]

    def draw_secret_santa(self):
        selected_people = []
        results = []

        for person in self.list_people:
            # Exclude people already selected, self, and partner (if exists)
            if person in self.dict_partners:
                people_not_selected_yet = [i for i in self.list_people if i not in selected_people and i != person and i != self.dict_partners[person]]
            else:
                people_not_selected_yet = [i for i in self.list_people if i not in selected_people and i != person]

            # Handle edge cases for couples to avoid assignment deadlocks
            if self.dict_partners:
                if (person == self.list_people[-4]
                        and (self.list_people[-2] in people_not_selected_yet)
                        and (self.list_people[-1] in people_not_selected_yet)):
                    selected_person = random.choice([self.list_people[-2], self.list_people[-1]])
                elif person == self.list_people[-3] and self.list_people[-2] in people_not_selected_yet:
                    selected_person = self.list_people[-2]
                elif person == self.list_people[-3] and self.list_people[-1] in people_not_selected_yet:
                    selected_person = self.list_people[-1]
                else:
                    selected_person = random.choice(people_not_selected_yet)
            # losowanie w sytuacji gdy sa same single
            else:
                # If only singles
                if person == self.list_people[-2] and self.list_people[-1] in people_not_selected_yet:
                    selected_person = self.list_people[-1]
                else:
                    selected_person = random.choice(people_not_selected_yet)
            selected_people.append(selected_person)
            results.append((person, selected_person))

        return results

    def send_info_email(self, results):
        # Warning: fill in SMTP data and password before sending emails
        user = 'your_email@example.com'
        password = 'your_password'

        for (person, selected_person) in results:
            message = f'''From: Secret Santa
Subject: Your Secret Santa Assignment!

Hi {person}!

You have been assigned to give a gift to: {selected_person}!
The agreed budget is: $35.
Remember to keep it a secret!

Good luck!
'''
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login(user, password)
                server.sendmail(user, self.mails[person], message)
                server.close()
                print(f'Email sent to {person}: {self.mails[person]}.')
            except Exception as e:
                print(f'Error sending email to {person}', e)


def main():

    secret_santa = SecretSanta()
    assignments = secret_santa.draw_secret_santa()
    secret_santa.send_info_email(assignments)


if __name__ == "__main__":
    main()
