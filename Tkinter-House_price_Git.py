import tkinter as tk
from tkinter import ttk
from tkinter import StringVar, messagebox
from turtle import onclick
from tkinter import filedialog
import numpy
import pandas as pd
import tkinter as tk

# モデル作成は別途　jupyter notebook で実施　作成したモデルをpickle で復元
import pickle
from lightgbm import LGBMRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import StandardScaler


class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        master.geometry("640x480")
        master.title("House Price Predictor")

def predict():
    # 予測モデルの読み込み
    filename1 = 'C:/Users/####/Documents/Python/LightGBM_opt2.pkl2' 
    with open(filename1, mode='rb') as f:
        loaded_rf_model = pickle.load(f)
    filename2='C:/Users/#####/Documents/Python/LightGBM_opt2sc'
    with open(filename2, mode='rb') as f:
        sc= pickle.load(f)
    
    #　予測用データの設定（入力値から）
    dist=dist_iv.get()
    maguchi=maguchi_iv.get()
    area=area_iv.get()
    totalarea=totalarea_iv.get()
    roadwidth=roadwidth_iv.get()
    tikunen=tikunen_iv.get()
   
    
    input_data=numpy.array([dist, area, maguchi, totalarea, roadwidth, tikunen])
    X_test=input_data.reshape(1,-1)
    X_test_std=sc.transform(X_test)
    
    #　予測の実施
    y_pred = loaded_rf_model.predict(X_test_std)
    y_pred_man=numpy.round(y_pred/10000)
    
    #　予測結果の表示
    print (f'予測価格は{int(y_pred_man)}万円です')
    Label20=ttk.Label(root, text=f'予測価格は{int(y_pred_man)}万円です', font=("メイリオ","12")) 
    Label20.place(x=30, y=300)
    
def main():
    global root
    root = tk.Tk()
    app = Application(master=root)
    Label1=ttk.Label(root, text=u'住宅データを入力してください', font=("メイリオ","12","bold"))
    Label1.place(x=10, y=5, width=300, height=40)
    
    # x=df[['最寄駅：距離（分）','間口','面積（㎡）','延床面積（㎡）','前面道路：幅員（ｍ）','容積率（％）','築年数']]
    
    Label2=ttk.Label(root, text=u'最寄駅：距離（分）', font=("メイリオ","8")) 
    Label2.place(x=30, y=50)
    global dist_iv
    dist_iv=tk.IntVar()
    textBoxS_2=ttk.Entry(root, width=10, textvariable=dist_iv)
    textBoxS_2.place(x=30, y=80)
    
    Label3=ttk.Label(root, text=u'間口', font=("メイリオ","8")) 
    Label3.place(x=150, y=50)
    global maguchi_iv
    maguchi_iv=tk.IntVar()
    textBoxS_3=ttk.Entry(root, width=10, textvariable=maguchi_iv)
    textBoxS_3.place(x=150, y=80)
    
    Label4=ttk.Label(root, text=u'面積（㎡）', font=("メイリオ","8")) 
    Label4.place(x=250, y=50)
    global area_iv
    area_iv=tk.IntVar()
    textBoxS_4=ttk.Entry(root, width=10, textvariable=area_iv)
    textBoxS_4.place(x=250, y=80)
    
    Label5=ttk.Label(root, text=u'延床面積（㎡）', font=("メイリオ","8")) 
    Label5.place(x=350, y=50)
    global totalarea_iv
    totalarea_iv=tk.IntVar()
    textBoxS_5=ttk.Entry(root, width=10, textvariable=totalarea_iv)
    textBoxS_5.place(x=350, y=80)
    
    Label6=ttk.Label(root, text=u'前面道路：幅員（ｍ）', font=("メイリオ","8")) 
    Label6.place(x=30, y=130)
    global roadwidth_iv
    roadwidth_iv=tk.IntVar()
    textBoxS_6=ttk.Entry(root, width=10, textvariable=roadwidth_iv)
    textBoxS_6.place(x=30, y=160)
    
    Label7=ttk.Label(root, text=u'築年数', font=("メイリオ","8")) 
    Label7.place(x=150, y=130)
    global youseki_iv
    global tikunen_iv
    tikunen_iv=tk.IntVar()
    textBoxS_7=ttk.Entry(root, width=10, textvariable=tikunen_iv)
    textBoxS_7.place(x=150, y=160)

    
    Label10=ttk.Label(root, text=u'上記のデータから住宅価格を予測します。', font=("メイリオ","10")) 
    Label10.place(x=30, y=220)
    
    Button_1=ttk.Button(root, text=u'予　測',width=20, command=predict)
    Button_1.place(x=150, y=250)
    
    app.mainloop()


if __name__ == "__main__":
    main()

