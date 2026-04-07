import json



def load_Data():
    try: 
        with open("youtube.txt", "r") as file:
            content = file.read().strip()
            if not content:  # if file is empty
                return []
            return json.loads(content)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_Data(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)

def list_All_Videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']}, Time: {video['time']}")
    print("\n")
    print("*" * 70)

def add_videos(videos):
    
    name = input("Enter video name: ")
    time = input("Enter video time: ")

    videos.append({
        "name": name,
        "time": time        
    })

    save_Data(videos)

def update(videos):
    list_All_Videos(videos)

    index = int(input("Enter the number for update the video: "))
    if 1 <= index <= len(videos):
        name = input("Enter the title: ")
        time = input("Enter the time: ")

        videos[index-1] = {'name': name, 'time': time}
        save_Data(videos)

    

def delete_video(videos):
    list_All_Videos(videos)
    index = int(input("Enter the numbe for delete: "))
    if 1 <= index <= len(videos):
        del(videos[index -1])

        save_Data(videos)


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
      