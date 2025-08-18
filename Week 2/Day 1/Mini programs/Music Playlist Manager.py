playlists = {
    "Workout": ["Song A", "Song B"],
    "Relax": ["Song C", "Song D"]
}

# Set of all unique songs in library
all_songs = set(["Song A", "Song B", "Song C", "Song D"])

def show_playlists():
    print("\nPlaylists:")
    for name, songs in playlists.items():
        print(f"{name}: {songs}")

def add_song(playlist, song):
    if playlist in playlists:
        playlists[playlist].append(song)
        all_songs.add(song)
        print(f"Added {song} to {playlist} playlist.")

def unique_songs():
    print("\nUnique songs across all playlists:", all_songs)

# --- Demo ---
show_playlists()
add_song("Workout", "Song E")
unique_songs()
