def add_time(start, duration, *args):

    [H, MODE] = start.split(" ")
    [HORA, MIN] = H.split(":")
    [somaHORA, somaMIN] = duration.split(":")
    future_days = 0
  
    day_of_week = [
      "Sunday",
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday"
    ]

    total_horas = int(HORA) + int(somaHORA)
    total_mins = int(MIN) + int(somaMIN)

    if total_mins >= 60:
      total_mins -= 60
      total_horas += 1

    if total_mins < 10:
      total_mins = f"{total_mins}".zfill(2)    # Preenche a quantidade de caracteres sobrando com zeros

    if total_horas >= 12:
      [times, remain] = divmod(total_horas, 12)
      # Se o total_horas for menor que 12, atribui ao restante do divmod, se for igual a 12, atribui a total_horas
      total_horas = remain if remain else total_horas
      if total_horas > 12:
        # Se o total_horas for maior que 12 significa que não é igual (se fosse pararia na linha 22), portanto subtrai da quantidade de vezes que total_horas pode ser dividido por 12 MENOS as últimas 12 horas (times-1) multiplicado por 12 para ter o valor em HORAS.
        total_horas = total_horas - ((times-1) * 12)
        
  
      if times > 0:
        if MODE == 'PM':
          future_days = ((times-1) // 2) + 1
        else:
          future_days = times // 2
      
      if times > 0 and times % 2 != 0:
        MODE = "AM" if MODE == "PM" else "PM"
  
    new_time = str(total_horas) + ":"
    new_time += str(total_mins) + f" {MODE}"

    if args:
      day = args[0].title()
      if future_days > 0:
        index_of_param = day_of_week.index(day)
        index_of_param += future_days

        
        print(index_of_param)
        print(len(day_of_week))

        
        if index_of_param > len(day_of_week):
          index_of_param = index_of_param - future_days -1 
        elif index_of_param == len(day_of_week):
          index_of_param = index_of_param - 7
        else:
          index_of_param = index_of_param

        print(index_of_param)

        day = day_of_week[index_of_param]
          
      
      new_time += f", {day}"

    if future_days == 1:
      new_time += " (next day)"
    elif future_days > 1:
      new_time += f" ({future_days} days later)"
  

    return new_time

#print(add_time("11:30 AM", "2:32", "Monday"))

#print(add_time("10:10 PM", "3:30"))
#print(add_time("11:43 PM", "24:20", "Friday"))
#print(add_time("11:59 PM", "24:05", "Wednesday"))

#'Expected calling "add_time()" with "11:59 PM", "24:05", "Wednesday" to return "12:04 AM, Friday (2 days later)"')

#print(add_time("11:59 PM", "24:05", "Wednesday"))
#print(add_time("8:16 PM", "466:02", "tuesday"))
#print(add_time("2:59 AM", "24:00", "saturDay"))

#print(add_time("3:30 PM", "2:12", "Monday"))