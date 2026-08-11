class Calendar:
    def __init__(self):
        self.events = {}

    def is_leap_year(self, year):
        return year % 4 == 0
        
    def get_days_in_month(self, month, year):
        match month: 
            case 1: 
                return 31 
            case 2: 
                if self.is_leap_year(year): 
                    return 29 
                else: 
                    return 28 
            case 3: 
                return 31 
            case 4: 
                return 30 
            case 5: 
                return 31 
            case 6: 
                return 30 
            case 7: 
                return 31 
            case 8: 
                return 31 
            case 9: 
                return 30 
            case 10: 
                return 31 
            case 11: 
                return 30 
            case 12: 
                return 31 
            case _: 
                return -1
    
    def get_month_name(self, month):
        match month:
            case 1: 
                return "January"
            case 2: 
                return "February"
            case 3: 
                return "March"
            case 4: 
                return "April"
            case 5: 
                return "May"
            case 6: 
                return "June"
            case 7: 
                return "July"
            case 8: 
                return "August"
            case 9: 
                return "September"
            case 10: 
                return "October"
            case 11: 
                return "November"
            case 12: 
                return "December"
            case _: 
                return "Invalid Month"
    
    def is_valid_date(self, day, month, year):
        if year < 2026 or year > 2028:
            print("[ERROR] Year must be between 2026 and 2028")
            return False
        if month < 1 or month > 12:
            print("[ERROR] Month must be between 1 and 12")
            return False
        
        max_days = self.get_days_in_month(month, year)

        if day < 1 or day > max_days:
            print(f"[ERROR] Day must be between 1 and {max_days} for {self.get_month_name(month)}, {year}")
            return False
        return True
    
    def add_event(self):
        print("\n--- ADD AN EVENT ----")
        print("Enter the date: ")

        year = int(input("Year(2026-2028): "))
        month = int(input("Month (1-12): "))
        day = int(input("Day: "))

        if not self.is_valid_date(day, month, year):
            return

        event_name = input("Enter event name: ")
        date_key = (year, month, day)

        if date_key not in self.events:
            self.events[date_key] = []

        self.events[date_key].append(event_name)

        print(f"\n[SUCCESS] Event '{event_name}' Added on {self.get_month_name(month)} {day}, {year}!")

    def view_events_on_date(self):
        print("\n--- VIEW EVENTS ON A DATE ----")
        print("Enter the date:")

        year = int(input("Year(2026-2028): "))
        month = int(input("Month (1-12): "))
        day = int(input("Day: "))

        if not self.is_valid_date(day, month, year):
            return

        date_key = (year, month, day)

        if date_key in self.events:
            print(f"\nEvents on {self.get_month_name(month)} {day}, {year}:")
            for event in self.events[date_key]:
                print(f"- {event}")
        else:
            print("[INFO] No events found for this date.")

    def view_all_events(self):
        print("\n--- VIEW ALL EVENTS ----")

        if not self.events:
            print("[INFO] No events available.")
            return

        for (year, month, day) in sorted(self.events):
            print(f"\n{self.get_month_name(month)} {day}, {year}:")
            for event in self.events[(year, month, day)]:
                print(f"- {event}")

    def delete_event(self):
        print("\n--- DELETE AN EVENT ----")
        print("Enter the date:")

        year = int(input("Year(2026-2028): "))
        month = int(input("Month (1-12): "))
        day = int(input("Day: "))

        if not self.is_valid_date(day, month, year):
            return

        date_key = (year, month, day)

        if date_key not in self.events:
            print("[INFO] No events found for this date.")
            return

        print("\nEvents:")
        for i, event in enumerate(self.events[date_key], start=1):
            print(f"{i}. {event}")

        choice = int(input("Enter event number to delete: "))

        if 1 <= choice <= len(self.events[date_key]):
            removed = self.events[date_key].pop(choice - 1)
            print(f"[SUCCESS] Event '{removed}' deleted!")

            if not self.events[date_key]:
                del self.events[date_key]
        else:
            print("[ERROR] Invalid choice!")

def main():
    cal = Calendar()

    while True:
        print("\n---- MAIN MENU----")
        print("1. Add an Event")
        print("2. View Events on a Date")
        print("3. View All Events")
        print("4. Delete an Event")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            cal.add_event()
        elif choice == "2":
            cal.view_events_on_date()
        elif choice == "3":
            cal.view_all_events()
        elif choice == "4":
            cal.delete_event()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("[ERROR] Invalid choice!")
            
if __name__ == "__main__":
    main()