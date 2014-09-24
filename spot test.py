#tavonga mudzana
#24/09/2014
#spot check

print("hello please enter the following dimensions")

pool_width=float(input("please enter the width of the pool: "))
pool_length=float(input("please enter the length of the pool: "))
pool_depth=float(input("please enter the depth of the pool: "))

mainsection_volume=pool_length*pool_width*pool_depth

circle_radius=pool_width/2

circle_area=3.14*(circle_radius*circle_radius)

half_circle_volume=(circle_area/2)*pool_depth

pool_volume=mainsection_volume+half_circle_volume

print("pool voume ={0}".format(pool_volume))

