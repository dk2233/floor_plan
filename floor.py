lp1 = 72.5
ap1 = 13.0
distance = 0.8

#how many rows
a1 = 283.5
#length of room with length of one plank 
l1 = 215.0


class OneSection:
    def __init__(self,name, dx, dy, distance_from_wall, first_x_shorter , first_y_short = 0, whole_room_y = False):
        print("class of section ",name)
        self.nr_of_plank = (dx - distance_from_wall*2 - first_x_shorter) / lp1

        self.nr_of_x_part = (dx - distance_from_wall*2- first_x_shorter) % lp1 
        print("how many in l1 ", self.nr_of_plank)

        if whole_room_y is not True: 
            y_m = 1
        else:
            y_m = 2
           
        
        print(" last one ", self.nr_of_x_part) 
        if first_x_shorter != 0:
            print(" first one shorter ", first_x_shorter)

        self.how_many_rows = (dy - distance_from_wall * y_m - first_y_short) / ap1
        self.last_row = (dy - distance_from_wall * y_m - first_y_short) % ap1 
        if (first_y_short != 0):
            self.how_many_rows +=1.0


        

        print(" how many rows ",self.how_many_rows)
        print(" last row size ",self.last_row)




s1 = OneSection("near door", l1, a1, distance, 0)
s1a = OneSection("near door", l1, a1, distance, 72.5 - 24.0, 0)

sfull = OneSection("full", l1, 560, distance, 0, 0, True)
#sfull = OneSection("full 2", l1, 560, distance, 0, 10, True)





