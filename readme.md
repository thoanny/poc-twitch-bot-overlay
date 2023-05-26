# PoC: Twitch Bot & Overlay

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