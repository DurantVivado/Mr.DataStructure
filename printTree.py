'''
visualize a tree
@author: Durant
@email: durant2019@sina.com
'''
import turtle
printTree_switch = True
if printTree_switch:
    t = turtle.Turtle()
    t.penup()
    t.speed('fast')#'fastest' 'fast' 'normal' 'slow' 'slowest'
    t.shape('turtle')#arrow", "turtle", "circle", "square", "triangle", "classic"
class printTree():
    def __init__(self,tree):
        self.radius = 50
        self.level = 0
        self.branch_length = 4*self.radius
        self.node_memo = {}
        self.draw_binary_tree(tree,(0,300),self.level)
        
    def draw_node(self,data,start_pos):
        # draw the node
        (x,y) = start_pos
        length = len(str(data))
        t.setx(x);t.sety(y)
        t.pendown()
        t.setheading(0)
        t.circle(self.radius)
        t.penup();t.goto(x-length/2*16,y+self.radius-8);t.pendown()
        t.write(data, font=("Arial", 16, "normal"))
        t.penup()
        t.setx(x)
        t.sety(y)
    
    def draw_branch(self,start_pos,orient,level):
        #draw the branch
        (x,y) = start_pos
        t.setx(x);t.sety(y)
        t.pendown()
        t.setheading(180)
        if orient == 'left':
            t.left(15+20*level)
            t.forward(self.branch_length-level*20)
        elif orient == 'right':
            t.left(180-(15+20*level))
            t.forward(self.branch_length-level*20)
        t.penup()
        return t.pos()

    
    def draw_binary_tree(self,p,start_pos,level):
        (x,y) = start_pos
        self.node_memo[p] = (x,y+self.radius)
        if p!=None:
            level+=1
            print("level:",level)
            self.draw_node(p.data,(x,y))
            if p.left_child!=None:
                (x1,y1) = self.draw_branch((x,y),'left',level)
                self.draw_binary_tree(p.left_child,(x1,y1-2*self.radius),level)
            
            if p.right_child!=None:
                (x2,y2)=self.draw_branch((x,y),'right',level)
                self.draw_binary_tree(p.right_child,(x2,y2-2*self.radius),level)
    
    def get_node_coord(self,node)->tuple:
        #return the coord of the node circle centre
        return self.node_memo[node]
    
    def draw_line(self,coord1, coord2,pensize=5,pen_color='red'): #from 1 to 2
        (x,y) = coord1  
        t.penup()
        t.pensize(pensize)
        t.pencolor(pen_color)
        t.setx(x);t.sety(y)
        t.pendown()
        t.goto(coord2[0],coord2[1])
        
def thank_turtle():
    turtle.done() 