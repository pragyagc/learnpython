car_command=""
started = False
while True:
  car_command=input("car command:  ").lower()
  if car_command == "start":
      if started:
            print("car is already started  ")
      else:
            started = True
            print("car started ...ready to go")
  elif car_command =="stop":
       if not started:
             print("car is already stopped")
       else:
             started=False
             print("car has been stopeed")
  elif car_command=="help":
       print("""
start=yo start the car
stop= stop the car
quit= quit
       """
       )
  elif car_command=="quit":
      break
else:
    print("i dont understand")