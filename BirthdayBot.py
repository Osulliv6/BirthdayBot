import requests
import datetime
import pytz

# GroupMe Bot ID 
GROUPME_BOT_ID = "fb8d0f5232f967db8ae3a8352c"

# dict of birthdays
BIRTHDAYS = {
    "Michael Kadus": "2000-11-16",
    "Michael Gorokhovsky": "2000-12-05",
    "Meredith Meyer": "2000-12-27",
    "Shreya Kurdukar": "2001-01-03",
    "Sofia Lopez": "2001-01-25",
    "Isabelle Yates": "2001-02-11",
    "Vin Silva": "2001-03-29",
    "Katy Zaloudek": "2001-04-02",
    "Raymond Shreve": "2001-04-16",
    "Aras Dapkus": "2001-05-18",
    "Bobby Albertson": "2001-06-26",
    "Adithya Iyengar": "2001-07-20",
    "Elisabeth Casetti": "2001-08-14",
    "Zachary Carpenter": "2001-08-25",
    "Alexa Stern": "2001-10-20",
    "Amanda Munsell": "2001-10-20",
    "Grace Mathews": "2002-01-08",
    "Joshua Facello": "2002-02-12",
    "Autumn Wuebben": "2002-05-02",
    "Ben Pekarek": "2002-05-11",
    "Kaitlyn Yu": "2002-05-16",
    "Ryan Stewart": "2002-06-26",
    "Eyal Pery": "2002-08-02",
    "Ben Pulver": "2002-08-22",
    "Adrienne Cibulka": "2002-08-24",
    "Roey Kuo": "2002-09-01",
    "Kaley Bahary": "2002-09-20",
    "Victoria Booth": "2002-10-27",
    "Braden Kirkendall": "2002-11-22",
    "Alexander Beuerle": "2002-11-23",
    "Eli Lechien": "2002-12-09",
    "Zoe Baker": "2003-02-01",
    "Ishika Mukherjee": "2003-03-11",
    "Landon Goetz": "2003-03-19",
    "Addison Clauss": "2003-03-29",
    "Heather Sledzinski": "2003-06-29",
    "Abdullah Alkazemi": "2003-08-15",
    "Kendall Gibson": "2003-08-24",
    "Sam Schwartz": "2003-10-09",
    "Emma Kessinger": "2003-11-26",
    "Rebecca Patino": "2003-12-31",
    "Nathaniel Petrucci": "2004-01-22",
    "Jaatani Abdi": "2004-03-03",
    "Sruthi Anil": "2004-03-05",
    "Paul Swift": "2004-04-07",
    "Kathleen O'Sullivan": "2004-06-05",
    "Devon Christner": "2004-06-21",
    "Gabriel Ogbalor": "2004-06-23",
    "Amartya Singh": "2004-07-27",
    "Michael Svara": "2004-07-29",
    "Caroline Bodnar": "2004-08-14",
    "Sydney Lawrence": "2004-08-20",
    "Lucia Morton": "2004-11-20",
    "Maximo Vedoya": "2004-12-21",
    "Cody Andis": "2005-01-13",
    "Logan O'Connell": "2005-01-13",
    "Karishma Dhayagude": "2005-01-28",
    "Eeshwar Doma": "2005-02-14",
    "Sedef Mergen": "2005-02-23",
    "Carter Holbrook": "2005-02-25",
    "Samuel Ahn": "2005-02-27",
    "Kaitlin Stephens": "2005-03-04",
    "Connor Kirkendall": "2005-04-07",
    "Sophia Guerrero": "2005-04-14",
    "Paige Bryan": "2005-05-18",
    "Cathy Kuo": "2005-06-24",
    "Ben Dimmic": "2005-09-15",
    "Ethan Williamson": "2005-09-26",
    "Madie Kim": "2006-01-15",
    "Dan Capka": "2006-01-25",
    "Kate Bradford": "2006-02-02",
    "Kate Bos": "2006-02-12",
    "Olivia DeScipio": "2006-03-06",
    "Tim Tkach": "2006-03-08",
    "Shivam Dave": "2006-03-28",
    "Annelie Gustafsson": "2006-04-02",
    "Ella Niemann": "2006-04-10",
    "Campbell Carlson": "2006-05-11",
    "Sydney Lin": "2006-06-15",
    "Stephanie Morin": "2006-07-02",
    "Ashwin Parab": "2006-07-08",
    "Sudeepthi Ravipati": "2006-08-02",
    "Kyra Li": "2006-08-17",
}


def check_birthdays():
    est = pytz.timezone("America/New_York") 
    today = datetime.datetime.now(est).date()

    for name, birthdate in BIRTHDAYS.items():
        birth_date = datetime.datetime.strptime(birthdate, "%Y-%m-%d").date()

        if today.month == birth_date.month and today.day == birth_date.day:
            age = today.year - birth_date.year
            send_birthday_message(name, age)

def send_birthday_message(name, age):
    message = f"@{name} is {age} today - Happy Birthday!!! 🎉🎂"
    url = "https://api.groupme.com/v3/bots/post"
    payload = {
        "bot_id": GROUPME_BOT_ID,
        "text": message
    }

    response = requests.post(url, json=payload)
    if response.status_code == 202:
        print(f"Sent birthday message for {name}")
    else:
        print(f"Failed to send message: {response.text}")

# Run the script at 9 AM EST
if __name__ == "__main__":
    check_birthdays()
