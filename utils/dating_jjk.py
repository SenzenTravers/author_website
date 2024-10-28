import random

class Character:
    def __init__(
            self,
            name,
            url,
            won_fight,
            friendship,
            love,
    ) -> None:
        self.name = name
        self.url = url
        self.won_fight = won_fight
        self.friendship = friendship
        self.love = love

class Rooster:
    akari = Character(
        "Nitta Akari",
        "https://jujutsu-kaisen.fandom.com/wiki/Akari_Nitta",
        [
            "Much to her surprise, Akari actually won the fight! She takes a moment to recover from the shock and does a little fist bump.",
            "To her utter and complete stupefaction, Akari won thanks to an unexpectedly efficient leg sweep and a convenient brick jutting out of the pavement. She later dedicates a shrine to the brick.",
            "Akari... won? Outraged fans start twitter storms and Discord downpours while Gege cackles madly in the background."
        ],
        [
            "Akari and {roommate} became BFF! Yaaay! :D",
            "Akari and {roommate} became friends, and they went and got fried yakisoba together!",
            "Akari and {roommate} became friends! To celebrate, they went racing in a modded car (and won!)"
        ],
        [
            "Much to her surprise, Akari and {roommate} became lovers! Not exatly what she had in mind, but eyh, when happiness knocks...",
            "Akari and {roommate} fell in love and eloped to Malaysia, where they lived happily ever after.",
            "Following a surprising and contrived set of circumstances, Akari and {roommate} got into the cutest whirlind romance. OTP <3"
         ]
    )
    aoi = Character(
        "Todo Aoi",
        "https://jujutsu-kaisen.fandom.com/wiki/Aoi_Todo",
        [
            "The fight was a though one but thanks to TAKADA-CHAN's precious (imaginary) help, Todo won!",
            "Not only did Todo win, but he also got to learn {roommate}'s type of people in the process!",
            "Much to no-one's surprise (probably), Todo won!"
        ],
        [
            "Much to everyone's confusion, Todo and {roommate} became best friends since kintergarden!",
            "It turned out that {roommate} was also a fan of Takada-chan! Faced with this, Todo had no choice (and neither did {roommate}): they are now best friends.",
            "Unexpectedly, this meeting was a meeting of the minds, of the heart, of the soul: Todo and {roommate} are now friends."
        ],
        [
            "Much to everyone's confusion, Todo and {roommate} became spouses promised to each other since infancy.",
            "Todo's charisma, assurance, mighty torso and penchant for nakedness — how could {roommate} resists? True love was born today.",
            "Todo's feverish rendition of Takada-chan's latest single stole {roommate}'s heart. They became fellow fans; friends; something more...",
            "It turned out that Todo was wrong: actually, {roommate} was his type of woman! People. Anyway, congrats!"
        ],
    )
    arata = Character(
        "Nitta Arata",
        "https://jujutsu-kaisen.fandom.com/wiki/Arata_Nitta",
        [
            "Arata won... What? Why are you looking at me like that? He did. Random choice-based apps never make a mistake.",
            "Arata WON, and he worked HARD for it."
        ],
        [
            "Arata became friends with {roommate}, because he's a good guy.",
            "Arata and {roommate} became friends. Whether this bodes well for Arata or not is a matter of oppinion, headcanons and reading comprehension."
        ],
        [
            "Arata and {roommate} fell in love. Kyoto schoo's other students are already staging an intervention."
            "Arata and {roommate} fell in love. Whether this bodes well for Arata or not is a matter of oppinion, headcanons and reading comprehension."            
        ]
    )
    atsuya = Character(
        "Atsuya Kusakabe",
        "https://jujutsu-kaisen.fandom.com/wiki/Atsuya_Kusakabe",
        [
            "Kusakabe won! And he deserved it, too!",
            "Kusakabe won with the power of: an extreme will to live.",
            "Kusakabe won! He plans to celebrate his victory by resolving to only fighting opponents weaker than him from now on. Which was also his previous resolution but well, life."
        ],
        [
            "{roommate} and Kusakabe are now friends! And not just because Kusakabe thought {roommate} could help him out in case of trouble!",
            "Kusakabe and {roommate} are now friends. Yay! Friendship!"
        ],
        [
            "Kusakabe and {roommate} fell in love, much to a certain number of people's confusion.",
            "Because we get the love we need, not that we deserve... Or is that the other way around? Huh... Anyway. So, Kusakabe and {roommate} are an item now."
        ]
    )
    charles = Character(
        "Charles Bernard",
        "https://jujutsu-kaisen.fandom.com/wiki/Charles_Bernard"
        [
            "Charles Bernard won, somehow!",
            "Charles Bernard won! Why not? Do you have a thing against mangaka?"
        ],
        [
            "Following a few off-hand comments, {roommate} and Charles discovered they had the same favourite mangakas! {roommate} never had a choice from now on. They were friends whether they wanted to or not.",
            "{roommate} and Charles became friends! {roommate} read all of Charles' favourite author to make him happy. Aw."
        ],
        [
            "It turns out that {roommate} has a thing for tormented artists.It turns out that Charles is one. It turns out that... huh... Congratulations to the happy couple?",
            "Charles and {roommate} fell in love together! Charles drew them a whole manga with their self-inserts as the main couple. It was very sweet (?)."
        ]
    )
    choso = Character(
        "Choso",
        [],
        [],
        []
    )
    dagon = Character(
        "Dagon",
        [],
        [],
        []
    )
    takaba = Character(
        "Takaba Fumihiko",
        [],
        [],
        []
    )
    # joke pair
    johnson = Character(
        "Garry K. Johnson",
        [
            "Gary K. Johnson won because AAAAAAAMEEEEEERICAAAAA (you wanted this.)",
            "Gary K. Johnson won in exchange for promising an unreasonnable amount of exclusive Netflix-related spoilers.",
            "Gary K. Johnson won! How could he not win? Do you not trust a man with this face and this name?!"
        ],
        [
            "Highly impressed with Gary K. Johnson's dashing facial hair, {roommate} shyly asked for a bond of friendship which was granted. Congrats!"
        ],
        [
            "Seduced by Gary K. Johnson's piercing single-eyed stare and mighty sharp-angled jaw, {roommate} couldn't do anything but to launch into an elaborate courtship which ended in success. Congrats!"
        ]
    )
    daido = Character(
        "Daido Hagane",
        [
            "KATANAAAAAAAAAAAAAAAAAA (Daido won!)",
            "Daido WON! Thanks to the POWER of the KATANA, the SOUL OF THE JAPANESE MAN and also ANY PERSON WHO WANTS TO, APPARENTLY.",
            "Daido WON! He celebrated by leaving to cut down more stuff with his KATANA!"
        ],
        [
            "KATANAAAAAAAAAAAAAAAAAA (Daido and {roommate} became friends!)",
            "Daido and {roommate} are now besties! They still fought, though, because there's no sense into letting a perfectly fine katana-bound fight go to waste.",
            "Daido and {roommate} are now friends! {roommate} has started dreaming about katanas at night..."
            ],
        [
            "KATANAAAAAAAAAAAAAAAAAA (Daido and {roommate} became lovers!)",
            "After a whirlwind and steel-bound romance, Daido and {roommate} are now spouses! But what's a katana wedding? Does it even exists?",
            "{roommate} are now lovers. Together, they're collecting katanas <3 and using katanas <3 and seeing a councelor about katana addiction <3"
            
        ]
    )
    kashimo = Character(
        "Kashimo Hajime",
        [
            "Kashimo WON! Although he used his technique and perished soon afterwards. Well, at least he died doing what he loved.",
            "Kashimo won, showered in applause by Hakari and a cautious Panda. He vividly asserted his lack of need for any social support before running off to his next victoiry (but slow enough that Hakari could follow while carrying Panda.)",
            "Following a fight involving gratuitous property damage and a lot of physics, Kashimo won."
        ],
        [],
        []
    )
    hana = Character(
        "Kurusu Hana",
        [],
        [],
        []
    )
    hanami = Character(
        "Hanami",
        [
            "Hanami-kun won, which gave her the courage to ask Jogo-kun for a date. They lived ever happily after, even though this had turned into the high school AU somewhere along the way.",
            "Hanami won, much to the delight of real ecology enthusiasts still alive in the vicinity.",
            "Hanami won. Surprisingly, they were then scouted by mysterious people calling themselves the \"Dragons of the Earth\", switched mangas and were soon killed off anyway as CLAMP isn't any kinder than Gege Akutami." 
        ],
        [],
        []
    )
    higuruma = Character(
        "Higuruma Hiromi",
        [
            "Higuruma won, tiredly."
        ],
        [],
        []
    )
    jogo = Character(
        "Jogo",
        "https://jujutsu-kaisen.fandom.com/wiki/Jogo"
        [
            "Jogo won! Congrats, Jogo! You did your best!",
            "Jogo won. Why not? GEGE SAID HE'S ACTUALLY VERY STRONG, YOU KNOW",
            "Jogo-kun won, which was an encouragement to declare his love to Hanami-chan. They lived ever happily after, even though this had turned into the high school AU somewhere along the way."
        ],
        [
            "Jogo and {roommate} became best friends! Jogo's wholesome influence actually helped {roommate} become a better person, probably.",
            "Jogo and {roommate} became friends! Even contradictory opinions and genocide can't prevail over THE POWER OF FRIENDSHIP when you have respect and healthy communication on your side!",
            "Jogo and {roommate} became great friends! How sweet!"
        ],
        [
            "Jogo and {roommate} fell in love. Let's be real, though: {roommate} is the lucky one.",
            "Jogo and {roommate} fell madly in love and left the plot to become farmer in Okinawa! Well, why not?",
        ]
    )
    junpei = Character(
        "Yoshino Junpei",
        [],
        [],
        []
    )
    miwa = Character(
        "Miwa Kasumi",
        [],
        [],
        []
    )
    kenjaku = Character(
        "Kenjaku",
        [
            "Kenjaku won, gloatingly (this is my toy and I can make up words if I want to.)",
            "Kenjaku lost!... But this was actually all part of his plan from the start so, actually, he won.",
            "Kenjaku won, and then beat {roommate} at mahjong and at a pun competition to further drive the point home."
        ],
        [],
        []
    )
    nanami = Character(
        "Nanami Kento",
        [
            "Nanami won, tiredly.",
            "Nanami won. He looked distinctly unimpressed by the fact.",
            "Nanami won and then retired to Malaysia, and all was well. This is canon now"
        ],
        [],
        []
    )
    hakari = Character(
        "Hakari Kinji",
        [],
        [],
        []
    )
    kirara = Character(
        "Hoshi Kirara",
        [],
        [],
        []
    )
    ijichi = Character(
        "Ijichi Kiyotaka",
        [],
        [],
        []
    )
    muta = Character(
        "Kokichi Muta",
        [],
        [],
        []
    )
    kurourushi = Character(
        "Kurourushi",
        [],
        [],
        []
    )
    mahito = Character(
        "Mahito",
        [],
        [],
        []
    )
    mai = Character(
        "Zen'in Mai",
        [],
        [],
        []
    )
    maki = Character(
        "Zen'in Maki",
        [],
        [],
        []
    )
    yaga = Character(
        "Yaga Masamichi",
        [],
        [],
        []
    )
    megumi = Character(
        "Fushiguro Megumi",
        [],
        [],
        []
    )
    meimei = Character(
        "Mei Mei",
        [],
        [],
        []
    )
    miguel = Character(
        "Miguel Oduol",
        "https://jujutsu-kaisen.fandom.com/wiki/Miguel_Oduol",
        [
            "Miguel WON! And he DESERVED IT, DAMNIT!",
            "Miguel finally picked an opponent outside of the \"strongest sorcerer(s) alive\" category and won! Congrats!"
        ],
        [
            "Miguel and {roommate} became best friends! Apparently, Miguel's a bit of a tsundere, who'd have known?",
            "Miguel and {roommate} became an unexpectedly cute pair of friends. Aaaw."
        ],
        [
            "Miguel and {roommate} fell in love! Does Miguel deserves his partner? Does {roommate} deserves him? That's another question.",
            "Miguel and {roommate} fell in love! How romantic."
        ]
    )
    momo = Character(
        "Nishimiya Momo",
        [],
        [],
        []
    )
    naoya = Character(
        "Zen'in Naoya",
        "https://jujutsu-kaisen.fandom.com/wiki/Naoya_Zenin",
        [
            "Naoya won, misogynistically.",
            "Well, Naoya won, and we're all disappointed.",
            "Naoya won. Good for him. What more does he wants? A medal?"
        ],
        [
            "Somehow, possibly after an incident involving one or both of them hitting their head and developping amnesia, Naoya and {roommate} became friends.",
            "Naoya and {roommate} became great friends! They've exchanged friendship bracelet and everything.",
            "Much to the dismay of {roommate}'s entourage, Naoya became {roommate}'s friend."
        ],
        [
            "Naoya and {roommate} fell in love! Ew.",
            "Apparently, {roommate} was the catalyst for Naoya to change for better! They became a very sweet, wholesome couple.",
            "Naoya and {roommate} eloped and ran off to Italy for a shotgun wedding. Why Italy? Well, why Naoya?"
        ]
    )
    nobara = Character(
        "Kugisaki Nobara",
        [],
        [],
        []
    )
    # if it's a fight, takada always wins
    takada = Character(
        "Takada Nobuko",
        [],
        [],
        []
    )
    kamo = Character(
        "Noritoshi Kamo (Junior)",
        [],
        [],
        []
    )
    panda = Character(
        "Panda",
        "https://jujutsu-kaisen.fandom.com/wiki/Panda",
        [
            "Panda won! It's a victory for all of non-pandakind.",
            "Panda won. Tremble, humanity!"
        ],
        [
            "Panda and {roommate} became friends, having a worrying (?) amount of things in common.",
            "Panda and {roommate} became friends, though it's suspected {roommate} only did it to be able to cuddle Panda."
        ],
        [
            "Panda and {roommate} fell in love. As it's technically not zoophilia, everyone's trying their best to be supportive.",
            "Panda and {roommate} are now an item, which is wildly unexpected but — huh — as long as everyone's involved are consenting ad... consenting... Well... It's the jujutsu world, okay? Things get weird sometimes."
        ]
    )
    reggie = Character(
        "Reggie Star",
        [],
        [],
        []
    )
    rika = Character(
        "Rika",
        [],
        [],
        []
    )
    amai = Character(
        "Amai Rin",
        "https://jujutsu-kaisen.fandom.com/wiki/Rin_Amai",
        [
            "Amai won. What? It's my app. If I say it happened, it happened, okay?",
            "Thanks to a series of contrivences that might have been rejected as \"too unlikely\" in a Tex Avery Cartoon, Amai WON! Congrats!"
        ],
        [
            "Amai and {roommate} became friends! It's the start of something beautiful. Or terribly unfortunate.",
            "Much to everyone's surprise, Amai and {roommate} instantly hit it off and are now the best of what's-the-gender-neutral-equivalent-of-bro."
        ],
        [
            "Amai and {roommate} are in love, bringing to Jujutsu Kaisen that touch of romance some complained that it lacked.",
            "{roommate} and Amai are now an item! Amai's ability may be to thank (?) for that: the way to someone's heart, etc., etc... In any case, isn't love beautiful?"
        ]
    )
    miyo = Character(
        "Miyo Rokujushi",
        "https://jujutsu-kaisen.fandom.com/wiki/Rokujushi_Miyo",
        [
            "SUMOOOOOOOOOOOO (Miyo won)",
            "\"SUMOOOOOOOOOOOOOOOOO\", Miyo screamed enthusiastically as he won thanks to the power of sumo.",
            "Miyo won thanks to sumo, and then forced {roommate} to do more sumo until he was satisfied."],
        [
            "SUMOOOOOOOOOOOO (Miyo became friends with {roommate})",
            "\"You know what? Sumo's kinda fun,\" {roommate} said, earning Miyo's undying friendship. Then there was no choice for {roommate} but to accept that they were besties.",
            "Somehow, {roommate}'s attempt to troll and/or appease and/or act friendly to Miyo turned into real appreciation for the sport. They've founded their own school and everything... Congrats?"
        ],
        [
            "SUMOOOOOOOOOOOO (Miyo became lovers with {roommate}!)",
            "Thanks to {roommate}, Miyo finally found someone he loved as much as sumo. Well, almost as much.",
            "Miyo and {roommate} became lovers and sumo partners for life. Their sumo school shall be remembered for centuries to come. Perhaps the next Gojo Satoru will be trapped into the Sumo Realm rather than the prison realm?"
        ]
    )
    ryu = Character(
        "Ishigori Ryu",
        [],
        [],
        []
    )
    gojo = Character(
        "Gojo Satoru",
        "https://jujutsu-kaisen.fandom.com/wiki/Satoru_Gojo",
        [
            "Gojo won! Obviously.",
            "Gojo won. Hordes of fen take note of the event and use it as proof for their pet theories.",
            "Gojo won, quite obviously, as he's never had difficulties winning anything except his students' respect."
        ],
        [
            "Gojo and {roommate} became friends! {roommate} may even have consented to this.",
            "Gojo and {roommate} are the best of friends! {roommate} even framed the penis drawing that Gojo offered them for their friendship birthday. How sweet.",
            "Gojo and {roommate} became friends! Aaaw."
        ],
        [
            "Gojo and {roommate} became lovers! Sorry, {roommate}.",
            "These eyes, these lips, that face, these hands, these shoulders, this – well, in short, {roommate} can be forgiven for getting into a whirlwind romance with Gojo.",
            "{roommate} being a person of taste, they started a ferocious courtship which actually ended in success! Congrats(?)!"
        ]
    )
    shoko = Character(
        "Shoko Ieiri",
        "https://jujutsu-kaisen.fandom.com/wiki/Shoko_Ieiri",
        [
            "Shoko won out of the sheer power of her coolness.",
            "Shoko won! In a drinking competition."
        ],
        [
            "Shoko and {roommate} became friends! Aaaw.",
            "Shoko and {roommate} became besties, became Shoko deserves best friends as much as Gojo and Geto! Whether {roommate} deserves the honour is another, trickier question."
        ],
        [
            "Shoko and {roommate} became lovers. We can understand {roommate}.",
            "Even though {roommate} doesn't deserve Shoko, they fell in love together! Congrats, I guess.",
        ]
    )
    geto = Character(
        #TODO
        "Suguru Geto",
        [],
        [],
        [
        ]
    )
    sukuna = Character(
        "Sukuna",
        "https://jujutsu-kaisen.fandom.com/wiki/Sukuna",
        [
            "Sukuna won! Obviously.",
            "Sukuna won, quite obviously, as he's never had difficulties winning anything except a reprieve from Yorozu's attention.",
        ],
        [
            "Sukuna and {roommate} became friends after {roommate} revealed an unexpected skill for haikus.",
            "{roommate} and Sukuna just hit it off and became the best of friends? Unexpected, but {roommate} will take it.",
            "What can we say? Sukuna and {roommate} were clearly born to be besties. Congrats!"
        ],
        [
            "Sukuna and {roommate} eloped together, much to everyone's extreme surprise. This solved the entire course of JJK and offended Kenjaku to the nth degree. Fen claim this end is the best one, as it wasn't written by Gege.",
            "Sukuna fell in love with {roommate} and launched into a very sweet courtship. Poems were delivered. Flowers were arranged. How could {roommate} resist?",
            "Sukuna and {roommate} fell in love! They exchange haiku"
        ]
    )
    ino = Character(
        "Ino Takuma",
        "https://jujutsu-kaisen.fandom.com/wiki/Takuma_Ino",
        [
            "Ino won! Good for him!",
            "Ino won, displaying the full advertised might of his shikigami! How impressive, Ino!"
        ],
        [
            "Ino and {roommate} became great friends! Aaaw.",
            "Apparently, {roommate} reminds Ino of Nanami (?!?). Anyway, they became friends."
        ],
        [
            "Ino and {roommate} fell in love! Ino does little shows for {roommate} with his shikigami; it's all very sweet.",
            "Ino and {roommate} became lovers! Aaaw."
        ]
    )
    tengen = Character(
        "Tengen",
        "https://jujutsu-kaisen.fandom.com/wiki/Tengen",
        [
            "Tengen won! And then went off to play pachinko or any such old person hobby.",
            "Tegen won. Take that, ageists!"
        ],
        [
            "Tengen and {roommate} became friends. It turns out that all-seeing immortals are a treasure trove of gossips.",
            "{roommate} and Tengen became friends! Secretly, {roommate} had always wanted a friendly grandmaish presence in their life."
        ],
        [
            "Tengen and {roommate} became lover, which is probably illegal in some countries.",
            "Tengen and {roommate} fell in love. Take that, age gap haters!"
        ]
    )
    toge = Character(
        "Inumaki Toge",
        "https://jujutsu-kaisen.fandom.com/wiki/Toge_Inumaki",
        [
            "Mentaiko.",
            "Salmon chicken wasabi.",
            "Cucumber."
         ],
        [
            "Tuna mayo.",
            "Tuna mayo kelp sate.",
            "Octopus cheese."
        ],
        [
            "Apple pie. :3",
            "Peach salmon roe.",
            "Tuna mayo mochi."
        ]
    )
    toji = Character(
        "Fushiguro Toji",
        "https://jujutsu-kaisen.fandom.com/wiki/Toji_Fushiguro"
        [
            "Toji won, very sexily.",
            "Toji won thanks to the power of his sexy, sexy muscles and sexy, sexy physical abilities. Stupid sexy Toji."
            "Toji won at fighting, but not at life ):"
        ],
        [
            "Toji and {roommate} became friends! Toji didn't even sold them out when he got the chance to! How moving.",
            "It turns out that {roommate} has a knack for making remarks that inspire Toji to bet on the right horses, so! They're best friends now, much to {roommate}'s surprise."
        ],
        [
            "{roommate} is the latest lucky person to get to support Toji! Congrats <3",
            "Having realized that {roommate} could provide him with generous funds, Toji promptly endeavoured to seduce him and succeeded! Yay, romance!",
        ]
    )
    uiui = Character(
        "Ui Ui",
        "https://jujutsu-kaisen.fandom.com/wiki/Ui_Ui"
        ""
        [
            "Ui Ui won, incestuously.",
            "Ui Ui won! Duh."
        ],
        [
            "Ui Ui and {roommate} became friends, which was very unexpectedly wholesome.",
            "Ui Ui and {roommate} became the best of friends after {roommate} made a positive comment about Mei Mei."
        ],
        [
            "Ui Ui and {roommate} became... lovers? Is that legal? That's probably illegal.",
            "Ui Ui and {roommate} became an item. Mei Mei negociated a dowry in exchange for her supports for the relationship.",
            "Much to everyone's dismay except Mei Mei's, Ui Ui and {roommate} fell in love."
        ]
    )
    uraume = Character(
        "Uraume",
        "https://jujutsu-kaisen.fandom.com/wiki/Uraume"
        [
            "Uraume won, and looked very pretty doing it.",
            "Uraume won. They celebrated with a feast for Sukuna.",
            "Uraume won, snobbily."
        ],
        [
            "Uraume and {roommate} became a very unexpectedly cute pair of friends. They've exchanged friendship bracelets and everything.",
            "Uraume and {roommate} became besties! They're having cook-off at each other's house and everything. Sukuna tolerates {roommate} because he gets to judge the cook-off."
        ],
        [
            "Uraume... fell in love with {roommate}? Sukuna got so upset that he accidentally helped an old lady cross the street the other day.",
            "Uraume and {roommate} eloped after a steamy courtship. Sukuna's gone to sulk into the mountains ever since. Kenjaku is very upset."
        ]
    )
    iori = Character(
        "Utahime Iori",
        "https://jujutsu-kaisen.fandom.com/wiki/Utahime_Iori",
        [
            "Utahime won! She deserved it for putting up with Gojo for so long.",
            "Supported by her very determined students and colleagues, beloved Utahime-sensei won! It's her victory and we'll all attest to it.",
            "Utahime won! At karaoke."
        ],
        [
            "Following an unexpected but exhilarating meeting at a baseball game that their favourite team won, Utahime and {roommate} became friends!",
            "Following an beer-fuelled evening where alcohol and karaoke united hearts, Utahime and {roommate} became friends."
        ],
        [
            "Entranced by Utahime's voice, {roommate} fell madly in love and started a feverish courtship. Now they're an item! Congrats!",
            "{roommate} and Utahime fell in love! Rumour has it, she serenaded {roommate}."
        ]
    )
    yorozu = Character(
        "Yorozu",
        "https://jujutsu-kaisen.fandom.com/wiki/Yorozu",
        [
            "Yorozu WON, but what's the POINT if it's not against SUKUNA??? ARGH!!!!",
            "Yorozu won thanks to the power of violence and geometry!"
        ],
        [
            "Yorozu and {roommate} became friends! In an impressive display of genuine devotion, {roommate} even managed to remain awake through a live reading of Yorozu's Sukuna-themed scrapbook.",
            "Yorozu and {roommate} became friends! The main focus of their conversation is love talk. So, so much love talk."
        ],
        [
            "Yorozu and {roommate} fell in love! It was intense, it was passionnate, and it was very unexpected.",
            "Yorozu and {roommate} fell in love! Apparently, {roommate} \"looked lonely\". Now, they won't ever be! Romance! :D",
        ]
    )
    gakuganji = Character(
        "Gakuganji Yoshinobu",
        "https://jujutsu-kaisen.fandom.com/wiki/Yoshinobu_Gakuganji",
        [
            "Gakuganji won with the power of music and intimidating eyebrows!",
            "Gakuganji won! Up yours, ageism!"
        ],
        [
            "Much to everyone's great surprise, Gakuganji and {roommate} ended up the best of friends! {roommate} even became his band's new drummer.",
            "It turned out that {roommate} actually love Jimi Hendrix! Gakuganji as well! The power of fandom prevailed! They're now best friends!"
        ],
        [
            "Gakuganji's surprisingly moving rendition of Starway to Heaven was the start of a very, very unexpected romance. Congrats?",
            "Unexpectedly, {roommate} had a thing for musicians. Very unexpectedly, Gakuganji ended up on the end of that thing."
        ]
    )
    haibara = Character(
        "Haibara Yu",
        'https://jujutsu-kaisen.fandom.com/wiki/Yu_Haibara',
        ["Haibara won!... We wish.", "Haibara won! :D:D:D He gets a pat from his sempais."],
        [
            "Haibara and {roommate} became besties!! :D :D",
            "Haibara's puppy aura won out: {roommate} had to grant him friendship."
        ],
        [
            "Haibara and {roommate} are now going out! Is that legal? Is that moral? Does {roommate} deserve Haibara's endless reserves of cinnamon rollness? Probably not! But them's the break.",
            "Looking deep into Haibara's pure eyes, {roommate} underwent a complete change of character and is now his tender, devoted spouse. Congrats!"
        ]
    )
    yuuji = Character(
        "Itadori Yuuji",
        "https://jujutsu-kaisen.fandom.com/wiki/Yuji_Itadori",
        [
            "Yuuji won with the power of cinnamon rollness and heavy violence! Congrats!",
            "Yuuji won thanks to the power of genetics, Sukuna's seeping influence, cheating, and HARD WORK, mister Your Honor, so we'll grant him full merit for that victory.",
            "Yuuji won! Congrats, Yuuji! <3"
        ],
        [
            "Yuuji and {roommate} are now friends. Congrats to {roommate}!",
            "Yuuji and {roommate} are now friends. Obviously. It's Yuuji.",
            "Yuuji and {roommate} are now friends, because Yuuji deserves all the friends in the world."
        ],
        [
            "As {roommate} is a person of taste, at least in some regards, they fell in love with Yuuji and seduced him with an impressive (if slightly worrying) series of grant gestures.",
            "{roommate} and Yuuji fell in love! Was it legal? Moral? Does {roommate} deserves Yuuji? Does Yuuji care? The answer to at least two of these questions is \"no\", but that's life and Jujutsu Kaisen for you!",
            "As the way to a person's heart is their stomach or, occasionnaly, them receiving a well-deserved pummelling, Yuuji used one of these two ways to accidentally seduce {roommate}. They're now the sweetest couple, I swear. Congrats!"
        ]
    )
    yuki = Character(
        "Tsukumo Yuki",
        "https://jujutsu-kaisen.fandom.com/wiki/Yuki_Tsukumo",
        [
            "Yuki WON! Yes she did.",
            "Yuki won thanks to her mighty cursed energy and sexy, sexy abs."
        ],
        [
            "Yuki sufficiently approves of {roommate}'s choice in significant others to grant them her friendship. How generous of her!",
            "Yuki actually became besties with {roommate}. Friendship always wins!"
        ],
        [
            "Yuki's cool muscles, her cool sense of fashion, her cool motorcycle and her cool shikigami... {roommate} never had a chance. They had no choice but to fall in love.",
            "Following a very unexpected meet (or re-meet) cute followed by a number of unexpected events, Yuki and {roommate} are now lovers.",
            "Yuki and {roommate} are now married. And off to a motorcycle honeymoon. How? Why? Because they can."
        ]
    )
    yuuta = Character(
        "Okkotsu Yuuta",
        "https://jujutsu-kaisen.fandom.com/wiki/Yuta_Okkotsu"
        [
            "{roommate} and Yuuta fought... and Yuuta won! He almost didn't eat anyone in the process, too!",
            "Yuuta won via violence and a few well-invested kisses.",
            "Yuuta won, and Maki is very proud of him."
        ],
        [
            "Yuuta and {roommate} are now friends!",
            "Somehow, Yuuta and {roommate} hit it off and began a very sweet friendship.",
            "{roommate} and Yuuta are now friends for life! And possibly beyond <3"
        ],
        [
            "{roommate} and Yuuta fell in love! Apparently, Yuuta's a great kisser.",
            "Yuuta and {roommate} became lovers! Their main challenge as a couple is to keep Rika down in certain moments.",
            "Who'd resist these puppy eyes? And that killer gaze? Yuuta and {roommate} are now an item! "
        ]
    )
    

    class Pairing:
        def __init__(self, roommates) -> None:
            self.roommates = roommates
            self.winner = random.choice(self.roommates)

        #property to calculate possible outcomes depending on winner (select winner, and then select their outcome)
        def pick_result(self):
            roommates_names = [char.name for char in self.roommates]
            #HERE, LINK TO RETURN OUTCOMES AS CHAR A + CHAR B outcome = 

            if "Todo Aoi" in roommates_names and "Itadori Yuuji" in roommates_names:
                outcome = [
                    "Todo and Yuuji fought and Todo won! Because Yuuji tried to flee at every turn.",
                    "Todo and Yuuji fought for fun! Yuuji won. Todo is overjoyed and overbruised.",
                    "Todo and Yuuji became fr... Wait, Todo and Yuuji always WERE friends. Best friends. Since high school.",
                    "Todo and Yuuji were born friends and remained friends.",
                    "Todo and Yuuji became lovers?! Nobara and Megumi are staging an intervention.",
                    "For some godforsaken reason, Todo and Yuuji returned married. Everyone is frantically trying to investigate while preventing Nobara from murder and Megumi from severe depression."
                ]

            if "Yorozu" in roommates_names and "Sukuna" in roommates_names:
                # TODO: Seuls les outcomes de Yorozu changent 
                outcomes = [
                    "Yorozu won! Alright, so Sukuna was distracted by a cloud that looked like Gojo, but STILL! A win's a win and a marriage's a (postmortem) marriage!",
                    "Yorozu won thanks to the power of love, geometry and Sukuna yawning at an unfortunate time for him",
                    "Yorozu and Sukuna have become friends... AS IF! Friends with benefits at the very least!!",
                    "Yorozu and Sukuna got married after Sukuna died from a ruptured aneurysm, which Yorozu still counted as a win! Congrats!",
                    "Yorozu and Sukuna eloped and got married! It was a beautiful ceremony, though Yorozu was dismayed to realize that Japan's ageing population meant that there were no (young) handsome men to be found in villages."
                ]

            if "Uraume" in roommates_names and "Sukuna" in roommates_names:
                # TODO: Seuls les outcomes de Uraume changent 
                outcomes = [
                    "Uraume won... AS IF. Uraume lost, as is proper from someone in their station.",
                    "Uraume won! The right to massage Sukuna's feet. Congrats!",
                    "Uraume and Sukuna became friends... AS IF. Uraume and Sukuna remained master and servant, as is proper."
                    "Uraume and Sukuna fell in love! In another life, another time.",
                    "Uraume and Sukuna eloped and got married in Malaysia, much to everyone's surprise except Sukuna and including Uraume."
                ]
            if "Uraume" in roommates_names and "Hikari Kinji" in roommates_names:
                #TODO : seuls les outcomes hostiles de Uraume changent
                won_fight = [
                    "Uraume won! And was left with severe gambling addiction.",
                    "Uraume won at pachinko but lost at life ):"
                ]
            if "Ui Ui" in roommates_names and "Mei Mei" in roommates_names:
                won_fight = [
                    "Ui Ui won... AS IF. Of course, Mei Mei won and Ui Ui wouldn't allow anything else.",
                    "Mei Mei won, if only because Ui Ui was too busy squeeing to hit her back.",
                    "Mei Mei won. Legend as it that the real challenge she's trying to take on is to lose against her brother, but so far she's failed and he won't have it any other way."
                ]
                friendship = ["Mei Mei and Ui Ui are friends! Or rather, siblings. Or rather, accomplices."]
                love = [
                    "Ui Ui and Mei Mei are lovers! Oh no.",
                    "Ui Ui and Mei Mei got married for fiscal reasons."
                ]
            if "Gojo Satoru" in roommates_names and "Geto Suguru" in roommates_names:
                #TODO: seuls les outcomes friendship des deux changent
                friendship = [
                    "Geto et Gojo sont devenus am... Hum. Voilà qui est embarassant.",
                    "Geto et Gojo sont amis et l'ont toujours été et c'est le problème."
                ]
