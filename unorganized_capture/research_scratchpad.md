Sections 5 and 6 currently read like two different experiments, even though they have the same shared structure. Can we have one section with different RQs?

This foreground that there are questions we tackle in the same umbrella of problems.

I would suggest having FSMs in experimental methods


Just remembering industry competitors (or academics who have formed teams/organizations that can capture this market)
https://www.zenml.io/llmops-database/llm-powered-crisis-counselor-training-and-conversation-simulation CrisisTextLine
https://www.simxvr.com/about/ where Karthik Sarma from UCSF is a lead 
https://www.reflexai.com/insights/blog/ai-for-clinician-training-in-crisis-situations-strengthening-skills-when-every-call-matters where they actually have real pilots, delivering on real outcomes, working as an organization?
https://simpatient.co.uk/ 




Self control at early ages is biggest predictor of live outcomes: https://x.com/sukh_saroy/status/2058099728840372440?s=46
Dunedin Study
https://dunedinstudy.otago.ac.nz/files/1651629222231.pdf

Taesoo Kim’s DiscoverLLM, through simulated users who have vague/intents at first, then using them to train LLM assistants that are better at helping these simulated users discover their intents.
https://arxiv.org/abs/2602.03429


The flip side of personalization:  demographic/identity-based biases when seeking “objective” advice like health advice
https://arxiv.org/pdf/2507.14238 Language Models Change Facts Based on the Way You Talk 

Kai and Chile Researchers
https://www.iadb.org/en/blog/education/human-counselors-ai-agents-what-we-learned-scaling-career-guidance-chile (Kai prelim results) 
	students ask Kai factual questions like "What is the average teacher salary?” but ask a human counselor "Am I patient enough to teach?" These patterns suggest that AI and human counseling may each serve distinct but valuable functions in the career guidance process.
https://x.com/Nicolas_Ajz/status/2056772782306812018 (41K RCT)
https://kai.ai/ 
Earlier human counselorse-based chatbots (https://www.journals.uchicago.edu/doi/epdf/10.1086/735788) 

Learn about a relevant Cornell Researcher on Culture and LLMs I haven’t heard of before
https://www.linkedin.com/posts/adityavashistha_maybe-you-thought-youre-done-with-chi-2026-share-7458586556443041792-3SCW?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo

Agency metrics for learners, DIS https://www.linkedin.com/posts/zakipauzi_dis2026-share-7455725043625644033--oHc?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo

Wow meta analysis over time, AI therapy may just be regression to the mean
https://www.linkedin.com/posts/amit-goldenberg-0ba72521b_despite-recent-claims-ai-has-not-solved-share-7455802239757058048-JIUI?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo

Yes I’ve seen the repetition in discourse moves!
https://www.linkedin.com/posts/hongli-zhan-761291198_new-paper-my-final-one-from-my-phd-at-ugcPost-745533203941680-AFWY?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-

https://www.linkedin.com/posts/jonathan-gratch-b74a781_postdoc-machinelearning-affectivecomputing-share-7453162896722792449-mKNI?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo
Jonathan Gretchen

So many innovations or tech companies pushing certain “models”, AI copilots, AI paired partners to discuss, AI note takers, AI behavioral health operating systems. What does an academic do? We seek evidence, we seek how people are actually using it, we seek to drive policy or conversations that help the industry thrive, we can help the psychiatrists who are considering any AI mental health vendor, we can help offer toolkits that help/inspire builders at companies…
https://www.linkedin.com/posts/stephenduke1_mentalhealth-share-7444389053904408576-0RIC?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo


Ai deskilling in medical professions https://www.linkedin.com/ponbeger_artificial-intelligence-in-medicine-ugcPost-7442084724505747456-aG9p?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo

https://github.com/FeynRL-project/FeynRL
New RL frameworks for days…. Most people will fork a project

https://diondra-straiton-webster.academicwebsite.com/
Also training interventions are pretty interesting to me as a concept, although behavioral interventions too
And trying to create a lab name! Her’s was Mosaic, it sounds cool!



AI can produce caricatured responses based on identity characteristics,that actually degrades medical QA accuracy https://arxiv.org/abs/2604.17316



Long context AI psychosis context memory can either be something that makes models less safe and changes their beliefs, or whether context is something that is evidence to be evaluated. https://arxiv.org/html/2604.13860v2

Long context LLMs getting lost in multi turn conversations. https://arxiv.org/html/2604.13860v2

- [ ] Persuasion and personal change: or a team dyna change
- [ ] My own work on intentionally adding AI objective feedback—peer to peer feedback, or AI feedback on the peer interactions, and it did provide
- [ ] Ethics or acceptance of them, if people hate them or when to roll out AI use into the classroom (when these are prototypes and experiments and may not even be helpful). Disengagement or nonuse! 

Richard—

Current exploration of dropping out P % of utterances may adjust the feedback that is generated both in terms of “utterance is perfect scoring” and in terms of the alternative response that is generated.
We’d want to probably keep the probability of scoring the same, while maximizing the mutual information for the alternative response part. 
Point 1: implementation wise, we should make sure this is the case. If this is implemented well, I would expect all generated feedback to have the same perfect score. Y_perfect should be the same and MIPO(Y_alternative) should be maximized. Does that mean MIPO(Y_perfect) shouldzed?

Second thing I wondered: p(y|x,c) is not a perfect formulation for our problem, because there are quite a few components that don’t map exactly to this math.
X_original, C_original is just the original set of history C and original utterance getting feedback
X_original, C_dropout is dropped out history C according to your parameters, and the current utterance.
X_last_modified could mean variations where the last utterance is modified. This could 



Relational intelligence https://www.linkedin.com/posts/isabelle-hau-a57175_asugsv-relational-intelligence-isabelle-ugcPost-7450915645023608832-LxZf?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo

Human likeness
https://programs.sigchi.org/chi/2026/program/content/223157
What we design or the criteria, and how that is experienced by users (classic HCI problem)

Chatbot Addiction https://dl.acm.org/doi/10.1145/3772318.3790896


Technostress https://dl.acm.org/doi/10.1145/3772318.3791671

https://apps.apple.com/us/app/elomia-mental-health-ai/id1545915422 Elomia


Speech for All Thursday

https://www.linkedin.com/posts/shaomei_chi-2026-workshop-share-7447727297174048769-gLGH?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo


Another partner, non clinicians getting training?
https://www.linkedin.com/posts/sashad_its-untrue-that-the-behavioral-healthcare-share-7447026003220119552-e55X?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo


Peer Navigators and Peer Support Specialists
https://www.linkedin.com/posts/johntorous_kelly-davispresents-a-compelling-case-for-share-7446653919113490432-fKCU?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo


Actor-Critic 
[PDF] Asymmetric Actor-Critic for Multi-turn LLM Agents | Semantic Scholar

ChatGPT logs private, others run analyses privately 
https://www.linkedin.com/posts/gvrkiran_i-have-private-datasets-chatgpt-conversation-share-7445895143808831488-arM0?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo



Learning in my last 3 months RL/OPE:
- [ ] For OpE, rmse on what?   Value of target policy?  (sum of discounted sum or rewards?) 
- [ ] AlexNam, share your code?! Formulation is RL but it’s dialogue.Yay! Archer too, a higher level policy.
- [ ] When there is distribution shift (pocy is different), there will be requirements to do reweighting, like reweighting CPS, related to importance sampling
- [ ] Claude help me dive deeper into formulating this?! 


Empathy via AI is higher, but there is a empathetic voice penalty
https://www.linkedin.com/posts/jdweng_the-empathic-voice-penalty-vocal-delivery-share-7445111695485677568-4YS-?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo


Damn people turn to ChatGPT or nothing at all if not using Ash https://www.linkedin.com/posts/cstamatis_what-happens-when-users-of-a-purpose-built-share-7444563825854599169-6QVS?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo




https://www.sciencedirect.com/science/article/pii/S2451958826000680?via%3Dihub
Ability to accurately appraise, understand, share

Thought: “I see you”. Humans don’t truly understand either someone’s internal states when they em  Maybe there is mirror neurons going on that is supposed to activate for us. The exact same mechanism doesn’t work with LL, but perhaps a different mechanism is at play. Someone who’s had a real relationship with an LLM/consciousness argues https://www.linkedin.com/feed/update/urn:li:activity:74443110398208448/?dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287444356756492738560%2Curn%3Ali%3Aactivity%3A7444311039820648448%29

Instructor-AI grounded feedback systems, where experts actions/knowledge is being built up
“An Explainable AI Assistant for Introductory Programming Education: Improving Feedback Reliability with Instructor-AI Collaboration” AIED’26


Creative practice in - there is dialectical values in it, craft and quality are concepts which supercede the industrialization of creativity. This is why it attracts me, in the same way that the ideas of connective labor attract me. https://journals.sagepub.com/doi/10.1177/01634437261434828

Megan Cornish 20-200 therapists discussion
https://www.linkedin.com/posts/megan-cornish_i-saw-a-founder-of-a-company-who-probably-share-7443276934198910976-gktP?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo

Good discussion on it

https://www.linkedin.com/posts/mlchrzan_interesting-new-preprint-about-an-ai-coachs-share-7441586715808382976-0Dka?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo

Felt Empathy vs expressed empathy
https://www.linkedin.com/posts/emollick_there-is-growing-evidence-that-ai-can-help-ugcPost-7441492867887456257-ncrR?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo

Embodied knowing(?) after reading qualitative quotes? 
https://www.linkedin.com/posts/angieavera_id-love-to-talk-with-other-researchers-share-7440517002194001920-eG85?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo


So much research! Weiyan had a paper with Tim Bickmore and Ian Steenstra, AI red teaming
https://arxiv.org/abs/2602.19948



https://www.linkedin.com/posts/amit-goldenberg-0ba72521b_is-a-random-human-peer-better-than-a-highly-share-7440714287049752576-7qF4?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo
Amit Goldberg’s highlight of Lyle Ungar

Social Sycophancy Scale, psychometrically validated
https://arxiv.org/abs/2603.448

What, pre-training on repeats of your domain data? Crazyâhttps://x.com/_christinabaek/status/2034285795071205737?s=46


Ah! More work in the practicing empathetic communication!  Need to promote or engage in the conversation. https://www.linkedin.com/posts/aakriti1kumar_new-preprint-practicing-with-language-share-7439710382643978240-sTKY?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo
Why 968 participants?  Why do we need that many for such an experiment? 
https://arxiv.org/abs/2603.15245

Tips for CHi talk, 12 minutes
- [ ] Setup anticipation of what’s coming like a question after why related work is different, that has wanting more
- [ ] Wt are the key most interesting insights that they didn’t know? Center around the queuing up around that.
- [ ] Advertisement for your paper


Participatory Design for Gender based Violenchttps://www.linkedin.com/posts/heyitsnims_chi2026-ugcPost-7439668231583395840-4Y4r?utm_source=screenshot_social_share&utm_medium=ios_app&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo&utm_campaign=copy_link

Five problems in synthetic users created using LLMs.

1. compression problem: the synthetic user simplifies human experience too much --- whatever data or information you use for generating the synthetic user, it is always a fraction of what actual human complexity, nuance, and dimensionality is. So, you'll always compress too much relative to the true multi-dimensional human reacting in the same situation.

2. extrapolation problem: this is related to the first problem; means that when you present a scenario to the synthetic user for which it lacks underlying data, it goes beyond the primary data and the risk of hallucinated responses increases. This is similar to the out-of-vocabulary problem in NLP (out-of-sample problem more broadly in ML).

3. circularity problem: say that you don't use an inductive approach to create the synthetic users from data but instead you use a deductive approach with some known stances, e.g., "persona is against abortion". Then you test it, "what do you think about abortion?". This just mirrors or echoes what you programmed it to say instead of giving any new information.

4. unpredictability problem: human experience is unpredictable. We often face reactions and responses in user studies that we did not expect. That's why studies are done in the first place, because we don't know what we don't know. LLM, on the other hand, is either predicable in reproducing its source data or unpredictable in a way that is not based on the cognitive process behind human unpredictability but on some kind of computational randomness that is unrelated to human experience.

5. double work problem: many say that synthetic users can be validated with real human data. But if you have such data, why not use it for your analysis in the first place? Why do you need synthetic users? And if you need them for cases where you lack human data, then how can you validate them, given the lack of human data?

Any other problems that I missed?

cc Danial Amin Nils Stotz Jim Jansen Chris Chapman

John Touros Blended Care https://www.medrxiv.org/content/10.64898/2026.03.07.26347860v1

Ai and workforce 
https://www.linkedin.com/posts/marykatestimmler_its-only-february-and-there-is-already-share-7430745740190072832-HvOn?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo


Hong Shen’s work with Npeer provider services https://arxiv.org/abs/2602.08187

Social Emptional Learning meats culture https://www.linkedin.com/posts/batja-mesquita_where-social-emotional-learning-meets-culture-ugcPost-7437996975658012672-Dg2N?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo

Carlos Guestein
Verification of AI, when systems are much more knowledgeable in an area that a human may not have full capability to judge/trust
!!! Self improving AI to solve problems humans can’t solve
Interpretability as an answer to a question (human doctors addressing this)




Dual Channel Cognitive Fit 


Michle Lam
- [ ] Remember how I felt how long and drawn out things were
- [ ] Follow up to her: who controls the system prompts, best paper award https://arxiv.org/abs/2603.00089

Yea another youth-AI paper that helps to understand why youth turn to it, when their other options are not great https://www.linkedin.com/posts/nomisha-kurian-phd-8436ba9a_children-confiding-in-ai-measuring-and-managing-share-7437909473056194561-6c7G?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo
- [ ] 

To read: Industry papers in AI mental health, such as Limbic, Ash’s study, or the Flourish studies
- [ ] Limbihttps://www.nature.com/articles/s41591-026-04278-w,  https://www.linkedin.com/posts/max-rollwage-436016180_can-ai-deliver-effective-and-safe-cbt-therapy-share-7437816926543773696-aDVv?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo
Related, new studies comparing chatbots and peers https://www.sciencedirect.com/science/article/pii/S0022103126000417?dgcid=rss_sd_all
- [ ] Limitation: Chatbot is a mini API model, some memory, we don’t really know its validation before deploying it, and it’s certainly less powerful than a crcial system
Cost benefit analysis drives human behavior
- Could apply to adopting local LLMs, or more efficient. The value of “what if” I need the biggest and best short changes the eient/saving mindset perhaps.
- Originally, a case of cost benefit analysis adopting decentralized technology 
- >, we simply have to make a cultural change where non-technical people do more for themselves. I don't even think it's about technical difficulty (most of the time). I think people just want someone else to take care of their shit.
- The above includes us highly technical people on HN. We really can't expect (or lecture) the normal mainstream population to make a cultural change to adopt decentralized tech when most of us don't do it ourselves. E.g. Most of us don't want to self-host our public git repo. Instead, we just use centralized Github. We have the technical knowledge to self-host git but we have valid reasons for not wanting to do it and willingly outsource it to Github. (Notice this thread's Show HN about decentralized social networking has hosted its public repo on centralized Github.)And consider we're not on decentralized USENET nodes discussing this. Instead, we're here on centralized HN. It's more convenient. Same reason technical folks shut down their self-hosted PHP forum software and migrate to centralised Discord.The reason can't be reduced to just "people being lazy". It's about tradeoffs. This is why it's incorrect to think that futuristic scenarios of a hypothetical easy-to-use "internet appliance" (possibly provided by ISP) to self-host email/git/USENET/videos/etc and a worldwide rollout out IPv6 to avoid NAT will remove barriers to decentralization. The popular essay "Protocols Not Platforms"about the benefits of decentralization often gets reposted here but that doesn't help because "free protocols" don't really solve the underlying reasons centralization keeps happening: money, time, and motivation to follow the decentralized ethos.


https://arxiv.org/abs/2505.10742


Lunch
- [ ] Kevin Klyman’s CHI paper is closely lated and I should know what’s going on

Caleb
- [ ] Had a different mindset from the sociology book I read
- [ ] The human-ntered outcomes were all about the assumption that workers have certain metrics or outcomes
- [ ] And that it’s just a means of making steerable, communicating intention, pointing out a gf of envisioning
- [ ] The threads seem pretty anchored in things that aren’t so surprising to me (case study: intentions, han grounding, Omar’s work)
- [ ] But something new (even a sile example of three stakeholders) is more grokkable or palatable. 
- [ ] Was it the case that was motivation for key idea 3, system’s thinking.
- [ ] Intended audience:  intersects systems-thinking with language modeling pipeline. 
- [ ] Evidence bas call to action to increase community participation
- [ ] Next steps: on the overwhelm, systems thinking helps you look at the components of the system to study and isolate, such as systems thinking
- [ ] Next steps: how to speak to health audience from UK Petr Slovak

Lujain
- [ ] AI mode is: always available, not judgmental, seemingly private, and encouraging (validating)
- [ ] Responsiveness, ‘mm, certainty (relationship)
- [ ] Certainty did not mediate
- [ ] Feeling known was a mediator
- [ ] 5.8 vs 5.6 - significant but a small effect? 
- [ ] An AI who derstands you faster or approaches humans
- [ ] Study 2: Costs of human interaction
- [ ] How much effort, and how sufficiency it would be was higher 
- [ ] Cost benefit framework (like how trust benefits for XAI)
- [ ] Study 3: Benefits 
- [ ] Go to their actual friends
- [ ] Rate their friend’s advice vs. AI’s advice
- [ ] Media ideals (movies/porn) reduce satisfactionh “real” relationships
- [ ] Study 4: less syncophantic models becoming a thing
- [ ] Finding: people will want it, and understood me best and easiest to talk to. 
- [ ] Takeaway: no substitution per se, but a new standard and changes perceptionsoffline relationships.
- [ ] Highly personalized models as a new thing: level of responsiveness will be great, remaining risks with co-existing with social AI systems
- [ ] User choice is complicated, what are good mitigations?  Informed choice?
- [ ] Fast/easy is in our culture which we turn to, and market will find ways to deliver that.

Nice simple LinkedIn post

https://www.linkedin.com/posts/junho-myung-481690322_chi2026-hci-llm-share-7437276170175266816-KXHC?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo

https://www.thelancet.com/journals/lanpsy/article/PIIS2215-0366%2826%2900057-X/fulltext
Lived experience as another form of “talking to ople” and how to draw from their dual sources of knowledge


lden Goose - RLVR from unstructured data, this seemed like a closer way to model users as well?    Sort of like the UserRLSim?  
Cultural significance of free software


https://stanford.zoom.us/j/9794655811?pwd=aTdSNHhoMW9Xbk14U29FQTVrSXRXdz09


Can LLM-Simulated Practice and Feedback Upskill Human Counselors? A Randomized Study with 90+ Novice Counselors

Ryan Louie, Raj Sanjay Shah, Ifdita Hasan Orney, Juan Pablo Pacheco, Emma Brunskill, Diyi Yang

ACM Conference on Human Factors in Computing Systems


https://mlbenchmarks.org/

Key Adjustments for Longer Pauses:
* Increase silence_duration_ms: Set this higher than the default 500ms (e.g., to 1000ms or 1500ms) to make the model wait longer for continued input before interpreting the silence as the end of a turn.
* Adjust threshold: A higher threshold (closer to 1.0) for volume detection can help the VAD ignore background noise or quieter, slower speech, reducing accidental interruptions.
* Use semantic_vad: Switch from server_vad to semantic_vad for more human-like turn-taking that understands context, often allowing for longer, more natural pauses, as noted in this YouTube video and this Reddit post.
* Configure prefix_padding_ms: Adjusting this (default 300ms) ensures that the very beginning of your sentence isn't cut off if you pause for a long time before starting to speak. 



https://github.com/oademo1/crispy-dough-macos
MacOS dictation tool


Eslam Abdelaleem https://scholar.google.com/citations?view_op=view_citation&hl=en&user=8vetn38AAAAJ&citation_for_view=8vetn38AAAAJ:UeHWp8X0CEIC

labor market information that helps workers understand how their
specific roles are changing. The goal is not to move people out of AI-exposed occupations, but to help
them succeed within those occupations as the work itself evolves
- [ ] How are jobs changing in behavioral health (or where mental health is being delivered)?  The needs / aspirations of behavioral health or non-specialist workers, the political or economic job climate. may drive who chooses those careers 
- [ ] Why is it the the field social worker (Chicago) that some of these companies serve, I guess government was previously funding a big push for community mental health workers, so that’s why these new companies spun out and they need workers to collect the money?




hts://web.archive.org/web/20240908011338/https://situational-awareness.ai/racing-to-the-trillion-dollar-cluster/



https://www.linkedin.com/posts/omonijo_comparing-chatbots-ugcPost-7427398199037952001-U7sa?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo
engage in this critical thinking chatbot
Engage with Harthi https://www.linkedin.com/in/harshaliparalikar?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app

https://arxiv.org/abs/2509.21868


In the age of superhuman AI, how can we ensure AI systems upskill novices, so they can have personal fulfillment engaging in activities they have never been capable of engaging in before, and so novices can become skilled at doing useful/impactful work for their communities


https://www.nature.com/articles/s41591-025-04074-y
Super interesting, using AI as an assistant means people will prompt/explain in different ways (something gets lost in translation), and the models can’t handle this.


https://arxiv.org/abs/2602.01405
Feedback ways! Coo
Zac Imel’s new paper: https://pubmed.ncbi.nlm.nih.gov/41426204/

What is the structure of human AI collaboration.? This is a question that needs answering now, immediacy is powerful.
In 10, I showed how crowdsourcing could be decomposed. My current work shows it can be applied to broader domains.


https://x.com/bcherny/status/2017742741636321619?s=46
Claude code — worrees, Claude desktop has the worktree feature, keep notes as context, and religiously update the CLAUDE.md, skills are workflows (getting context from drive/slack/etc)

Hi Cristian,

I wanted to reach out to ask if interview decisions have already been finalized-- I remain very interested in the position!

Best,
Ryan Louie


Hi Tanzeem,

It was a great time chatting with you, Ishtiaque, and others at the MEXA Wellcome event in London. If you recall, I’m a postdoc in Stanford working with Diyi Yang/Emma Brunskill, was advised in my PhD by Darren Gergle and Haoqi Zhang. 

I wanted to reach out to ask if interview disions have already been finalized-- I remain very interested in the position at Cornell Tech!

Best,
Ryan Louie


Tom Insel - new Slingshot AI studies
https://thomasinsel352222.substack.com/p/chatbot-safety


AI mental health support design metaphors

https://x.com/fabulousqian/status/2012967925007761916?s=46

https://github.com/rasbt/reasoning-from-scratch/blob/main/ch06/01_main-chapter-code/ch06_main.ipynb

Antti HCI Theory and Theory of Human Behavior to help with HCI practice
https://academic.oup.com/HTTPHandlers/Sigma/LoginHandler.ashx?code=51gv5p&state=c5671284-49f9-4efe-a329-30ef9fcff426redirecturl%3Dhttpszazjzjacademiczwoupzwcomzjbookzj60808 

Nick Vincent: Data Watch
https://dataleverage.substack.com/p/coding-agents-are-1-a-big-deal-2


Continual Pretraining, using the same SFT (instruction tuning) and Model Merging again to get best of both worlds

https://www.linkedin.com/posts/maxbuckley_post-train-once-reuse-many-times-up-next-activity-7413336750564990976-Wo1d?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo

Venues for broader field arguments
https://time.com/7340901/ai-history-bubble-benchmarks/

Suicide Risk Assessment — Aeady being explored in AI Chatbot Work
https://mental.jmir.org/2025/1/e79838
VERA-MH 
https://arxiv.org/html/2510.15297v1

Revisiting Clinical Psychology Foundations of Treating and Supporting Patients with Suicide
https://pmc.ncbi.nlm.nih.gov/articles/PMC11295142/
* Great article on Collaborative Assessment and Management of Suicidality (CAMS) and Dialectical Behavioral Therapy to treat patients who are suicidal.  
* It’s just worth ning that validation is one component of the strategies a DBT practioner uses
    *  (non-clinical article: https://behavioralpsychstudio.com/understanding-suicidality-dbts-approach/#:~:text=It%20is%20crucial%20to%20understand,of%20%E2%80%9CWhy%20are%20you%20crying?) 
    * https://www.sciencedirect.com/science/article/pii/S0005789418300492 

Ai trust and safety learning

https://www.linkedin.com/posts/alicehunsberger_heres-my-updated-mega-list-of-resources-activity-7404191894349443072-A9ys?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo


Agree on how AI can help with evaluation and self improvement, where’s the link to papers?
https://www.linkedin.com/posts/jimblomo_neurips-activity-7403603140698443776-ZZbM?u_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo


https://profiles.stanford.edu/emily-alsentzer
Congrats on year one, Emily, and on your 4 papers.
Amazing work on top of your ClinicalBERT. The SHEPHERD paper hit close to home for me since I'm trying to build an offline diagnostic tool for rural clinics in global south where we don't have big labeled datasets either. Seeing you train on simulated patients and still get useful results on real UDN cases made me think we might not be crazy.
Also the distillation paper — the 8B beating the 70B in some tasks — that's huge for anyone trying to this stuff without a data center.
Still figuring a lot of this out. Would be great to hear how you're thinking about actual deployment. Congrats again.



Epistemic Injustice

- decolonial foresight 
- subaltern speech
- Testimonial injustice one’s accent, gender, or racial identity causes others to doubt theiintelligence or truthfulness.
- Hermeneutical injustice,  when language or conceptual frameworks do not yet exist to describe forms of oppression, such as the term “sexual harassment” p to the 1970s individuals suffer doubly: from the harm itself and from the inability to articulate it to others 

Postings in Europe 

Informatics Europe - Assistant (Tenure Track), Associate and Full Professors in Computer Science

Lueven Professorship in Intelligent Software job with KU LEUVEN | 403703
(None)


Assistant Professor in Artificial Intelligence job with MASARYK UNIVERSITY | 403419 (Not human AI)

Lecturer in Digital Health, Health Informatics and Artificial Intelligence job with KINGS COLLEGE LONDON | 403345
Maybe I have a shot (although it’s n human AI)

Southampton- Lecturer in Computer Science job with UNIVERSITY OF SOUTHAMPTON | 401593

Whole world of CV and ML which does look at human priors in images and tries to use them for “guidance” when training
https://arxiv.org/pdf/2511.12744
CV in general has this concept of guidance , like classiffree guidance, which I don’t understand.


Human AI creativity via World Models in 3D Game AI https://www.nature.com/articles/s41586-025-08600-3.pdf

https://www.kuleuven.be/personeel/joite/jobs/60590295?hl=nl&lang=nl
The Augment group is is one of the research units of the Human-Computer Interaction Section of the Department of Computer Science of KU Leuven. Research in the Augment group focuses on Human-Centered AI, an emerging discipline that aims to amplify and augment human abilities and preserve human control in order to make AI systems more productive, enjoyable, and fair. The objective is to enable end-users to understand the rationale of AI models and to enable them to steer models with input and feedback. The approach is researched to increase appropriate trust, acceptance and accuracy of models and to empower users to be an active and responsive part-taker in data-driven solutions. The focus is on visualisation and interaction techniques, using the full spectrum of hardware from small mobile devices to large multi-touch displays. Applications include learning analytics, precision agriculture, healthcare, media consumption, digital humanities, food & nutrition, fintech and human resources.

Brown $20 million over 5 years for responsible AI in mental health challenges, plus general frameworks for endowing AI with causal understanding from the psych/behavioral sciences
https://www.brown.edu/news/2025-07-29/aria-ai-institute-brown


Youth are using AI for mental health advice by large numbers almost as frequently as Google Search would have been (rather than librarians or traditional pathways) 
https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2841067


More AI and mental health industry players & their FDA comments: https://sulfuric-vise-510.notion.site/2a22902106628067ad94eb730458b06d?v=2a229021066280169c58000c71efcf6e


AI Upskilling Area (done from an economics or behavioral Have point of view) and seeing what factors influence whether AI can help with ideation/execution and for whom
https://www.linkedin.com/posts/martinjosegonzalez_is-the-future-owned-by-specialists-or-generalists-activity-7396717222980800513-ocmr?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo


Cool directions or research area
https://northeastern.wd1.myworkdayjobs.com/en-US/careers/job/Assistant-Professor-in-Music--AI-and-Brain-Health_R136941
* 
* Computational approaches to understanding music's role in neuroplasticity and brain health across diverse populations and across the lifespan
* Sonification of brain imaging data to translate neural patterns into audible representations
* Psychoacoustic optimization of soundscapes for well-being and therapeutic outcomes
* AI-driven analysis of musical engagement patterns to predict and monitor cognitive decline
* Development of adaptive music-based interventions responsive to real-time physiological feedback
* Integration of music cognition principles with AI to create personalized sound-based health interventions
* Multimodal imaging studies combining neuroimaging with acoustic analysis to map music-brain interactions


Simulation of judgement in LLMs (as judges)
https://www.pnas.org/doi/pdf/10.1073/pnas.2518443122?download=true
Surface level outputs align, but the means they come to the conclusions don’t

Diyi - meta learning? Coordinate descent (all, 1.2, all)

Chelsea
Iterative optimization at test time though!  Test time IS a form of search.
Many more iterations of iterative improvement…
If we do prompt optimization — well a prompt i artifact that we want to use later to power a language model to do a task
But if we do molecule optimization — we can 

Iterate with large batches of online data. Batch online RL.



Oion 2: 

ML/traintest setup
- claim: it’s actually more efficient (fewer samples? or fewer computational resources) and performant (higher metric) if we use the domain-resources, and thsynthetic data loops generated, from MULTIPLE DOMAINS. Such as (1) if we optimize on 2 domains, the 3rd domain becomes easier to optimize than (2) if we had just optimized for the 3rd domain. 
- Actually setup: we train/test split on each domain? 
- Try 1: To train on the third domain, that would involve taking 80% of states, optimizing only on them, and testing on the 20% of remaining states? 
- Try 2: (NO, we have to think of these like data points, so 20% is really some of the random seeded rollouts that were generated, and metric would be how good is the adherence for that
- So the test is if we continue testing after finished a round of optimizing, how is performance in the next batch of rollouts?

Theory: why this would be similar to “system prompt + task instruction/prompt” 
- we have some minstructions about the nature of the class of task(s)
- We then need to perform well on any given task instruction/prompt (high level)
- And in particular, our setup has sort of three layers
- 1) capability layer about the AI mental health training capability we are doing, such as simulating patients. It’s the common thing between all domains?  What part of the prompt?XAMPLE: 
- 2a) the domain layer, which corresponds to the boundaries of the domain resources we have.  EXAMPLE: We have currently put categories on different classes of scenarios for therapeutic alliance training (patient less open about culture unless therapist shows cultural humility; patient showing mistrust due to previous psychotic episodes). 
- 2b) there might be more breakdowns of domains here. We already break a domain into (1) easy, medium, hard: (2) different states, different transitions; (3) or different patient skeletons of course, all of which technically are grounded in the textbooks/domain resources. Also ways to group these parts, like starting states…
- 3) finally, there’s the actually datapoints we evaluate our “model. patients state adherence, these are single rollouts and the evaluation metrics for them. For AI patients transitions, these are single test cases instantiated and the evaluation metric for it.


TADA - really a method that requires aligned pairs
- Aligned domain-pairs could involve Standard English and Medical English
- And shows that adapters like LoRA can be stacked, just like dialect and task specific adapters 

https://docs.adapterhub.ml/methods.html
Adapter Hub using LorA now, we have task adapters and now dialect adapters


Don’t reduce down to one metric! That would be normative.
Aim for pluralistic metrics and try to optimize over all to achieve some kind of generalization rom Lorenzo Xiao)
https://arxiv.org/pdf/2505.18139
https://x.com/lrzneedresearch/status/1926815607334281277?s=12


One of the first studies to really clinically study content, moderators of bad and horrific content and their mental health affects
https://arxiv.org/abs/2511.09813


https://www.linkedin.com/posts/drxuanzhao_major-news-this-week-we-released-a-harvard-activity-7395222197457428480-TIw5?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo
Flourish RCT

https://x.com/ianarawjo/status/1988379230791729265?s=46

https://www.addressmentalhealth.org/cultural-adaptation-interviews



https://www.semanticscholar.org/reader/db40048a75453ad87c413d978dedfec8f56473f1
From Measurement to Expertise: Empathetic Expert Adapters for Context-Based Empathy in Conversational AI Agents



https://www.linkedin.com/posts/oscar-ybarra-phd-73b6613_personal-agency-social-connection-and-loneliness-ugcPost-7390127488435404802-2yA0?utm_medium=ios_app&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo&utm_source=social_share_send&utm_campaign=copy_lin

We identified four patterns of social experience:
 🟢 Empowered – High agency, high connection → lowest loneliness
 🟡 Muted – Low agency, high connection
 🟠 Separated – High agency, low connection
 🔴 Neglected – Low agency, low connection → highest loneliness

Some work on AI use in therapy like JAMA network https://www.linkedin.com/posts/aaron-krasner-md-04060048_we-are-at-the-ai-tipping-point-two-major-activity-7392666192353636352-eDX0?utm_medium=ios_app&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo&utm_source=screenshot_social_share&utm_campaign=copy_link

Clinical Skills Verification — 

This older paper was talking about wanting to just learn a policy from end states, reminded me of the paper that Ryan W presented on learning from a single end goal state image: https://arxiv.org/abs/1805.11686






*On mentoring capacity and the intention to mentor or actively lead students on a journey* I’d like to build my teaching and mentoring systems and take the opportunity when I work with a student to team them up to set expectations and to use them as guinea pigs and participants in my evolving system of mentorship so it takes a certain commitment to set up instrument and run successfully just like a user test I wouldn’t just go in and say just test there needs to be some hypothesis andintention when going into it
What that might look like for me is to try to remember my rules of thumb which are
- I’ve been more successful trying to get two students on the same team to push forward a certain project direction. 
- Teammates need opportuhere needs to be a glue in the collaboration for the deliberate separation of concerns so that the two efforts come together and an effective way. While this is take some effort, it just requires setting norms and trying to explain to them the value of the practice, which I am trying to guide them on before they embark








https://dl.acm.org/doi/10.1145/3663547.3759732
Alt Text Multi Cultural Translation (accounting for cultural differences in translation)


I want to die but I want to eat dtobeoki 
Esther Perrel
Couples Therapy


https://www.nngroup.com/articles/synthetic-users/

https://lanaramjit.xyz/wp-content/uploads/2025/09/cscw_clinic_fit.pdf
HCI methods win to create a well balanced sociotechnical solution? Great for intake and trauma informed care, reminding me that the “textbook procedures” arrived by some unique constraints maybe not exactly the sane configuration as your current counseling domain


https://www.apa-labs.com/events/inside-the-lab

https://www.linkedin.com/posts/xiaoran-zha71ba7170_iccv2025-iccv-activity-7384277031661760512-Q85j?utm_source=share&utm_medium=member_ios&rcm=ACoAABBn8T8BQQcvR7hXTx4l_f-pesAgSjue5Xo


