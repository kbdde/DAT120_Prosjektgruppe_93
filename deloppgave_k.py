from deloppgave_g import lineærregresjon
from lister_for_del_1 import temperaturer   
from lister_for_del_1 import temperaturer_tidspunkter   

<<<<<<< Updated upstream
a,b=lineærregresjon(temperaturer_tidspunkter, temperaturer)
print(a,b)

if a > 0 :
    print('trenden på temperaturen er stigende')
elif a < 0 :
    print('trenden på temperaturen er synkende')
else:
    print('Temperaturen trender ikke i disse tider')
=======
    sum_y_axis = 0
    for i in range(n):
        
        sum_y_axis += y_axis[i]
    
    gjennomsnitt_y = sum_y_axis / n
    
    a1=0
    for i in range(n):
        a1 += (x_axis[i]-gjennomsnitt_x)*(y_axis[i]-gjennomsnitt_y)

    a2=0
    for i in range(n):
        a2 += (x_axis[i]-gjennomsnitt_x)**2

    a= a1/a2

    b= gjennomsnitt_y-(a*gjennomsnitt_x)
    
    print ('f(x)='+str(a)+'x +'+str(b))
    return a, b
    
x_axis = [1, 6] 
y_axis = [5, -3] 
print(lineærregresjon(x_axis, y_axis))
>>>>>>> Stashed changes
