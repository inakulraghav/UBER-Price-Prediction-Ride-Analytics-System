
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import joblib
from PIL import Image,ImageTk

model = joblib.load(r'C:\Users\Lenovo\OneDrive\Desktop\Projects\IICS\model selection and training\uber_model.pkl')
scaler = joblib.load(r'C:\Users\Lenovo\OneDrive\Desktop\Projects\IICS\model selection and training\scaler.pkl')
features_list = joblib.load(r'C:\Users\Lenovo\OneDrive\Desktop\Projects\IICS\model selection and training\features_list.pkl')

def predict_price():
    try:
        vtat = float(ent_vtat.get())
        ctat = float(ent_ctat.get())
        dist = float(ent_dist.get())
        hour = int(ent_hour.get())
        if hour<0 or hour>23:
            messagebox.showerror("Invalid Input","Plzz enter correct hour between 0 to 23")
            return
        v_type = selected_vehicle.get()

        df = pd.DataFrame([[vtat, ctat, dist, hour,0,0,0,0,0,0]],columns=features_list)
        df[f"vehicle_type_{v_type}"]=1

        df = df[features_list]
        scaled_data = scaler.transform(df)
        pred_y = model.predict(scaled_data)[0]
        lbl_result.config(text=f"Estimated Price: ₹{round(pred_y, 2)}")
    
    except Exception as e:
        messagebox.showerror("Error", f"Invalid Input: {e}")

# gui
root = tk.Tk()
root.title("Uber Price Predictor")
root.geometry("900x670")
root.resizable(width=False,height=False)
root.config(bg="white")
logo = tk.PhotoImage(file=r"C:\Users\Lenovo\OneDrive\Desktop\Projects\IICS\pictures and logos\icons8-uber-50.png")
root.iconphoto(True, logo)

# bg image 
bg_image = Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Projects\IICS\pictures and logos\IntercityComfort.png")
bg_image = bg_image.resize((450, 550), Image.LANCZOS) 
bg_render = ImageTk.PhotoImage(bg_image)
img_label = tk.Label(root, image=bg_render, bg="white")
img_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# frame 
main_frame = tk.Frame(root, bg="black", padx=40, pady=30)
main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

# headings 
heading=tk.Label(main_frame, text="Ride Details", bg="black", fg="white", font=("Arial", 18, "bold"))
heading.pack(pady=(0, 20))

# ride Distance
tk.Label(main_frame,text="Ride Distance (km):",bg="black",fg="#AAAAAA",font=("Arial", 10, "bold")).pack(anchor="w", pady=(10, 0))
ent_dist = tk.Entry(main_frame,font=("Arial", 11, "bold"),width=30,bg="light grey",fg="black",relief="flat")
ent_dist.pack(anchor="w", pady=5, ipady=5)

# hour of Day
tk.Label(main_frame,text="Hour of Day (0-23):",bg="black",fg="#AAAAAA",font=("Arial", 10, "bold")).pack(anchor="w", pady=(10, 0))
ent_hour = tk.Entry(main_frame,font=("Arial", 11, "bold"),width=30,bg="light grey",fg="black",relief="flat")
ent_hour.pack(anchor="w", pady=5, ipady=5)

# avg VTAT
tk.Label(main_frame,text="Avg VTAT:",bg="black",fg="#AAAAAA",font=("Arial", 10, "bold")).pack(anchor="w", pady=(10, 0))
ent_vtat = tk.Entry(main_frame,font=("Arial", 11, "bold"),width=30,bg="light grey",fg="black",relief="flat")
ent_vtat.pack(anchor="w", pady=5, ipady=5)

# avg CTAT
tk.Label(main_frame,text="Avg CTAT:",bg="black",fg="#AAAAAA",font=("Arial", 10, "bold")).pack(anchor="w", pady=(10, 0))
ent_ctat = tk.Entry(main_frame,font=("Arial", 11, "bold"),width=30,bg="light grey",fg="black",relief="flat")
ent_ctat.pack(anchor="w", pady=5, ipady=5)

# vehicle type 
tk.Label(main_frame, text="Vehicle Type:", bg="black", fg="#AAAAAA", font=("Arial", 10, "bold")).pack(anchor="w", pady=(10, 0))
vehicles = ["Auto", "Bike", "eBike", "Go Sedan", "Premier Sedan", "Uber XL"]
selected_vehicle = tk.StringVar()
combo = ttk.Combobox(main_frame,textvariable=selected_vehicle,values=vehicles,width=30,font=("Arial", 10),state="readonly")
combo.pack(anchor="w", pady=10)

# predict button
btn_predict = tk.Button(main_frame, text="Calculate Fare", command=predict_price,bg="white", fg="black", font=("Arial", 12, "bold"), width=25, pady=10, relief="flat",cursor="hand2")
btn_predict.pack(pady=25)
btn_predict.bind("<Enter>", lambda e: btn_predict.config(bg="green", fg="black"))
btn_predict.bind("<Leave>", lambda e: btn_predict.config(bg="white", fg="black"))

# result 
lbl_result = tk.Label(main_frame, text="", font=("Arial", 18, "bold"), bg="black", fg="green")
lbl_result.pack()
root.mainloop()


