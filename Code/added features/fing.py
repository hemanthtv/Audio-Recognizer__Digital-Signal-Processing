from dejavu import Dejavu

config = {
    "database": {
        "host": "127.0.0.1",
        "user": "root",
        "passwd": "thimmareddy@1", 
        "db": "dejavu"
    }
}
djv = Dejavu(config)
djv.fingerprint_directory(r"C:\Users\Hemanth\dejavu\mp3", [".mp3"], 3)
