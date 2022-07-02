import subprocess
import os
import re
from collections import namedtuple
import configparser

def get_windows_saved_ssids():
    """Returns a list of saved SSIDs in a Windows machine using netsh cmmand"""
    # get all saved profiles in the PC
    output = subprocess.check_output('netsh wlan show profiles').decode()
    ssids = []
    profiles = re.findall(r'All User Profile\s(.*)',output)
    for profile in profiles:
        # for each SSID, remove spaces and colon
        ssid = profile.strip().strip(':').strip()
        # add to the  list
        ssids.append(ssid)
    return ssids

def get_windows_saved_wifi_passwords(verbose=1):
    """Extracts saved Wi-Fi passwords saved in a Windows machine, this function extracts data using netsh
    command in Windows
    Args:
        verbose (int, optional): whether to print saved profiles real-time. Defaults to 1.
    Returns:
        [list]: list of extracted profiles, a profile has the fields ['ssid', 'ciphers','key']
    """
    ssids  = get_windows_saved_ssids()
    Profile = namedtuple('Profile', ['ssid', 'cipher', 'key'])
    profiles = []
    for ssid in ssids:
        ssid_details = subprocess.check_output(f"""netsh wlan show profile '{ssid} key=clear""").decode()
        # getthe ciphers
        ciphers = re.findall(r'cipher\s(.*)', ssid_details)
        # clear spaces and colon
        ciphers = '/'.join([c.strip().strip(':').strip() for c in ciphers])
        # get the Wi-Fi password
        key = re.findall(r'key Content\s(.*)', ssid_details)
        # clear spaces and colon
        try:
            key = key[0].strip().strip(':').strip()
        except IndexError:
            key = 'None'
        profile = Profile(ssid=ssid, ciphers=ciphers, key=key)
        if verbose >=1:
            print_windows_profile(profile)
            profiles.append(profile)
    return profiles

def print_windows_profile(profile):
    """Prints a single profile on windows"""
    print(f'{profile.ssid:25}{profile.ciphers:15}{profile.key:50}')


def print_windows_profiles(verbose):
    """Prints all extracted SSIDs along with key on windows"""
    print('SSID      CIPHER(S)  KEY')
    print('-'*50)
    get_windows_saved_wifi_passwords(verbose) 

def print_profiles(verbose = 1):
    if os.name == 'nt':
        print_windows_profiles(verbose)
    elif os.name == 'posix':
        print_windows_profiles(verbose)
    else:
        raise NotImplemented('code only works on linux or windows') 

# It means if the program is run (instead of being imported), run the game:
if __name__ == '__main__':
    print_profiles()               