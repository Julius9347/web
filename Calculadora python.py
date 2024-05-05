Calculadora_activa = True
while Calculadora_activa:
    

    print(" ______________________")
    print("|     calculadora      |")
    print("|______________________|")
    print("|operantes disponibles:|")   #diseño de la calculadora
    print("|suma: +               |")
    print("|resta: -              |")
    print("|multiplicar: *        |")
    print("|dividir: /            |")
    print("|Potencia: **          |")
    print("|Resido de división: //|")
    print("|______________________|")
    operante = str (input("asigne un operador: "))
   

    sumar = "+"
    restar = "-"
    multi = "*" 
    dividir = "/"     #elecciones para operar
    poten = "**"
    residuo = "//"
    ope = sumar; restar; multi, dividir, poten; residuo

    if operante == sumar:
        n1 = (input("numero uno: "))   #variables numericas para operar
        if n1.isdigit():
             n2 = (input("numero dos: "))
             if n2.isdigit():
               result_suma = float (n1) + float (n2)
               print ("Su suma es =", result_suma)
             else:
                print("elija un número para poder operarlo.")
        else:
           print("elija un número para poder operarlo.")

    elif operante == restar:
      n1 = (input("numero uno: "))   #variables numericas para operar
      if n1.isdigit():
             n2 = (input("numero dos: "))
             if n2.isdigit():
               result_resta = float (n1) - float (n2)
               print ("Su resta es =", result_resta)
             else:
                print("elija un número para poder operarlo.")
      else:
           print("elija un número para poder operarlo.")

    elif operante == multi:
       n1 = (input("numero uno: "))   #variables numericas para operar
       if n1.isdigit():
             n2 = (input("numero dos: "))
             if n2.isdigit():
               result_multi = float (n1) * float (n2)
               print ("Su multiplicación es =", result_multi)
             else:
                print("elija un número para poder operarlo.")
       else:
           print("elija un número para poder operarlo.")

    elif operante == dividir:
       n1 = (input("numero uno: "))   #variables numericas para operar
       if n1.isdigit():
             n2 = (input("numero dos: "))
             if n2.isdigit():
               if n2 != "0":
                 result_dividir = float (n1) / float (n2)
                 print ("Su divición es =", result_dividir)
               else:
                   print("No es posible dividir por cero, por favor use otro numero.")
             else:
                print("elija un número para poder operarlo.")
       else:
           print("elija un número para poder operarlo.")

    elif operante == poten:
       n1 = (input("numero uno: "))   #variables numericas para operar
       if n1.isdigit():
             n2 = (input("numero dos: "))
             if n2.isdigit():
               result_poten = float (n1) ** float (n2)
               print ("Su operanter de la división es =", result_poten)
             else:
                print("elija un número para poder operarlo.")
       else:
           print("elija un número para poder operarlo.")

    elif operante == residuo:
       n1 = (input("numero uno: "))   #variables numericas para operar
       if n1.isdigit():
             n2 = (input("numero dos: "))
             if n2.isdigit():
               if n2 != "0":
                 result_residuo = float (n1) / float (n2)
                 print ("Su divición es =", result_residuo)
               else:
                   print("No es posible dividir por cero, por favor use otro numero.")
             else:
                print("elija un número para poder operarlo.")
       else:
           print("elija un número para poder operarlo.") 
 
    elif operante != ope:
       print("opcion invalida, por favor elija alguna de las opciones disponobles.")
       
    reinicio = input ("Ejecutar una nueva calculadora.")


      
