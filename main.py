import os
import sys
import time
import random
import subprocess
import requests

R = "\033[31m"
G = "\033[32m"
B = "\033[34m"
W = "\033[0m" 
Y = "\033[33]"
print (f"test {R}R{G}G{B}B{Y}Y{W}W")
def check_adb_devices():
    # Run the 'adb devices' command and capture the output
    result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    output = result.stdout.strip()

    # Parse the output to find connected devices
    lines = output.split("\n")
    devices = [line.split("\t")[0] for line in lines[1:] if "\tdevice" in line]

    # Log the command and output
    log_output("adb devices", output)

    # Check the number of devices
    if len(devices) == 1:
        print(f"Device connected: {devices[0]}")
        log("Device is good, continue")
        return devices[0]  # Continue with the connected device
    elif len(devices) == 0:
        print("Error: No ADB devices connected, if you are in fastboot this can be ignored, if not, check logs.", file=sys.stderr)
        log("No phone connected (check wiki or reconnect)")
    else:
        print("Error: Multiple ADB devices connected. Please connect only one.", file=sys.stderr)
        log("Multiple devices connected (adb kill-server might help)")
    sys.exit(1)  # Exit with an error if no devices or multiple devices are connected

def log_output(command, output):
    with open("log.txt", "a") as log_file:
        log_file.write(f"Executing: {command}\n")
        log_file.write(f"Output:\n{output}\n{'-'*40}\n")
        
def log(command):
    with open("log.txt", "a") as log_file:
        log_file.write(f"Logged: {command}\n")

def run_command(command):
    # Run the command and capture the output
    process = subprocess.run(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # Log the command and output to a file
    log_output(command, process.stdout + process.stderr)
    # Check for errors and exit if the command fails
    if process.returncode != 0:
        print(f"{R}[ERROR]{W}: {command}. Check log.txt for details.", file=sys.stderr)

def loading_screen(wait_time=2):
    loading_messages = [
        "Flipping the bits..", 
        "Calling the maid..", 
        "Preheating the server..", 
        "Adjusting the matrix..", 
        "Summoning the AI overlords..", 
        "Rebooting the hamster wheel..", 
        "Charging the flux capacitor..", 
        "Tuning the space-time continuum..", 
        "Cleaning the intergalactic dust..", 
        "Cracking the code.."
    ]
    
    # Randomly pick a message from the list
    message = random.choice(loading_messages)
    print(message, flush=True)
    log("Loading")

def display_menu():
    print("\nSelect Function:")
    print("1. Clean dirt apps")
    print("2. Uninstall unnecessary apps")
    print("3. Chinafy your phone (WILL RESET HOME LAYOUT (nothing else)")
    print("4. Install Super Wallpapers")
    print("5. Install helpful tools")
    print("6. Reboot")
    print("0. Exit")

def reboot():
    print("1. Reboot to system")
    print("2. Reboot to fastboot")
    print("3. Reboot to fastbootd")  
    print("4. Reboot to system (from fastboot)")
    print("0. Back")
    ans = input("Enter your choice : ")
    if ans == '1':
        run_command("adb reboot")
    elif ans == '2':
        run_command("adb reboot bootloader")
    elif ans == '3':
        run_command("adb reboot fastboot")
    elif ans == '4':
        run_command("fastboot reboot")
    elif ans == '0':
        print("Main Menu")
          
def clean_dirt_apps():
    loading_screen(2)
    log("db start")
    apps_to_uninstall = [
        "com.google.android.adservices.api", "com.miui.analytics", "com.google.android.marvin.talkback", 
        "com.google.android.projection.gearhead", "com.android.egg", "com.google.android.apps.restore", 
        "com.google.android.as", "android.qvaoverlay.common", "com.mi.globalminusscreen", 
        "com.longcheertel.AutoTest", "com.miui.backup", "com.android.bluetoothmidiservice", 
        "com.miui.extraphoto", "com.xiaomi.barrage", "com.xiaomi.calendar", "com.android.calllogbackup", 
        "com.android.cameraextensions", "com.longcheertel.cit", "com.miui.cleaner", "com.miui.cloudbackup", 
        "com.android.cellbroadcastreceiver.overlay.common", "com.android.inputsettings.overlay.miui", 
        "com.android.managedprovisioning.overlay", "com.android.overlay.gmscontactprovider", 
        "com.android.overlay.gmssettingprovider", "com.android.overlay.gmssettings", 
        "com.android.overlay.gmstelecomm", "com.android.overlay.gmstelephony", 
        "com.android.providers.partnerbookmarks", "com.android.settings.overlay.miui", 
        "com.android.stk.overlay.miui", "com.android.systemui.accessibility.accessibilitymenu", 
        "com.android.systemui.overlay.common", "com.android.systemui.overlay.miui", 
        "com.android.virtualmachine.res", "com.google.android.cellbroadcastreceiver.overlay.miui", 
        "com.google.android.cellbroadcastrservice.overlay.miui", "com.google.android.federatedcompute", 
        "com.google.android.overlay.gmsconfig.asi", "com.google.android.overlay.healthconnect", 
        "com.google.android.overlay.modules.captiveportallogin.forframework", 
        "com.google.android.overlay.modules.documentsui", "com.google.android.overlay.modules.permissioncontroller", 
        "com.miui.miwallpaper.overlay", "com.miui.miwallpaper.overlay", "com.miui.miwallpaper.overlay.customize", 
        "com.miui.phone.carriers.overlay.h3g", "com.miui.phone.carriers.overlay.vodafone", "com.miui.qr", 
        "com.miui.settings.rro.deivce.hide.statusbar.overlay", "com.miui.settings.rro.devjice.type.overlay", 
        "com.miui.system.overlay", "com.miui.wallpaper.overlay", "com.miui.wallpaper.overlay", 
        "com.miui.wallpaper.overlay.customize", "com.qti.service.colorservice", "com.qualcomm.atfwd2", 
        "com.qualcomm.qti.devicestatisticsservice", "com.qualcomm.qti.qms.service.trustzoneaccess", 
        "com.qualcomm.qti.uim", "com.qualcomm.qti.uimGbaApp", "com.qualcomm.uimremoteclient", 
        "com.qualcomm.uimremoteserver", "com.google.ambient.streaming", "com.google.android.apps.restore", 
        "com.qti.dcf", "com.google.android.apps.turbo", "com.qti.qualcomm.deviceinfo", "com.google.android.gms.supervision", 
        "com.goodix.gftest", "com.google.android.gms.location.history", "com.xiaomi.glgm", 
        "com.google.android.apps.healthdata", "com.qualcomm.location", "com.google.mainline.adservices", 
        "com.google.android.feedback", "com.facebook.system", "com.facebook.services", "com.xiaomi.payment", 
        "com.miui.videoplayer", "com.xiaomi.trustservice", "com.miui.msa.global", "com.qualcomm.qti.performancemode", 
        "com.qualcomm.qti.server.qtiwifi", "com.qualcomm.qti.ridemodeaudio", "com.xiaomi.mtb", 
        "com.fingerprints.sensortesttool"
    ]
    for app in apps_to_uninstall:
        run_command(f"adb uninstall {app}")
    print("The picomi program has cleared the 'dirt' apps")
    log("db finish")

def uninstall_unnecessary_apps():
    loading_screen(2)
    log("db2 start")
    apps_to_uninstall = [
        "com.google.android.apps.youtube.music", "com.miui.player", "com.miui.micloudsync", 
        "com.mi.globalbrowser", "com.facebook.appmanager", "com.google.android.apps.tachyon", 
        "com.google.android.feedback", "com.google.android.videos", "com.google.android.onetimeinitializer", 
        "com.google.android.apps.subscriptions.red", "com.xiaomi.mipicks", "com.miui.phrase", 
        "com.miui.fmservice", "com.miui.fm", "com.miui.bugreport"
    ]
    for app in apps_to_uninstall:
        run_command(f"adb uninstall {app}")
    print("The picomi program has cleared the unnecessary apps")
    log("db2 finish")

def chinafy_phone():
    loading_screen(2)
    log("China-fy Started")
    run_command('adb shell pm uninstall --user 0 com.miui.home')
    run_command("adb install home.apk")
    run_command("adb install miai.apk")
    run_command('adb shell pm uninstall --user 0 com.android.thememanager')
    run_command('adb install themes.apk')
    run_command('adb shell pm uninstall --user 0 com.xiaomi.mipicks')
    run_command("adb install apps.apk")
    run_command('adb shell pm uninstall --user 0 com.xiaomi.xmsf')
    run_command("adb install fwk.apk")
    run_command("adb install clock.apk")
    ans = input("Do you want to install chinese-only music? y/n : ")
    if ans == 'y' :
        run_command("adb shell pm uninstall --user 0 com.miui.player")
        run_command("adb install music.apk")
        log("HyperOS music installed")
    run_command("adb install settings.apk")
    run_command("adb install uiplugin.apk")
    run_command('adb shell monkey -p com.mi.pico -c android.intent.category.LAUNCHER 1')
    print("PLEASE UNLOCK YOUR PHONE!")
    log("China-fy End")

def install_super_wallpapers():
    loading_screen(3)
    log("Installing Superwallpaper")
    run_command("adb install superearth.apk")
    run_command("adb install supermountain.apk")
    run_command("adb install wallpapers.apk")
    run_command("adb install live.apk")
    print("The wallpaper managing app is: Google Wallpapers")
    log("SW installed")

def install_helpful_tools():
    response = requests.get('https://github.com/maybe-asdf/picomi/raw/refs/heads/main/Piercera.apk')
    with open('piercera.apk', 'wb') as f:
        f.write(response.content)
    run_command("adb install piercera.apk")
    # https://github.com/samolego/Canta/releases/download/2.2.2/app-release.apk

if __name__ == "__main__":
    check_adb_devices()

    ans = input("WARNING! What you do with your devices and this script is your responsibility, I will not be held accountable if you break your phone, void your warranty, etc. THIS IS YOUR RESPONSIBILITY! If you agree to these terms, please type yes or no: ")
    if ans == 'yes':
        print("Alright! Let's start")
        log("Agreed, continue")
        run_command("adb install helper.apk")
        run_command("adb shell monkey -p com.mi.pico -c android.intent.category.LAUNCHER 1")
    else:
        log("Disagreed to terms (check caps?)")
        quit()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            clean_dirt_apps()
        elif choice == '2':
            uninstall_unnecessary_apps()
        elif choice == '3':
            chinafy_phone()
        elif choice == '4':
            install_super_wallpapers()
        elif choice == '5':
            install_helpful_tools()
        elif choice == '6':
            reboot()
        elif choice == '0':
            print("Exiting, thank you for using picomi!")
            log("Done. Exiting")
            run_command("adb uninstall com.mi.pico")
            break
        else:
            print("Invalid choice, please try again.")
