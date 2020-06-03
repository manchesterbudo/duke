import pygame;import pygame.locals
pygame.init()

BLACK=(0,0,0);RED=(255,0,0)
x,y,w,h=50,50,50,50
d=pygame.display.set_mode((500,500))
pygame.key.set_repeat(100,100)

points=[]
unlocked=True

done=False
while not done:

    pygame.event.pump()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        break
    if keys[pygame.K_d]:
        x+=50

    events=pygame.event.get()
    for event in events:
        if event.type == pygame.locals.QUIT:
            done=True
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_LEFT]:
                x-=50
        if event.type == pygame.MOUSEBUTTONUP:
            unlocked=True

    mouse_position = pygame.mouse.get_pos()
    left,mid,right = pygame.mouse.get_pressed()
    if mid:
        break
        
    x=mouse_position[0]
    y=mouse_position[1]
    
    
    if left and unlocked:
        points.append((x,y))
        unlocked=False


    #print(points)
    d.fill(BLACK)
    
    for point in points:
        pygame.draw.rect(d,RED,(point[0],point[1],w,h))
        
    if right:
        for i in range(0,len(points)-1):
            pygame.draw.line(d, (255, 255, 255), (points[i][0],points[i][1]), (points[i+1][0],points[i+1][1]))
        print(i)
        pygame.draw.line(d, (255, 255, 255), (points[i+1][0],points[i+1][1]), (points[0][0],points[0][1]))

    pygame.draw.rect(d,RED,(x,y,w,h))
    pygame.display.update()

pygame.quit()
