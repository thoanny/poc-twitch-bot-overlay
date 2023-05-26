# PoC: Twitch Bot & Overlay

Configurer TwitchIO, en créant un fichier `.env` avec :

```
TMI_TOKEN= # https://twitchapps.com/tmi/
CLIENT_ID= # Identifiant Twitch de l'app à créer sur https://dev.twitch.tv
BOT_NICK= # Pseudo du Bot, doit correspondre au compte connecté pour TMI_TOKEN
BOT_PREFIX= # Préfixe des commandes ("!" par exemple)
CHANNEL= # Nom de la chaîne
```

Pour lancer le serveur Python (http://localhost:8000) :

``py main.py``

Pour travailler sur l'overlay (http://localhost:5173) :

```
cd overlay
npm run dev
```

Le serveur Pyhon pointe vers `overlay/dist`, il faut donc build l'application Vue pour que les modifications soient visibles :

```
cd overlay
npm run build
```