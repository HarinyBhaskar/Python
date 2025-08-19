def create_playlist(user_name, *songs, **settings):
    print(f"\nPlaylist for {user_name}")
    print("-" * 40)

    print("Songs Added:")
    for s in songs:
        print(f"- {s}")

    shuffle = settings.get("shuffle", False)
    repeat = settings.get("repeat", False)
    volume = settings.get("volume", 50)

    print("-" * 40)
    print(f"Shuffle Mode : {'ON' if shuffle else 'OFF'}")
    print(f"Repeat Mode  : {'ON' if repeat else 'OFF'}")
    print(f"Volume Level : {volume}")
    print("-" * 40)


# Example usage
create_playlist(
    "Devika",
    "Kesariya", "Tum Hi Ho", "Senorita",
    shuffle=True, repeat=False, volume=70
)

create_playlist(
    "Arjun",
    "Shape of You", "Blinding Lights"
)
