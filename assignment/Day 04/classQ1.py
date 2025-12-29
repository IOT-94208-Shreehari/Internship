def km_to_m(km) :
    return km * 1000

def m_to_cm(m):
    return m *100

def cm_to_mm(cm):
    return cm *10

def feet_to_inches(feet):
    return feet * 12

def inches_to_cm(inches):
    return inches * 2.54

def distance_converter(distance , conversion_type , conversion_function) :
    result = conversion_function(distance)
    print(f"{distance}{conversion_type.split('_to_')[0]} = {result}{conversion_type.split('_to_')[1]}")

distance=float(input("Enter the distance: "))

print("<--------------------Distance conversion---------------->")
distance_converter(distance,"Km_to_m",km_to_m)
distance_converter(distance,"m_to_cm",m_to_cm)
distance_converter(distance,"cm_to_mm",cm_to_mm)
distance_converter(distance,"feet_to_inches",feet_to_inches)
distance_converter(distance,"inches_to_cm",inches_to_cm)
distance_converter(distance,"inches_to_cm",inches_to_cm)
