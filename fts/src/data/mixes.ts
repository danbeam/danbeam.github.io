export interface Mix {
  id: string;
  name: string;
  mixcloudUrl?: string;
  soundcloudUrl?: string;
  spotifyUrl?: string;
  picture: string;
  tags: string[];
  duration: string;
  date: string;
}

export const MIXES: Mix[] = [
  {
    id: "house-blend-medium-roast",
    name: "House Blend: Medium Roast",
    mixcloudUrl: "https://www.mixcloud.com/funk-the-system/house-blend-medium-roast/",
    soundcloudUrl: "https://soundcloud.com/funk-the-system/house-blend-medium-roast",
    spotifyUrl: "https://open.spotify.com/playlist/7nS1KaJ3oJMVT4dZvAEOVV",
    picture: "https://thumbnailer.mixcloud.com/unsafe/600x600/extaudio/9/d/d/9/280e-7c16-4ec4-a87e-6246fc602ad5",
    tags: ["Melodic House", "House"],
    duration: "35m",
    date: "2026-03-08"
  },
  {
    id: "without-you-i-cant-funktion",
    name: "Without You I Can't Funktion",
    mixcloudUrl: "https://www.mixcloud.com/funk-the-system/without-you-i-cant-funktion/",
    soundcloudUrl: "https://soundcloud.com/funk-the-system/without-you-i-cant-funktion",
    spotifyUrl: "https://open.spotify.com/playlist/7qxfTgNrOTuJl3iUr1DT2T",
    picture: "https://thumbnailer.mixcloud.com/unsafe/600x600/extaudio/3/d/b/4/45e5-7c86-4ad2-a21c-b2b18e07eef3",
    tags: ["Funktronica", "Dream Pop", "Funk"],
    duration: "1h 19m",
    date: "2026-01-04"
  },
  {
    id: "halloweenie-roast-2025",
    name: "Halloweenie Roast 2025",
    mixcloudUrl: "https://www.mixcloud.com/funk-the-system/halloweenie-roast-2025/",
    soundcloudUrl: "https://soundcloud.com/funk-the-system/halloweenie-roast-2025",
    spotifyUrl: "https://open.spotify.com/playlist/2wYlPc8nxtYABq9u7elQDg",
    picture: "https://i1.sndcdn.com/artworks-Vzp9bwBFlB6Th0nu-IyWGUQ-t500x500.jpg",
    tags: ["Bass House", "Dubstep"],
    duration: "57m",
    date: "2025-10-30"
  },
  {
    id: "cruel-summer",
    name: "Cruel Summer",
    mixcloudUrl: "https://www.mixcloud.com/funk-the-system/cruel-summer/",
    soundcloudUrl: "https://soundcloud.com/funk-the-system/cruel-summer",
    spotifyUrl: "https://open.spotify.com/playlist/4IoDO99HIQJnCGCxS3gghc?si=7f94b6eeeff1436b",
    picture: "https://thumbnailer.mixcloud.com/unsafe/600x600/extaudio/6/e/2/1/5b94-2ad1-4f83-9b7d-0d683d7b27e4",
    tags: ["Tropical House", "Afro House"],
    duration: "1h 17m",
    date: "2025-07-04"
  },
  {
    id: "chill-the-funk-out",
    name: "Chill The Funk Out",
    soundcloudUrl: "https://soundcloud.com/funk-the-system/chill-the-funk-out",
    spotifyUrl: "https://open.spotify.com/playlist/2mC7QKMb7HJtHBCsk6W40Q",
    picture: "https://i1.sndcdn.com/artworks-ywHVi9Yb79xragVZ-ePPNVg-t500x500.jpg",
    tags: ["Chill", "Funk"],
    duration: "1h 12m",
    date: "2025-06-17"
  },
  {
    id: "remix-radio-hour",
    name: "Remix Radio Hour",
    soundcloudUrl: "https://soundcloud.com/funk-the-system/remix-radio-hour",
    spotifyUrl: "https://open.spotify.com/playlist/12i7gmFjPDzNW9suM9TUHT",
    picture: "https://i1.sndcdn.com/artworks-LrmSEWyGVmyN0rPu-jfVnIg-t500x500.jpg",
    tags: ["Remix", "Radio"],
    duration: "1h 0m",
    date: "2025-03-12"
  },
  {
    id: "halloweenie-roast-2024-haunted-house",
    name: "Halloweenie Roast 2024: Haunted House",
    mixcloudUrl: "https://www.mixcloud.com/funk-the-system/halloweenie-roast-2024-house-party/",
    spotifyUrl: "https://open.spotify.com/playlist/217IN8bKxBkmuoRiwV0x8s?si=3df78b3924bf436e",
    picture: "https://thumbnailer.mixcloud.com/unsafe/600x600/extaudio/4/2/7/e/1771-475d-4954-b634-a5ff2c88e31b",
    tags: ["House", "Spooky"],
    duration: "34m",
    date: "2024-10-30"
  },
  {
    id: "halloweenie-roast-2024-its-a-trap",
    name: "Halloweenie Roast 2024: It's A Trap!",
    mixcloudUrl: "https://www.mixcloud.com/funk-the-system/halloweenie-roast-2024-its-a-trap/",
    spotifyUrl: "https://open.spotify.com/playlist/1raS1id7qiBFsu9Klc2qZG?si=8555322f102f4391",
    picture: "https://thumbnailer.mixcloud.com/unsafe/600x600/extaudio/b/a/7/f/3d4a-f00c-41ea-a679-4f85fe93a483",
    tags: ["Bass", "Trap", "Midtempo"],
    duration: "37m",
    date: "2024-10-30"
  },
  {
    id: "halloweenie-roast-2024",
    name: "Halloweenie Roast 2024",
    soundcloudUrl: "https://soundcloud.com/funk-the-system/halloweenie-roast-2024",
    spotifyUrl: "https://open.spotify.com/playlist/303D1MDpgquviFb1hZSnaZ",
    picture: "https://i1.sndcdn.com/artworks-CBJNX76jnXTCKh9T-5grCIg-t500x500.png",
    tags: ["Halloween", "Mix"],
    duration: "58m",
    date: "2024-10-30"
  }
];
