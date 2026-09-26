Ultron

Your friendly neighbourhood AI assistant. Slightly less evil than the original.

Ultron is a small Python voice assistant that can listen to commands, speak back, search the web/Wikipedia, calculate things, set timers, read news, and perform a few questionable dice/card tricks.

Setup

1. Create a virtual environment

python -m venv .venv
.venv\Scripts\Activate.ps1

2. Install dependencies

pip install pyttsx3 SpeechRecognition wikipedia pygame requests

You may also need a working microphone and the audio dependencies required by your operating system.

3. Add NEWS_API_KEY (optional)

The news feature uses NewsAPI and is optional. Ultron reads the key from the NEWS_API_KEY environment variable.

Get your API key

Go to newsapi.org/register.

Create a NewsAPI account and verify your email if requested.

Sign in and copy your API key from the NewsAPI dashboard.

In PowerShell, set it for your current terminal:

$env:NEWS_API_KEY="your-api-key-here"

Then start Ultron from that same terminal.

Keep the key secret. Do not commit it to GitHub. Add .env and other secret files to .gitignore if you use them.

Run Ultron

python Ultron_v2.py

Wait for Ultron to greet you, then call its name and give it a command.

Things to try

Say things like:

"Ultron" → wake him up

"set a timer for 5 minutes" → timer + alarm

"what time is it" → current time

"what is the date" → current date

"what day is it" → current day

"search Python decorators" → web search

"Wikipedia Alan Turing" → Wikipedia search

"calculate 25 * 4" → calculator

"news" → choose top, sports, entertainment, or business headlines

"open YouTube" → open a site/application supported by Ultron

"roll a dice" → because apparently this was important

"pick a card" → trust Ultron at your own risk

"bye" → exit the conversation

Project notes

News headlines are requested from NewsAPI using country=in.

Email sending requires working SMTP credentials.

tune.mp3 should be available beside the Python file if you want the timer sound.

Keep secrets out of source control. A good pattern is:

.env          # real secrets, never commit
.env.example  # variable names/placeholders, safe to commit

Have fun. Just remember: Ultron is a Python script, not an actual world-ending superintelligence. Probably.