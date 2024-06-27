define fadehold = Fade(0.5, 1.0, 0.5)
define m = Character("Man", who_color="#c8ffc8")
define b = Character("Bad Guy", who_color="#7d8f2f")
define n = Character("Narrator")
define g = Character("Grocery", who_color="#a83283")
define p = Character("Pal", who_color="#a83283")
define END = Character("End", who_color="#570000", what_color="#570000")
define restart_count = 0
define items = 1
define gun_counter = 0
define end_track = 1
label start:
    play music "main.mp3"
  
    scene house front night

    n "Hello reader."
    python:
        name = renpy.input("What's your name?")
        name = name.strip() or "Guy Shy"
    n "Your name isnt that important anyway!"
    n "Are you tired of all of those really complicated stories?"
    n "Is modern gaming to much for you to follow?"
    n "Well I have a story made just for you!"
    show man the happy

    n "This is man"
    m "Hello! I am Man."

    n "He lives here on SaltBread RD"
    n "and his life is everything you could ask for!"
    n "Everything here is perfect!"
    n "everyone in the neighborhood is happy and perfect!"
    n "well that is execept"
    n "Bad Guy, Man's closest neighbor."
    jump restart

label restart:
    play music "Badguy.mp3" fadein 1.5
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
    m "Oh hey bad guy what do you want?"
    jump choice1_done

label choice1_ignore:
    $ menu_flag = False
    m "..."
    b "Are you ignoring me right now?"
    m "I'll show you!"
    jump choice1_done

label choice1_done:
    b "Take this man!"
    b " Feel the power of hate!"
    m "what?"
    b "shut up I wanted to sound cool"

label scene_change:
    scene house front fire
    show man the sad at right
    show bad guy at left
    with wiperight


    m "Oh no!"
  
menu:
    "run away from bad guy and his power of hate" :
        jump mans_badtime1


    "stay and fight bad guy with gun" :
        jump mans_fight

label mans_badtime1:
    scene black
    play music "uplifting.mp3" fadein 1.0
    n "and so man ran away from bad guy"
    n " to where you might ask?"
    n "well to his favorite place in town of course"
    n "store mart"
    jump store1

label mans_fight:
    m "try me bad guy!"
    b "take this man!"
    if gun_counter == 0:
        jump die_type_check
    else:
        jump secrect_end

label store1:
    scene store
    show man the happy
    m "finally"
    m "I got away from bad guy!"
    m "and I can finally relax at my favorite place"
    m "store mart"
    
menu:
    "shop for groceries":
        jump gear_up

    "search for help":
        jump help_wanted

label gear_up:
    scene store 2
    n "as man walks down the isles he comes to a choice"
    n "he can only afford to grab one item, ceral or an abnormal looking gun."

menu:
    "Ceral":
        $ items = 1
    
    "A weird looking gun":
        $ items = +2
        $ gun_counter = 1

label help_wanted:
    scene store 
    scene store 2    
    show man the happy at truecenter
    with fade
    show man the happy at right
    with move
    show grocery at left
    with moveinbottom
    n "man is stopped in the isle"
    if items == 1:
        n "as he grabbed his box of cereal"
    elif items > 1:
        n "as he attempted to pull the strange gun out of the shelf"
    else:
        n "as he looks for someone to help him"
    g "You must be man"
    m "indeed I am, and you are?"
    g "I am pal"
    p "I heard about Bad Guy's evil plans to take you down"
    p "and I'm here to help"

menu:
    "Decline pal's offer":
        $ gun_counter = 0
        jump kick_out
    "Accept this pal into your story.":
        jump team_up

label kick_out:
    $ items = 0
    $ gun_counter = 0
    scene street
    show man the sad at right
    show grocery at left
    p "and stay out"
    jump bad_end

label team_up:
    jump end
    scene roof
    show man the happy at right with moveinbottom
    show grocery at left with moveinbottom
label die_type_check:
    if gun_counter < 1:
        jump man_die_no_gun
    else:
        jump man_die

label man_die:
    play music "end.mp3" fadein 0.5
    scene black
    show man is die
    n "this was the end of Man"
    jump end_menu

label man_die_no_gun:
    play music "end.mp3" fadein 0.5
    scene black
    show man is die at truecenter
    with blinds
    n "Man tried to fight bad guy with a gun."
    n "a gun he did not have"
    n "this was the end of man."
    n " maybe try again after you find a gun ;)"
    jump end_menu

label end_menu:
    if end_track == 1:
        END "Bad Ending"
        $ gun_counter = 0
    elif end_track == 2:
        scene house front night
        with fadehold
        show grocery at left with moveinbottom
        show man the happy at right with moveinbottom
        END "Nutrual Ending"
    elif end_track == 4:
        scene manthegame
        END "true ending"

label true_route_check:
    if end_track == 1:
        show black
    else:
        jump true_route

menu: 
   
    "restart":
        $ restart_count = +1
        jump restart
        $ gun_counter == 0
       
    "quit":
        return

label true_route:
    if end_track == 2:
        show black
    elif end_track == 4:
        jump quit_real

menu: 
   
    "GO BACK!":
        $ restart_count = +1
        jump restart
    
       
    "give up":
        return

label quit_real:
    scene manthegame
menu:     
    "Finish this Man's story.":
        return

label bad_end:
    scene house front fire
    END "and so man failed to stop bad guy"
    $ end_track = 1
    $ gun_counter == 0
    jump man_die

label end:
    play music "ending.mp3" fadein 0.5
    scene house front night with pushup
    END "and so man did it"
    $ end_track = 2
    jump end_menu

label good_end:

    $ end_track = 3

label secrect_end:
    play music "ending.mp3" fadein 0.5
    $ end_track = 4
    jump end_menu