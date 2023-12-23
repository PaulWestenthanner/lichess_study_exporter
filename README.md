# Lichess Study Exporter
Export the mistakes you made in lichess studies into a training database.
The training database can be uploaded to chessable and is meant to be used in a Woodpecker method fashion.

# Run locally

In order to run a PyScript app locally, it does not suffice to open the html in a browser but you need to start a local web server:
`python3 -m http.server`



# My PyScript Experience
*This should be a blog post once I decide to create a blog*

When a FM friend of mine told me about his problem of curating tactics training exercises from his own studies, 
I thought I'll give PyScript a shot.  
When PyScript came out in 2022 it was very much hyped on Hacker News and everyone was like 
"now you can run Python in your browser and you will never have to learn Java Script".
Since I recently did some web development anyway I got curious.


## The nice things
It works! There is some reasonable documentation that allowed me to create the app in a few hours.
Both Firefox and Chrome executed the PyScript code as intended.
But that's about it with the nice things.

## The not so nice things
- The whole document logic looks like Java Script anyway, so you might just learn it. Knowing Python does not mean you know PyScript automatically
- Some packages just don't work. For example the usual `requests` library won't work in PyScript as it only supports some asyncronous alternatives.
  This is unfamiliar for most Python developers
- Load time: This is basically a deal breaker. When starting the app, it takes over three seconds. Even worse during these 3 seconds the users sees 
  what's going on (installing packages). This will confuse most users. A no-go for me in any consumer facing application.

## Conclusion
I don't think I'll give PyScript another shot. Learning the framework is similar to learning Java Script with fewer tutorials, documentation and resources.
Also the apps you can build with Java Script are more mature and don't need a way-too-long time to start.
