from .videoDuration import getDuration
import os
import json

class video:
    def __init__(self, path, name, year) -> None:
        if os.path.exists(path):
            self.path = path
        else:
            raise FileNotFoundError("The Video File Does Not Exists, Please Check Your Spelling.")
        self.name = name
        self.year = year
        try:
            self.duration = getDuration(path)
        except Exception as e:
            raise Exception(f"Some Error Occured While finding video Duration: {str(e)}")


    def to_dict(self):
        return {
            "path": self.path,
            "name": self.name,
            "year": self.year,
            "duration": self.duration
        }
    
def getPath(path):
    return path.split("/")[-1]
    
    
def addVideo(vid):
    vid = vid.to_dict()
    with open("Backend_Scripts/ListofVideos.json", 'r') as File:
        videolist = json.load(File)

    videolist.append(vid)

    with open("Backend_Scripts/ListofVideos.json", "w") as file:
        json.dump(videolist, file)


def removeVideo(vid):
    vid = vid.to_dict()
    with open("Backend_Scripts/ListofVideos.json", 'r') as File:
        videolist = json.load(File)

    videolist.remove(vid)

    with open("Backend_Scripts/ListofVideos.json", "w") as file:
        json.dump(videolist, file)



if __name__ == "__main__":
    one = video('static/Videos/Classical Training.mp4', 'Training in Classical with the Kids', 2024)
    two = video('static/Videos/Classical Singing 2.mp4', 'Classical Practice 2', 2023)
    three = video('static/Videos/Singing Classes.mp4', 'Durga Puja Music Reharsal with Alaap', 2022)
    four = video('static/Videos/Singing Songs with Children.mp4', 'Singing with the Lil\' ones', 2024)

    listofVideos = [one, two, three, four]
    listofVideos = [video.to_dict() for video in listofVideos]
    with open("Backend_Scripts/ListofVideos.json", "w") as file:
        json.dump(listofVideos, file)