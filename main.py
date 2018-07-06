"""

Codecademy Project.

    Updated in this version:
        1) add own line to input requesting menu option
                make initial statement/ var request for input separate
        2) Fixed the home_vist() function
        3) Stylistic modifications
        4) Bug Fixes
"""

def cs_service_bot():
    print('Hello! Welcome to the DNS Cable Company\'s Service Portal. Are you a new or existing customer?\n[1] New Customer\n[2] Existing Customer')
    response = input('Please enter the number corresponding to your choice: ')
    if response == '1':
        new_customer()
    elif response == '2':
        existing_customer()
    else:
        print('Sorry, we didn\'t understand your selection')
        return cs_service_bot()

def existing_customer():
    print('What kind of support do you need?\n[1] Television Support\n[2] Internet Support\n[3] Speak to a support representative.')
    exist_response = input('Please enter the number corresponding to your choice: ')
    if exist_response == '1':
        television_support()
    elif exist_response == '2':
        internet_support()
    elif exist_response == '3':
        live_rep("support")
    else:
        print('Sorry, we didn\'t understand your selection.')
        existing_customer()

def new_customer():
    print('We\'re excited to have you join the DNS family. how can we help you?\n[1] Sign up for service.\n[2] Schedule a home visit\n[3] Speak to a sales representative.')
    new_response = input('Please enter the number corresponding to your choice: ')
    if new_response == '1':
        sign_up()
    elif new_response == '2':
        home_visit()
    elif new_response == '3':
        live_rep('sales')
    else:
        print('Sorry, we didn\'t understand your selection.')
        new_customer()

def television_support():
    print('[1] I can\'t access certain channels.\n[2] My picture is blurry.\n[3] I keep losing service.\n[4] Other issues.')
    tv_issues = input('Please enter the number corresponding to your choice: ')
    if tv_issues == '1':
        print('Please check the channel lists at DefinitelyNotSinister.com. If the channel you cannot access is there, please contact a live representative.')
        did_that_help()
    elif tv_issues == '2':
        print('Try adjusting the antenna above you television set.')
        did_that_help()
    elif tv_issues == '3':
        print('Is it raining outside? if so, wait until it is not raining and then try again.')
        did_that_help()
    elif tv_issues == '4':
        live_rep("support") 
    else:
        print('Sorry, we didn\'t understand your selection.')
        television_support()

def internet_support():
    print('[1] I can\'t connect to the internet.\n[2] My connection is very slow.\n[3] I can\'t access certain sites.\n[4] Other issues.')
    int_issues = input('Please enter the number corresponding to your choice: ')
    if int_issues == '1':
        print('Unplug your router, then plug it back in, then give it a good whack, like the Fonz.')
        did_that_help()
    elif int_issues == '2':
        print('make sure that all cell phones and other peoples computers are not connected to the interent, so that you can have all the backwidth.')
        did_that_help()
    elif int_issues == '3':
        print('Move to a different region or install a VPN. Some areas bloack certain sites.')
    elif int_issues == '4':
        live_rep("support") 
        did_that_help()
    else:
        print('Sorry, we didn\'t understand your selection.')
        internet_support()

def did_that_help():
    prob_solved = input('Was your problem solved? Enter Y for yes, or N for no: ')
    if prob_solved == 'y':
        print('Thank you')
    elif prob_solved == 'n':
        not_fixed = input('Would you rather talk to a live representative or schedule a home visit? Enter either \'talk\' to speak with a live representative, or \'schedule\' to schedule a home visit: ')
        if not_fixed == 'talk':
            live_rep("support")
        elif not_fixed == 'schedule':
            home_visit("support")
        else:
            print('Sorry, we didn\'t understand your selection.')
            did_that_help()
    else:
        print('Sorry, we didn\'t understand your selection.')
        did_that_help()

def sign_up():
    print('Great choice, friend! We\'re excited to have you joen the DNS family! Here are the packages available in your area: \n[1] Bundle Deal (Internet + Cable)\n[2] Internet\n[3] Cable')
    package = input('Please select the package you are interested in signing up for: ')
    if package == '1':
        print('You\'ve selected the Bundle Package! Please schedule a home visit and our technician will come and set up your new service.')
        home_visit("new install")
    elif package == '2':
        print('You\'ve selected the Internet Only Package! Please schedule a home visit and our technician will come and set up your new service.')
        home_visit("new install")
    elif package == '3':
        print('You\'ve selected the Cable Only Package! Please schedule a home visit and our teechnician will come and set up you ew service.')
        home_visit("new install")
    else:
        print('Sorry, we didn\'t understand your selection.')
        sign_up()

def home_visit(purpose = 'none'): 
    if purpose == "none":
        print('[1] New service installation.\n[2] Existing service repair\n[3] Location scouting for unserviced region.')
        options = input('Please enter the corresponding number: ')
        if options == '1':
            home_visit("new install")
        elif options == '2':
            home_visit("support")
        elif options == '3':
            home_visit("scout")
        else:
            print('Sorry, we didn\'t understand your selection.')
            home_visit()
    if purpose == 'new install':
        print('Please enter a date below when you are available for a technician to come to your home and install your services.')
        visit_date = input('Date: ')
        print('Wonderful! A technician will come visit you on %s. Please be availabe between the hours of 1:00 am and 11:00 pm.' % (visit_date))
        return visit_date
    if purpose == 'service':
        print('Please enter a date below when you are available for a technician to come to your home and provide the necessary service.')
        visit_date = input('Date: ')
        print('Wonderful! A technician will come visit you on %s. Please be available between the hours of 1:00 am and 11:00 pm.' % (visit_date))
        return visit_date
    if purpose == 'scout':
        print('Please enter a date below when you are available for a technician to come to your home and scout your region.')
        visit_date = input('Date: ')
        print('Wonderful! A scout will come visit your region on %s. Please be available between the hours of 1:00 am and 11:00 pm.' % (visit_date))
        return visit_date

def live_rep(purpose):
    if purpose == 'sales':
        print('Please hold while we connect you with a live sales representative. The wait time will be between two minutes and six hours. We thank you for your patience.')
    elif purpose == 'support':
        print('Please hold while we connect you with a live support representative. The wait time will be between two minutes and six hours. We thank you for your patience.')

cs_service_bot()
