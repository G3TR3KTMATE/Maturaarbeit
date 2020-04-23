

# num beginnt mit 0 und hat somit nach der ersten for Schleife die Zahl, welche der 1 Buchstabe oder die erste Zahl in der utf-8 Umformung besitzt (1-256)
# zum Beispiel bei h = 104
# In der 2 forschleife kommt wird die alte Zahl mit 256 multipliziert und danach die andere zahl dazugerechnet
# Somit wird nach und nach eine Zahl generiert, welche die Information von allen Zahlen/Buchstaben enthält und man einfach zurückrechnen kann

def convert_to_num(s):
    bytes = s.encode("utf-8")
    num = 0
    for b in bytes:
        num = num * 256 + b
    return num


# Zuerst wird mit y herausgefunden um wie viele Buchstaben und Zahlen es sich handelt um diese Infomration danach an der unteren Vorschlefie weiterzugeben

# Die Zahl s wird dabei kopiert, weile diese in der while schlefie veraendert wird und man die Originalzahl im unteren Teil braucht

# Die 2 print Funktionen sind wieder nur für die ueberprüfung -- im jetzigen Standpunkt funktioniert etwas in der Enschluesslung nicht - die Liste wird nie laenger als 2 Zahlen :/

# Durch y wird jeder Buchstabe mit %256 zurueckverfolgt und der Liste angesetzt

# Mit der zweiten Linie wird das Resultat durch 256 geteilt und die Komma Zahl direkt abgeschrieben - somit ist der Prozess fehlerfrei wiederholbar

# Sie gerunden Zahlen sind im Programm nicht noetig aber damit möchte ich meine urspruengliche Loesung demonstrieren.
# Ich habe mehrere Tage an dem Fehler gescuht, da mein Programm ursprünglich nur 7 korrekte Buchtsabe/Zahlen zurückgegeben hat
# Der Fehler fand ich nach kompletten verzweifeln beim / der Rechnung - das Resultat wird unendlich Gross und geht unendlich in Komma Richtung
# Es gibt eine Minimale Abweichung, welches mein Programm ab der 7 Zahl zu einem Fehler veranlasste

def convert_to_text(s):
    word_list = []
    y = 1
    s_original = s
    while s > 256:
        s = s // 256
        y = y + 1
    print(y)
    while y >= 1:
        word_list.append(s_original % 256)
        s_original = s_original // 256
        print(s_original)
        s_original = s_original.__round__()
        print(s_original.__round__())
        y = y - 1
    print(word_list)
    barray = bytearray(word_list)
    barray.reverse()
    m = (barray.decode("utf-8"))
    return m


# Zuerst habe ich das Programm hier geschrieben und das beim Ausfuehren des Richtigen Programmes nicht dieser Code ausgeführt wird, steht dieser in dieser if funktion
# Nur wenn ich mich auf dieser Seite befinde und das Programm von hier aus starte, wird dieser Code auch ausgefuehrt

if __name__ == "__main__":
    input_m = input("Gebe eine Nachricht ein \n")
    word_list = []
    new_m = convert_to_num(input_m)
    print(new_m)
    convert_to_text(new_m)

# def convert_to_text(s, s_original):
#    y = 1
#    while s > 256:
#        s = s / 256
#        y = y + 1
#    print(y)
#    while y >= 1:
#        word_list.append(s_original % 256)
#        s_original = s_original / 256
#        print(s_original)
#        s_original = s_original.__round__()
#        print(s_original.__round__())
#        y = y - 1
#    print(word_list)
#    barray = bytearray(word_list)
#    barray.reverse()
#    print(barray.decode("utf-8"))

# def convert_to_text(s, s_original):
#    y = 1
#    while s > 256:
#        s = s / 256
#        y = y + 1
#    print(y)
#    while y >= 1:
#        n = y
#        n = n % 7
#        word_list.append(s_original % 256)
#        s_original = s_original / 256
#        print(s_original)
#        s_original = s_original.__round__()
#        print(s_original)
#        y = y - 1
#        if n == 0:
#           alte_word_list = word_list.copy()
#            word_list.clear
#       else:
#            alte_word_list = []
#    print(word_list)
#    barray1 = bytearray(word_list)
#    barray = bytearray(alte_word_list)
#    barray.reverse()
#    barray1.reverse()
#    print(barray1.decode("utf-8"))
#    print(barray.decode("utf-8"))
