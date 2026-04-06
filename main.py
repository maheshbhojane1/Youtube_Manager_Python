import json


def load_Data():
    try: 
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_Data(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file, indent=4)

def list_All_Videos(videos):
   for video, index in enumerate(videos, start=1):
       print(f"{index} .")


def add_videos(videos):
    
    name = input("Enter video name: ")
    time = input("Enter video time: ")

    videos.append({
        "name": name,
        "time": time        
    })

    save_Data(videos)

def update(videos):
    pass

def delete_video(videos):
    pass




def main():
    videos = load_Data()

    while True:
        print("\n Youtube Maneger / Choosse an options")
        print("1. List of all youtube videos")
        print("2. Add new youtube videos")
        print("3. Update youtube videos details")
        print("4. Delete youtube videos")
        print("5. Exit from app")
        print(videos)



        choice = input("Enter the number:  ")

        match choice:
            case "1":
                list_All_Videos(videos)
            case "2":
                add_videos(videos)
            case "3":
                update(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("Exiting the app...")
                break
            case _:
                print("Invalid choice. Please try again.")       


main()
      