# Contact Management Program

# Initialize an empty dictionary to store contacts
contacts = {}

def add_contact():
  # Prompt user to input contact information
  name = input("Enter contact name: ")
  phone = input("Enter contact phone number: ")
  email = input("Enter contact email address: ")

  # Store contact information in the dictionary
  contacts[name] = {"phone": phone, "email": email}

  print(f"Contact '{name}' added successfully!")

def view_contacts():
  # Display the contact list
  print("Contact List:")
  for name, info in contacts.items():
    print(f"  {name}: {info['phone']} ({info['email']})")

def edit_contact():
  # Prompt user to input the contact name to edit
  name = input("Enter the contact name to edit: ")

  # Check if the contact exists
  if name in contacts:
    # Prompt user to input new contact information
    phone = input("Enter new phone number: ")
    email = input("Enter new email address: ")

    # Update the contact information
    contacts[name]["phone"] = phone
    contacts[name]["email"] = email

    print(f"Contact '{name}' updated successfully!")
  else:
    print("Contact not found.")

def delete_contact():
  # Prompt user to input the contact name to delete
  name = input("Enter the contact name to delete: ")

  # Check if the contact exists
  if name in contacts:
    # Delete the contact
    del contacts[name]
    print(f"Contact '{name}' deleted successfully!")
  else:
    print("Contact not found.")

def save_contacts():
  # Save the contacts to a file
  with open("contacts.txt", "w") as f:
    for name, info in contacts.items():
      f.write(f"{name}:{info['phone']}:{info['email']}\n")

  print("Contacts saved to file.")

def load_contacts():
  # Load the contacts from a file
  global contacts
  contacts = {}

  try:
    with open("contacts.txt", "r") as f:
      for line in f:
        name, phone, email = line.strip().split(":")
        contacts[name] = {"phone": phone, "email": email}
  except FileNotFoundError:
    pass

  print("Contacts loaded from file.")

# Main program
load_contacts()

while True:
  print("Contact Management Program")
  print("----------------------------")
  print("1. Add Contact")
  print("2. View Contacts")
  print("3. Edit Contact")
  print("4. Delete Contact")
  print("5. Save Contacts")
  print("6. Exit")

  choice = input("Enter your choice: ")

  if choice == "1":
    add_contact()
  elif choice == "2":
    view_contacts()
  elif choice == "3":
    edit_contact()
  elif choice == "4":
    delete_contact()
  elif choice == "5":
    save_contacts()
  elif choice == "6":
    break
  else:
    print("Invalid choice. Please try again.")
