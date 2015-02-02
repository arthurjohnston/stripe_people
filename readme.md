# How Stripe Employees describe themselves


Over the weekend I was looking into using Stripe for a project. While reading their documentation I clicked on their [about page](https://stripe.com/about). On it they seem to have pictures of (I believe) all of their employees. Scrolling over each of these pictures a short bio pops up. Viewing the source, you can see that the bios all look like this: 

```
<span class="bio" style="top: -121px; left: -60px;">
                    <span class="inner">
                        <em>Patrick Collison</em>
                              Before Stripe, Patrick co-founded Auctomatic and wrote Encyclopedia. He
      studied math at MIT.

                    </span>
                    <span class="arrow"></span>
                </span>
```

After looking at a few of these I wondered if there were any common themes. Since I needed a 20 minute break from my **actual** project I decided to do some analysis. Since each of these mini biographies is in well formed html it was easy to use BeautifulSoup to pull out the raw text of each bio. After extracting the data and filtering out any stop words using NLTK I was curious to see what words were most common. The 25 lines to do this are all in main.py

## Results
Since there are 180 bios on the page I looked for words that appeared in at least 5% or 9 biographies (making the simplifying assumption that in a given bios no word appears twice)

* stripe appeared 114 times
* studied appeared 85 times
* worked appeared 57 times
* previously appeared 36 times
* joining appeared 29 times
* enjoys appeared 26 times
* university appeared 25 times
* grew appeared 24 times
* science appeared 22 times
* computer appeared 20 times
* time appeared 20 times
* works appeared 17 times
* team appeared 15 times
* prior appeared 15 times
* loves appeared 15 times
* harvard appeared 15 times
* new appeared 14 times
* support appeared 14 times
* stanford appeared 13 times
* school appeared 13 times
* also appeared 13 times
* engineering appeared 12 times
* mit appeared 11 times
* things appeared 11 times
* berkeley appeared 10 times
* originally appeared 10 times
* infrastructure appeared 10 times
* dan appeared 10 times
* d appeared 9 times (this is an artifact of how I cleaned up the text)
* lives appeared 9 times
* facebook appeared 9 times
* founded appeared 9 times
* google appeared 9 times
* likes appeared 9 times

Ignoring words that are obviously about their transition to Stripe ('stripe', 'previously', 'joining') the most obvious trend is everyone talking about their education. 'studied' is the most common word after 'stripe' beating out 'worked' by a comfortable margin, 'university' and 'science' also making it into the top 10. People also tend to mention their alma matter with Harvard, MIT, Stanford and Berkeley getting a combined 49 mentions.

Another interesting trend you can glean is it doesn't look like they have a lot of employees from any particular company. 'google' and 'facebook' are the only two companies that have at least 9 mentions. But they're both tied with 'founded'. As in the person was a founded/co-founded a company 

