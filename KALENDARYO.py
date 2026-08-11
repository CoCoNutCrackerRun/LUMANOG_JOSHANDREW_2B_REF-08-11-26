import tkinter as tk
from tkinter import ttk, messagebox, font
import calendar
from datetime import datetime, date
import json
import os

SAVE_FILE = "my_calendar_events.json"
APP_TITLE = "My Class Calendar"
DAY_NAME = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
MONTH_NAMES = [calendar.month_name [i] for i in range (1,13)]

class EventManager:
    def __init__(self):
        self.events = {}
        self.load_events()
    def load_events(self):
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE,"r") as file:
                    print (f"Events Loaded From '{SAVE_FILE}' ")
            except Exception as error:
                print(f"Could Not Load Events: {error}")
                self.events = {}
        else:
            print ("No Save File Found.")
            self.events = {}
    def save_events(self):
        try:
            with open(SAVE_FILE, "w") as file:
                json.dump(self.events, file, indent=2)
                print (f"Could Not Save Events: {error}")
        except Exception as error:
            def get_date_key(self,year,month,day):
                return f"{year:04d}-{month:02d}-{day:02d}"
    def add_event(self,year,month,day,event_text,event_time):
        full_event = f"{event_time}-{event_text}"
        key = self.get_date_key(year,month,day)
        if key not in self.events:
            self.events[key] = []
        self.events[key].append(full_event)
        self.save_events()
    def get_events(self,year,month,day):
        key = self.get_date_key(year,month,day)
        return self.events.get(key,[])
    def delete_event(self,year,month,day,event_index):
        key = self.get_date_key(year,month,day)
        if key in self.events and 0 <= event_index <len(self.events[key]):
            del self.events[key][event_index]
        if not self.events[key]:
            del self.events[key]
            self.save_events()
            return True
        return False
    def has_events(self,year,month,day):
        key = self.get_date_key(year,month,day)
        return bool(self.events.get())
    
class CalendarApp:
    def __init__(self,root):
        self.root = root
        self.event_manager = EventManager()
        now = datetime.now()
        self.current_month = now.month
        self.current_year = now.year
        self.current_day = now.date.today()
        self.selected_day = None
        self.day_buttons = {}
        self.setup_window()
        self.build.ui()
        self.render_calendar
    def setup_window(self):
        self.root(APP_TITLE)
        self.root.configure(bg=COLORS ["bg_dark"])
        self.root.resizable(True,True)
        self.root.minsize(700,550)
        window_width = 860
        window_height = 680
        screen_width = self.root.winfo_screenwidth
        screen_height = self.root.winfo_screenheight
        x = (screen_width - window_width) //2
        y = (screen_height - window_height) //2
        self.root.geometry (f"{window_width}x{window_height}+{x}+{y}")
    def build_ui(self):
        self.main.frame = tk.Frame(self.root, bg=COLORS["bg_dark"])
        self.main_frame.pack(fill="both",expand=True,padx=12,pady=12)
        self.left_panel = tk.Frame(self.main_frame,bg=COLORS["bg-dark"])
        self.left_panel.pack(side="left",fill="both",expand=True)
        self.right_panel = tk.Frame(self.main_frame,bg=COLORS["bg_card"],width=240,relief="flat")
        self.right_panel.pack(side="right",fill="y",padx=(10,0))
        self.right_panel.pack_propagate(False)
        self.build_header()
        self.build_day_labels()
        self.build_calendar_grid()
        self.build_right_panel()
    def build_header(self):
        header = tk.Frame(self.left_panel,bg=COLORS["bg_header"],pady=8)
        prev_btn = tk.Button(
            header, 
            text="◄",
            bg=COLORS["bg_header"],
            fg=COLORS["text_secondary"],
            font = ("Courier", 14, "bold"),
            relief="flat",
            cursor="hand2",
            activebackground=COLORS["hover"],
            activebackground=COLORS["accent"],
            )
        prev_btn.pack(side="left",padx=8)
        self.header_label = tk.label(
            header,
            text="",
            bg=COLORS["bg_header"],
            fg=COLORS["text_primary"],
            font=("Courier", 18, "bold")
            )
        self.header_label.pack(side="left",expand=True)
        next_btn = tk.Button(
            header,
            text="►",
            command = self.go_next_month,
            bg=COLORS["bg_header"],
            fg=COLORS["text_secondary"],
            font = ("Courier", 14, "bold"),
            relief="flat",
            cursor="hand2",
            activebackground=COLORS["hover"],
            activebackground=COLORS["accent"],
            )
        next_btn.pack(side="right",padx=8)
        today_btn = ttk.Button(
            header,
            text="Today",
            command=self.go_to_today,
            bg=COLORS["today"],
            fg="#000",
            font=("Arial", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=8, pady=2
            )
        today_btn.pack(side="right",padx=4)
    def build_day_labels(self):
        day_header_frame = tk.Frame(self.left_panel, bg=COLORS["bg_dark"])
        day_header_frame.pack(fill="x",pady=(0,2))
        for i, day in enumerate(DAY_NAME):
            color=COLORS["weekend"] if i >=5 else COLOR["text_muted"]
            label = tk.Label(
                day_header_frame,
                text=day,
                bg=COLORS["bg_dark"],
                fg=color,
                font=("Arial", 9, "bold"),
                width=5
            )
            label.grid(row=0,column=i,padx=1,pady=2,sticky="nsew")
            day_header_frame.columnconfigure(i,weight=1)
    def build_calendar_grid(self):
        self.grid_frame = tk.Frame(self.left_panel, bg=COLORS['bg_dark'])
        self.grid_frame.pack(fill="both",expand=True)
        for col in range(7):
            self.grid_frame.columnconfigure(col,weight=1)
        for col in range(6):
            self.grid_frame.columnconfigure(col,weight=1)
    def build_right_panel(self):
        tk.Label(
            self.right_panel,
            text="📅 Events",
            bg=COLORS["bg_dark"],
            fg=COLORS["accent"],
            font=("Courier", 13, "bold"),
            anchor="w",
            padx=10,padx=12
        ).pack(fill="x")
        tk.Frame(self.right_panel, bg=COLORS["border"],height=1).pack(fill="x")
        self.selected_day = tk.Label(
            self.right_panel,
            text="Click a date to see events",
            bg=COLORS["bg_card"],
            fg=COLORS["text_secondary"],
            font=("Arial", 9),
            wraplength=200,
            justify="center",
            pady=8
        )
        self.selected_date_label.pack(fill="x", padx=8)
        self.events_frame = tk.Frame(self.right_panel, bg=COLORS["bg_card"])
        self.events_frame.pack(fill="both",expand=True, padx=8, pady=4)
        add_btn = tk.Button(
		self.right_panel,
		text="+ Add Event",
		command=self.open_add_event_dialog,
		bg=COLORS["accent"],
		fg="white",
		font=("Arial", 10, "bold"),
		relief="flat",
		cursor="hand2",
		pady=8,
		activebackground=COLORS["accent2"],
		activeforeground="white"
	    )
        add_btn.pack(fill="x", padx=12, pady=10, side="bottom")
    def render_calendar(self):
        self.header_label.config(
            text = f"{MONTH_NAMES[self.current_month -1]} {self.current_year}"
            )
        for widget in self.grid_frame.winfo_children():
            widget.destroy
        self.day_buttons = {}
        weeks = calendar.monthcalendar(self.current_year,self.current_month)
        for row_index, week in enumerate(week):
            for col_index, day_num in enumerate(week):
                if day_num == 0:
                    empty = tk.Frame(
                        self.grid_frame,
                        bg=COLORS["bg_dark"]
                    )
                    empty.grid(
                        row = row_index, column = col_index,
                        padx=2, pady=2, sticky="nsew"
                    )
                else:
                    self.create_day_button(row_index,col_index,day_num)