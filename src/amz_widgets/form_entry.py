import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import DEFAULT

class FormEntry(ttk.Frame):

    def __init__(self, master, text:str, width:int, **kwargs) -> None:
               
        super().__init__(master=master,**kwargs)

        self._text = text
        self._width = width
        
       
        self._build()
        
        
    def _build(self):
        self._label = ttk.Label(master=self, text=self._text)
        self._label.pack(
            side=tk.TOP,
            anchor=tk.W,
            pady=2,
        )

        self._entry = ttk.Entry(
            master=self,
            width=self._width
        )
        self._entry.pack(
            side=tk.TOP,
            pady=2,
            fill=tk.X,
        )

    @property
    def entry(self) -> ttk.Entry:
        return self._entry
    
    @property
    def label(self) -> ttk.Label:
        return self._label





# Example of usage
if __name__ == "__main__":
    from ttkbootstrap.constants import PRIMARY, SECONDARY

    app = ttk.Window(
        title="Test FormEntry Class",
        themename="litera",
    )
    fentry1 = FormEntry(master=app,text="Name",width=50)
    fentry1.pack(side=tk.TOP, anchor=tk.W, padx=5, pady=5)

    fentry2 = FormEntry(master=app,text="Age",width=3)
    fentry2.pack(side=tk.TOP, anchor=tk.W, padx=5,pady=5)

    lbl1 = ttk.Label(master=app,text="")
    lbl1.pack(side=tk.TOP,pady=30)
    
    def _event(seconds):
        if seconds == 0:
            txt = "Done!"
            fentry1.label.configure(bootstyle=PRIMARY)
        else:
            txt = f'"Name" string will change in {seconds} seconds'
        lbl1.configure(text=txt)
        # "recursive" call
        if seconds > 0:
            app.after(1000, lambda: _event(seconds-1))

    
    _event(5)
   
    tk.mainloop()