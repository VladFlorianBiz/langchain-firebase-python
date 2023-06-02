# dev
```bash
cd functions
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
firebase emulators:start --only functions
```

# deploy
```bash
firebase deploy --only functions
```