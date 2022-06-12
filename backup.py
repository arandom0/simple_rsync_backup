import os

def run():
    display_welcome_msg()
    srcDir = get_dir_user_input_and_confirmation("ENTER SOURCE DIR:")
    destDir = get_dir_user_input_and_confirmation("ENTER DESTINATION DIR:")
    perform_rsync_backup(srcDir, destDir)
    
def display_welcome_msg():
    msg = "*** WARNING !!!\n"
    msg += "This is a backup script.\n"
    msg += "It makes the destination folder look exactly like the source folder.\n"
    msg += "Files at the destination are added, deleted and over-written if necessary.\n"
    msg += "Be very careful not to confuse source with destination.\n\n"
    msg += "PRESS ENTER TO CONTINUE"
    input(msg)

def get_dir_user_input_and_confirmation(msg):
    os.system("clear")
    while 1==1:
        usrInput = input(f"{msg}\n").strip()
        if usrInput.endswith("/"): usrInput = usrInput[:-1]

        os.system("clear")
        if not os.path.isdir(usrInput): print("*** Invalid directory, try again"); continue
        
        while 1==1:
            usrInputConfirm = input(f"YOU ENTERED:\n{usrInput}\n\nARE YOU SURE? (y/n)\n").strip().lower()
            os.system("clear")
            if usrInputConfirm == "y": return usrInput
            elif usrInputConfirm == "n": break
            else: print("*** Invalid user response, try again"); continue

def perform_rsync_backup(srcDir, destDir):
    os.system("clear")
    print("----------------------------\nPERFORMING BACKUP\n----------------------------\n\n")
    # rsync -av --delete "/src/dir/" "/dest/dir/"
    os.system(f"rsync -av --delete \"{srcDir}/\" \"{destDir}/\"")
    print("\n\n----------------------------\nOPERATION COMPLETE\n----------------------------\n")
    input("PRESS ENTER TO EXIT")

run()
