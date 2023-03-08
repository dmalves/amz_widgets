import tkinter as tk
import ttkbootstrap as ttk

from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.constants import PRIMARY

class HelpFrame:

    def __init__(self, window:tk.Misc,parent_frame:tk.Frame|ttk.Frame, title:str,help:list[tuple],callback=None, close_button_text="Close", width=400, height=200,):
        
        self._window = window
        self._parent_frame = parent_frame
        self._title = title
        self._help = help
        self._callback = callback
        self._close_button_text = close_button_text
        self._width = width
        self._height = height
        
        self._x = parent_frame.winfo_width() // 2
        self._y = parent_frame.winfo_height() // 2

        # to keep track off all images references
        self._images: list[tk.PhotoImage] = []

        self._build()
    
    def show(self):
        self._frm.place(x=self._x, y=self._y, in_=self._parent_frame)


    def _add_image(self, file_path:str) -> tk.PhotoImage:
        img = tk.PhotoImage(file=file_path)
        self._images.append(img)

        return img

    def _build(self):
        self._frm = ttk.Frame(master=self._window)
        # frm.place(x=self._x, y=self._y, in_=self._parent_frame)
        
        lbl_title = tk.Label(
            master=self._frm,
            text=self._title,
            font=("TkHeadingFont", "12", "bold"),
        )
        
        lbl_frm = ttk.LabelFrame(
                master=self._frm,
                labelwidget=lbl_title,
                bootstyle=PRIMARY, 
            )
        lbl_frm.pack()

        scrfrm = ScrolledFrame(
            master=lbl_frm,
            autohide=False,
            width=self._width,
            height=self._height,
        )
        scrfrm.pack()

        for header, text, icon in self._help:
            
            tk.Label(master=scrfrm, text=header, font=("TkHeadingFont", "10", "bold")).pack(
                side=tk.TOP,
                anchor=tk.W,
            )
            if icon:
                frm_icon = tk.Frame(master=scrfrm)
                frm_icon.pack(side=tk.TOP, anchor=tk.W)

                ttk.Label(master=frm_icon, text=text, font=("TkDefaultFont", "10"),).pack(
                    side=tk.LEFT,
                    padx=10,
                    anchor=tk.W,
                )
                img = self._add_image(icon)
                tk.Label(
                    master=frm_icon,
                    image=img,
                ).pack(
                    side=tk.LEFT,
                )
            else:
                ttk.Label(master=scrfrm, text=text, font=("TkDefaultFont", "10"),).pack(
                    side=tk.TOP,
                    padx=10,
                    anchor=tk.W,
                )

        def _command():
            if self._callback:
                self._callback()
            
            self._frm.place_forget()

        btn_close = ttk.Button(master=self._frm, text=self._close_button_text, command=_command)
        btn_close.pack(side=tk.BOTTOM, fill=tk.X)


# def mostrar_frame_ajuda(
#     window: tk.Misc,
#     título: str,
#     parente: ttk.Frame,
#     widget: ttk.Label | ttk.Button,
#     ajuda: list[tuple],
# ):
#     """Mostra frame de ajuda com botão de fechar.

#     * master: toplevel/window. Janela onde será mostrada a ajuda.
#     * título: título do frame de ajuda.
#     * parente: frame que servirá para posicionar a ajuda.
#     * widget: label ou button que será
#               desativado/ativado ao abrir/fechar a ajuda.
#     * ajuda: lista usada para construir a ajuda. É uma lista de tuple.
#     cada tuple tem CATEGORIA, TEXTO, IMAGEM. Imagem pode ser None.

#     exemplo:

#     ajuda [
#         ("CPF", "CPF é obrigatório para PF", "imagens/cpf.png")
#     ]


#     """
#     widget.config(state=tk.DISABLED)

#     x = parente.winfo_width() // 2
#     y = parente.winfo_height() // 2

#     frm_ajuda = ttk.Frame(master=window)
#     frm_ajuda.place(x=x, y=y, in_=parente)
#     lbl_título = tk.Label(
#         master=frm_ajuda,
#         text=título,
#         font=("TkHeadingFont", "12", "bold"),
#     )

#     lbl_frm = ttk.LabelFrame(
#         master=frm_ajuda,
#         labelwidget=lbl_título,
#         bootstyle=PRIMARY,  # type: ignore
#     )
#     lbl_frm.pack()
#     frm = ScrolledFrame(
#         master=lbl_frm,
#         autohide=False,
#         width=400,
#         height=200,
#     )
#     frm.pack()

#     for cabeçalho, texto, icone in ajuda:
#         tk.Label(master=frm, text=cabeçalho, font=("TkHeadingFont", "10", "bold")).pack(
#             side=tk.TOP,
#             anchor=tk.W,
#         )
#         if icone:
#             frm_icone = tk.Frame(master=frm)
#             frm_icone.pack(side=tk.TOP, anchor=tk.W)

#             ttk.Label(master=frm_icone, text=texto, font=("TkDefaultFont", "10"),).pack(
#                 side=tk.LEFT,
#                 padx=10,
#                 anchor=tk.W,
#             )
#             tk.Label(
#                 master=frm_icone,
#                 image=imagem_tk_cache(
#                     arquivo=icone,
#                     largura=24,
#                     altura=24,
#                 ),
#             ).pack(
#                 side=tk.LEFT,
#             )
#         else:
#             ttk.Label(master=frm, text=texto, font=("TkDefaultFont", "10"),).pack(
#                 side=tk.TOP,
#                 padx=10,
#                 anchor=tk.W,
#             )

#     def _cmd():
#         window.after(100, lambda: widget.config(state=tk.NORMAL))
#         frm_ajuda.place_forget()

#     btn_fechar = ttk.Button(master=frm_ajuda, text="Fechar", command=_cmd)
#     btn_fechar.pack(side=tk.BOTTOM, fill=tk.X)

