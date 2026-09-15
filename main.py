# modules
import customtkinter as ctk
import json

# function
def show_element_details(element):
    # element_window -----------------------------------------------
    element_window = ctk.CTkToplevel()
    element_window.title(element)
    element_window.geometry("750x500")
    element_window.resizable(False, False)
    element_window.iconbitmap("icon.ico")

    # element_title ------------------------------------------------
    title_frame = ctk.CTkFrame(element_window, width=730, height=40)
    title_frame.pack(pady=5)
    ctk.CTkLabel(title_frame, text=f"{elements[element]["Basic Info"]["Name"]}"
                , font=("Segoe UI", 20, "bold")
                , text_color="orange").pack()
    
    title_frame.pack_propagate(False)

    # element_show_details ------------------------------------------------------------
    properties_frame = ctk.CTkFrame(element_window,width=730,height=280)
    properties_frame.pack(padx=10, pady=5)
    basic_info_frame = ctk.CTkFrame(properties_frame,width=236,height=280)
    basic_info_frame.pack(side="left", padx=5)
    physcal_properties_frame = ctk.CTkFrame(properties_frame,width=236,height=280)
    physcal_properties_frame.pack(side="left", padx=5)
    atomic_properties_frame = ctk.CTkFrame(properties_frame,width=236,height=280)
    atomic_properties_frame.pack(side="left", padx=5)
    uses_frame = ctk.CTkFrame(element_window, width=730, height=40)
    uses_frame.pack()
    history_frame = ctk.CTkFrame(element_window, width=730, height=40)
    history_frame.pack(pady=5)
    fun_fact_frame = ctk.CTkFrame(element_window, width=730, height=40)
    fun_fact_frame.pack()

    parts = {
    "Basic Info": basic_info_frame,
    "Physical Properties": physcal_properties_frame,
    "Atomic Properties": atomic_properties_frame,
    "Uses": uses_frame,
    "History": history_frame,
    "Fun Fact": fun_fact_frame
    }

    x = 0

    for e in elements[element]:
        frame = parts[e]
        # title
        if e in ("Fun Fact", "Uses", "History"):
            ctk.CTkLabel(frame, text=f"{e:<10}  ==>", text_color="red", font=("Segoe UI", 15, "bold")).pack(side="left")
        else:
            ctk.CTkLabel(frame, text=f"======= {e} =======", text_color="red", font=("Segoe UI", 15, "bold")).pack() 

        # details
        if e == "Uses":
            uses = ""
            for i in elements[element][e]:
                uses += f"{i}  -  "
            ctk.CTkLabel(frame, text=uses, font=("Segoe UI", 15, "bold")).pack(pady=5, side="left", padx=20)

        elif e == "Fun Fact":
            ctk.CTkLabel(frame, text=elements[element][e], font=("Segoe UI", 15, "bold")).pack(pady=5, side="left", padx=20)

        elif e == "History":
            ctk.CTkLabel(frame, 
                        text=f"Discoverer: {elements[element][e]["Discoverer"]} | Year: {elements[element][e]["Year"]} | Country: {elements[element][e]["Country"]}", 
                        font=("Segoe UI", 13, "bold")).pack(pady=5, side="left", padx=20)

        else:
            for k, v in elements[element][e].items():
                ctk.CTkLabel(frame, text=f"{k}:  {v}",font=("Segoe UI", 15, "bold")).pack(anchor="w", pady=2)
            
        x += 1

    properties_frame.pack_propagate(False)
    basic_info_frame.pack_propagate(False)
    physcal_properties_frame.pack_propagate(False)
    atomic_properties_frame.pack_propagate(False)
    uses_frame.pack_propagate(False)
    history_frame.pack_propagate(False)
    fun_fact_frame.pack_propagate(False)

# data ======================================
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

# main window ===============================
window = ctk.CTk()
window.title("BM Periodic Table")
window.resizable(False, False)
window.geometry("750x500")
window.iconbitmap("icon.ico")

tabview = ctk.CTkTabview(window, segmented_button_selected_color="red", segmented_button_selected_hover_color="darkred")
tabview.pack(fill="both", expand=True, padx=5, pady=5)

Table_tab = tabview.add("🧪 Table")

# /=============== [tabs] ==================\
# TABLE TAB =================================
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

# ......... =================================

window.mainloop()