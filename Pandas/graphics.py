from Pandas.Pandas import frame_principal
import matplotlib.pyplot as plt

dataset_teclado = frame_principal.loc[frame_principal['notebook']=='Rainbow Gaming Keyboard and Mouse Set For PS4/PS3/Xbox One LED Multi-Colored Changing Backlight Mouse']
dataset_notebook = frame_principal.loc[frame_principal['notebook']=='Refurbished Dell Gaming Computer Nvidia GT 1030 HDMI WiFi Quad i5 3.1GHz 8GB 500GB Windows 10 [Refurbished]']
dataset_teclado.rename(columns={'notebook':'Notebook','price':'Preço','star':'Star','reviews':'Reviews','data_inserida':'Data'}, inplace = True)

x = []
for i in range(1, 31):
    x.append(i)

plt.plot(x, dataset_teclado["Preço"])
plt.show()