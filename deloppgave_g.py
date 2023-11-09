def lineaerregresjon(x_axis, y_axis):
       
    n=len(x_axis)
    sum_x_axis = 0
    for i in range(n):
    
        sum_x_axis += x_axis[i]
    
    gjennomsnitt_x = sum_x_axis / n

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
    

