h= float(input("According to your height and"))
w= int(input(" weight"))
result= w/(h**2)

if result < 18.5:
   print(". You are Underweight")
elif result >= 18.5 and result<25:
   print (". You are Normal")
elif result >=25 and result<30:
   print (". You are Overweight")
elif result >= 30:
   print (". You fall in the group of Obesity")
