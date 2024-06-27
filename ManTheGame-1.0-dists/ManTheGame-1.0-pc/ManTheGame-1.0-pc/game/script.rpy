
define e = Character("Man", who_color="c8ffc8")
define b = Character("Bad Guy")
define n = Character("Narrator")
define restart_count = 0
label start:

  
    scene house front night

    n "Hello reader."
    n "Are you tired of all of those really complicated stories?"
    n "Is modern gaming to much for you to follow?"
    n "Well I have a story made just for you!"
    show man the happy

    n "This is man"
    e "Hello! I am Man."

    n "He lives here on SaltBread RD"
    n "and his life is everything you could ask for!"
    n "Everything here is perfect!"
    n "everyone in the neighborhood is happy and perfect!"
    n "well that is execept"
    n "Bad Guy, Man's closest neighbor."
    jump restart

label restart:
    if restart_count > 0:
        scene house front night
        with pushright
    else:
        scene house front night
    show man the happy
    show man happy at right
    with move
    show bad guy at left
    b "hello i am bad guy"
    n "little did man know, his perfect life was about to change."
    jump restart_check

label restart_check:
    if restart_count > 0:
        jump choice1_done

# choice for bad guy
menu:
    "Oh hey there bad guy":
        jump choice1_hi

    "Ignore":
        jump choice1_ignore

label choice1_hi:
    $ menu_flag = True
    e "Oh hey bad guy what do you want?"
    jump choice1_done

label choice1_ignore:
    $ menu_flag = False
    e "..."
    b "Are you ignoring me right now?"
    e "I'll show you!"
    jump choice1_done

label choice1_done:
    b "Take this man!"
    b " Feel the power of hate!"
    e "what?"
    b "shut up I wanted to sound cool"

label scene_change:
    scene house front fire
    show man the sad at right
    show bad guy at left
    with wiperight


    e "Oh no!"
  
menu:
    "run away from bad guy and his power of hate" :
        jump mans_badtime1

    "stay and fight bad guy with gun" :
        jump mans_fight

label mans_badtime1:
    scene black
    n "and so man ran away from bad guy"
    n " to where you might ask?"
    n "well to his favorite place in town of course"
    n "store mart"
    jump store1

label mans_fight:
    e "try me bad guy!"
    b "take this man!"
    jump man_die

label store1:
    scene store
    show man the happy
    e "finally"
    e "I got away from bad guy!"
    e "and I can finally relax at my favorite place"
    e "store mart"
    
menu:
    "shop for groceries":
        jump gear_up

    "search for help":
        jump help_wanted

label gear_up:
    scene store
    with fade(.5)
    pause .5
    scene store 2
    n "as man walks down the isles he comes to a choice"

label help_wanted:
    scene store 
    scene store 2    
    show man the happy at truecenter
    with fade


    n "gun"
    
label man_die:
    scene black
    show man is die
    n "this was the end of Man"

menu: 
    "restart":
        $ restart_count = +1
        jump restart
    
       
    "quit":
        return