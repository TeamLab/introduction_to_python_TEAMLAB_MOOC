import fah_converter

print ("Enter a celsius value: "),
celsius = float(input())
fahrenheit = fah_converter.covert_c_to_f(celsius) # my_module의 c_to_f 호출
print ("That's ", fahrenheit, " degrees Fahrenheit")
