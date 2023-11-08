# lib/helpers.py
from models.animal import Animal
from models.client import Client
from models.client_animal import Client_Animal

# import sqlite3
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

def create_client():
    name= input("Enter the client's name: ")
    type= input("Enter the client's event type: ")
    phone_number= input("Enter the client's phone number: ")
    try:
        client= Client.create(name, type, phone_number)
        print(f"Success: {client}")
    except Exception as exc:
        print("Error creating client: ", exc)
    

def find_client_by_id():
    id_= input("Enter client ID: ")
    client= Client.find_by_id(id_)
    if client: 
        print(f"Client {client.id}: {client.name}, event type: {client.type}, phone number: {client.phone_number}")
    
    
    
    else: 
        print(f"Client {id_} not found")


def delete_client():
    id_= input("Enter client's ID: ")
    if client := Client.find_by_id(id_):
        client.delete()
        print(f'Client {id_} deleted')
    else:
        print(f'Client {id_} not found')
   

def client_by_name():
    name = input("Enter client name: ")
    client = Client.find_by_name(name)
    print(client) if client else print(f"Client {name} not found")


def display_all_clients():
    clients = Client.display_all_clients()
    for client in clients:
        print(client)


def all_clients_by_type(): 
    choice = inquirer.select(
        message = "Select client type",
        choices = [
            "Corporate Seminar",
            "Team-Building Event",
            "Birthday Party",
            Choice(value=None, name="Go Back"),
        ],
        default = "name"
    ).execute()
# type= input('Enter client event type: ')
    clients= Client.view_by_type(choice)
    if clients:
        for client in clients:
            print(client)
    else:
        print("No clients have that event type")
    

def client_animals():
    id_= input("Enter client ID: ")
    client= Client.find_by_id(id_)
    if client:
        for animal in client.animals():
            print(animal)
    else:
        print("Client doesn't exist")


def create_animal():
    name= input("Enter the animal's name: ")
    species= input("Enter the animal's species: ")
    breed= input("Enter the animal's breed: ")
    skill= input("Enter the animal's skill: ")
    try:
        animal= Animal.create(name, species, breed, skill)
        print(f"Success: {animal}")
    except Exception as exc:
        print("Error creating animal: ", exc)


def find_animal_by_id():
    id_= input("Enter animal ID: ")
    animal= Animal.find_by_id(id_)
    print(animal) if animal else print(f"Animal {id_} not found")

def delete_animal():
    id_= input("Enter animal's ID: ")
    if animal := Animal.find_by_id(id_):
        animal.delete()
        print(f'Animal {id_} deleted')
    else:
        print(f'Animal {id_} not found')

def display_all_animals():
    animals= Animal.all()
    for animal in animals:
        print(animal)

def find_animal_by_species():
    species= input("Enter animal species: ")
    animals= Animal.find_by_species(species)
    if animals:
        for animal in animals:
            print(animal)
    else:
        print("None of our animals belong to that species")

def find_animal_by_name():
    name= input("Enter animal name: ")
    animal= Animal.find_by_name(name)
    print(animal) if animal else print(f"Animal {name} not found")

def animal_clients():
    id_= input("Enter animal id: ")
    animal= Animal.find_by_id(id_)
    if animal:
        for client in animal.clients():
            print(client)
    else:
        print("Animal doesn't exist")


def create_event():
    event_date = input("Enter event date: ")
    client_id = input("Enter client ID: ")
    animal_id = input("Enter animal ID: ")
    try:
        new_event = Client_Animal.create(event_date, int(client_id), int(animal_id))
        print(f"Event created: {new_event}")
    except Exception as exc:
        print("Error creating event: ", exc)

def find_event_by_id():
    id_ = input("Enter event ID: ")
    event = Client_Animal.find_by_id(id_)
    print(event) if event else print(f"Event {id_} not found")

def delete_event():
    id_ = input("Enter event ID: ")
    if event := Client_Animal.find_by_id(id_):
        event.delete()
        print(f"Event {id_} deleted")
    else:
        print(f"Event {id_} not found")

def display_all_events():
    events = Client_Animal.view_all()
    for event in events:
        print(event)

def event_by_date():
    date = input("Enter date: ")
    try:
        events = Client_Animal.find_by_date(date)
        for event in events:
            print(event)
    except Exception as exc:
        print("Error: ", exc)

def event_by_animal_type():
    species = inquirer.select(
        message = "Select animal type",
        choices = [
            "Dog",
            "Pony",
            Choice(value=None, name="Go Back"),
        ],
        default = "Dog"
    ).execute()
    if events := Client_Animal.find_by_animal_type(species):
        for event in events:
            print(event)
    else:
        print(f"No events found for animal species: {species}")

def event_by_client_type():
    type_ = input("Enter client event type: ")
    if events := Client_Animal.find_by_client_type(type_):
        for event in events:
            print(event)
    else:
        print(f"No events found for client event type: {type_}")

def show_available_animals():
    date = input("Enter date: ")
    try:
        if animals := Client_Animal.available_animals(date):
            for animal in animals:
                print(animal)
        else:
            print(f"No animals available on {date}")
    except Exception as exc:
        print("Error: ", exc)


def exit_program():
    print("Goodbye!")
    exit()
