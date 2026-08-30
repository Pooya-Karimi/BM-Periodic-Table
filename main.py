# modules
import customtkinter as ctk
import json

# function
def show_element_details(element):
    element_window = ctk.CTkToplevel()
    element_window.title(element)
    element_window.geometry("750x500")
    element_window.resizable(False, False)
    element_window.iconbitmap("icon.ico")

    # title frame
    title_frame = ctk.CTkFrame(element_window, width=730, height=40)
    title_frame.pack(pady=5)
    ctk.CTkLabel(title_frame, text=f"{elements[element]["Basic Info"]["Name"]}", font=("Segoe UI", 20, "bold"), text_color="orange").pack()
    title_frame.pack_propagate(False)

    # properties frame
    properties_frame = ctk.CTkFrame(element_window,width=730,height=280)
    properties_frame.pack(padx=10, pady=5)
    properties_frame.pack_propagate(False)


    # basic info frame
    basic_info_frame = ctk.CTkFrame(properties_frame,width=236,height=280)
    basic_info_frame.pack(side="left", padx=5)
    basic_info_frame.pack_propagate(False)

    ctk.CTkLabel(basic_info_frame,text="======= Basic Info =======",text_color="red",font=("Segoe UI", 15, "bold")).pack()
    for k, v in elements[element]["Basic Info"].items():
        ctk.CTkLabel(basic_info_frame,text=f"{k}:  {v}",font=("Segoe UI", 15, "bold")).pack(anchor="w", pady=2)


    # physical properties frame
    physcal_properties_frame = ctk.CTkFrame(properties_frame,width=236,height=280)
    physcal_properties_frame.pack(side="left", padx=5)
    physcal_properties_frame.pack_propagate(False)

    ctk.CTkLabel(physcal_properties_frame,text="==== Physical Properties ====",text_color="red",font=("Segoe UI", 15, "bold")).pack()
    for k, v in elements[element]["Physical Properties"].items():
        ctk.CTkLabel(physcal_properties_frame,text=f"{k}:  {v}",font=("Segoe UI", 15, "bold")).pack(anchor="w", pady=15)


# atomic properties frame
    atomic_properties_frame = ctk.CTkFrame(properties_frame,width=236,height=280)
    atomic_properties_frame.pack(side="left", padx=5)
    atomic_properties_frame.pack_propagate(False)

    ctk.CTkLabel(atomic_properties_frame,text="==== Atomic Properties ====",text_color="red",font=("Segoe UI", 15, "bold")).pack()
    for k, v in elements[element]["Atomic Properties"].items():
        ctk.CTkLabel(atomic_properties_frame,text=f"{k}:  {v}",font=("Segoe UI", 13, "bold")).pack(anchor="w", pady=25)


    # uses
    uses_frame = ctk.CTkFrame(element_window, width=730, height=40)
    uses_frame.pack()
    ctk.CTkLabel(uses_frame,text="Uses        ==>",text_color="red",font=("Segoe UI", 15, "bold")).pack(side="left")
    uses = ""
    for v in elements[element]["Uses"]:
        uses += f"{v}   -   "
    ctk.CTkLabel(uses_frame, text=uses,font=("Segoe UI", 13, "bold")).pack(pady=5, side="left", padx=20)
    uses_frame.pack_propagate(False)

    # history
    history_frame = ctk.CTkFrame(element_window, width=730, height=40)
    history_frame.pack(pady=5)
    ctk.CTkLabel(history_frame,text="History    ==>",text_color="red",font=("Segoe UI", 15, "bold")).pack(side="left")
    ctk.CTkLabel(history_frame, text=f"Discoverer: {elements[element]["History"]["Discoverer"]} | Year: {elements[element]["History"]["Year"]} | Country: {elements[element]["History"]["Country"]}",font=("Segoe UI", 13, "bold")).pack(pady=5, side="left", padx=20)
    history_frame.pack_propagate(False)

    # fun fact
    fun_fact_frame = ctk.CTkFrame(element_window, width=730, height=40)
    fun_fact_frame.pack()
    ctk.CTkLabel(fun_fact_frame,text="Fun Fact  ==>",text_color="red",font=("Segoe UI", 15, "bold")).pack(side="left")
    ctk.CTkLabel(fun_fact_frame, text=f"{elements[element]["Fun Fact"]}",font=("Segoe UI", 13, "bold")).pack(pady=5, side="left", padx=20)
    fun_fact_frame.pack_propagate(False)

def show_table(category_colors, elements):
    for i in elements:
        if i == "La" or i == "Ac":
            ctk.CTkButton(Table_tab, text=i, fg_color=category_colors[elements[i]["Basic Info"]["Category"]], width=40, height=40, font=("Segoe UI", 13, "bold"), cursor="hand2", hover_color="darkred", border_width=1, border_color="#2B2B2B", command=lambda element=i:show_element_details(element)).grid(row=elements[i]["Basic Info"]["Period"], column=elements[i]["Basic Info"]["Group"] - 1)
        elif elements[i]["Basic Info"]["Category"] == "Lanthanide":
            ctk.CTkLabel(Table_tab, text=" ").grid(row=elements[i]["Basic Info"]["Period"] + 2, column=elements[i]["Basic Info"]["Atomic Number"] - 56)
            ctk.CTkButton(Table_tab, text=i, fg_color=category_colors[elements[i]["Basic Info"]["Category"]], width=40, height=40, font=("Segoe UI", 13, "bold"), cursor="hand2", hover_color="darkred", border_width=1, border_color="#2B2B2B", command=lambda element=i:show_element_details(element)).grid(row=elements[i]["Basic Info"]["Period"] + 3, column=elements[i]["Basic Info"]["Atomic Number"] - 55)
        elif elements[i]["Basic Info"]["Category"] == "Actinide":
            ctk.CTkButton(Table_tab, text=i, fg_color=category_colors[elements[i]["Basic Info"]["Category"]], width=40, height=40, font=("Segoe UI", 13, "bold"), cursor="hand2", hover_color="darkred", border_width=1, border_color="#2B2B2B", command=lambda element=i:show_element_details(element)).grid(row=elements[i]["Basic Info"]["Period"] + 4, column=elements[i]["Basic Info"]["Atomic Number"] - 87)
        else:
            ctk.CTkButton(Table_tab, text=i, fg_color=category_colors[elements[i]["Basic Info"]["Category"]], width=40, height=40, font=("Segoe UI", 13, "bold"), cursor="hand2", hover_color="darkred", border_width=1, border_color="#2B2B2B", command=lambda element=i:show_element_details(element)).grid(row=elements[i]["Basic Info"]["Period"], column=elements[i]["Basic Info"]["Group"] - 1)


# data
with open("elements.json", "r", encoding="utf-8") as f:
    elements = json.load(f)

category_colors = {
    "Alkali Metal": "#FF6347",
    "Alkaline Earth Metal": "#FFA500",
    "Transition Metal": "#4B0082",
    "Post-Transition Metal": "#228B22",
    "Metalloid": "#FFD700",
    "Nonmetal": "#00CED1",
    "Halogen": "#8B008B",
    "Noble Gas": "#1E90FF",
    "Lanthanide": "#FF69B4",
    "Actinide": "#FF4500"
}

# main window
window = ctk.CTk()
window.title("BM Periodic Table")
window.resizable(False, False)
window.geometry("750x500")
window.iconbitmap("icon.ico")

tabview = ctk.CTkTabview(window, segmented_button_selected_color="red", segmented_button_selected_hover_color="darkred")
tabview.pack(fill="both", expand=True, padx=5, pady=5)

Table_tab = tabview.add("Table")

# periodic table
show_table(category_colors, elements)

window.mainloop()