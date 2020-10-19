import pyttsx3

def voice_msg(var):
    """
       This function is used to convert any input into speech..
       For this we need to istall 'pyttsx3' package using 'pip3 install pyttsx3'
    """
    speak = pyttsx3.init()
    speak.setProperty('rate',170)
    speak.setProperty('volume',1)
    voices = speak.getProperty('voices')
    speak.setProperty('voice',voices[1].id)
    for i in var:
        speak.say(i)
    speak.runAndWait()

def input_data(): 
    """
       From here you can select a desired plant about which you want to know
       It returns the uses of that plant as output 
    """  
    print('You can choose from below options :')
    print('1.Neem','2.Tulasi','3.Alovera','4.Hibiscus',sep='\n')
    n=int(input('Enter your choice[1-4] : '))
    if n==1:
        print('Common Name = Neem',
        'Telugu Name = VapaPandu',
        'Medicinal use : skin diseases,hair growth...etc',
		'-> Maintains your blood sugar levels',
		'-> Aids in cancer treatment',
        '-> Relieves fungal infection',
        '-> Used to treat head lice',
        '-> Acts as mosquito repellent',
        '-> Is effective against skin problems',
        '-> Prevents oral problems',sep='\n')
    elif n==2:
        print('Common Name = Tulasi',
            'Parts Used = Leaves/Seed',
	        'Medicinal use : vitamin A and C,fever,skin...etc',
            '-> Its acts as a detoxifying, cleansing and purifying agent - both from within and without.',
            '-> Therefore it is good for skin - both when consumed and applied topically.',
            '-> It is aso effective in treating skin disorders, itching ans issues like ringworms.',
            '-> It can be made into teas or can be had raw, powdered, paste ot in form herbal supplements.',
            '-> Is great for dental health and for healthy gums.',
            '-> It helps in relieving from fever, headache, sore throat, cold, cought, fly and chest congestion.',sep='\n')
    elif n==3:
        print('Common name = Aloe vera',
            'Telugu name = Kalabanda',
            'Medicinal use : Vitamin-C,Cough,Diabetes,cold,Laxativ,hyper acidity.',
            '->  Aloe vera is good for irritated or inflamed skin.',
            '->  Aloe vera helps repair your skin from the most tender of wounds.',
            '->  Aloe vera helps speed the process of healing to burns and other wounds.',
            '->  Aloe vera is hydrating, rejuvenating and toning for your skin.',sep='\n')
    elif n==4:
        print('Common Name = Hibiscus',
            'Parts Used = Flowers and Leaves',
            'Medicinal use : vitamin C, minerals and various antioxidants',
            '-> Conditioner for hair',
            '-> Skin care , Anti-ageing',
            '-> Reduces blood pressure , Weight loss and digestion',
            '-> Treat wounds Oil',
            '-> Lower cholesterol , Cough and cold.',sep='\n')
    else :
        voice_msg(['Looks like an invalid input ...'])
        voice_msg(['Please select from given options..']) 
  
