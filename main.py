import traceback, os, getpass
from threading import Thread


print("Please confirm account deletion Y/N :")

user_response = input()


def start_deletion():
    if user_response == "Y" or user_response == "y":
        try:
            current_user = getpass.getuser()
            print(current_user)
            # set the directory path to C:\Users
            user_dir = "C:\\Users\\"

            # list all directories in the user directory
            directories = os.listdir(user_dir)

            # loop through the directories and delete only the ones that are not default and not the current user's directory
            for directory in directories:
                if (
                    directory
                    not in [
                        "Default",
                        "Public",
                        "All Users",
                        "Default User",
                        "desktop.ini",
                        "Administrator",
                        "TEMP",
                        "Admin",
                        "Temp",
                    ]
                    and directory != current_user
                ):
                    dir_path = os.path.join(user_dir, directory)
                    try:
                        # delete the directory and all its contents recursively

                        os.system('rmdir /S /Q "{}"'.format(dir_path))
                        print("Directory '{}' deleted successfully.".format(directory))
                    except Exception as e:
                        print(
                            "Failed to delete directory '{}'. Error: {}".format(
                                dir_path, e
                            )
                        )

                        print(
                            "All user profiles except the current and system profiles have been deleted."
                        )
                    except:
                        print(str(traceback.format_exc()))

        except:
            print("ads")


x = Thread(target=start_deletion)
x.start()
x.join()

input("Press Enter to continue...")
