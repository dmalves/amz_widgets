import configure_tests

import ttkbootstrap as ttk

from amz_widgets.help_frame import HelpFrame


if __name__ == "__main__":
    app = ttk.Window(
        title="Test HelpWindow Class",
        themename="litera",
        size = (800,800),
    )

    help_list = [
        ("Header1","text1",None),
    ]

    for i in range(1,11):
        ttk.Label(master=app,text=f"Text {i}").pack()
    
    frame = ttk.Frame(master=app)
    frame.pack()
    
    help_window = HelpFrame(window=app,parent_frame=frame,title="help example",help=help_list,)

    btn = ttk.Button(master=frame,text="press me!",command=lambda:help_window.show())
    btn.pack()
    

    app.mainloop()