import tkinter
import customtkinter


class ScrollableCheckBoxFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, item_list, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.checkbox_list = []
        for i, item in enumerate(item_list):
            self.add_item(item)

        def add_item(self, item):
            checkbox = customtkinter.CTkCheckBox(self, text=item)
            if self.command is not None:
                checkbox.configure(command=self.command)
            checkbox.grid(row=len(self.checkbox_list), column=0, pady=(0, 10))
            self.checkbox_list.append(checkbox)

        def remove_item(self, item):
            for checkbox in self.checkbox_list:
                if item == checkbox.cget("text"):
                    checkbox.destory()
                    self.checkbox_list.remove(checkbox)
                    return

        def get_checked_items(self):
            return [checkbox.cget("text") for checkbox in self.checkbox_list if checkbox.get() == 1]


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("ToDo App")
        self.geometry("720x480")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # create scrollable checkbox frame
        # self.scrollable_checkbox_frame = ScrollableCheckBoxFrame()


# Run app
if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    app = App()
    app.mainloop()
