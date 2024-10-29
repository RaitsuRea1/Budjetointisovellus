import json

def main():
    budget_items = {
        "Vuokra": 0,
        "Vakuutukset": 0,
        "Kouluruokailu": 0,
        "Sähkö": 0,
        "Liikkuminen": 0
    }

    print("Syötä kuukausittaiset kulut:")
    for item in budget_items.keys():
        budget_items[item] = float(input(f"{item}: "))

    while True:
        print("\nValitse toiminto:")
        print("1. Lisää budjettikohde")
        print("2. Muokkaa budjettikohdetta")
        print("3. Tallenna budjetti")
        print("4. Lataa budjetti")
        print("5. Näytä budjetti")
        print("6. Lopeta")

        choice = input("Valinta: ")

        if choice == "1":
            add_budget_item(budget_items)
        elif choice == "2":
            edit_budget_item(budget_items)
        elif choice == "3":
            month = input("Syötä kuukauden nimi: ")
            save_budget(budget_items, month)
        elif choice == "4":
            month = input("Syötä kuukauden nimi: ")
            budget_items = load_budget(month)
            print("Budjetti ladattu:", budget_items)
        elif choice == "5":
            display_budget(budget_items)
        elif choice == "6":
            print("Lopetetaan ohjelma.")
            break
        else:
            print("Virheellinen valinta, yritä uudelleen.")

def add_budget_item(budget_items):
    new_item = input("Lisää uusi budjettikohde: ")
    amount = float(input(f"{new_item}: "))
    budget_items[new_item] = amount
    print(f"{new_item} lisätty budjettiin.")

def edit_budget_item(budget_items):
    item_to_edit = input("Minkä budjettikohteen haluat muokata? ")
    if item_to_edit in budget_items:
        new_amount = float(input(f"Uusi summa {item_to_edit}: "))
        budget_items[item_to_edit] = new_amount
        print(f"{item_to_edit} päivitetty.")
    else:
        print("Budjettikohdetta ei löydy.")

def save_budget(budget_items, month):
    with open(f"budget_{month}.json", "w") as file:
        json.dump(budget_items, file)
    print(f"Budjetti tallennettu kuukaudelle {month}.")

def load_budget(month):
    try:
        with open(f"budget_{month}.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Budjettia ei löydy.")
        return {}

def display_budget(budget_items):
    print("\nBudjetti:")
    for item, amount in budget_items.items():
        print(f"{item}: {amount}€")

if __name__ == "__main__":
    main()
