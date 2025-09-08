#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
sukupuoli = input("Sukupuoli?")
hemoglobiiniarvo = int(input("Hemoglobiiniarvo?"))

if sukupuoli == "mies" and hemoglobiiniarvo <= 134:
    print("Hemoglobiinitasosi on alhainen.")

if sukupuoli == "mies" and hemoglobiiniarvo >=195:
    print("Hemoglobiinitasosi on korkea.")

elif sukupuoli == "mies" and  hemoglobiiniarvo >=134 <195:
    print("Hemoglobiinitasosi on normaali")

if sukupuoli == "nainen" and hemoglobiiniarvo <= 117:
    print("Hemoglobiinitasosi on alhainen.")

if sukupuoli == "nainen" and hemoglobiiniarvo >= 175:
    print("Hemoglobiinitasosi on korkea.")

elif sukupuoli == "nainen" and hemoglobiiniarvo >=117 <=175:
    print("Hemoglobiinitasosi on normaali.")


