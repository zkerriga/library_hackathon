# library_hackathon
📃🔎 Project for a hackathon from The Russian State Library (RSL).

### Task:
Our task was to process a dataset with **text strings** to extract specific **dates** or **time intervals** from them. The dataset can be found on the competition [page in the Kaggle](https://www.kaggle.com/c/retropress-temporal-markup/) system.

### Our solution:
Our team decided to process strings by gradual filtering.
The string was first cleared: *synonyms* were replaced, and *extra characters* were removed.
After that, we used the [natasha](https://github.com/natasha/natasha) module to replace all letter entries of numbers with numbers. We sent the result to our improved [dateparser](https://github.com/scrapinghub/dateparser) module.

### Team:
* [Daniil Eletskii](https://github.com/zkerriga)
* [Aleksandr Marakulin](https://github.com/pichkasik)
* [Safiulin Evgenii](https://github.com/mainseo4all)
