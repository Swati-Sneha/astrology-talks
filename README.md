## Get Your Horoscope

Make a horoscope generator. Use LLMs to generate a horoscope based on the current date, a user's name, and a user's zodiac sign.

1. With hardcoded user settings and date settings, query an LLM (probably OpenAI's ChatGPT) for a horoscope.
    - So, if all goes well, you should be able to get a response from the LLM like below:
      "Hi <Username>, what a beautiful day today to be a <Zodiac sign>! You'll have great luck today!"
2. Store user information (can be very minimal, doesn't need to contain password/login stuff, but you can do that if you want) in a database, so users can use only their username (and if you want, password) to get a new horoscope the next day, and of course, make sure that info is used.
3. Horoscopes are sometimes different than you want, so make sure you add a 'regenerate' button for those cases.
4. We're SAAS, so expose an API so that other services can use your amazing solution by just giving you all the information you think you need.
5. Now send a bunch of requests, see if your stuff breaks.
    1. If yes, why? How to solve it?
    2. If no, good job! How many queries can you handle per second? (if you did some kind of caching of the horoscopes, turn it off, and go to step 5. again)
6. Free form. If you've come this far, but haven't run out of time, we're proud of you! (To be fair, we already were, otherwise we wouldn't have challenged you with this assignment). Feel free to stop now and hand in the assignment, or just continue adding whatever you want on top.
    - Want to deploy it somewhere/somehow? Go ahead!
    - Want to add payment options so you can get rich? 🤑🤑🤑
    - Want to add multilanguage support? Yay!
    - Want to add multi-model support (e.g., have users (or admins) choose between `ChatGPT`, `GPT-4`, `Claude-v1`, or `Claude-v1-instant`)? Cool!
    - Want to add support for local LLMs or LLMs run through Huggingface 🤗 Transformers? Amazing!
    - Something else?! Also equally epic.
# AstrologyTalks
# AstrologyTalks
