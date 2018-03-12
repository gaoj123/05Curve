from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
edges = []
transform = new_matrix()

#Test Cases
#add_circle(edges, 250, 250, 0, 50, 500)
#add_curve(edges,121,305,340,278,-74,-273,29,241,500,"hermite")
#draw_lines(edges,screen,color)
#display(screen)

# print_matrix( make_translate(3, 4, 5) )
# print
# print_matrix( make_scale(3, 4, 5) )
# print
# print_matrix( make_rotX(math.pi/4) )
# print
# print_matrix( make_rotY(math.pi/4) )
# print
# print_matrix( make_rotZ(math.pi/4) )

#Mr. DW's script
color = [ 0, 255, 0 ]
#parse_file( 'script', edges, transform, screen, color )

#My script (mushroom)
color=[255,1,1]
parse_file( 'script2', edges, transform, screen, color )
