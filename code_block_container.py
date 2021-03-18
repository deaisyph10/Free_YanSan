if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_0:
        net_menu_window = True
    if event.key == pygame.K_LSHIFT:
        interior_window = True
        int_window.blit(interior_layout, (10, 10))

if event.type == pygame.KEYUP:
    if event.key == pygame.K_1:
        battle = False
    if event.key == pygame.K_0:
        net_menu_window = False
    if event.key == pygame.K_LSHIFT:
        interior_window = False
    if event.key == pygame.K_RETURN:
        radar_screen_value = False

#            if event.key == pygame.K_RETURN:
            # radar_screen_value = True
            # if event.key == pygame.K_LEFT:
            #    cursor.curpos(-curmov, 0)
            # if event.key == pygame.K_RIGHT:
            #   cursor.curpos(curmov, 0)
            # if event.key == pygame.K_DOWN:
            #    cursor.curpos(0, curmov)
            # if event.key == pygame.K_UP:
            #    cursor.curpos(0, -curmov)
# if event.key == pygame.K_DOWN:
            #    world_map.cursor(0, curmov)
            # if event.key == pygame.K_LEFT:
            #    world_map.cursor(-curmov, 0)
            # if event.key == pygame.K_RIGHT:
            #    world_map.cursor(curmov, 0)
            # if event.key == pygame.K_UP:
            #    world_map.cursor(0, -curmov)