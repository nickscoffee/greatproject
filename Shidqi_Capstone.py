from tabulate import tabulate
from colorama import init
from termcolor import colored
import os
import time
jkt = {'East Jakarta','West Jakarta','Central Jakarta','South Jakarta','North Jakarta','Seribu Islands'}
jawa_barat = {'Bandung','West Bandung','Banjar','Bekasi','Bogor','Ciamis','Cianjur','Cimahi','Cirebon','Depok','Garut','Indramayu','Karawang','Kuningan','Majalengka','Pangandaran','Purwakarta','Subang','Sukabumi','Sumedang','Tasikmalaya'}
tangsel = {'Tangerang','South Tangerang','Serang','Lebak','Cilegon','Pandeglang'}
jogjakarta = {'Sleman','Bantul','Yogyakarta','Gunung Kidul','Kulon Progo'}
jateng = {'Brebes','Tegal','Cilacap','Purbalingga','Banyumas','Banjarnegara','Wonosobo','Purbalingga','Kebumen','Magelang','Purworejo','Klaten','Wonogiri','Boyolali','Karanganyar','Blora','Grobogan','Sukoharjo','Pati','Rembang','Jepara','Kudus','Demak','Temanggung','Salatiga','Surakarta','Kendal','Batang','Pekalongan','Pemalang','Semarang','Sragen'}
jawatimur = {'Kediri','Blitar','Malang','Probolinggo','Pasuruan','Mojokerto','Madiun','Surabaya','Batu','Pacitan','Ponorogo','Trenggalek','Tulungagung','Lumajang','Jember','Banyuwangi','Bondowoso','Situbondo','Sidoarjo','Jombang','Nganjuk','Magetan','Ngawi','Bojonegoro','Tuban','Lamongan','Gresik','Bangkalan','Sampang','Pamekasan','Sumenep'}
Jakarta = [
    {
        'Organization': 'Marigame Udon',
        'Phone': '08799917629',
        'City': 'East Jakarta',
        'Locality':'Cipinang Melayu',
        'Street Name': 'Kalimalang 40'
    },
    {
        'Organization': 'Siang Malam',
        'Phone': '0869271999',
        'City': 'South Jakarta',
        'Locality': 'Kemang',
        'Street Name': 'Kemang 20'
    },
    {
        'Organization': 'Saratoga Investama Sedaya Tbk',
        'Phone': '087918909728',
        'City': 'South Jakarta',
        'Locality': 'Setiabudi',
        'Street Name': 'H.R. Rasuna Said X5'
    },
    {
        'Organization': 'Mulanpada Hospital Jakarta',
        'Phone': '0877782917361',
        'City': 'South Jakarta',
        'Locality': 'Lebak Bulus',
        'Street Name': 'Lebak Bulus I Kavling 29'
    }
]
West_Java = [
    {
        'Organization': 'Parahyangan Catholic University',
        'Phone': '089826182618',
        'City': 'Bandung',
        'Locality': 'Cidadap',
        'Street Name': 'Ciumbuleuit 94'
    },
    {
        'Organization': 'Malah Dicubo',
        'Phone': '082918193829',
        'City': 'Bandung',
        'Locality': 'Andir',
        'Street Name': 'South Train Station Hall 27'
    },
    {
        'Organization': 'Put Your Hands Up',
        'Phone': '081123242102',
        'City': 'Bandung',
        'Locality': 'Coblong',
        'Street Name': 'Ir. H. Juanda 113'
    },
    {
        'Organization': 'Santa Baramundi Hospital',
        'Phone': '082325192719',
        'City': 'Bandung',
        'Locality': 'Coblong',
        'Street Name': 'Ir. H. Juanda 100'
    }
]
Central_Java = [
    {
        'Organization': "Sate Kambing Wendy's",
        'Phone': '0877236271761',
        'City': 'Tegal',
        'Locality': 'Tegal Baru',
        'Street Name': 'Kapten Ismail 5',
    },
    {
        'Organization': 'Doctor Kariadi Public Hospital',
        'Phone': '0827172618271',
        'City': 'Semarang',
        'Locality': 'South Semarang',
        'Street Name': 'DR. Sutomo 16',
    },
    {
        'Organization': 'Diponegoro University',
        'Phone': '081172637162',
        'City': 'Semarang',
        'Locality': 'Tembalang',
        'Street Name': 'Professor Sudarto 13',
    },
    {
        'Organization': 'Solo Grand Mall',
        'Phone': '0876271682618',
        'City': 'Surakarta',
        'Locality': 'Laweyan',
        'Street Name': 'Slamet Riyadi 273',
    }
] 
East_Java = [
    {
        'Organization': 'Pakuwon City Mall',
        'Phone': '086627261726',
        'City': 'Surabaya',
        'Locality': 'Mulyorejo',
        'Street Name': 'White Laguna KJW Tambak 2',
    },
    {
        'Organization': 'Pondok Pesantren Tebu Ireng',
        'Phone': '086726182617',
        'City': 'Jombang',
        'Locality': 'Diwek',
        'Street Name': 'Irian Jaya 10',
    },
    {
        'Organization': 'Avian Office Tower',
        'Phone': '08662716271',
        'City': 'Surabaya',
        'Locality': 'Gayungan',
        'Street Name': 'East Menanggal 1',
    },
    {
        'Organization': 'Fraton Body Repair & Painting',
        'Phone': '087728172812',
        'City': 'Surabaya',
        'Locality': 'Benowo',
        'Street Name': 'Kendung 78',
    }
] 
Yogyakarta = [
    {
        'Organization': 'Gadjah Mada University',
        'Phone': '08112736261',
        'City': 'Sleman',
        'Locality': 'Depok',
        'Street Name': 'Bulaksumur Caturnunggal 1',
    },
    {
        'Organization': 'Tentrem Hotel',
        'Phone': '08627162712',
        'City': 'Yogyakarta',
        'Locality': 'Jetis',
        'Street Name': 'Prince Mangkubumi 72A',
    },
    {
        'Organization': 'Beringharjo Traditional Market',
        'Phone': '082636216271',
        'City': 'Yogyakarta',
        'Locality': 'Gondomanan',
        'Street Name': 'Margo Mulyo 16',
    },
    {
        'Organization': 'Indonesia International Islamic University',
        'Phone': '085627362712',
        'City': 'Sleman',
        'Locality': 'Ngemplak',
        'Street Name': 'Kaliurang KM. 14,5',
    }
] 
Banten = [
    {
        'Organization': 'Purwadhika Digital School',
        'Phone': '087261726172',
        'City': 'South Tangerang',
        'Locality': 'Cisauk',
        'Street Name': 'BSD Green Office Park 9 - G Floor',
    },
    {
        'Organization': 'Sositi Coffee & Bar',
        'Phone': '089273827192',
        'City': 'South Tangerang',
        'Locality': 'Pagedangan',
        'Street Name': 'Main Street BSD Foresta Business District 6',
    },
    {
        'Organization': 'Indonesia Convention Exhibition',
        'Phone': '08299127812',
        'City': 'South Tangerang',
        'Locality': 'Pagedangan',
        'Street Name': 'BSD Grand Boulevard 1',
    },
    {
        'Organization': 'Krakatau Steel (Persero) Tbk',
        'Phone': '081273727172',
        'City': 'Cilegon',
        'Locality': 'Purwakarta',
        'Street Name': 'Cilegon City Industry 5',
    }
] 

def greetings():
    os.system('cls')
    time.sleep(0.4)
    print("""
            Welcome to Nick's Express Organization Address Database Chapter Java, Indonesia

            Menu :
            1. Preview Nick's Express Address Database
            2. Change Nick's Express Address Database
            3. Delete Data from Nick's Address Database
            7. Exit
          """)
def categories_choose():
        os.system('cls')
        time.sleep(0.4)
        print("""
            Nick's Express Address Database Sub-Menu #1: Database Category
            Menu :
            1. Special Region of Jakarta
            2. West Java
            3. Central Java
            4. East Java
            5. Special Region of Yogyakarta
            6. Banten  
            0. Back
        """)
def sub_menu2 ():
     os.system('cls')
     time.sleep(0.4)
     print("""
            What you want to do Sub-Menu #1: Create or update data
            Menu :
            1. Add Data
            2. Update Data
            0. Back
        """)
def back():
        back = input('Back to previous menu type (Y), to main menu press (N): ').capitalize()
        return back
def numbers(input):
    return input.isdigit()
def show_jakarta(Jakarta):
    os.system('cls')
    time.sleep(0.4)
    indexed_jakarta = [{'Index': 'DKI - '+ str(i+1), **row} for i, row in enumerate(Jakarta)]
    list_jakarta = (tabulate(indexed_jakarta,headers= 'keys', tablefmt= 'github'))
    print(colored("Nick's Express Special Region of Jakarta Database\n",'green'))
    print(list_jakarta)
    return
def show_westjava(West_Java):
    os.system('cls')
    time.sleep(0.4)
    indexed_westjava = [{'Index': 'JABAR - ' + str(i+1), **row} for i, row in enumerate(West_Java)]
    list_westjava = (tabulate(indexed_westjava,headers= 'keys', tablefmt= 'github'))
    print(colored("Nick's Express West Java Database\n",'green'))
    print(list_westjava)
    return
def show_centraljava(Central_Java):
    os.system('cls')
    time.sleep(0.4)
    indexed_central = [{'Index': 'JATENG - ' + str(i+1), **row} for i, row in enumerate(Central_Java)]
    list_central = (tabulate(indexed_central,headers= 'keys', tablefmt= 'github'))
    print(colored("Nick's Express Central Java Database\n",'green'))
    print(list_central)
    return
def show_eastjava(East_Java):
    os.system('cls')
    time.sleep(0.4)
    indexed_east = [{'Index': 'JATIM - ' + str(i+1), **row} for i, row in enumerate(East_Java)]
    list_east = (tabulate(indexed_east,headers= 'keys', tablefmt= 'github'))
    print(colored("Nick's Express East Java Database\n",'green'))
    print(list_east)
    return
def show_yogyakarta(Yogyakarta):
    os.system('cls')
    time.sleep(0.4)
    indexed_yogya = [{'Index': 'YK - ' + str(i+1), **row} for i, row in enumerate(Yogyakarta)]
    list_yogyakarta = (tabulate(indexed_yogya,headers= 'keys', tablefmt= 'github'))
    print(colored("Nick's Express Special Region of Yogyakarta Database\n",'green'))
    print(list_yogyakarta)
    return
def show_banten(Banten):
    os.system('cls')
    time.sleep(0.4)
    indexed_banten = [{'Index': 'A - ' + str(i+1), **row} for i, row in enumerate(Banten)]
    list_banten = (tabulate(indexed_banten,headers= 'keys', tablefmt= 'github'))
    print(colored("Nick's Express Banten Database\n",'green'))
    print(list_banten)
    return
def new_data(Jakarta):
    print(colored("===================# Add Data to Jakarta Database #Sub-Menu 3 #===================","green"))
    time.sleep(1.5)
    show_jakarta(Jakarta)
    while True:
        new_organization = input('Organization Name : ').title()
        new_phone = input('Organization Phone Number : ')
        city_jkt = input("City : ").title()
        while city_jkt not in jkt:
            print(colored("The city are not in Special Region of Jakarta! Please input city in Special Region of Jakarta.",'yellow'))
            city_jkt = input("City : ").title()
        new_locality = input("Locality : ").title()
        new_street_name = input('Street Address : ').title()
        check = input('Are you sure to input this data (Y/N)? : ').capitalize()
        while check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.", 'red'))
            check = input('Are you sure to input this data (Y/N)?: ').capitalize()
        if(check == 'Y'):
            Jakarta.append({
            'Organization': new_organization,
            'Phone': new_phone,
            'City': city_jkt,
            'Locality': new_locality,
            'Street Name': new_street_name
            })
            print(colored(f"{new_organization} succesfully added.", 'green'))
            time.sleep(1.0)
            show_jakarta(Jakarta)
        else:
            print(colored(f"Information of {new_organization} isn't added to databases.", 'red'))
            time.sleep(1.0)
            show_jakarta(Jakarta)
        double_check = str(input("Add another data (Y/N)? : ")).capitalize()
        while double_check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.",'red'))
            double_check = str(input("Add another data (Y/N)? : ")).capitalize()
        if(double_check == 'Y'):
            continue
        else:
            break
    return
def add_data(West_Java):
    print(colored("===================# Add Data to West Java Database #Sub-Menu 3 #===================","green"))
    time.sleep(1.5)
    show_westjava(West_Java)
    while True:
        new_organization = input('Organization Name : ').title()
        # if(new_organization == (West_Java[x]['Organization'])):
        #     print(colored(f'The {new_organization} information is already in database.','yellow'))
        #     continue
        # else:
        new_phone = input('Organization Phone Number : ')
        new_city = input("City : ").capitalize()
        while new_city not in jawa_barat:
            print(colored("The city are not in West Java! Please input the right city.",'yellow'))
            new_city = input("City: ").capitalize()
        new_locality = input("Locality : ").title()
        new_street_name = input('Street Address : ').title()
        check = input('Are you sure to input this data (Y/N)? : ').capitalize()
        while check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.", 'red'))
            check = input('Are you sure to input this data (Y/N)?: ').capitalize()
        if(check == 'Y'):
            West_Java.append({
            'Organization': new_organization,
            'Phone': new_phone,
            'City': new_city,
            'Locality': new_locality,
            'Street Name': new_street_name
            })
            print(colored(f"{new_organization} succesfully added.", 'green'))
            time.sleep(1.0)
            show_westjava(West_Java)
        else:
            print(colored(f"Information of {new_organization} isn't added to databases.", 'red'))
            time.sleep(1.0)
            show_westjava(West_Java)
        double_check = input("Add another data (Y/N)? : ").capitalize()
        while double_check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.",'red'))
            double_check = input("Add another data (Y/N)? : ").capitalize()
        if(double_check == 'Y'):
            continue
        else:
            break
    return
def baru_data(Central_Java):
    print(colored("===================# Add Data to Central Java Database #Sub-Menu 3 #===================","green"))
    time.sleep(1.5)
    show_centraljava(Central_Java)
    while True:
        new_organization = input('Organization Name : ').title()
        new_phone = input('Organization Phone Number : ')
        kab = input("City : ").title()
        while kab not in jateng:
            print(colored("The city are not in Cental Java! Please input city in Central Java.",'yellow'))
            kab = input("City : ").title()
        new_locality = input("Locality : ").title()
        new_street_name = input('Street Address : ').title()
        check = input('Are you sure to input this data (Y/N)? : ').capitalize()
        while check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.", 'red'))
            check = input('Are you sure to input this data (Y/N)?: ').capitalize()
        if(check == 'Y'):
            Central_Java.append({
            'Organization': new_organization,
            'Phone': new_phone,
            'City': kab,
            'Locality': new_locality,
            'Street Name': new_street_name
            })
            print(colored(f"{new_organization} succesfully added.", 'green'))
            time.sleep(1.0)
            show_centraljava(Central_Java)
        else:
            print(colored(f"Information of {new_organization} isn't added to databases.", 'red'))
            time.sleep(1.0)
            show_centraljava(Central_Java)
        double_check = input("Add another data (Y/N)? : ").capitalize()
        while double_check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.",'red'))
            double_check = input("Add another data (Y/N)? : ").capitalize()
        if(double_check == 'Y'):
            continue
        else:
            break
    return
def tulis_data(East_Java):
    print(colored("===================# Add Data to East Java Database #Sub-Menu 3 #===================","green"))
    time.sleep(1.5)
    show_eastjava(East_Java)
    while True:
        new_organization = input('Organization Name : ').title()
        new_phone = input('Organization Phone Number : ')
        sby = input("City : ").title()
        while sby not in jawatimur:
            print(colored("The city are not in East Java! Please input city in East Java.",'yellow'))
            sby = input("City : ").title()
        new_locality = input("Locality : ").title()
        new_street_name = input('Street Address : ').title()
        check = input('Are you sure to input this data (Y/N)? : ').capitalize()
        while check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.", 'red'))
            check = input('Are you sure to input this data (Y/N)?: ').capitalize()
        if(check == 'Y'):
            East_Java.append({
            'Organization': new_organization,
            'Phone': new_phone,
            'City': sby,
            'Locality': new_locality,
            'Street Name': new_street_name
            })
            print(colored(f"{new_organization} succesfully added.", 'green'))
            time.sleep(1.0)
            show_eastjava(East_Java)
        else:
            print(colored(f"Information of {new_organization} isn't added to databases.", 'red'))
            time.sleep(1.0)
            show_eastjava(East_Java)
        double_check = str(input("Add another data (Y/N)? : ")).capitalize()
        while double_check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.",'red'))
            double_check = str(input("Add another data (Y/N)? : ")).capitalize()
        if(double_check == 'Y'):
            continue
        else:
            break
    return
def catat_data(Yogyakarta):
    print(colored("===================# Add Data to Special Region of Yogyakarta Database #Sub-Menu 3 #===================","green"))
    time.sleep(1.5)
    show_yogyakarta(Yogyakarta)
    while True:
        new_organization = input('Organization Name : ').title()
        new_phone = input('Organization Phone Number : ')
        sultan = input("City : ").title()
        while sultan not in jogjakarta:
            print(colored("The city are not in Special Region of Yogyakarta! Please input city in Special Region of Yogyakarta.",'yellow'))
            sultan = input("City : ").title()
        new_locality = input("Locality : ").title()
        new_street_name = input('Street Address : ').title()
        check = input('Are you sure to input this data (Y/N)? : ').capitalize()
        while check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.", 'red'))
            check = input('Are you sure to input this data (Y/N)?: ').capitalize()
        if(check == 'Y'):
            Yogyakarta.append({
            'Organization': new_organization,
            'Phone': new_phone,
            'City': sultan,
            'Locality': new_locality,
            'Street Name': new_street_name
            })
            print(colored(f"{new_organization} succesfully added.", 'green'))
            time.sleep(1.0)
            show_yogyakarta(Yogyakarta)
        else:
            print(colored(f"Information of {new_organization} isn't added to databases.", 'red'))
            time.sleep(1.0)
            show_yogyakarta(Yogyakarta)
        double_check = input("Add another data (Y/N)? : ").capitalize()
        while double_check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.",'red'))
            double_check = input("Add another data (Y/N)? : ").capitalize()
        if(double_check == 'Y'):
            continue
        else:
            break
    return
def nyatet_data(Banten):
    print(colored("===================# Add Data to Banten Database #Sub-Menu 3 #===================","green"))
    time.sleep(1.5)
    show_banten(Banten)
    while True:
        new_organization = input('Organization Name : ').title()
        new_phone = input('Organization Phone Number : ')
        kota = input("City : ").title()
        while kota not in tangsel:
            print(colored("The city are not in Banten! Please input city in Banten.",'yellow'))
            kota = input("City : ").title()
        new_locality = input("Locality : ").title()
        new_street_name = input('Street Address : ').title()
        check = input('Are you sure to input this data (Y/N)? : ').capitalize()
        while check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.", 'red'))
            check = input('Are you sure to input this data (Y/N)?: ').capitalize()
        if(check == 'Y'):
            Banten.append({
            'Organization': new_organization,
            'Phone': new_phone,
            'City': kota,
            'Locality': new_locality,
            'Street Name': new_street_name
            })
            print(colored(f"{new_organization} succesfully added.", 'green'))
            time.sleep(1.0)
            show_banten(Banten)
        else:
            print(colored(f"Information of {new_organization} isn't added to databases.", 'red'))
            time.sleep(1.0)
            show_banten(Banten)
        double_check = input("Add another data (Y/N)? : ").capitalize()
        while double_check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.",'red'))
            double_check = input("Add another data (Y/N)? : ").capitalize()
        if(double_check == 'Y'):
            continue
        else:
            break
    return
def update_data(Jakarta):
    show_jakarta(Jakarta)
    while True:
        upd_index = input('Put Number Index The Data You Want to Update : ')
        if not numbers(upd_index):
            print(colored("Just Input Number! Please Input Again",'red'))
            time.sleep(1.0)
            continue
        update_index = int(upd_index)
        if((update_index-1) > len(Jakarta) or update_index < 0):
            print(colored(f'Index {update_index} not in Database.','red'))
            time.sleep(0.4)
            continue
        else:
            update_phone = input(f"{Jakarta[update_index - 1]['Organization']} New Phone Number : ")
            update_locality = input(f"{Jakarta[update_index - 1]['Organization']} New Locality : ").title()
            update_street_name = input(f"{Jakarta[update_index - 1]['Organization']} New Street Address : ").title()
            check = input(f"Are you sure to update {Jakarta[update_index - 1]['Organization']} data (Y/N)?: ").capitalize()
            while check not in ['Y', 'N']:
                print(colored("Invalid function! Just type Y or N.", 'red'))
                check = input(f"Are you sure to update {Jakarta[update_index - 1]['Organization']} data (Y/N)?: ").capitalize()
            if(check == 'Y'):
                Jakarta[update_index -1]['Phone'] = update_phone
                Jakarta[update_index -1]['Locality'] = update_locality
                Jakarta[update_index -1]['Street Name'] = update_street_name
                print(colored(f"Information of {Jakarta[update_index -1]['Organization']} is succesfully updated.", 'green'))
                time.sleep(1.0)
                show_jakarta(Jakarta)
            else:
                print(colored(f"Information of {Jakarta[update_index -1]['Organization']} isn't updated.", 'red'))
                show_jakarta(Jakarta)
        double_check = input("Update another data (Y/N)? : ").capitalize()
        while double_check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.",'red'))
            double_check = input("Update another data (Y/N)? : ").capitalize()
        if(double_check == 'Y'):
            continue
        else:
            break
    return
def perbaharui_data(West_Java):
    show_westjava(West_Java)
    while True:
        upd_index = input('Put Number Index The Data You Want to Update : ')
        if not numbers(upd_index):
            print(colored("Just Input Number! Please Input Again",'red'))
            time.sleep(1.0)
            continue
        update_index = int(upd_index)
        if((update_index - 1) > len(West_Java) or update_index < 0):
          print(colored(f"Index {update_index} isn't in Database.",'red'))
          time.sleep(0.4)
          continue
        else:
            update_phone = input(f"{West_Java[update_index - 1]['Organization']} New Phone Number : ")
            update_locality = input(f"{West_Java[update_index -1]['Organization']} New Locality : ").title()
            update_street_name = input(f"{West_Java[update_index - 1]['Organization']} New Address : ").title()
            check = input(f"Are you sure to update {West_Java[update_index - 1]['Organization']} data (Y/N)?: ").capitalize()
            while check not in ['Y', 'N']:
                print(colored("Invalid function! Just type Y or N.", 'red'))
                check = input(f"Are you sure to update {West_Java[update_index - 1]['Organization']} data (Y/N)?: ").capitalize()
            if(check == 'Y'):
                West_Java[update_index - 1]['Phone']= update_phone
                West_Java[update_index -1]['Locality']= update_locality
                West_Java[update_index - 1]['Street Name']= update_street_name
                print(colored(f"Information of {West_Java[update_index-1]['Organization']} is succesfully updated.", 'green'))
                time.sleep(1.0)
                show_westjava(West_Java)
            else:
                print(colored(f"Information of {West_Java[update_index-1]['Organization']} isn't updated to databases.", 'red'))
                time.sleep(1.0)
                show_westjava(West_Java)
        double_check = input("Update another data (Y/N)? : ").capitalize()
        while double_check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.",'red'))
            double_check = input("Update another data (Y/N)? : ").capitalize()
        if(double_check == 'Y'):
            continue
        else:
            break
    return
def pembaharuan_data(Cental_Java):
    show_centraljava(Cental_Java)
    while True:
        upd_index = input('Put Number Index The Data You Want to Update : ')
        if not numbers(upd_index):
            print(colored("Just Input Number! Please Input Again",'red'))
            time.sleep(1.0)
            continue
        update_index = int(upd_index)
        if((update_index-1) > len(Cental_Java) or update_index < 0):
            print(colored(f'Index {update_index} not in Database.','red'))
            time.sleep(0.4)
            continue
        else:
            update_phone = input(f"{Cental_Java[update_index - 1]['Organization']} New Phone Number : ")
            update_locality = input(f"{Cental_Java[update_index - 1]['Organization']} New Locality : ").title()
            update_street_name = input(f"{Cental_Java[update_index - 1]['Organization']} New Street Address : ").title()
            check = input(f"Are you sure to update {Cental_Java[update_index - 1]['Organization']} data (Y/N)?: ").capitalize()
            while check not in ['Y', 'N']:
                print(colored("Invalid function! Just type Y or N.", 'red'))
                check = input(f"Are you sure to update {Cental_Java[update_index - 1]['Organization']} data (Y/N)?: ").capitalize()
            if(check == 'Y'):
                Cental_Java[update_index -1]['Phone'] = update_phone
                Cental_Java[update_index -1]['Locality'] = update_locality
                Cental_Java[update_index -1]['Street Name'] = update_street_name
                print(colored(f"Information of {Cental_Java[update_index -1]['Organization']} is succesfully updated.", 'green'))
                time.sleep(1.0)
                show_centraljava(Central_Java)
            else:
                print(colored(f"Information of {Cental_Java[update_index -1]['Organization']} isn't updated.", 'red'))
                show_jakarta(Cental_Java)
        double_check = input("Update another data (Y/N)? : ").capitalize()
        while double_check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.",'red'))
            double_check = input("Update another data (Y/N)? : ").capitalize()
        if(double_check == 'Y'):
            continue
        else:
            break
    return
def perubahan_data(East_Java):
    show_eastjava(East_Java)
    while True:
        upd_index = input('Put Number Index The Data You Want to Update : ')
        if not numbers(upd_index):
            print(colored("Just Input Number! Please Input Again",'red'))
            time.sleep(1.0)
            continue
        update_index = int(upd_index)
        if((update_index-1) > len(East_Java) or update_index < 0):
            print(colored(f'Index {update_index} not in Database.','red'))
            time.sleep(0.4)
            continue
        else:
            update_phone = input(f"{East_Java[update_index - 1]['Organization']} New Phone Number : ")
            update_locality = input(f"{East_Java[update_index - 1]['Organization']} New Locality : ").title()
            update_street_name = input(f"{East_Java[update_index - 1]['Organization']} New Street Address : ").title()
            check = input(f"Are you sure to update {East_Java[update_index - 1]['Organization']} data (Y/N)?: ").capitalize()
            while check not in ['Y', 'N']:
                print(colored("Invalid function! Just type Y or N.", 'red'))
                check = input(f"Are you sure to update {East_Java[update_index - 1]['Organization']} data (Y/N)?: ").capitalize()
            if(check == 'Y'):
                East_Java[update_index -1]['Phone'] = update_phone
                East_Java[update_index -1]['Locality'] = update_locality
                East_Java[update_index -1]['Street Name'] = update_street_name
                print(colored(f"Information of {East_Java[update_index -1]['Organization']} is succesfully updated.", 'green'))
                time.sleep(1.0)
                show_eastjava(East_Java)
            else:
                print(colored(f"Information of {East_Java[update_index -1]['Organization']} isn't updated.", 'red'))
                show_eastjava(East_Java)
        double_check = input("Update another data (Y/N)? : ").capitalize()
        while double_check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.",'red'))
            double_check = input("Update another data (Y/N)? : ").capitalize()
        if(double_check == 'Y'):
            continue
        else:
            break
    return
def ganti_data(Yogyakarta):
    show_yogyakarta(Yogyakarta)
    while True:
        upd_index = input('Put Number Index The Data You Want to Update : ')
        if not numbers(upd_index):
            print(colored("Just Input Number! Please Input Again",'red'))
            time.sleep(1.0)
            continue
        update_index = int(upd_index)
        if((update_index-1) > len(Yogyakarta) or update_index < 0):
            print(colored(f'Index {update_index} not in Database.','red'))
            time.sleep(0.4)
            continue
        else:
            update_phone = input(f"{Yogyakarta[update_index - 1]['Organization']} New Phone Number : ")
            update_locality = input(f"{Yogyakarta[update_index - 1]['Organization']} New Locality : ").title()
            update_street_name = input(f"{Yogyakarta[update_index - 1]['Organization']} New Street Address : ").title()
            check = input(f"Are you sure to update {Yogyakarta[update_index - 1]['Organization']} data (Y/N)?: ").capitalize()
            while check not in ['Y', 'N']:
                print(colored("Invalid function! Just type Y or N.", 'red'))
                check = input(f"Are you sure to update {Yogyakarta[update_index - 1]['Organization']} data (Y/N)?: ").capitalize()
            if(check == 'Y'):
                Yogyakarta[update_index -1]['Phone'] = update_phone
                Yogyakarta[update_index -1]['Locality'] = update_locality
                Yogyakarta[update_index -1]['Street Name'] = update_street_name
                print(colored(f"Information of {Yogyakarta[update_index -1]['Organization']} is succesfully updated.", 'green'))
                time.sleep(1.0)
                show_yogyakarta(Yogyakarta)
            else:
                print(colored(f"Information of {Yogyakarta[update_index -1]['Organization']} isn't updated.", 'red'))
                show_yogyakarta(Yogyakarta)
        double_check = input("Update another data (Y/N)? : ").capitalize()
        while double_check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.",'red'))
            double_check = input("Update another data (Y/N)? : ").capitalize()
        if(double_check == 'Y'):
            continue
        else:
            break
    return
def anyar_data(Banten):
    show_banten(Banten)
    while True:
        upd_index = input('Put Number Index The Data You Want to Update : ')
        if not numbers(upd_index):
            print(colored("Just Input Number! Please Input Again",'red'))
            time.sleep(1.0)
            continue
        update_index = int(upd_index)
        if((update_index-1) > len(Banten) or update_index < 0):
            print(colored(f'Index {update_index} not in Database.','red'))
            time.sleep(0.4)
            continue
        else:
            update_phone = input(f"{Banten[update_index - 1]['Organization']} New Phone Number : ")
            update_locality = input(f"{Banten[update_index - 1]['Organization']} New Locality : ").title()
            update_street_name = input(f"{Banten[update_index - 1]['Organization']} New Street Address : ").title()
            check = input(f"Are you sure to update {Banten[update_index - 1]['Organization']} data (Y/N)?: ").capitalize()
            while check not in ['Y', 'N']:
                print(colored("Invalid function! Just type Y or N.", 'red'))
                check = input(f"Are you sure to update {Banten[update_index - 1]['Organization']} data (Y/N)?: ").capitalize()
            if(check == 'Y'):
                Banten[update_index -1]['Phone'] = update_phone
                Banten[update_index -1]['Locality'] = update_locality
                Banten[update_index -1]['Street Name'] = update_street_name
                print(colored(f"Information of {Banten[update_index -1]['Organization']} is succesfully updated.", 'green'))
                time.sleep(1.0)
                show_banten(Banten)
            else:
                print(colored(f"Information of {Banten[update_index -1]['Organization']} isn't updated.", 'red'))
                show_banten(Banten)
        double_check = input("Update another data (Y/N)? : ").capitalize()
        while double_check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.",'red'))
            double_check = input("Update another data (Y/N)? : ").capitalize()
        if(double_check == 'Y'):
            continue
        else:
            break
    return
def remove_jakarta(Jakarta):
    show_jakarta(Jakarta)
    while True:
        del_index = input('Put Index Number : ')
        if not numbers(del_index):
            print(colored("Just input Number! Please Input Again",'red'))
            time.sleep(1.0)
            continue
        delete_index = int(del_index)
        if (delete_index > len(Jakarta)):
            print(colored("Data not found. Please the exist Index!",'yellow'))
        else:
            check = input(f"Are you sure to delete {Jakarta[delete_index-1]['Organization']} (Y/N)?: ").capitalize()
            while check not in ['Y', 'N']:
                print(colored("Invalid function! Just type Y or N.", 'red'))
                check = input(f"Are you sure to delete {Jakarta[delete_index-1]['Organization']} (Y/N)?: ").capitalize()
            if(check == 'Y'):
                del Jakarta[delete_index-1]
                print(colored("Data succesfully deleted.",'red'))
                time.sleep(1.0)
                show_jakarta(Jakarta)
            else:
                print(colored(f"Data {Jakarta[delete_index -1]['Organization']} unsuccessful deleted.", 'yellow'))
                time.sleep(1.0)
                show_jakarta(Jakarta)
        double_check = input("Delete another data (Y/N)? : ").capitalize()
        while double_check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.",'red'))
            double_check = str(input("Add another data (Y/N)? : ")).capitalize()
        if(double_check == 'Y'):
            continue
        else:
            break
def remove_westjava(West_Java):
    show_westjava(West_Java)
    while True:
        del_index = input('Put Index Number : ')
        if not numbers(del_index):
            print(colored("Just Input Number! Please input again",'red'))
            time.sleep(1.0)
            continue
        delete_index = int(del_index)
        if (delete_index > len(West_Java)):
            print(colored("Data not found. Please input the existing Index!",'yellow'))
        else:
            check = input('Are you sure to delete the data (Y/N)?: ').capitalize()
            if(check == 'Y'):
                del West_Java[delete_index-1]
                print(colored("Data Succesfully Deleted.",'red'))
                time.sleep(1.0)
                show_westjava(West_Java)
            else:
                print(colored(f"Data {West_Java[delete_index -1]['Organization']} unsuccessful Deleted.", 'yellow'))
                time.sleep(1.0)
                show_westjava(West_Java)
        double_check = input("Delete another data (Y/N)? : ").capitalize()
        while double_check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.",'red'))
            double_check = str(input("Add another data (Y/N)? : ")).capitalize()
        if(double_check == 'Y'):
            continue
        else:
            break
def remove_centraljava(Central_Java):
    show_centraljava(Central_Java)
    while True:
        del_index = input('Put Index Number : ')
        if not numbers(del_index):
            print(colored("Just input Number! Please Input Again",'red'))
            time.sleep(1.0)
            continue
        delete_index = int(del_index)
        if (delete_index > len(Central_Java)):
            print(colored("Data not found. Please the exist Index!",'yellow'))
        else:
            check = input(f"Are you sure to delete {Central_Java[delete_index-1]['Organization']} (Y/N)?: ").capitalize()
            while check not in ['Y', 'N']:
                print(colored("Invalid function! Just type Y or N.", 'red'))
                check = input(f"Are you sure to delete {Central_Java[delete_index-1]['Organization']} (Y/N)?: ").capitalize()
            if(check == 'Y'):
                del Central_Java[delete_index-1]
                print(colored("Data succesfully deleted.",'red'))
                time.sleep(1.0)
                show_centraljava(Central_Java)
            else:
                print(colored(f"Data {Central_Java[delete_index -1]['Organization']} unsuccessful deleted.", 'yellow'))
                time.sleep(1.0)
                show_centraljava(Central_Java)
        double_check = input("Delete another data (Y/N)? : ").capitalize()
        while double_check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.",'red'))
            double_check = str(input("Add another data (Y/N)? : ")).capitalize()
        if(double_check == 'Y'):
            continue
        else:
            break
def remove_eastjava(East_Java):
    show_eastjava(East_Java)
    while True:
        del_index = input('Put Index Number : ')
        if not numbers(del_index):
            print(colored("Just input Number! Please Input Again",'red'))
            time.sleep(1.0)
            continue
        delete_index = int(del_index)
        if (delete_index > len(East_Java)):
            print(colored("Data not found. Please the exist Index!",'yellow'))
        else:
            check = input(f"Are you sure to delete {East_Java[delete_index-1]['Organization']} (Y/N)?: ").capitalize()
            while check not in ['Y', 'N']:
                print(colored("Invalid function! Just type Y or N.", 'red'))
                check = input(f"Are you sure to delete {East_Java[delete_index-1]['Organization']} (Y/N)?: ").capitalize()
            if(check == 'Y'):
                del East_Java[delete_index-1]
                print(colored("Data succesfully deleted.",'red'))
                time.sleep(1.0)
                show_eastjava(East_Java)
            else:
                print(colored(f"Data {East_Java[delete_index -1]['Organization']} unsuccessful deleted.", 'yellow'))
                time.sleep(1.0)
                show_eastjava(East_Java)
        double_check = input("Delete another data (Y/N)? : ").capitalize()
        while double_check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.",'red'))
            double_check = str(input("Add another data (Y/N)? : ")).capitalize()
        if(double_check == 'Y'):
            continue
        else:
            break
def remove_yogyakarta(Yogyakarta):
    show_yogyakarta(Yogyakarta)
    while True:
        del_index = input('Put Index Number : ')
        if not numbers(del_index):
            print(colored("Just input Number! Please Input Again",'red'))
            time.sleep(1.0)
            continue
        delete_index = int(del_index)
        if (delete_index > len(Yogyakarta)):
            print(colored("Data not found. Please the exist Index!",'yellow'))
        else:
            check = input(f"Are you sure to delete {Yogyakarta[delete_index-1]['Organization']} (Y/N)?: ").capitalize()
            while check not in ['Y', 'N']:
                print(colored("Invalid function! Just type Y or N.", 'red'))
                check = input(f"Are you sure to delete {Yogyakarta[delete_index-1]['Organization']} (Y/N)?: ").capitalize()
            if(check == 'Y'):
                del Yogyakarta[delete_index-1]
                print(colored("Data succesfully deleted.",'red'))
                time.sleep(1.0)
                show_yogyakarta(Yogyakarta)
            else:
                print(colored(f"Data {Yogyakarta[delete_index -1]['Organization']} unsuccessful deleted.", 'yellow'))
                time.sleep(1.0)
                show_yogyakarta(Yogyakarta)
        double_check = input("Delete another data (Y/N)? : ").capitalize()
        while double_check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.",'red'))
            double_check = str(input("Add another data (Y/N)? : ")).capitalize()
        if(double_check == 'Y'):
            continue
        else:
            break
def remove_banten(Banten):
    show_banten(Banten)
    while True:
        del_index = input('Put Index Number : ')
        if not numbers(del_index):
            print(colored("Just input Number! Please Input Again",'red'))
            time.sleep(1.0)
            continue
        delete_index = int(del_index)
        if (delete_index > len(Banten)):
            print(colored("Data not found. Please the exist Index!",'yellow'))
        else:
            check = input(f"Are you sure to delete {Banten[delete_index-1]['Organization']} (Y/N)?: ").capitalize()
            while check not in ['Y', 'N']:
                print(colored("Invalid function! Just type Y or N.", 'red'))
                check = input(f"Are you sure to delete {Banten[delete_index-1]['Organization']} (Y/N)?: ").capitalize()
            if(check == 'Y'):
                del Banten[delete_index-1]
                print(colored("Data succesfully deleted.",'red'))
                time.sleep(1.0)
                show_banten(Banten)
            else:
                print(colored(f"Data {Banten[delete_index -1]['Organization']} unsuccessful deleted.", 'yellow'))
                time.sleep(1.0)
                show_banten(Banten)
        double_check = input("Delete another data (Y/N)? : ").capitalize()
        while double_check not in ['Y', 'N']:
            print(colored("Invalid function! Just type Y or N.",'red'))
            double_check = str(input("Add another data (Y/N)? : ")).capitalize()
        if(double_check == 'Y'):
            continue
        else:
            break

while True:
    greetings()
    input_menu = input('Enter Menu you want : ')
    if(input_menu == '1'):
        while True:
            categories_choose()
            time.sleep(0.3)
            input_categories = input('Enter Menu you want : ')
            if(input_categories == '1'):
                print(colored("Nick's Express Special Region of Jakarta Database\n",'green'))
                time.sleep(1.0)
                show_jakarta(Jakarta)
            elif(input_categories == '2'):
                print(colored("Nick's Express West Java Database\n",'green'))
                time.sleep(1.0)
                show_westjava(West_Java)
            elif(input_categories == '3'):
                print(colored("Nick's Express Central Java Database\n",'green'))
                time.sleep(1.0)
                show_centraljava(Central_Java)
            elif(input_categories == '4'):
                print(colored("Nick's Express East Java Database\n",'green'))
                time.sleep(1.0)
                show_eastjava(East_Java)
            elif(input_categories == '5'):
                print(colored("Nick's Express Special Region of Yogyakarta Database\n",'green'))
                time.sleep(1.0)
                show_yogyakarta(Yogyakarta)
            elif(input_categories == '6'):
                print(colored("Nick's Express Banten Database\n",'green'))
                time.sleep(1.0)
                show_banten(Banten)
            elif(input_categories == '0'):
                break
            else:
                print(colored("Invalid function, please input again!", 'red'))
                time.sleep(1.0)
                continue
            toTheMoon = back()
            while toTheMoon not in ['Y', 'N']:
                print(colored("Invalid function! Just type Y or N.",'red'))
                toTheMoon = back()
            if(toTheMoon == 'Y'):
                continue
            else:
                break
    elif(input_menu == '2'):
        while True:
            sub_menu2()
            time.sleep(0.4)
            input_submenu2 = input('Enter Menu you want : ')
            if(input_submenu2 == '1'):
                while True:
                    categories_choose()
                    time.sleep(0.4)
                    input_categories = input('Enter Categories : ')
                    if(input_categories == '1'):
                        new_data(Jakarta)
                        break
                    elif(input_categories == '2'):
                        add_data(West_Java)
                        break
                    elif(input_categories == '3'):
                        baru_data(Central_Java)
                        break
                    elif(input_categories == '4'):
                        tulis_data(East_Java)
                        break
                    elif(input_categories == '5'):
                        catat_data(Yogyakarta)
                        break
                    elif(input_categories == '6'):
                        nyatet_data(Banten)
                        break
                    elif(input_categories == '0'):
                        break
                    else:
                        print(colored("Function not found. Please input again!",'red'))
                        time.sleep(1.0)
            elif(input_submenu2 == '2'):
                while True:
                    categories_choose()
                    time.sleep(0.4)
                    input_categories = input('Enter Categories : ')
                    if(input_categories == '1'):
                        update_data(Jakarta)
                        time.sleep(1.5)
                        break
                    elif(input_categories == '2'):
                        perbaharui_data(West_Java)
                        time.sleep(1.5)
                        break
                    elif(input_categories == '3'):
                        pembaharuan_data(Central_Java)
                        time.sleep(1.5)
                        break
                    elif(input_categories == '4'):
                        perubahan_data(East_Java)
                        time.sleep(1.5)
                        break
                    elif(input_categories == '5'):
                        ganti_data(Yogyakarta)
                        time.sleep(1.5)
                        break
                    elif(input_categories == '6'):
                        anyar_data(Banten)
                        time.sleep(1.5)
                        break
                    elif(input_categories == '0'):
                        break
                    else:
                        print(colored("Function not found. Please input again!",'red'))
                        time.sleep(1.0)
            elif(input_submenu2 == '0'):
                break
            else:
                print(colored("Invalid function, please input again!", 'red'))
                time.sleep(1.0)
                continue
            toTheMoon = back()
            while toTheMoon not in ['Y', 'N']:
                print(colored("Invalid function! Just type Y or N.",'red'))
                toTheMoon = back()
            if(toTheMoon == 'Y'):
                time.sleep(0.4)
                continue
            else:
                break
    elif(input_menu == '3'):
        while True:
            categories_choose()
            time.sleep(0.4)
            input_categories = input('Enter Category You Want to Delete: ')
            if(input_categories == '1'):
                remove_jakarta(Jakarta)
                time.sleep(1.5)
                break
            elif(input_categories == '2'):
                remove_westjava(West_Java)
                time.sleep(1.5)
                break
            elif(input_categories == '3'):
                remove_centraljava(Central_Java)
                time.sleep(1.5)
                break
            elif(input_categories == '4'):
                remove_eastjava(East_Java)
                time.sleep(1.5)
                break
            elif(input_categories == '5'):
                remove_yogyakarta(Yogyakarta)
                time.sleep(1.5)
                break
            elif(input_categories == '6'):
                remove_banten(Banten)
                time.sleep(1.5)
                break
            elif(input_categories == '0'):
                break
            else:
                print(colored("Function not found. Please input again!",'red'))
                time.sleep(1.0)
            toTheMoon = back()
            while toTheMoon not in ['Y', 'N']:
                print(colored("Invalid function! Just type Y or N.",'red'))
                toTheMoon = back()
            if(toTheMoon == 'Y'):
                time.sleep(0.4)
                continue
            else:
                break
    elif(input_menu == "7"):
        exit()
    else:
        print(colored("Function not found. Please input again!",'red'))
        time.sleep(1.0)